const me = {
    name: 'nina',
    lastName: 'jokhadze',
    height: 180,
    genderFemale: true
}

me.name = 'nini'
delete me.genderFemale

console.log(me)


const country = {
    name: 'Georgia',
    population: '3.7m',
    area: "69.7km*2",
    capital: 'Tbilisi',
    size: 'small',
    pupolationOf(){
        console.log(this.population)
    },
    placeToLive(){
        console.log("it's ight")
    }
}

// ობიექტი არის კუთვნილებების შემმცველი სივრცე/კონტეინერი და თითოეულ მათგანს გააჩნია მნიშვნელობა

// მეთოდი არის ფუნქცია, ღომელიც გაამოიყენება კონკრეტულ ობიექტში

// this key word გამოიყენება იმისთვის რომ, ობიქტში შეწმნილ ფუნქციაში აღვნიშნოტ ობიექტის სახელი

// შეგვიძლია კუთვნილებების მნიშვნელობა რომ შევცვალოთ, ამისთვის ვწერთ  ობიქტის სახელს --> წერტილი --> კუთვნილების სახელი და ვუტოლებთ
// ახალ მნიშვმნელობას

// წაშლას რაც ეხება, ვიყენებთ დოტ ნოტაციას: delete key word --> obj name --> dot --> property name





function Car (name, releaseDate) {

        this.name = name
        this.releaseDate = releaseDate


        this.printInfo = function () {
            console.log(this.name, this.releaseDate)
        }

    }

  
  
  const car1 = new Car("BMW", 1928);
  const car2 = new Car("Mustang", 1964);
  const car3 = new Car("audi", 1910)
  
  
  car2.printInfo()

//   კონსტრუქტორი არეს ფუნქცია, რომელსაც აკისრია იბიექტისშექმნა

// new ქმნის ახალ ცარიელ ობიექტს, რომელსაც გადაცემს კონსტრუქტორს --> კონსტრუქტორი ამ ცარიელი ობიექტს კუთვნილებებს ანიჭებს