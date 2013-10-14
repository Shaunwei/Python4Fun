Simplified Bidding System:(python version)
================================================================

The syntax of the server is:
Server
The server program should start to run the server and print out an available
port number dynamically, e.g., 10001.
The syntax of the client is:
client (IP_address | host_name) port_num command {parameter}
Where command {parameter} can be any of the following:

post itemName minBid

list

bid itemId biddingPrice
The response should be:

either return a non-zero itemID for success or a zero for failure
(e.g., duplicated itemName

return a list of itemId itemName minBid maxBid

either return the biddingPrice (means maxBid becomes biddingPrice)
or a zero for lost the bidding (i.e., biddingPrice <= maxBid)
Both servers and clients should display reasonable messages appropriately.