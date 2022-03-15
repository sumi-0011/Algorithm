function solution(fees, records) {
  const inCar = {}; //입차 되어 있는 차량의 입차 시간 (차량번호 - 입차시간)
  const accrueParkingTime = {}; //차량 누적 시간 (차량번호 - 누적 시간)

  for (let string of records) {
    [time, number, move] = string.split(" ");
    // console.log(time, number, move);

    if (move === "IN") {
      //입차
      //입차시에는 차량 입차시간 inCar에 입차시간 추가
      inCar[number] = time;
    } else {
      //출차
      //출차시에는 출차시간 - 입차시간을 누적 시간에 추가
      //inCar에서 차량 삭제
      const inTimeList = inCar[number].split(":");
      const outTimeList = time.split(":");
      const inTime = parseInt(inTimeList[0]) * 60 + parseInt(inTimeList[1]);
      const outTime = parseInt(outTimeList[0]) * 60 + parseInt(outTimeList[1]);
      if (number in accrueParkingTime) {
        //이미 누적시간이 존재하는 차량인 경우
        accrueParkingTime[number] += outTime - inTime; //누적 시간 저장
      } else {
        accrueParkingTime[number] = outTime - inTime; //누적 시간 저장
      }

      delete inCar[number]; //출차 후 입차시간 정보 삭제
    }
  }
  for (let number in inCar) {
    const inTimeList = inCar[number].split(":");
    const inTime = parseInt(inTimeList[0]) * 60 + parseInt(inTimeList[1]);
    const outTime = 23 * 60 + 59;
    if (number in accrueParkingTime) {
      //이미 누적시간이 존재하는 차량인 경우
      accrueParkingTime[number] += outTime - inTime; //누적 시간 저장
    } else {
      accrueParkingTime[number] = outTime - inTime; //누적 시간 저장
    }
  }
  // console.log("inCar", inCar);
  // console.log("누적", accrueParkingTime);
  var answer = [];
  const keyList = Object.keys(accrueParkingTime).sort();
  // console.log(key);

  for (let carNumber of keyList) {
    // 기본 시간, 기본 가격, 단위 시간, 단위 요금
    if (accrueParkingTime[carNumber] <= fees[0]) {
      // 기본 가격
      answer.push(fees[1]);
    } else {
      // 기본 가격 + ((누적 시간 - 기본 시간) / 단위 시간) * 단위 요금
      answer.push(
        fees[1] +
          Math.ceil((accrueParkingTime[carNumber] - fees[0]) / fees[2]) *
            fees[3]
      );
    }
  }
  return answer;
}
var result = solution(
  [180, 5000, 10, 600],
  [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
  ]
);
console.log(result);

document.querySelector("#result").innerHTML = result;

