from django.shortcuts import render

from django.forms import ModelForm

from static_ortoloco.models import *

# Create your views here.


def getBaseDict(request):
    return {
        'hasDocuments': Document.objects.count() > 0,
        'hasLinks': Link.objects.count() > 0,
        'hasMedias': Link.objects.count() > 0
    }


def home(request):
    """
    Homepage of "static" page
    """
    submenu = ""
    if StaticContent.objects.all().filter(name='HomeUnterMenu').__len__() > 0:
        submenu = StaticContent.objects.all().filter(name='HomeUnterMenu')[0].content
    welcome_text = ""
    if StaticContent.objects.all().filter(name='Willkommen').__len__() > 0:
        welcome_text = StaticContent.objects.all().filter(name='Willkommen')[0].content

    renderdict = getBaseDict(request)
    renderdict.update({
        'submenu': submenu,
        'welcomeText': welcome_text,
        'menu': {
            'home': 'active'
        }
    })

    return render(request, "home.html", renderdict)


def about(request):
    """
    About ortoloco of "static" page
    """

    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'about': 'active',
            'aboutChild': 'active'
        }
    })

    return render(request, "about.html", renderdict)


def portrait(request):
    """
    About ortoloco of "static" page
    """
    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'about': 'active',
            'portrait': 'active'
        }
    })

    return render(request, "portrait.html", renderdict)


def background(request):
    """
    About ortoloco of "static" page
    """
    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'about': 'active',
            'background': 'active'
        }
    })

    return render(request, "background.html", renderdict)


def abo(request):
    """
    About ortoloco of "static" page
    """
    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'about': 'active',
            'abo': 'active'
        }
    })

    return render(request, "abo.html", renderdict)


def faq(request):
    """
    FAQ ortoloco of "static" page
    """
    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'about': 'active',
            'faq': 'active'
        }
    })

    return render(request, "faq.html", renderdict)


def about(request):
    """
    About ortoloco of "static" page
    """

    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'about': 'active',
            'aboutChild': 'active'
        }
    })

    return render(request, "about.html", renderdict)


def organization(request):
    """
    Organization ortoloco of "static" page
    """
    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'about': 'active',
            'organization': 'active'
        }
    })

    return render(request, "organization.html", renderdict)	
	
	
def operatingmirror(request):
    """
    Operatingmirror ortoloco of "static" page
    """
    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'about': 'active',
            'operatingmirror': 'active'
        }
    })

    return render(request, "operatingmirror.html", renderdict)		

def philosophy(request):
    """
    Philosophy ortoloco of "static" page
    """
    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'about': 'active',
            'philosophy': 'active'
        }
    })

    return render(request, "philosophy.html", renderdict)		

	
def agenda(request):
    """
    Agenda ortoloco of "static" page
    """
    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'agenda': 'active'
        }
    })

    return render(request, "agenda.html", renderdict)			

def gardennews(request):
    """
    Garden news ortoloco of "static" page
    """
    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'gardennews': 'active'
        }
    })

    return render(request, "gardennews.html", renderdict)		
	
def join(request):
    """
    About ortoloco of "static" page
    """
    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'join': 'active'
        }
    })

    return render(request, "join.html", renderdict)


def media(request):
    """
    About ortoloco of "static" page
    """
    medias_list = []
    first = True
    first_year = ""
    for media in Media.objects.all().order_by('year').reverse():
        medias_list.append({
            'shown': first or first_year == media.year or request.GET.get("year") is not None and request.GET.get("year") == media.year,
            'year': media.year,
            'mediafile': media.mediafile,
            'name': media.name
        })
        if first:
            first = False
            first_year = media.year

    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'media': 'active'
        },
        'medias': medias_list,
    })

    return render(request, "media.html", renderdict)


def links(request):
    """
    Links to partners
    """
    links_list = Link.objects.all().reverse()

    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'links': 'active'
        },
        'links': links_list,
    })

    return render(request, "links.html", renderdict)


def documents(request):
    """
    Documents of Ortoloco
    """
    documents_list = Document.objects.all().reverse()

    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'documents': 'active'
        },
        'documents': documents_list,
    })

    return render(request, "documents.html", renderdict)


def downloads(request):
    """
    Downloads available
    """
    download_list = Download.objects.all().reverse()

    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'downloads': 'active'
        },
        'downloads': download_list,
    })

    return render(request, "downloads.html", renderdict)


def contact(request):
    """
    Contact page
    """

    class PolitolocoForm(ModelForm):
        class Meta:
            model = Politoloco
            fields = ['email']

    success = 0
    failure = 0
    message = ''

    f = PolitolocoForm()
    if request.method == 'POST':
        add_f = PolitolocoForm(request.POST)
        if add_f.is_valid():
            add_f.save()
            success = 1
            message = 'E-Mail Adresse beim Newsletter von Politoloco registriert.'
        else:
            failure = 1
            message = 'E-Mail Adresse ungueltig'

    renderdict = getBaseDict(request)
    renderdict.update({
        'menu': {
            'contact': 'active',
        },
        'request': request,
        'success': success,
        'failure': failure,
        'message': message
    })

    return render(request, "contact.html", renderdict)
