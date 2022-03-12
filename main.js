// function solution(s) {
//   var answer = -1;
//   reg =
//     /a{2}|b{2}|c{2}|d{2}|e{2}|f{2}|g{2}|h{2}|i{2}|j{2}|k{2}|l{2}|n{2}|m{2}|o{2}|p{2}|q{2}|r{2}|v{2}|s{2}|t{2}|u{2}|v{2}|w{2}|x{2}|y{2}|z{2}/g;
//   // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
//   while (s.match(reg) != null) {
//     s = s.replace(reg, "");
//     if (s.length % 2 == 1) {
//       return 0;
//     }
//     if (s.length == 0) {
//       return 1;
//     }
//   }
//   if (s.length == 0) {
//     return 1;
//   } else {
//     return 0;
//   }
//   console.log(s.match(reg));
//   return 0;
// }
function solution(s) {
  var answer = -1;
  let flag = true; //match유지
  while (flag && s.length > 0) {
    if (s.length % 2 == 1 || s.length == 0) {
      flag = false;
      break;
    }
    let i = 0;
    for (i = 0; i < s.length; i++) {
      if (i == s.length - 1) {
        flag = false;
      }
      if (s[i] == s[i + 1]) {
        let regex = new RegExp(s[i] + s[i], "g");
        s = s.replace(regex, "");
        break;
      }
    }
  }
  if (flag && s.length == 0) {
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
