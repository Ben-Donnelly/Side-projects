$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#body tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

function ti()
{
    var table = document.getElementById('myTable');

    for (var i = 1; i < table.rows.length; i++)
    {
        for (var j = 3; j < table.rows[i].cells.length - 3; j++)
        {
          time_until = table.rows[i].cells[5].innerHTML
          if (time_until < 21 && time_until > 10)
          {
            table.rows[i].cells[5].style["background-color"] = "orange";
            table.rows[i].cells[5].style.color = "white";
          }
          if (time_until < 11)
          {
            table.rows[i].cells[5].style["background-color"] = "red";
            table.rows[i].cells[5].style.color = "white";
          }
       }
    }
}
ti();