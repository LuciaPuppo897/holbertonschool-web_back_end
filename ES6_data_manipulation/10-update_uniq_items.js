export default function updateUniqueItems(groceryMap) {
  for (const [item, quantity] of groceryMap.entries()) {
    if (quantity === 1) {
      groceryMap.set(item, 100);
    }
  }

  return groceryMap;
}
