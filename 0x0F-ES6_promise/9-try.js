export default function guardrail(mathFunction) {
  const queue = [];
  const procMsg = 'Guardrail was processed';
  try {
    const maths = mathFunction();
    queue.push(maths, procMsg);
  } catch (err) {
    queue.push(`Error: ${err.message}`, procMsg);
  }
  return queue;
}
