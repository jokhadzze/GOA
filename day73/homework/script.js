class person {
    constructor(age, gender){
        this.age = age
        this.gender = gender
    }

    get concatenation(){
        return this.concatenate()
    }

    concatenate(){
        return this.gender + ' ' + this.age + ' years old'
    }
}

const actress = new person(20, 'female')
console.log(actress.concatenation)






class animals {
    constructor(name){
        this.name = name
    }
    makeSound(sound){
        this.sound = sound
        return sound
    }
}

class dog extends animals {
    constructor(name){
        super(name)
    }
}

const Dog = new dog('pepi')

console.log(Dog.makeSound('bark'))
















// class music {
//     constructor(genre, perfomer){
//         this.genre = genre
//         this.perfomancer = perfomer
//     }

//     static
// }


class calculator{
    static add(a, b){
        return a+b
    }
}


