library(jsonlite)
library(httr)

prettify(GET("http://localhost:5000/mine"))

string <- toJSON(list(sender = "d4ee26eee15148ee92c6cd394edd974e",
                      recipient = "someone-other-address",
                      amount = 5), auto_unbox = TRUE)

test <- POST(url = "http://localhost:5000/transactions/new", 
             add_headers(`content_type` = sprintf("application/json")),
             body = string)

prettify(GET("http://localhost:5000/chain"))
