

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



console.log(SoCInfoDB)

document.querySelector('#fetch-data').addEventListener('click', function(e){

    fetch('http://localhost:3000/api/info')
    .then((response) => response.json())
    .then((json) => showData(json))
    .catch((error) => console.log(error));
})



function showData(responseJson){

    console.log(responseJson.departments);
    responseJson.departments.forEach(element => {
        const li = document.createElement('li');
        li.innerHTML = `<strong>${element.title}</strong> --- <i>${element.url} </i>`;
        document.querySelector('ul').appendChild(li);
    });
    

}


