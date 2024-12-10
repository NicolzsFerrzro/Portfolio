
// function choisirPhrasesOuMots(){
//     // let choixPlayer = prompt("la liste de mots(tapez mots) ou la liste de phrases(tapez phrases) ?")
//     // while (choixPlayer !== "mots" && choixPlayer !== "phrases"){
//     //     choixPlayer = prompt("la liste de mots(tapez mots) ou la liste de phrases(tapez phrases) ?")
        
        
//     // }
// // return choixPlayer;
//     let choixPlayer = "mots"
// return choixPlayer ;
// }

// function lancerBoucleDeJeu(choix){
    
//     for (let i = 0; i < choix.length; i++) {
//         // let MotUtilisateur = prompt("Tapez : " + choix[i])
//         if (MotUtilisateur == choix[i]){
//             score ++
//         } else {
//             score += 0
//         }
        
//     } 
    
// return score, choix.length;
// }

function afficherResultat(score, nbQ){
    // score 
    let afficherScore = document.querySelector(".zoneScore span")
    
    let afficherMessage = `${score} / ${nbQ}`
    afficherScore.innerText = afficherMessage
    
    // let resultat = "Vous avez " + score + " sur " + nbQ
    // console.log(resultat)
}

function afficherProposition(proposition){
    // //Proposer mot ou phrase
    let propositionSpan = document.querySelector(".zoneProposition span")
    propositionSpan.innerText = proposition
}



function lancerJeu(){
    let score = 0
    let i = 0
    let choixListe = listeMots

    // selectionner les boutons radio grace à leur nom commun
    const radioButtons = document.querySelectorAll('input[name="optionSource"]');
    // verifier si on change de bouton 
    radioButtons.forEach(radio => {
        radio.addEventListener('change', () => {
            // renvoyer une liste en fonction de la valeur du bouton radio
            if (radio.value === "2") {
                choixListe = listePhrases;
            } else {
                choixListe = listeMots;
            }
            
            afficherProposition(choixListe[i])
            
        });
    });

    
    afficherProposition(choixListe[i])
    
    boutonValider.addEventListener("click", () => {
        console.log(zoneTexte.value)
        
        if (zoneTexte.value === choixListe[i]){
            score ++
        } else {
            score += 0
        }
        afficherResultat(score, i+1)
        i++
        zoneTexte.value = ""
        if (choixListe[i] === undefined){
            afficherProposition("Bravo")
            boutonValider.disabled = true
        } else {afficherProposition(choixListe[i])}
        
    });
    
    
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// choisir entre mots et phrases 
let listeInputRadio = document.querySelectorAll(".zoneChoix input")
for (let i = 0; i < listeInputRadio.length; i++) {
    console.log(listeInputRadio[i]);
};

// Zone de propostion 
let zoneProposition = document.querySelector(".zoneProposition")

// Zone de réponse
let zoneReponse = document.getElementById("zoneReponse")
console.log(zoneReponse);

// Entrer la réponse
let zoneTexte = document.querySelector("#zoneReponse input")
console.log(zoneTexte);

// Empêcher le copier-coller
zoneTexte.addEventListener("copy", (e) => e.preventDefault());
zoneTexte.addEventListener("cut", (e) => e.preventDefault());
zoneTexte.addEventListener("paste", (e) => e.preventDefault());

// Empêcher le clic droit
zoneTexte.addEventListener("contextmenu", (e) => e.preventDefault());

// Empêcher les raccourcis clavier (Ctrl+C, Ctrl+V, etc.)
zoneTexte.addEventListener("keydown", (e) => {
if (e.ctrlKey && (e.key === "c" || e.key === "v" || e.key === "x")) {
    e.preventDefault();
}
});

// Faire apparaitre toutes les touches tapées dans la console
// document.addEventListener('keydown', (event) => {
//     console.log(event.key);
// });


// Valider réponse
let boutonValider = document.querySelector("#valider")
console.log(boutonValider);
// boutonValider.addEventListener("click", function () {
//     console.log("Vous avez cliqué sur le bouton")
// });


// zone de score
let zoneAffichageScore = document.querySelector(".zoneScore")
console.log(zoneAffichageScore);


//////// Injecter du contenu html

let contentTitre = "Cod.exe"
let contentParagraph = "Apprends à écrire du JavaScript de manière ludique"

/// créer les elements html
let nouvelleDiv = document.createElement("div")
let nouveauTitre = document.createElement("h1")
let nouveauParagraphe = document.createElement("p")

/// indiquer un objet html existant
let section = document.querySelector("section")

/// remplir les elements
nouveauTitre.textContent = contentTitre
nouveauParagraphe.textContent = contentParagraph

/// lier les elements hierarchiquement
nouvelleDiv.appendChild(nouveauTitre)
nouvelleDiv.appendChild(nouveauParagraphe)

section.appendChild(nouvelleDiv)







