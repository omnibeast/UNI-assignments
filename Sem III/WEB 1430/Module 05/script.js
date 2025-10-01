//function to initialize the dashboard
function initializeDashboard() {
    const container = document.getElementById('mission-container');

    //creating title
    const title = document.createElement('h1');
    title.textContent = 'Secret Agent Dashboard';
    container.appendChild(title);

    //creating mission list
    const missionList = document.createElement('ul');
    missionList.id = 'mission-list';

    const missions = ['Decode encrypted message', 'Gather intel', 'Disable security system'];
    missions.forEach(mission => {
        const li = document.createElement('li');
        li.textContent = mission;
        missionList.appendChild(li);
    });
    container.appendChild(missionList);
}

//functions to add missions
function addMission(mission) {
    const missionList = document.getElementById('mission-list');
    const li = document.createElement('li');
    li.textContent = text;
    missionList.appendChild(li);
}

//function to update a mission
function updateMission(index, newText) {
    const missionList = document.getElementById('mission-list');
    const items = missionList.getElementsByTagName('li');
    if (index >= 0 && index < items.length) {
        items[index].textContent = newText;
    }
}

//function to remove a mission
function removeMission(index) {
    const missionList = document.getElementById('mission-list');
    const items = missionList.getElementsByTagName('li');
    if (index >= 0 && index < items.length) {
        missionList.removeChild(items[index]);
    }
}

//function to insert a mission after another
function insertAfter(newText, referenceIndex) {
    const missionList = document.getElementById('mission-list');
    const items = missionList.getElementsByTagName('li');

    if (referenceIndex >= 0 && referenceIndex < items.length) {
        const li = document.createElement('li');
        li.textContent = newText;
        items[referenceIndex].insertAdjacentElement('afterend', li);
    }
}

