export default function cleanSet(set, startString) {
  const Str = [];
  if (!startString || startString.length === 0)  
    return ''; 

  Array.from(set).map((a) => {
    const position = a.search(startString);

    if (position !== 1) Str.push(a.slice(position + startString.length));
    return null;
  });

  return Str.join('-');
}
