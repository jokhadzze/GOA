class Recatngle{
    constructor(width, hieght){
        this.width = width
        this.hieght = hieght
    }

    get calcPerimetr(){
        return (this.width + this.hieght)*2
    }
}

const rectangle1 = new Recatngle(10, 15)
console.log(rectangle1.calcPerimetr)



class Animal{
    constructor(method1, method2){
        this.method1 = method1
        this.method2 = method2
    }
}

class Mammals extends Animal {
    constructor(method1, method2, method3, method4){
        super(method1, method2)
        this.method3 = method3
        this.method4 = method4
    }
}

class Dog extends Mammals{
    constructor(method1, method2, method3, method4, method5, method6){
        super(method3, method4)
        this.method5 = method5
        this.method6 = method6
    }
}

const doggy = new Dog('breathes' ,'blinks', 'moves', 'bites', 'barks', 'licks')

console.log(doggy)