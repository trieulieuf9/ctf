// This is a mess

const turnMap = {"left": -1, "middle": 0, "right": 1}
function calcIndex(shift, indices) {
   return scanArray[shift+indices[0]] + scanArray[shift+indices[1]] + scanArray[shift+indices[2]]
}

function countZero(array) {
  return array.slice(0,7).filter(v => v === 0).length;
}

function currentPosition(array) {
  const zeros = countZero(array)
  let pos = "soso"
  if (zeros == 1) {
    pos = "right"
  } else if (zeros < 4) {
    pos = "~right"
  } else if (zeros == 4) {
    pos = "middle"
  } else if (zeros < 7) {
    pos = "~left"
  } else if (zeros == 7) {
    pos = "left"
  }
  return pos;
}

let shift = countZero(scanArray) - 4
let currentPos = currentPosition(scanArray)

leftIndex = calcIndex(shift, [4,5,6])
middleIndex = calcIndex(shift, [7,8,9])
rightIndex = calcIndex(shift, [10,11,12])

let turn;

if (!turn) {
    if ((middleIndex >= leftIndex) && (middleIndex >= rightIndex)) {
        turn = "middle"
    } else if (leftIndex > rightIndex) {
        turn = "left"
    } else {
        turn = "right"
    }
}

if (turn === "middle" && !(currentPos === "middle")) {
  console.log("go to middle")
  if (currentPos === "right" || currentPos === "~right") {
    turn = "left"
  } else {
    turn = "right"
  }
}

console.log("currentPos === middle", (currentPos === "middle"));
console.log("currentPos === turn", currentPos === turn);
if (!(currentPos === "middle") && currentPos === turn) {
  console.log("hey????")
  turn = "middle"
}


console.log(scanArray, leftIndex, middleIndex, rightIndex, shift, currentPos, turn)
return turnMap[turn];