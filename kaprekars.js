let count = 1;
function KaprekarsConstant(num) {
  let numAsString = num.toString();
  if (numAsString.length !== 4) {
    numAsString += '0';
  }
  const numAsArray = numAsString.split('');
  const ascending = numAsArray.sort();
  const ascendingAsNumber = arrayAsNumber(ascending);
  const descending = ascending.reverse();
  const descendingAsNumber = arrayAsNumber(descending);
  const difference = descendingAsNumber - ascendingAsNumber;
  if (difference === 6174) {
    return count;
  }
  count ++;
  return KaprekarsConstant(difference);
}

function arrayAsNumber(numberArray) {
  const numberAsString = numberArray.join('');
  const number = Number(numberAsString);
  return number;
}

KaprekarsConstant(testNum);
