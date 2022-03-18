function solution(s) {
  let list = s.slice(2, s.length - 2).split("},{");
  let set = new Set();
  let dict = {};
  for (let x of list) {
    let numList = x.split(",");
    for (number of numList) {
      let n = parseInt(number);
      set.add(n);
      if (n in dict) dict[n] += 1;
      else dict[n] = 1;
    }
  }
  let result = Array.from(set);
  result.sort(function (a, b) {
    return dict[b] - dict[a];
  });
  console.log(result);
  console.log(dict);
  return result;
}
var result = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}");
console.log(result);

document.querySelector("#result").innerHTML = result;
