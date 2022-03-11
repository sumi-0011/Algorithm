function solution(s) {
  let list = [
    /zero/g,
    /one/g,
    /two/g,
    /three/g,
    /four/g,
    /five/g,
    /six/g,
    /seven/g,
    /eight/g,
    /nine/g,
  ];
  for (let i = 0; i < list.length; i++) {
    s = s.replace(list[i], i + "");
  }
  return parseInt(s);
}

s = "2three45sixseven";
console.log(solution(s));
