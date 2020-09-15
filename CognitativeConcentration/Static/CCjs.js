//document.getElementById('myTable').style.filter = "blur(150px)";

$(document).ready(function()
{
  document.getElementById('myTable').style.filter = "blur(5px)";
});

let func = function()
{
  var timeleft = 3;
  var downloadTimer = setInterval(function()
  {
    if (timeleft <= 0)
    {
      document.getElementById("countdown").innerHTML = ""
      document.getElementById('myTable').style.filter = "unset";
      timer();
    }
    else
    {
      document.getElementById("countdown").innerHTML = timeleft;
    }
    timeleft -= 1;
  }, 1000);

}


let elem = $('#MyB');

elem.one('click', func);


function timer()
{
  var startTime = Date.now();

  interval = setInterval(function()
  {
    var elapsedTime = Date.now() - startTime;
    document.getElementById("timer").innerHTML = (elapsedTime / 1000).toFixed(3);
  }, 100);
}



function ti()
{
  var table = document.getElementById('myTable');
  for (var i = 0; i < table.rows.length; i++)
  {
    for (var j = 0; j < table.rows[i].cells.length; j++)
    {
      table.rows[i].cells[j].style["background-color"] = "orange";
    }
  }
}

count = 1;
$("td").click(function()
{
  if ($(this).text() == count)
  {
    if (count == 16)
    {
      clearInterval(interval);
      x = 0
      while (x < 3)
      {
        console.log(x);
        $('#timer').fadeOut(500).fadeIn(500);
        x++;
      }
    }
    console.log(count);
    $(this).css('backgroundColor', 'grey');
    $(this).html('');

    count++;
  }
});

