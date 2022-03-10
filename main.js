// include 쓰는 법 찾기!

function solution(lottos, win_nums) {
  const rank = [6, 6, 5, 4, 3, 2, 1]; // 6까지 존재이므로 length == 7
  let [cnt, zeroCnt] = [0, 0]; //초기값

  for (const x of lottos) {
    if (x == 0) {
      zeroCnt++;
    } else if (win_nums.includes(x)) {
      cnt++;
    }
  }
  console.log(cnt, zeroCnt);
  return [rank[cnt + zeroCnt], rank[cnt]];
}

lottos = [45, 4, 35, 20, 3, 9];
win_nums = [20, 9, 3, 45, 4, 35];
console.log(solution(lottos, win_nums));
