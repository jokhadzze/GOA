const person = {
    name: 'Nina',
    age: 17,
    city: 'Tbilisi'
}

person.age = 21

person.hobby = 'undefined'

delete person.city


const car = {
    model: 'BMW E38 750iL V12',
    year: 1994
}

const calculator ={
    a: 19,
    b: 21,
    add(){
        console.log(this.a + this.b)
    }
}


const book1 = {
    title: "ვეფხისტყაოსანი",
    author: "შოთა რუსთაველი",
    stanzas: 1662 
}

const book2 = {
    title: "დიდოსტატის მარჯვენა",
    author: "კონსტანტინე გამსახურდია",
    pages: 376 
}

const book3 = {
    title: "no longer human",
    author: "osamu dazai",
    pages: 142 
}



function Animal(name, sound) {
    this.name = name
    this.sound = sound
}

Animal.makeSound = function() {
    console.log(this.sound);
}

Animal.prototype.changeName = function(newName) {
    this.name = newName
}

const tiger = new Animal('Tiger', 'Roar')
const monkey = new Animal('monkey', 'oo-ah')
const dog = new Animal('Dog', 'Woof')
const cat = new Animal('Cat', 'Meow')

tiger.makesound()

tiger.changeName('Lion')
console.log(tiger.name)
lion.makeSound()

monkey.makeSound()
dog.makeSound()
cat.makeSound()
