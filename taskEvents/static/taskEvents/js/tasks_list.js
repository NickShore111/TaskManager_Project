$(function() {
    $('#task-select-form').children().change(function() {
        console.log("selection made");
        $('#task-select-form').submit()
    })
})
