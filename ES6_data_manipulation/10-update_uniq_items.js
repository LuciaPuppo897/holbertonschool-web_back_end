export default function updateUniqueItems(groceryMap) {
  if (!(map instanceof Map)) throw new Error('cannont process');
  for (const [item, quantity] of groceryMap.entries()) {
    if (quantity === 1) {
      groceryMap.set(item, 100);
    }
  }

  return groceryMap;
}
