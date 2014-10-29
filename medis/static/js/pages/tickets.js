$(document).ready(
    function () {
        var form = $('#filter-form');

        function updateStats(data) {
            for (var key in data['stats_data']) {
                $("tr:has(td:contains(" + key + ")) td:nth-child(3)").text(data.stats_data[key].tickets);
                $("tr:has(td:contains(" + key + ")) td:nth-child(4)").text(data.stats_data[key].patients);
            }
        }

        function getMonthStats() {
            $.ajax({
                url: form.attr('action'),
                data: form.serialize(),
                type: form.attr('method'),
                success: updateStats,
            });
            return false;
        }

        form.submit(getMonthStats);
    }
);