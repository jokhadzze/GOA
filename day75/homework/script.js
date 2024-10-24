// 1
class Animal {
    constructor(name) {
      this.name = name;
    }
  
    speak() {
      return `${this.name} makes a noise.`;
    }
  }
  

class Dog extends Animal {
    speak() {
      return `${this.name} barks.`;
    }
  }


const randomAnimal = new Animal('an animal')
console.log(randomAnimal.speak())

const doggy = new Dog('dog')
console.log(doggy.speak())


// 2
class Music{
  constructor(instrument){
    this.instrument = instrument
  }
  sound() {
    return `${this.instrument} makes certain noises`
  }
}

class Guitar extends Music{
  sound() {
    return `${this.instrument} is known for variety of sounds such as strumming, slide, and so on.`
  }
}

const randomInstrument = new Music('a music insturment')
console.log(randomAnimal.sound())

const guitar1 = new Guitar('a guitar')
console.log(guitar1.sound())

// 3
class VideoGames {
  constructor(name){
    this.name = name
  }

  expirience(){
    return `${this.name} is playable`
  }
}

class TheLastOfUsGame extends Games{
  expirience(){
    return `${this.name} is reffered to as a therapy by me`
  }
}

const randomGame = new VideoGames('a game')
console.log(randomGame.expirience())

const TheLastOfUs = new TheLastOfUsGame('The Last Of Us')
console.log(TheLastOfUs.expirience())