// Filter table by search
$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#body tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

// For table colouring if late, <= 20 mins, <= 10 mins
function ti()
{
    var table = document.getElementById('myTable');

    for (var i = 1; i < table.rows.length; i++)
    {
        for (var j = 3; j < table.rows[i].cells.length - 3; j++)
        {
          var time_until = table.rows[i].cells[5].innerHTML
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

    // For Time status
    for (var i = 1; i < table.rows.length; i++)
    {
      var time_until1 = table.rows[i].cells[6].innerHTML

      if(time_until1 == 0)
      {
        table.rows[i].cells[6].innerHTML = "On time"
      }

      else if(time_until1 < 0)
      {
        table.rows[i].cells[6].innerHTML = `Early (${time_until1} minutes)`
      }

      else
      {
        table.rows[i].cells[6].innerHTML < 2 ? table.rows[i].cells[6].innerHTML = `Late (+ ${time_until1} minute)`
        :
        table.rows[i].cells[6].innerHTML = `Late (+ ${time_until1} minutes)`
      }
    }

}
ti();


