// class Piece {
//     constructor(couleur, position) {
//         this.couleur = couleur; // "blanc" ou "noir"
//         this.position = position; // Exemple : "e4"
//     }
    
//     deplacement(nouvellePosition) {
//         if (this.mouvementValide(nouvellePosition)) {
//             this.position = nouvellePosition;
//             console.log(`${this.type} ${this.couleur} déplacée en ${nouvellePosition}`);
//         } else {
//             console.log(`Déplacement invalide pour ${this.type} ${this.couleur}`);
//         }
//     }
// }
// class Roi extends Piece {
//     mouvementValide(nouvellePosition) {
//         const [coloneActuelle, ligneActuelle] = [this.position[0], parseInt(this.position[1])]; // séparer colone et ligne de position et en faire 2 variables
//         const [coloneCible, ligneCible] = [nouvellePosition[0], parseInt(nouvellePosition[1])];

//     // coloneActuelle === ligneActuelle || coloneCible === ligneCible; // verification de l'égalité des colones ou des lignes A === A (meme colone donc déplacement verticale)
    

//         // Le roi ne peut se déplacer que d'une case (horizontal, vertical, diagonal)
//         const coloneDifference = Math.abs(coloneActuelle.charCodeAt(0) - coloneCible.charCodeAt(0)); // soustrait les valeur ASCII
//         const ligneDifference = Math.abs(ligneActuelle - ligneCible); // math.abs donne un nombre absolue

//         return coloneDifference <= 1 && ligneDifference <= 1;
//     }
// }
// // Création d'un roi blanc
// const roiBlanc = new Roi('blanc', 'e1');

// // Déplacer le roi blanc
// roiBlanc.deplacement('e2'); // Valide : Le roi se déplace d'une case
// roiBlanc.deplacement('e4'); // Invalide : Déplacement de plus d'une case
// // Déplacement et validation

// console.log(Piece.mouvementValide('e2')); // true
// Piece.deplacement('e2'); 


// Zone de Jeu Echequier 


// // Créer des objets basés sur la classe
// const personne1 = new Personne("Alice", 30);
// const personne2 = new Personne("Bob", 25);

// // Appeler la méthode "saluer" sur les objets
// personne1.saluer(); // Bonjour, je m'appelle Alice et j'ai 30 ans.
// personne2.saluer(); // Bonjour, je m'appelle Bob et j'ai 25 ans.

const pieces = document.querySelectorAll('.draggable');
const cases = document.querySelectorAll('.container');

pieces.forEach(item => {
    item.addEventListener('dragstart', dragStart); // Début du glisser
});

cases.forEach(container => {
    container.addEventListener('dragover', dragOver); // Permet le dépôt
    container.addEventListener('drop', drop); // Action de déposer
});
// Début du glisser
function dragStart(piece) {
    piece.dataTransfer.setData('text/plain', piece.currentTarget.id);
}

// Permet au conteneur de recevoir un élément déplaçable
function dragOver(piece) {
    piece.preventDefault(); // Autorise le dépôt
}

// Déplacement de l'élément
function drop(piece) {
    piece.preventDefault();
    const id = piece.dataTransfer.getData('text/plain'); // Récupère l'ID
    const draggable = document.getElementById(id); // Récupère l'élément par son ID
    draggable.style.opacity = '1'; // Rétablit l'opacité
    piece.currentTarget.appendChild(draggable); // Ajoute l'élément au conteneur cible
}