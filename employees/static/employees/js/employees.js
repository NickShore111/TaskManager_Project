$(function() {
    $("#id_start_date").datepicker({
    dateFormat: "yy-mm-dd",
    });
    $("#employeeSelect").change(function(e) {
        console.log("New Employee Selected")
        var employeeID = $(this).val();
        console.log(employeeID);
        $.ajax({
            method: "GET",
            url: "display/" + employeeID,
            success: function(response) {
                console.log(response);
                $('#display_employee_info').html(response);
            },
            error: function() {
                $('#display_employee_info').html("");
            }
        });
        return false;
    })
});