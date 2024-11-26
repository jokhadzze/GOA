const animals = [
    {
        name: "Dog",
        image: "https://images.app.goo.gl/13vfqHdQE48rLxVf7",
        description: "Dogs are loyal and friendly animals, often called 'man's best friend.'"
    }
]


const app = document.getElementById("main")


document.body.style.margin = "0"
document.body.style.padding = "0"
document.body.style.fontFamily = "Arial, sans-serif"
document.body.style.display = "flex"
document.body.style.justifyContent = "center"
document.body.style.alignItems = "center"
document.body.style.minHeight = "100vh"
document.body.style.backgroundColor = "#f0f8ff"

animals.forEach(animal => {
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
    img.src = animal.image
    img.alt = animal.name
    img.style.width = "100%"
    img.style.borderRadius = "8px"
    img.style.marginBottom = "10px"
    card.appendChild(img)


    const title = document.createElement("h2")
    title.textContent = animal.name
    title.style.margin = "10px 0"
    title.style.fontSize = "1.5em"
    title.style.color = "#333"
    card.appendChild(title)

    const description = document.createElement("p")
    description.textContent = animal.description
    description.style.color = "#555"
    description.style.fontSize = "1em"
    card.appendChild(description)

    app.appendChild(card)
})
