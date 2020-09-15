//document.getElementById('myTable').style.filter = "blur(150px)";

if(performance.navigation.type == 2)
{
    location.reload(true);
}
$(document).ready(function()
{
  document.getElementById('myTable').style.filter = "blur(5px)";
});

let func = function()
{
time_mappings = {3 : "Ready", 2 : "Set", 1 : "Go!"}
  var timeleft = 3;
  var downloadTimer = setInterval(function()
  {
    if (timeleft <= 0)
    {
      document.getElementById("countdown").innerHTML = ""
      document.getElementById('myTable').style.filter = "unset";
      clearInterval(downloadTimer);
      timer();
    }
    else
    {
     $("#countdown").html(time_mappings[timeleft]);
      $("#countdown").fadeIn(0);
      $("#countdown").fadeOut(500);
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
        $('#timer').fadeOut(1000).fadeIn(1000);
        x++;
      }
    }
//    console.log(count);
       $(this).addClass("crossed");
    count++;
  }
});

