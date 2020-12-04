const fs = require('fs');
const readline = require('readline');

//const fileStream = fs.createReadStream('input.txt');
//const rl = readline.createInterface({input:fileStream, crlfDelay: Infinity});
var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('input.txt')
});

tmpPass = {};
passList = [];

const requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]; // "cid"
const chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"] // you can prolly do some hex shit here
const ecl = ["amb","blu","brn","gry","grn","hzl","oth"]


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
      //console.log(field);
    } else if(valid) {

      switch(field) {
        case "byr":
          tmp = parseInt(tmpPass[field]);
          if (tmp >= 1920 && tmp <= 2002) {
            valid = valid;
          }
          else {
            
            console.log("invalid byr: " + tmp);
            valid = false;
          }
          break;
        case "iyr":
          tmp = parseInt(tmpPass[field]);
          if (tmp >= 2010 && tmp <= 2020) {
            valid = valid;
          }
          else {
            valid = false;
            console.log("invalid iyr: " + tmp);
          }
          break;
        case "eyr":
          tmp = parseInt(tmpPass[field]);
          if (tmp >= 2020 && tmp <= 2030) {
            valid = valid;
          }
          else {
            valid = false;
            console.log("invalid eyr: " + tmp);
          }
          break;
        case "hgt":
          if (tmpPass[field].includes("cm")) {
            hgt = parseInt(tmpPass[field].substring(0, tmpPass[field].indexOf("c")))
            valid = (hgt >= 150 && hgt <= 193)
          } else if (tmpPass[field].includes("in")) {
            hgt = parseInt(tmpPass[field].substring(0, tmpPass[field].indexOf("i")))
            valid = (hgt >= 59 && hgt <= 76)
          } else {
            valid = false;
          }
          if (!valid) console.log("invalid hgt: " + tmpPass[field]);
          break;
        case "hcl":
          if (tmpPass[field].charAt(0) != "#") {valid = false; console.log("wrong first char for hcl:"+tmpPass[field].charAt(0))}
          for (const c of tmpPass[field].substring(1)) {
            if (valid && !chars.includes(c)) {valid = false;console.log("invalid char in hcl: " + tmpPass[field] + ", char: " + c);}
          }
          if (!valid) console.log("invalid hcl: " + tmpPass[field]);
          break;
        case "ecl":
          valid = ecl.includes(tmpPass[field]); 
          if (!valid) console.log("invalid ecl: " + tmpPass[field]);
          break;
        case "pid":
          valid = (tmpPass[field].length == 9);
          if (!valid) console.log("invalid pid: " + tmpPass[field]);
          break;
      }
    }
  });
  if (valid) {
    passList.push(1); //idk how cloning works man
    tmpPass = {};
    console.log(passList.length);
  }
  else {
    //console.log("invalid");
    //console.log(tmpPass);
    tmpPass = {};
    console.log(passList.length);
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
