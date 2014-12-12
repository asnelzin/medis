$(document).ready(
    function () {
        var form = $('#filter-form');

        function updateStats(data) {
            var month = $("#id_month option:selected").attr("value");
            var year = $("#id_year option:selected").text();
            for (var idx in data) {
                var url = "/stats/spec/?specialty=" + data[idx].pk + "&month=" + month + "&year=" + year;
                console.log(url);
                $("tr:has(td:contains(" + data[idx].name + ")) td:nth-child(2) a").attr("href", url);
                $("tr:has(td:contains(" + data[idx].name + ")) td:nth-child(3)").text(data[idx].tickets);
                $("tr:has(td:contains(" + data[idx].name + ")) td:nth-child(4)").text(data[idx].patients);

            }
        }

        function getMonthStats() {
            $.ajax({
                url: form.attr('action'),
                data: form.serialize(),
                type: form.attr('method'),
                success: updateStats
            });
            return false;
        }

        form.submit(getMonthStats);
        getMonthStats();
    }
);