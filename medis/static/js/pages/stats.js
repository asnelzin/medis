(function() {

    function ajaxSuccess(data) {
        var month = $("#id_month").find("option:selected").attr("value");
        var year = $("#id_year").find("option:selected").text();
        for (var idx in data) {
            var url = "/stats/spec/?speciality=" + data[idx].pk + "&month=" + month + "&year=" + year;
            $("tr:has(td:contains(" + data[idx].name + ")) td:nth-child(2) a").attr("href", url);
            $("tr:has(td:contains(" + data[idx].name + ")) td:nth-child(3)").text(data[idx].tickets);
            $("tr:has(td:contains(" + data[idx].name + ")) td:nth-child(4)").text(data[idx].patients);
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