function solution(numbers) {
  console.log(numbers);
  numbers.sort((a, b) => {
    return a - b;
  });
  var answer = 0;
  let index = 0;
  for (let i = 0; i < 10; i++) {
    if (numbers[index] != i) {
      answer += i;
    } else {
      index++;
    }
  }

  return answer;
}
s = "FRANCE";
s2 = "french";
result = solution([5, 8, 4, 0, 6, 7, 9]);
console.log(solution(result));

document.querySelector("#result").innerHTML = result;
