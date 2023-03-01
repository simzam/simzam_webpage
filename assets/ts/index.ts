import { Application, Container } from "pixi.js"

const app = new Application({
  view: document.getElementById("pixi-canvas") as HTMLCanvasElement,
  resolution: window.devicePixelRatio || 1,
  autoDensity: true,
  backgroundColor: 0x6495ed,
  width: 1200,
  height: 1000
});

// class OpenCard extends ParticleContainer {
//   private card: Graphics;

//   constructor(shape: number,
//               numberShapes: number,
//               color: number,
//               fill: number,
//               cardSize: number[]) {
//     super();
//     this.card = new Graphics();
//     this.createCard(cardSize);
//   }
//   createCard(cardSize: number[]) {
//     this.card.beginFill(0xFFFFFF);
//     this.card.lineStyle(6, 0x000000, 2);
//     this.card.drawRoundedRect(0, 0, cardSize[0], cardSize[1], 20);
//   }
//   makeShapes(shape: number, numberShapes) {

//   }
// }

class Board extends Container {
  //private numberCards: number;
  // private tableCards: Graphics[];
  private deckCards: number[][] = [];
  // private colorShapes: Graphics[];

  constructor() {
    super();

    //this.numberCards = 12;
    let colors: number[] = [0xFF00AF, 0xAAFF00, 0x00AA03];

    this.makeDeckCards([], 4, 3);
    this.shuffleCards();
    console.log(this.deckCards);
    this.makeColorShapes(colors);
  }

  private makeColorShapes(colors: number[]): void {
    console.log(colors);
  }

  private shuffleCards(): void {
    let i: number;
    let tmp: number[];
    for (i = this.deckCards.length - 1; i > 0; i--) {
      let j: number = Math.floor(Math.random() * (i + 1));
      tmp = this.deckCards[i];
      this.deckCards[i] = this.deckCards[j];
      this.deckCards[j] = tmp;
    }
    return;
  }

  private makeDeckCards(tmpCard: number[], lengthCard: number, properties: number): void{
    if (tmpCard.length < lengthCard) {
      for (let i = 0; i < properties; i++) {
        this.makeDeckCards(tmpCard.concat([i]), lengthCard, properties);
      }
    } else {
      // console.log(tmpCard);
      this.deckCards.push(tmpCard);
    }
    return;
  }
}


new Board()
console.log(app);
