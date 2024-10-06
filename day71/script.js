// Swap the values of nums[0] and nums[1]
const nums = [1, 2];

[nums[0, nums[1]]] = [nums[1], nums[0]]

console.log(nums)


// Extract the name and age properties from the following object into separate variables.
const person = { name: 'Alice', age: 25, city: 'New York' };
// Extract the 'name' and 'age' properties

const { name, age } = person

console.log(name, age)


// Destructure the following nested array to get the value 4.
const nestedArray = [1, [2, 3, [4, 5]]];
// Extract the value 4

const [numb1,[numb2, numb3,[numb4, numb5]]] = nestedArray

console.log(numb4)



// Destructure the array and set a default value for a missing element.
const fruits = ['apple'];
// Destructure the first element and set 'banana' as the default for the second element

const [ obj1, obj2= 'banana' ] = fruits

console.log(obj1, obj2)



// Destructure the properties of the following object into variables with different names.
const user = { id: 101, username: 'john_doe' };
// Extract 'id' and 'username' into variables named 'userId' and 'userName'

const {userId = id, userName = username} = user

console.log(userId, userName)


// Use the spread operator to merge two arrays into one.
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
// Merge array1 and array2

const merged = [...array1, ...array2]
console.log(merged)



// Create a copy of the following array using the spread operator.
const colors = ['red', 'green', 'blue'];
// Create a copy of 'colors'

const clonedColors = [...colors]
console.log(clonedColors)



// Use the spread operator to merge two objects.
const objOne = { a: 1, b: 2 };
const objTwo = { c: 3, d: 4 };
// Merge obj1 and obj2

const mergedObjects = {...objOne, ...objTwo}

console.log(mergedObjects)



// Destructure the first element of the array and gather the rest of the elements using the rest operator.
const numbers = [10, 20, 30, 40, 50];
// Destructure the first element and gather the remaining elements

const [first, ...arr] = numbers

console.log(first, arr)



// Create a function that uses the rest parameter to accept multiple arguments and logs them as an array.
// Function that accepts multiple arguments

function logArgsAsArray(...arr) {
    console.log(arr);
  }
  
logArgsAsArray(1, 2, 3, 4)




// Use the spread operator to pass elements of an array as arguments to a function.
const numberss = [1, 2, 3];
// Function that takes 3 parameters
function add(a, b, c) {
    return a+b+c
}

const result = add(...numberss)

console.log(result)



// Create a clone of the following object using the spread operator.
const userr = { name: 'John', age: 30 };
// Create a clone of 'user'

const userClone = {...userr}



// Destructure specific properties from an object and gather the remaining properties using the rest operator.
const car = { brand: 'Toyota', model: 'Corolla', year: 2020, color: 'blue' };
// Destructure 'brand' and 'model' and gather the remaining properties

const {firstt, second, ...obj} = car

console.log(obj)



const fruitss = ['banana', 'cherry'];
// Add 'apple' at the beginning and 'mango' at the end using the spread operator

const updated = ['apple,', ...fruitss, 'mango']

console.log(updated)



// Create a function that uses the rest parameter and a default parameter.
// Function with a default parameter and rest parameter
function greet(greeting = 'Hello', ...names) {
    names.forEach(name => {
        console.log(`${greeting}, ${name}`)
      })
    }
    

greet('hello', 'humanbeing', 'certain person')



