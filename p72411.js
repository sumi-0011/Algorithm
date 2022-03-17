function solution(orders, course) {
  var answer = [];
  let dict = {};
  for (let i of course) {
    let tempDict = {};

    for (let order of orders) {
      if (i > order.length) {
        continue;
      }
      let combis = combination(order.split(""), i);
      for (var x of combis) {
        let t = x.sort().join("");
        if (t in tempDict) tempDict[t] += 1;
        else {
          tempDict[t] = 1;
        }
        // console.log(t, tempDict[t]);
      }
    }
    dict[i] = tempDict;
  }
  for (const [dkey, dvalue] of Object.entries(dict)) {
    let maxCount = Math.max.apply(null, Object.values(dvalue));
    // console.log(dkey, maxCount);
    if (maxCount < 2) continue;
    for (const [key, value] of Object.entries(dvalue)) {
      if (value == maxCount) {
        // console.log(key, value);
        answer.push(key);
      }
    }
  }
  answer.sort();
  return answer;
}

function combination(arr, num) {
  const res = [];
  if (num === 1) return arr.map((v) => [v]);

  arr.forEach((v, idx, arr) => {
    const rest = arr.slice(idx + 1);
    const combinations = combination(rest, num - 1);
    const attach = combinations.map((combination) => [v, ...combination]);
    res.push(...attach);
  });
  return res;
}

var result = solution(["XYZ", "XWY", "WXA"], [2, 3, 4]);
console.log(result);

document.querySelector("#result").innerHTML = result;
