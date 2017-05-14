// csrftoken
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
        settings.data = JSON.stringify(settings.data);
    },
    processData: false
});

define([], function () {

    $("#filter-table thead th").each(function () {
        var title = $(this).text();
        if( title != "Boehnlis" && title != "Boehnlis Kernbereich" ) {
            $(this).prepend("<input type='text' placeholder='' style='width: 100%;' />");
        }
    });

    var table = $("#filter-table").DataTable({
        "paging": true,
        "info": false,
        "search": {
            "regex": true,
            "smart": false
        },
        "drawCallback": function (settings) {
            updateSendEmailButton( settings._iRecordsDisplay );
        },
        "processing": true, // activate loading indicator
        "serverSide": true, // get data from server
        searchDelay: 1000,   // throttle the server request to 1 per second
        ajax: {
            url: "/api/membertable/", // api location
            type: 'POST'
        },
        "columns": [
            { "name": "first_name" },
            { "name": "Boehnlis", "orderable": false, "searchable": false },
            { "name": "Boehnlis Kernbereich", "orderable": false, "searchable": false },
            { "name": "areas__name" },
            { "name": "abo__depot__name" },
            { "name": "email" },
            { "name": "phone" },
            { "name": "mobile_phone" }
        ],
        "language": {
            "decimal":        "",
            "emptyTable":     "Tabelle ist leer",
            "info":           "Zeige Eintrag _START_ bis _END_ von _TOTAL_ Einträgen",
            "infoEmpty":      "Zeige Eintrag 0 bis 0 von 0 Einträgen",
            "infoFiltered":   "(gefiltert von insgesamt _MAX_ Einträgen)",
            "infoPostFix":    "",
            "thousands":      ",",
            "lengthMenu":     "Zeige _MENU_ Einträge",
            "loadingRecords": "Lade...",
            "processing":     "Verarbeite...",
            "search":         "Suche:",
            "zeroRecords":    "Keine passenden Einträge gefunden",
            "paginate": {
                "first":      "Erste",
                "last":       "Letzte",
                "next":       "Nächste",
                "previous":   "Vorherige"
            },
            "aria": {
                "sortAscending":  ": aktivieren um Spalte aufsteigend zu sortieren",
                "sortDescending": ": aktivieren um Spalte absteigend zu sortieren"
            }
        }
    });

    function updateSendEmailButton(count) {
        $("button#copy-email").prop('disabled', false)
        if (count == 0) {
            $("button#copy-email").prop('disabled', true)
            $("button#send-email")
                .prop('disabled', true)
                .text("Email senden");
        } else if (count == 1) {
            $("button#send-email")
                .prop('disabled', false)
                .text("Email an dieses Mitglied senden");
        } else {
            $("button#send-email")
                .prop('disabled', false)
                .text("Email an diese " + count + " Mitglieder senden");
        }
    }

    var column_search = $.fn.dataTable.util.throttle(
        function ( column, val ) {
            console.log(column.search())
            console.log(val)
            if (column.search() !== val) {
                column.search( val ).draw();
            }
        },
        1000
    );

    table.columns().every(function () {
        var that = this;
        $("input", this.header()).on("keyup change", function () {
            column_search(that, this.value);
        });
        $("input", this.header()).on("click", function (e) {
            e.preventDefault();
            e.stopPropagation();
        });
    });

    $("form#email-sender").submit(function( event ) {
        filter_columns = $("#filter-table th input");
        filter_value = {
            'global_filter' : $("#filter-table_filter input").val(),
            'column_filter' : [
                { "name": "first_name", "value": filter_columns.eq(0).val() },
                { "name": "areas__name", "value": filter_columns.eq(1).val() },
                { "name": "abo__depot__name", "value": filter_columns.eq(2).val() },
                { "name": "email", "value": filter_columns.eq(3).val() },
                { "name": "phone", "value": filter_columns.eq(4).val() },
                { "name": "mobile_phone", "value": filter_columns.eq(5).val() }
            ]
        };
        $("#filter_value").val(JSON.stringify(filter_value));
        return;
    });

});
