// Inventory Management System
// defining initial inventory
let inventory = [
    { id: 1, name: "Wireless Mouse", category: "Electronics", quantity: 50, price: 29.99 },
    { id: 2, name: "Keyboard", category: "Electronics", quantity: 25, price: 49.99 },
    { id: 3, name: "Notebook", category: "Stationery", quantity: 100, price: 2.5 },
    { id: 4, name: "Pen", category: "Stationery", quantity: 200, price: 1.2 },    

];

// function to add new product
function addProduct(name, category, quantity, price) {
    if (quantity <= 0 || price <= 0) {
        console.error("Error: Quantity and price must be positive numbers.");
        return;
    }

    const newProduct = {
        id: inventory.length > 0 ? inventory[inventory.length - 1].id + 1 : 1,
        name,
        category,
        quantity,
        price
    };
    inventory.push(newProduct);
    console.log(`Product "${name}" added successfully.`);
}

// function to remove product 
function removeProduct(id) {
    const index = inventory.findIndex(product => product.id === id);
    if (index === -1) {
        console.error(`Error: Product not found.`);
        return;
    }
    const removed = inventory.splice(index, 1);
    console.log(`Product "${removed[0].name}" removed successfully.`);
}

// function to update product quantity
function updateProductQuantity(id, newQuantity) {
    if (newQuantity < 0) {
        console.error("Error: Quantity cannot be negative.");
        return;
    }

    const product = inventory.find(p => p.id === id);
    if (!product) {
        console.error("Error: Product not found.");
        return;
    }
    product.quantity = newQuantity;
    console.log(`Product "${product.name}" quantity updated to ${newQuantity}.`);
}

// function to generate inventory report
function generateReport() {
    console.log("Inventory Report:");
    inventory.forEach(product => {
        const status = product.quantity < 10 ? " (Low Stock)" : "In Stock";
        console.log(`${product.name} (${product.category}) - Quantity: ${product.quantity}, Price: $${product.price.toFixed(2)} - ${status}`);       

    });
}

// function to filter products by category
function filterByCategory(category) {
    const results = inventory.filter(product => product.category.toLowerCase() === category.toLowerCase());
    if (results.length === 0) {
        console.log(`No products found in category "${category}".`);
    } else {
        console.log(`Products in category "${category}":`, results);
        }
    }

// function to calulate total inventory value
function calculateTotalInventoryValue() {
    const totalValue = inventory.reduce((sum, product) => sum + (product.price * product.quantity), 0);
    console.log(`Total Inventory Value: $${totalValue.toFixed(2)}`);
}

// function for low stock alert
function lowStockAlert(threshold = 10) {
    const lowStockItems = inventory.filter(product => product.quantity < threshold);
    if (lowStockItems.length === 0) {
        console.log("No low stock items.");
    } else {
        console.log("Low Stock Alert:");
        lowStockItems.forEach(item => {
            console.log(`${item.name} - Quantity: ${item.quantity}`);
        });
    }
}
