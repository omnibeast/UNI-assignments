const express = require('express');
const SocInfoApp = express();
const cors = require('cors');

/* TODO: You can change the data below to provide your own data */

const SoCInfoDB = [
{
id:'cs',
title:'Computer Science',
url: 'https://www.weber.edu/cs/', 
logo: 'http://localhost:3000/compsci_stacked.png',
video: 'https://1533221.mediaspace.kaltura.com/media/EAST_School+of+Computing/1_09uite8y/192676563'

},
{
id:'webux',
title:'Web and User Experience',
url: 'https://www.weber.edu/webux/',
logo: 'http://localhost:3000/wue_stacked.png',
video: 'https://1533221.mediaspace.kaltura.com/media/EAST_School+of+Computing/1_09uite8y/192676563'

},
{
id:'cyber',
title:'Cybersecurity and Network Management',
url: 'https://www.weber.edu/cyber/',
logo: 'http://localhost:300/cnmt_stacked.png',
video:'https://1533221.mediaspace.kaltura.com/media/EAST_School+of+Computing/1_09uite8y/192676563'

}
]
SocInfoApp.use(express.json());
SocInfoApp.use(express.static('public'));

/* TODO: Replace the origin id with the URL generated for your index.html page on client side*/
  var corsOptions = {
  origin: 'http://127.0.0.1:8081'
}
  
SocInfoApp.get('/api/info', cors(corsOptions), (req, res) => {
  

  /* TODO: Based on the data you have, you can use different vairable than departments */
 console.log(req);
  const data = {
    message: "OK",
    status: 200,
    departments:SoCInfoDB
  };
  //console.log(res);
  res.json(data);
});

SocInfoApp.listen(3000, () => {
  console.log('api location:   ' + 'http://localhost:3000/api/info')
  console.log("Server started. Now try to access your html file by operning it in browser.")
});