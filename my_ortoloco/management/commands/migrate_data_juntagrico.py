from django.core.management.base import BaseCommand, CommandError
from my_ortoloco.models import *
from juntagrico.models import *
import my_ortoloco
import juntagrico
from datetime import datetime
from django.db import connection

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            dest='clear',
            help='Clear target database',
        )

    def handle(self, *args, **options):
        # clear
        if options['clear']:
            juntagrico.models.RecuringJob.objects.all().delete()
            juntagrico.models.OneTimeJob.objects.all().delete()
            juntagrico.models.JobType.objects.all().delete()
            juntagrico.models.ActivityArea.objects.all().delete() # cleanup not possible, if jobs are already linked to this.
            Subscription.objects.all().delete()
            Share.objects.all().delete()
            juntagrico.models.Depot.objects.all().delete()
            cursor = connection.cursor()
            cursor.execute('DELETE FROM juntagrico_member')
            return
    
        # Members
        for loco in Loco.objects.all():
            print( loco.__dict__ )
            member_dict = {
                'user' : loco.user,
                'first_name' : loco.first_name,
                'last_name' : loco.last_name,
                'email' : loco.email,
                'addr_street' : loco.addr_street,
                'addr_zipcode' : loco.addr_zipcode,
                'addr_location' : loco.addr_location,
                'birthday' : loco.birthday,
                'phone' : loco.phone,
                'mobile_phone' : loco.mobile_phone,
                'confirmed' : loco.confirmed,
                'reachable_by_email' : loco.reachable_by_email,
                'block_emails' : False
            }
            Member.objects.update_or_create( **member_dict )
        
        # Depots
        for depot in my_ortoloco.models.Depot.objects.all():
            contact = Member.objects.filter( email = depot.contact.email )[0]
            depot_dict = {
                'code' : depot.code,
                'name' : depot.name,
                'contact' : contact,
                'weekday' : depot.weekday,
                'latitude' : depot.latitude,
                'longitude' : depot.longitude,
                
                'addr_street' : depot.addr_street,
                'addr_zipcode' : depot.addr_zipcode,
                'addr_location' : depot.addr_location,
                
                'description' : depot.description
            }
            juntagrico.models.Depot.objects.update_or_create( **depot_dict )    
        
        # ActivityArea (Tätigkeitsbereite)
        for activity_area in my_ortoloco.models.Taetigkeitsbereich.objects.all():
            #print( activity_area.__dict__ )
            #email = models.EmailField(null=True)
                
            coordinator = Member.objects.filter( email = activity_area.coordinator.email )[0]
            print( coordinator.__dict__ )
            emails = set( loco.email for loco in activity_area.locos.all() )
            members = Member.objects.filter( email__in = emails )
                
            activity_area_dict = {
                'name' : activity_area.name,
                'description' : activity_area.description,
                'core' : activity_area.core,
                'hidden' : activity_area.hidden,
                'coordinator' : coordinator,
            }
            
            createdActivityArea = juntagrico.models.ActivityArea.objects.update_or_create( **activity_area_dict )[0]
            
            # Add members to activities
            createdActivityArea.members = members
            createdActivityArea.save()

        # jobtypes
        for jobType in my_ortoloco.models.JobType.objects.all():
            print( jobType.__dict__ )
            
            activityarea = juntagrico.models.ActivityArea.objects.filter( name = jobType.bereich.name )[0]
            
            jobType_dict = {
                'name' : jobType.name,
                'displayed_name' : jobType.displayed_name,
                'description' : jobType.description,
                'activityarea' : activityarea,
                'duration' : jobType.duration,
                'location' : jobType.location
            }
            
            juntagrico.models.JobType.objects.create( **jobType_dict )      
        
        # recuring jobs + assignments
        for recuringJob in my_ortoloco.models.RecuringJob.objects.all():
            print( recuringJob.__dict__ )
            
            jobtype = juntagrico.models.JobType.objects.filter( name = recuringJob.typ.name )[0]
            
            recuringJob_dict = {
                'type' : jobtype,
                'slots' : recuringJob.slots,
                'time' : recuringJob.time,
                'pinned' : recuringJob.pinned,
                'reminder_sent' : recuringJob.reminder_sent,
                'canceled' : recuringJob.canceled,
            }
            
            createdJob = juntagrico.models.RecuringJob.objects.create( **recuringJob_dict )  
            
            # Böhnli / Assignment
            for bohne in Boehnli.objects.filter( job = recuringJob ):
                print( bohne.__dict__ )
                
                member = Member.objects.filter( email = bohne.loco.email )[0]
                
                assignment_dict = {
                    'job' : createdJob,
                    'member' : member,
                    'amount' : 1, # TODO: Wofür ist das?
                }
                Assignment.objects.create( **assignment_dict )  
        
        # One time jobs + assignments
        for onetimeJob in my_ortoloco.models.OneTimeJob.objects.all():
            print( onetimeJob.__dict__ )
            job = my_ortoloco.models.Job.objects.filter( id = onetimeJob.job_ptr_id )[0]
            print( job.__dict__ )
            
            activityarea = juntagrico.models.ActivityArea.objects.filter( name = onetimeJob.bereich.name )[0]
            
            onetimeJob_dict = {
                'slots' : job.slots,
                'time' : job.time,
                'pinned' : job.pinned,
                'reminder_sent' : job.reminder_sent,
                'canceled' : job.canceled,
                
                'name' : onetimeJob.name,
                'displayed_name' : onetimeJob.displayed_name,
                'description' : onetimeJob.description,
                'activityarea' : activityarea,
                'duration' : onetimeJob.duration,
                'location' : onetimeJob.location
            }
            
            createdJob = juntagrico.models.OneTimeJob.objects.create( **onetimeJob_dict )  
            
            # Böhnli / Assignment
            for bohne in Boehnli.objects.filter( job = job ):
                print( bohne.__dict__ )
                
                member = Member.objects.filter( email = bohne.loco.email )[0]
                
                assignment_dict = {
                    'job' : createdJob,
                    'member' : member,
                    'amount' : 1, # TODO: Wofür ist das?
                }
                Assignment.objects.create( **assignment_dict )  

        
        # Abos / Subscriptions
        # create size for subscription type
        size = SubscriptionSize.objects.update_or_create( name = "1 EAT", long_name = "1 Ernteanteil", size = 1 )[0]
        
        # create subscription type
        subType = SubscriptionType.objects.update_or_create( name = "Gemüse", size = size, shares = 1, required_assignments = 6, price = 600 )[0]
        
        # fill
        for abo in my_ortoloco.models.Abo.objects.all():
            print( abo.__dict__ )
            #types = models.ManyToManyField('SubscriptionType',through='TSST', related_name='subscription_set')
            #future_types = models.ManyToManyField('SubscriptionType',through='TFSST', related_name='future_subscription_set')

            #canceled = models.BooleanField('gekündigt', default=False)
            #activation_date = models.DateField('Aktivierungssdatum', null=True, blank=True)
            #deactivation_date = models.DateField('Deaktivierungssdatum', null=True, blank=True)
            #cancelation_date = models.DateField('Kündigüngssdatum', null=True, blank=True)
            #creation_date = models.DateField('Erstellungsdatum', null=True, blank=True, auto_now_add=True)
            #start_date = models.DateField('Gewünschtes Startdatum', null=False, default=start_of_next_business_year)
            #end_date = models.DateField('Gewünschtes Enddatum', null=True,blank=True)
            #notes = models.TextField('Notizen', max_length=1000, blank=True)
            
            primary_member = Member.objects.filter( email = abo.primary_loco.email )[0]
            depot = juntagrico.models.Depot.objects.filter( code = abo.depot.code )[0]

            abo_dict = {
                'active' : abo.active,
                'depot' : depot,

                'primary_member' : primary_member
            }
        
            createdSub = Subscription.objects.create( **abo_dict )

            # set sub to all of its members
            for loco in abo.bezieher_locos():
                m = Member.objects.filter( email = loco.email )[0]
                m.subscription = createdSub
                m.save()
                
            # insert types and future types (size / future_size)
            for i in range(0, abo.size ):
                TSST.objects.create( type = subType, subscription = createdSub )
            for i in range(0, abo.future_size ):
                TFSST.objects.create( type = subType, subscription = createdSub )

        # Anteilschein
        for share in my_ortoloco.models.Anteilschein.objects.all():
            print( share.__dict__ )
            #issue_date = models.DateField('Ausgestellt am', null=True, blank=True)
            #booking_date = models.DateField('Eingebucht am', null=True, blank=True)
            #cancelled_date = models.DateField('Gekündigt am', null=True, blank=True)
            #termination_date = models.DateField('Gekündigt auf', null=True, blank=True)
            #payback_date = models.DateField('Zurückbezahlt am', null=True, blank=True)
            #number = models.IntegerField('Anteilschein Nummer', null=True, blank=True)
            #notes = models.TextField('Notizen', max_length=1000, default='', blank=True)
            
            # skip unassigned shares
            if not share.loco:
                continue
            
            member = Member.objects.filter( email = share.loco.email )[0]
            
            share_dict = {
                'member' : member,
            }
            
            # paid_date setzten, wenn paid = true
            if share.paid:
                share_dict['paid_date'] = datetime.now()
        
            Share.objects.create( **share_dict )
        
