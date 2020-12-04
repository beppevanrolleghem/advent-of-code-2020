const fs = require('fs');
const readline = require('readline');

//const fileStream = fs.createReadStream('input.txt');
//const rl = readline.createInterface({input:fileStream, crlfDelay: Infinity});
var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('input.txt')
});

tmpPass = {};
passList = [];

var requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]; // "cid"

async function parseLine(line) {
  line.split(" ").forEach(str => {
    key = str.split(":")[0];
    val = str.split(":")[1];
    tmpPass[key] = val;
  });
}


async function finalisePassword() {
  valid = true;
  requiredFields.forEach(field => {
    if (!Object.keys(tmpPass).includes(field) && valid == true) {
      valid = false;
      console.log(field);
    } else if(valid) {
      switch(field) {
        case "byr":
          tmpPass[field] = parseInt(tmpPass[field]);
          valid = (tmpPass[field] >= 1920 && tmpPass <= 2002)
          break;
        case "iyr":
          tmpPass[field] = parseInt(tmpPass[field]);
          valid = (tmpPass[field] >= 2010 && tmpPass <= 2020)
          break;
        case "eyr":
          tmpPass[field] = parseInt(tmpPass[field]);
          valid = (tmpPass[field] >= 2020 && tmpPass <= 2030)
          break;
        case "hgt":
          if (tmpPass[field].includes("cm")) {
            hgt = parseInt(tmpPass[field].substring(0, tmpPass[field].indexOf("c")))
            valid = (hgt >= 150 && hgt <= 193)
          } else if (tmpPass[field].includes("in")) {
            hgt = parseInt(tmpPass[field].substring(0, tmpPass[field].indexOf("i")))
            valid = (hgt >= 150 && hgt <= 193)
          } else {
            valid = false;
          }
          break;
        case "hcl":
          //nog geen zin
          break;
        case "ecl":
          break;
        case "pid":
          break;
      }
    }
  });
  if (valid) {
    passList.push(1); //idk how cloning works man
    tmpPass = {};
    console.log(passList.length+1);
  }
  else {
    tmpPass = {};
  }
}

lineReader.on('line', async function (line) {

  if (line.length == 0) {
    await finalisePassword();
  } else {
    await parseLine(line);
  }
});

//for (const line of rl) {
//  console.log(line);
//}
