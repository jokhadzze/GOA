// შექმენით ფუნქცია სახელად manualFilter რომელსაც პირველი გადაეცემა ფუნქცია და მეორე მასივი, 
// ამ ფუნქციაში უნდა გამოიყენოთ for ციკლი და გადაუარეთ გადმოცემულ მასივს, გამოიყენეთ if და 
// გამოიძახეთ გადმოცემული ფუნქცია ამჟამინდელ ინდექსზე მდგომი მნიშნელობით, თუ დაბრუნებული 
// მნიშნელობა არის true დაამატეთ ახალ მასივში და თუ არის false არ დაამატოთ ახალ მასივში, როცა 
// მორჩება for ციკლის მუშაობა დააბრუნეთ ახალი მასივი, გადაცემული ფუნქციიდან აუცილებლად უნდა 
// ბრუნდებოეს boolean მნიშვნელობა, და უნდა იღებდეს ერთ მნიშნელობას გადაცემულ ფუნქციაში რას 
// შეამოწმებთ თქვენზეა დამოკიდებული

function manualFilter(func, arr) {
    let filteredArray = []
    
    // გადავიაროთ მასივი for ციკლით
    for (let i = 0; i < arr.length; i++) {
        // თუ გადმოცემული ფუნქციის შედეგი true-ა, ვამატებთ ახალ მასივში
        if (func(arr[i])) {
            filteredArray.push(arr[i])
        }
    }
    
    // ვაბრუნებთ ახალ გაფილტრულ მასივს
    return filteredArray
}

// მაგალითი: ფილტრაცია ლუწი რიცხვების მიხედვით
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function isEven(num) {
    return num % 2 === 0
}

let evenNumbers = manualFilter(isEven, numbers)
console.log(evenNumbers); // [2, 4, 6, 8, 10]








console.log(Math.sqrt(64))
console.log(Math.ceil(7.1))
console.log(Math.floor(7.9))
console.log(Math.trunc(9.1))
console.log(Math.pow(3,7))
console.log(Math.abs(-11.12))
console.log(Math.min(3,6,-9,0))
console.log(Math.max(3,6,-9,0))




const interval = setInterval(function() {
    const now = new Date();
    const currentMinute = now.getMinutes()

    if (currentMinute === 35) {
        console.log("Interval stopped. Minute is 35.")
        return
    }

    console.log("Current time: " + now)
}, 1000)





const dt = new Date()
console.log(dt.getFullYear())
console.log(dt.getMonth())
console.log(dt.getDate())
console.log(dt.getDay())
console.log(dt.getHours())
console.log(dt.getMinutes())
console.log(dt.getSeconds())
console.log(dt.getMilliseconds())





let date1 = new Date("2022-03-25")

let date2 = new Date("October 13, 2014 11:13:00")


console.log(date1.getFullYear())
console.log(date1.getMonth() + 1)
console.log(date1.getDate())
console.log(date1.getHours())
console.log(date1.getMinutes())
console.log(date1.getSeconds())


console.log(date2.getFullYear())
console.log(date2.getMonth())
console.log(date2.getDate())
console.log(date2.getHours())
console.log(date2.getMinutes())
console.log(date2.getSeconds())

