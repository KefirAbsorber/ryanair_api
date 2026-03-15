## Use 
To start using the script, first run config, and enter which flights you would like to track.  
Then I would recommend adding the apiryan script to some kind of autorun service, although you can run it by hand.  
The excel file will be created automatically in the script directory.  
The data you collect can help track how the price changes, depending on the time between buying the ticket and the actual flight.  
From my test it's different for different airports and flights.  


## Setup calrification 
frm, and to are represented using **IATA airport codes**. 

Example of a working section of ini file:  
*frm = WMI  
to = CIA  
date_from = 2026-04-02  
date_to = 2026-06-01*  

Which would be looking for the cheapest flight from Warszawa Modlin to Rome Ciampino, between the 2nd of April and 1st of June. 
