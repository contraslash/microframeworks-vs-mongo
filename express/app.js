const express = require('express')
const mongodb = require('mongodb')

const app = express()
var MongoClient = mongodb.MongoClient
url = 'mongodb://localhost:27017/framework_benchmark'

var db

MongoClient.connect(url, (err, database)=>
  {
      if (err)
      {
        return console.log(err)
      }
      db = database;
  })


app.get(
  '/',
  function(req, res)
  {
	   res.send('Hello World!')
  })

app.get(
  '/data',
  function(req, res)
  {
    db.collection('dummy_data').find().toArray((err, results)=>
    {
        if(err)
        {
          res.send(err)
        }
        else
        {
          res.send(results)
        }
    })
  }
)

app.listen(4000, ()=>{console.log("Running in port 3000")})
