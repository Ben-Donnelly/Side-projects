from bs4 import BeautifulSoup
from requests import get
from os import startfile
from time import sleep

global last_called


def get_data():
    site = "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=HSTON&NumMins=90&format=xml"
    start_site = get(site)

    soup = BeautifulSoup(start_site.text, "xml")

    # Get all parameters
    station_name = soup.find_all("Stationfullname")
    train_origin = soup.find_all("Origin")
    train_dest = soup.find_all("Destination")
    departure = soup.find_all("Origintime")
    arrival = soup.find_all("Destinationtime")
    due_in = soup.find_all("Duein")
    late_status = soup.find_all("Late")
    global last_called
    last_called = soup.find("Querytime").text

    # Put all into list
    data = []

    for i in range(0, len(station_name)):
        data.append([station_name[i].text, train_origin[i].text, train_dest[i].text, departure[i].text, arrival[i].text,
                     due_in[i].text, late_status[i].text])
    # string
    return f"""{data}"""


def main():
    # Start file once
    # Update every 30 seconds
    count = 0
    while True:
        to_html(count, get_data())
        count = 1
        sleep(30)


def to_html(count, data):
    global last_called

    # Clean up html
    data = data.replace('[', '<tr>')
    data = data.replace(']', '</tr>')
    data = data.replace(',', '')
    # data = data.replace("</tr>,", "\n")
    data = data.replace('\' ', '</td>')

    data = data.replace("<tr>\'", "<tr>\n\t\t<td>")
    data = data.replace("</td>\'", "</td>\n\t\t<td>")
    data = data.replace("</tr> <tr>", "</td>\n\t</tr>\n\t<tr>")
    data = f'''\
<html>

  <head>
    <link rel='stylesheet' type='text/css' href='style.css'>
    <meta http-equiv="refresh" content="30" />

    <link rel="shortcut icon" type="image/png" href="https://www.irishrail.ie/favicon.ico" />
  </head>
  <input id='myInput' class="button" type='text' placeholder='Search..'>
  <table class='T1' id='myTable'>
    <tr>
      <th>Station Name</th>
      <th>Origin</th>
      <th>Destination</th>
      <th>Depart Time</th>
      <th>Arrival Time</th>
      <th>Due In (minutes)</th>
      <th>Time status</th>
    </tr>
    <tbody id='body'> 
    {"".join(data)}
    </tbody>
  </table>
  Last updated: {last_called[:5]}
  <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'></script>
  <script src='functions.js'></script>

</html>

            '''
    data = data.replace("'", "")
    data = data.replace("</tr></tr>", "</tr>")
    data = data.replace("<tr><tr>", "<tr>")

    with open("table.html", "w", encoding="utf-8") as file:
        file.write(data)

    if count == 0:
        startfile("table.html")


if __name__ == "__main__":
    main()
