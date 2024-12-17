class Piece {
    constructor(type, color, position) {
        this.type = type; // Exemple : "roi", "dame", "cavalier"
        this.color = color; // "blanc" ou "noir"
        this.position = position; // Exemple : "e4"
    }
    isValidMove(newPosition) {
        // Logique simplifiée pour le déplacement du roi
        const [col1, row1] = [this.position[0], parseInt(this.position[1])];
        const [col2, row2] = [newPosition[0], parseInt(newPosition[1])];

        const colDiff = Math.abs(col1.charCodeAt(0) - col2.charCodeAt(0));
        const rowDiff = Math.abs(row1 - row2);

        return colDiff <= 1 && rowDiff <= 1; // Le roi peut se déplacer d'une case dans toutes les directions
    }
    isValidMove(newPosition) {
        const [col1, row1] = [this.position[0], parseInt(this.position[1])];
        const [col2, row2] = [newPosition[0], parseInt(newPosition[1])];

        return col1 === col2 || row1 === row2; // La tour se déplace en ligne droite
    }
}

// Zone de Jeu Echequier 

// Objet Piece{}
//  Attributs : type, couleur, position
//  Methode : Deplacement autorisé}

//class Personne {
//     // Constructeur : méthode spéciale pour initialiser les objets
//     constructor(nom, age) {
//         this.nom = nom; // Propriété "nom"
//         this.age = age; // Propriété "age"
//     }

//     // Méthode : une action ou un comportement
//     saluer() {
//         console.log(`Bonjour, je m'appelle ${this.nom} et j'ai ${this.age} ans.`);
//     }
// }

// // Créer des objets basés sur la classe
// const personne1 = new Personne("Alice", 30);
// const personne2 = new Personne("Bob", 25);

// // Appeler la méthode "saluer" sur les objets
// personne1.saluer(); // Bonjour, je m'appelle Alice et j'ai 30 ans.
// personne2.saluer(); // Bonjour, je m'appelle Bob et j'ai 25 ans.