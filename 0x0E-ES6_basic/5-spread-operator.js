export default function concatArrays(array1, array2, string) {
  const arr1 = [...array1, ...array2, ...string];
  return arr1;
}
