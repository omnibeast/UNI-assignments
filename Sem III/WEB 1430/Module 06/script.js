const addButton = document.getElementById('add-button');
const itemInput = document.getElementById('item-input');
const itemList = document.getElementById('item-list');

//function to add new item
addButton.addEventListener('click', () => {
  const itemText = itemInput.value.trim();

  if (itemText === '') return;

  const li = document.createElement('li');

  const span = document.createElement('span');
  span.textContent = itemText;

  const editBtn = document.createElement('button');
  editBtn.textContent = 'Edit';

  const deleteBtn = document.createElement('button');
  deleteBtn.textContent = 'Delete';

  li.appendChild(span);
  li.appendChild(editBtn);
  li.appendChild(deleteBtn);

  itemList.appendChild(li);

  itemInput.value = '';

  //function to delete item
  deleteBtn.addEventListener('click', () => {
    itemList.removeChild(li);
  });

  //function to edit item
  editBtn.addEventListener('click', () => {
    const newItem = prompt('Edit item:', span.textContent);
    if (newItem !== null && newItem.trim() !== '') {
      span.textContent = newItem.trim();
    }
  });
});
