$(function() {
    function round(num) {
        var m = Number((Math.abs(num) * 100).toPrecision(15));
        return Math.round(m) / 100 * Math.sign(num);
    }

    $("tr.reviewScore-row").each(function() {
        let txtScore = $(this).children(".score").text();
        let total = 0, count = 0;
    
        for(let i = 0; i < txtScore.length; i++) {
            num = txtScore[i];
            var intScore = parseInt(num, 10)
            total += intScore;
            if(intScore != 0) count++; 
        }
        let avgScore = total/count;
        let output = round(avgScore);
        $(this).find("#avgScore").html(output);
    });
    
    $('#review-select-form').children().change(function() {
        $('#review-select-form').submit()
    })

})