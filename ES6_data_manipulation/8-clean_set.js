export default function cleanSet(set, startString) {
  if (!(set instanceof Set) || typeof startString !== 'string') {
    throw new Error();
  }

  const filteredValues = Array.from(set).filter(value => value.startsWith(startString)).map(value => value.slice(startString.length));

  return filteredValues.join('-');
}
