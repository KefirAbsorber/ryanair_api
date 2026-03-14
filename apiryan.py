from datetime import datetime
import requests
from openpyxl import load_workbook
from openpyxl import Workbook
import pathlib

# get date for logs
now = datetime.now()

# path and excel setup
path = pathlib.Path(__file__).parent.resolve()
excel_file = path.joinpath('flights.xlsx')

try:
    wb = load_workbook(excel_file)
except FileNotFoundError:
    wb = Workbook()
ws = wb.active


# api request and formating
def find(frm, to, date_from, date_to):
    url: str = "https://services-api.ryanair.com/farfnd/3/oneWayFares?&departureAirportIataCode=" + frm + "&arrivalAirportIataCode=" + to + "&language=pl&limit=16&market=pl-pl&offset=0&outboundDepartureDateFrom=" + date_from + "&outboundDepartureDateTo=" + date_to
    response: requests.Response = requests.get(url)
    response: dict = response.json()

    flight_out_date = response["fares"][0]["outbound"]["departureDate"]
    flight_in_date = response["fares"][0]["outbound"]["arrivalDate"]
    cost = response["fares"][0]["summary"]["price"]["value"]

    result = [now, flight_out_date, flight_in_date, frm, to, cost]

    return result


"""
      finished tracking     
      
modlin lisbona 11-28 07
flight=find("WMI","LIS","2025-07-11","2025-07-28")
ws.append(flight)

modlin bari 11-28 10
poznan lisbona 11-28 07
flight=find("POZ","LIS","2025-07-11","2025-07-28")
ws.append(flight)

flight = find("WMI", "BRI", "2025-10-11", "2025-10-28")
ws.append(flight)

poznan bari 11-28 10
flight = find("POZ", "BRI", "2025-10-11", "2026-10-28")
ws.append(flight)

modlin madryt 11-28 10
flight = find("WMI", "MAD", "2026-10-11", "2026-10-28")
ws.append(flight)

modlin rzym 11-28 10
flight = find("WMI", "CIA", "2026-10-11", "2026-10-28")
ws.append(flight)
"""

#       currenty tracking      #
# wrocław rome 11-28 10
flight = find("WRO", "CIA", "2026-10-11", "2026-10-28")
ws.append(flight)

# save to worksheet
wb.save(excel_file)
