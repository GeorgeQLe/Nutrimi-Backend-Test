// Copyright 2019 George Le

// this url: https://aboutreact.com/example-of-sqlite-database-in-react-native/
// has the npm commands to install sqlite into the react native app
import { openDatabase } from 'react-native-sqlite-storage';

var custID = "cus_MASWsf9DntbhIV";
var signatureSecret = "b0cda13d-fc65-4243-ae73-32c2a59b7612";
var deliveryAPIkeySandbox = "5f1b5928-69f7-49de-a2c9-b54fb68796d1";

// curl -u fake-api-token-4-u: \
//  -d “dropoff_address=20 McAllister St, San Francisco, CA 94102” \
//  -d “pickup_address=101 Market St, San Francisco, CA 94105” \
//  -X POST https://api.postmates.com/v1/customers/cus_abc123/delivery_quotes

function requestPostMatesQuote(resturantAddress, pickupAddress) {
    var URL = "https://api.postmates.com/v1/customers/cus_MASWsf9DntbhIV/delivery_quotes";
    var response = $.ajax({
        type: 'POST',
        url: URL,
        headers: deliveryAPIkeySandbox,
        data: {
            dropoff_address: resturantAddress,
            pickup_address: pickupAddress
        },
        success: function(data) {
            console.log(data);
            // TODO get username from DB/ or from user
            // jsonToSQL(data);

            // send JSON data to Al to display

            /*
            
                Reply is in JSON form
                {
                    kind: "delivery_quote", 
                    id : "SOME STRING",
                    created: "YYYY-MM-DD-THH:MM:SSZ",
                    expired: "SAME AS ABOVE",
                    fee: $$$,
                    currency: "usd",
                    dropoff_eta: "SAME AS CREATED AND EXPIRED",
                    duration: "NUM"
                }

            */
        } 
    });
}

// function requestPostMatesOrder(resturantAddress, pickupAddress) {
//     var URL = "https://api.postmates.com/v1/customers/cus_MASWsf9DntbhIV/delivery_quotes";
//     var response = $.ajax({
//         type: 'POST',
//         url: URL,
//         headers: deliveryAPIkeySandbox,
//         data: {
//             dropoff_address: resturantAddress,
//             pickup_address: pickupAddress
//         },
//         success: function(data) {
//             console.log(data);
//             jsonToSQL(data);

//             // send JSON data to Al to display

//             /*
            
//                 Reply is in JSON form
//                 {
                        // “id”: “del_K7SD1dUd5aqLU-”
                        // “kind”: “delivery”,
                        // “live_mode”: false,
                        // “status”: “pending”,
                        // “complete”: false,
                        // “updated”: “2014–12–09T19:31:22Z”,
                        // “fee”: 799,
                        // “currency”: “usd”, 
                        // “quote_id”: “dqt_K7SCxZJzteH9R-”,
                        // “courier”: null,
                        // “created”: “2014–12–09T19:31:22Z”,
                        // “manifest”: {
                        // “description”: “1 Stuffed Puppy”
                        // },
                        // “pickup”: {
                        // “phone_number”: “555–555–5555”,
                        // “notes”: “Just come inside, give us order #123”,
                        // “location”: {
                        // “lat”: 37.7930812,
                        // “lng”: -122.395944
                        // },
                        // “name”: “Puppies On-Demand”,
                        // “address”: “101 Market Street”
                        // },
                        // “dropoff”: {
                        // “phone_number”: “415–555–5555”,
                        // “notes”: “”,
                        // “location”: {
                        // “lat”: 37.7811372,
                        // “lng”: -122.4123037
                        // },
                        // “name”: “Alice Customer”,
                        // “address”: “20 McAllister Street”
                        // },
                        // “dropoff_deadline”: “2014–12–09T20:31:22Z”,
                        // “pickup_eta”: null,
                        // “dropoff_eta”: null,
                        // }
//             */
//         } 
//     });
// }

function storeTransactionToJSON(jsonData, user_name, user_num_transaction) {
    var json = JSON.stringify(jsonData);
    var fs = require('fs');
    // could be changed to add the transaction date (and time) top the name of the json file
    var filename = btoa(username + user_num_transaction + ".json");

    fs.writeFile(filename, json, 'utf8', callback);
}

function storeMiscToJSON(data, filename) {
    var json = JSON.stringify(data);
    var fs = require('fs');
    fs.writeFile(filename, json, 'utf8', callback);
}

function readFromJSONFile(filename) {
    var fs = require('fs');
    var obj = null;
    fs.readFile(filename, 'utf8', function readFileCallback(err, data) {
        if(err) {
            console.log(err);
        }
        else {
            obj = JSON.parse(data);
        }
    });
    return obj;
}

function jsonToSQL(jsonData) {
    var db = openDatabase({name : 'TransactionDatabase.db'});
    db.transaction(function(tx) {
        // where user_name is:
        // user_contact is:
        // user_address is:
        tx.executeSQL(
            'INSERT INTO table_transaction (fee, pickup, dropoff, name, status) VALUES (?,?,?,?,?)',
            [jsonData["fee"], jsonData["pickup"], jsonData["dropoff"], jsonData["name"], jsonData["status"]]
        )
    });
}

function registerUserToSQL(user_name, user_contact, user_address) {
    var db = openDatabase({name : 'UserDatabase.db'});
    db.transaction(function(tx) {
        // where user_name is:
        // user_contact is:
        // user_address is:
        tx.executeSQL(
            'INSERT INTO table_user (user_name, user_contact, user_address) VALUES (?,?,?)',
            [user_name, user_contact, user_address]
        )
    });
}