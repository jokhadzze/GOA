class Animal {
    constructor(name, image, description) {
        this.name = name
        this.image = image
        this.description = description
    }

    
    createCard() {
        
        const card = document.createElement("div")
        card.style.backgroundColor = "#fff"
        card.style.border = "1px solid #ddd"
        card.style.borderRadius = "8px"
        card.style.width = "300px"
        card.style.textAlign = "center"
        card.style.padding = "20px"
        card.style.boxShadow = "0 4px 6px rgba(0, 0, 0, 0.1)"
        card.style.margin = "10px"

        
        const img = document.createElement("img")
        img.src = this.image
        img.alt = this.name
        img.style.width = "100%"
        img.style.borderRadius = "8px"
        img.style.marginBottom = "10px"
        card.appendChild(img)

        
        const title = document.createElement("h2")
        title.textContent = this.name
        title.style.margin = "10px 0"
        title.style.fontSize = "1.5em"
        title.style.color = "#333"
        card.appendChild(title)

        
        const description = document.createElement("p")
        description.textContent = this.description
        description.style.color = "#555"
        description.style.fontSize = "1em"
        card.appendChild(description)

        return card
    }
}


const animals = [
    new Animal("Dog", "https://place-puppy.comhttps://images.app.goo.gl/13vfqHdQE48rLxVf7", "Dogs are loyal and friendly animals."),
    new Animal("Cat", "https://images.app.goo.gl/rf4tC3fPMwUfWQbB9", "Cats are independent and curious creatures."),
    new Animal("Rabbit", "https://images.app.goo.gl/Hc4kWB5rLmJqqwUy5", "Rabbits are playful and gentle pets.")
]


const app = document.getElementById("main")


document.body.style.margin = "0"
document.body.style.padding = "0"
document.body.style.fontFamily = "Arial, sans-serif"
document.body.style.display = "flex"
document.body.style.flexWrap = "wrap"
document.body.style.justifyContent = "center"
document.body.style.backgroundColor = "#f0f8ff"


animals.forEach(animal => {
    const card = animal.createCard()
    app.appendChild(card)
})
