(function() {

    function ajaxSuccess(data) {
        var month = $("#id_month").find("option:selected").attr("value");
        var year = $("#id_year").find("option:selected").text();
        for (var item of data) {
            var url = "/stats/spec/?speciality=" + item.pk + "&month=" + month + "&year=" + year;
            $("tr:has(td:contains(" + item.name + ")) td:nth-child(2) a").attr("href", url);
            $("tr:has(td:contains(" + item.name + ")) td:nth-child(3)").text(item.tickets);
            $("tr:has(td:contains(" + item.name + ")) td:nth-child(4)").text(item.patients);
        }
    }

    var init = function() {
        var form = $('#filter-form')
        form.on('submit', function() {
            $.ajax({
                url: form.attr('action'),
                data: form.serialize(),
                type: form.attr('method'),
                success: ajaxSuccess
            });
            return false;
        });

        $('.form-control').change(function(e) {
            form.submit();
            return false;
        });

        form.submit();
    };

    $(init);
})();