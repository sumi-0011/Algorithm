function solution(s) {
  var answer = -1;
  list = [];
  if (s.length % 2 == 1) {
    //홀수면 바로 리턴
    return 0;
  }
  for (let i = 0; i < s.length; i++) {
    if (s[i] == list[list.length - 1]) {
      //pop() 메서드는 배열에서 마지막 요소를 제거하고 그 요소를 반환
      //같은 문자
      list.pop();
    } else {
      list.push(s[i]);
    }
  }
  console.log(list);
  if (list.length == 0) {
    return 1;
  } else {
    return 0;
  }
}
s = "baabaa";
s2 = "cdcd";
console.log(solution(s));
console.log(solution(s2));

// document.querySelector("#result").innerHTML = solution(s);
