var redis = require('redis')
var multer  = require('multer')
var express = require('express')
var httpProxy = require('http-proxy')
var fs      = require('fs')
var http = require('http');
var app = express()
// REDIS

var client = redis.createClient(6379, '127.0.0.1', {})

client.flushall();

client.lpush("serving_ips", 'http://127.0.0.1:8081')
client.lpush("serving_ips", 'http://127.0.0.1:8081')
client.lpush("serving_ips", 'http://127.0.0.1:8081')
client.lpush("serving_ips", 'http://127.0.0.1:8082')
///////////// WEB ROUTES

// Add hook to make it easier to get all visited URLS.
app.use(function(req, res, next) 
{
	console.log(req.method, req.url);

	// ... INSERT HERE.

	next(); // Passing the request to the next handler in the stack.
});


//var TARGET   = 'http://127.0.0.1:3000';

// Proxy.
var options = {};
var proxy   = httpProxy.createProxyServer(options);

var proxy_server  = http.createServer(function(req, res){
    client.rpoplpush("serving_ips","serving_ips", function (err,value) {

    console.log(value)
    proxy.web( req, res, {target: value } );
    //console.log('Example app listening at http://%s:%s', host, port)
    })
 
});

proxy_server.listen(4000,function () {
  console.log('proxy server started  at http://%s:%s', proxy_server.address().address, proxy_server.address().port)
});
