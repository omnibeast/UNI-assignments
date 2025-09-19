const adventure = {
    locations: ["Ancient Ruins", "Forbidden Forest", "Sunken Ship", "Mountain Peak", "Hidden Valley"],
    actions: ["explore", "escape", "discover treasure in", "climb", "navigate"],
    characters: ["an intrepid explorer", "a cunning pirate", "a mysterious stranger", "a daring adventurer", "a curious wizard"]
  };

function generateAdventure() {
    const location = adventure.locations[Math.floor(Math.random() * adventure.locations.length)];
    const action = adventure.actions[Math.floor(Math.random() * adventure.actions.length)];
    const character = adventure.characters[Math.floor(Math.random() * adventure.characters.length)];

    console.log(`You will ${action} ${location} with ${character}!`);
}

function addAdventure(array, newOption) {
    array.push(newOption);
    console.log(`New option added:`, array);
}

addAdventure(adventure.locations, "Mystic Caves");


generateAdventure();
generateAdventure();
generateAdventure();
