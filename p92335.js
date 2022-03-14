function solution(n, k) {
  let kNumber = n.toString(k); //k진수로 변환
  let list = kNumber.split("0"); //kNumber을 문자열로 자동 형변환후 "0"으로 split
  var answer = 0;
  for (let x of list) {
    let temp = parseInt(x);
    if (!isNaN(temp) && isPrime(temp)) {
      answer += 1;
    }
  }
  return answer;
}
function isPrime(num) {
  if (num <= 1) {
    // 음수와 1은 소수가 아니다
    return false;
  }

  // 2는 짝수 중 유일한 소수이다
  if (num % 2 === 0) {
    return num === 2 ? true : false;
  }

  // 이제 num이 홀수 일때 다른 수에 나눠지는지 판별한다

  // Math.sqrt(num) 즉, √num까지 나눠 떨어지는지 검사한다
  // 원리는 아래글 "에라토스테네스의 체" 참고

  const sqrt = parseInt(Math.sqrt(num));

  for (let divider = 3; divider <= sqrt; divider += 2) {
    if (num % divider === 0) {
      return false;
    }
  }
  console.log(num);
  return true;
}
s = "FRANCE";
s2 = "french";
console.log(solution(437674, 3));
// console.log(solution(s));
// console.log(solution(s2));

document.querySelector("#result").innerHTML = solution(437674, 3);
