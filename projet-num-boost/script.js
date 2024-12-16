document.getElementById("boutonSuivant").addEventListener("click", () => {
    // Remplacer texte et image du conteneur
        document.querySelector(".containerIndex").innerHTML =
                    `<div class="imgIndex2">
                <img src="image/20220122_095531.jpg" alt="Vieille prison sur une ile de banniare en guyane">
            </div>
            <div class="texteIndex2">
            <h1>Parcours</h1>
            <p>J'en suis venu au développement web par l'intermédiaire du pentesting,
                en m'interessant à la lecture de puces RFID. Des outils comme le ProxMark sont opensource et mis à jour constament sur GitHub
                et j'ai trouvé ça fascninant.
                J'ai commencé par du langage COBOL. Avec youtube j'ai appris à faire de petits programmes de calculs, calculs d'imc, calculs de vitesse moyenne en course à pied. 
                Je me suis ensuite tourné vers le langage Python, la syntaxe est simple et intuitive ce qui facilite l'apprentissage des bases à savoir les fonctions, 
                les conditions, les boucles ainsi que l'utilisation des collections. J'ai appris énormément sur l'algorithmie.
                Mais ces programmes ne fonctionnaient que dans la console, je voulais faire des applications qu'on pourrait utiliser sur une page web.
                j'ai donc appris les bases HTML, CSS et Javascript avec Openclassroom afin des faire des pages dynamiques.</a></p>
            </div>`
        
})
document.getElementById("boutonPrecedent").addEventListener("click", () => {
    // Remplacer texte et image du conteneur
    document.querySelector(".containerIndex").innerHTML =
                `<div class="texteIndex">
        <h1>Présentation</h1>
        <p>Ancien militaire dans l'armée de terre et titulaire d'un DUT techniques de commercialisation, 
            je souhaite me reconvertir en tant que concepteur d'application web.
            Le role du concepteur est de répondre au mieux aux besoins du client 
            en créant des applications sur mesure en abordant des themes importants 
            comme l'experience utilisateur, les fonctionnalités, les bases de données, la sécurité. 
            Pour y parvenir je me forme en autodidacte grâce à des plateformes comme Udémy, Openclassroom ainsi qu'IBM skillsbuild pour les fondamentaux du web. 
            Suite à ces différentes formations je suis capable de faire des page web dynamique avec HTML, CSS et Javascript, et écrire des scripts en Python.</p>
        </div>
        <div class="imgIndex">
            <img src="image/photo1.jpg" alt="moi sur une pirogue avec mes collegues">
        </div>`
})

// function annulerQuiconce (divTexteAchanger,divImageAchanger,divTexte,divImage ){
//     divTexteAchanger = divTexte
//     divImageAchanger = divImage
// return divTexteAchanger,divImageAchanger

// }annulerQuiconce(texteProjetJS2,asideProjetJS2,texteProjetJS,asideProjetJS)



    // const element = document.querySelector('.my-element');
    // element.classList.add('active');  // Ajoute une classe
    // element.classList.remove('hidden');  // Retire une classe
    // element.classList.toggle('highlight'); // Alterne la classe

    

    // Ou avant
    // reference.before(div);

