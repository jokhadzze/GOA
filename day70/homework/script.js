// 1. Log Each Element: Create an array of numbers and use forEach to log each number to the console.

const cars = ['BMW', 'Audi', 'Pagani']

cars.forEach((values)=>{
    console.log(values)
})



// 2. Calculate Sum: Use forEach to calculate the sum of an array of numbers and log the result.

const nums = [1,2,3,4,5]
res = 0
nums.forEach((values)=>{
    res+= values
})

console.log(res)



// 3. Print Student Names: Create an array of student names and use forEach to print each name in a formatted string.

const students = ['student1', 'student2', 'student3']

students.forEach((value)=>{
    console.log(`students are: ${value}`)
})


// 4. Double Values: Create an array of integers and use forEach to double each value and store the results in a new array.

newArr = []
nums.forEach((values)=>{
    newArr.push(values*2)
})

console.log(newArr)


// 5. Square Values: Use map to create a new array that contains the squares of each number from an existing array.

const doubled = nums.map(num => num ** 2)

console.log(doubled)


// 6. Extract Lengths: Create an array of strings and use map to create a new array that contains the lengths of each string.

let animeNames = ["Berserk", "Monster", "Vinland Saga"]
let strLengths = animeNames.map(string => string.length)

console.log(strLengths)


// 7. Convert to Uppercase: Create an array of lowercase strings and use map to convert each string to uppercase.

let uppers = animeNames.map(string => string.toUpperCase())

console.log(uppers)



// 8. Filter Even Numbers: Use filter to create a new array containing only the even numbers from an existing array of integers.

const numbers = [0, -6, 7, 9, 1]

const filtered = numbers.filter((number)=>{
    return number % 2 === 0
})

console.log(filtered)



// 9. Find Long Names: Create an array of names and use filter to find names that are longer than 5 characters.

const strings = ['tie', 'wrong', 'ar vici']

const filteredArr = strings.filter((string)=>{
    return string.length>3
})

console.log(filtered)



// 10. Filter Positive Numbers: Use filter to create a new array containing only the positive numbers from an array of integers.

const positive = numbers.filter((number)=>{
    return number>0
})

console.log(filtered)