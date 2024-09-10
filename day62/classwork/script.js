let masivi = []

for(let i = 0; i < 100; i++){
    Array.push(i)
}

let evenSum = 0
for(let i = 0; i < evenSum.length; i++){
    if(i % 2 === 0){
        evenSum += i;
    }
}


const cars = ["BMW", "Mustang", "Audi", "Mercedes"];
cars.push("Honda");

// ამატებს კონკრეტულ მნიშვნელობას სიაში

const Cars = ["BMW", "Mustang", "Audi", "Mercedes"];
Cars.pop();

//აშორებს ბოლო ელემენტს

const cArs = ["Banana", "Orange", "Apple", "Mango"];
cArs.shift();

// შლის ბოლო ელემენტს

const caRs = ["BMW", "Mustang", "Audi", "Mercedes"];
caRs.unshift("Honda", "Opel");

// ამატებს ელემენტებს სიაში

const carS = ["BMW", "Mustang", "Audi", "Mercedes"];
carS.splice(2,0,"Honda");

// კონკრეტულ ინდექსზე/პოზიციაზე ამატებს/შლის ელემენტს(ამ შემთხვევაში წაშალა 0 ელემენტი, დაამატა ჰონდა)

const CARS = ["BMW", "Mustang", "Audi", "Mercedes"];
const theBestOne = CARS.slice(1);

// ახალი სია იქმნება, რომელიც შედგება კონკრეტული ელემენტებისგან ძველი სიიდან(ამ შემთხვევაშ პირველ ინდექსამდე არსებული ანუ 0)



function manualSlice(arr, num1, num2){
    let slicedArr = new Array()
    for(let i = num1; i < num2; i++){
        slicedArr.push(arr[i])
    }

    console.log(slicedArr)
}


function manualReverse(arr){
    let reversedArr = new Array()
    for(let i = reversedArr.lenght - 1; i >=0; i--){
        reversedArr.push(arr[i]);
    }
}


function manualIndexOf(arr,element){
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === element){
            return i;
        }
    }
    return -1;
}


const arr = ["hello", "bye", "whatever"]
arr.indexOf('whatever')
arr.lastIndexOf()
arr.sort()
arr.reverse()