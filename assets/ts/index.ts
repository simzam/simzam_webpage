import { Application, Graphics, Container } from "pixi.js"

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
  private colorShapes: Graphics[] = [];
  public fig: Graphics;

  constructor() {
    super();

    //this.numberCards = 12;
    let colors: number[] = [0xFF00AF, 0xAAFF00, 0x00AA03];

    this.makeDeckCards([], 4, 3);
    this.shuffleCards();
    //console.log(this.deckCards);
    this.makeColorShapes(colors);

    let testFig: Graphics = new Graphics;
    //testFig.beginFill(colors[1]);
    testFig.beginFill(colors[0]);
    testFig.lineStyle(8, colors[2], 1);
    testFig.drawEllipse(60, 90, 50, 20);
    testFig.beginFill(colors[1], 0.5);
    testFig.drawRect(0,0,120,180);
    testFig.endFill();


    testFig.x = 200;
    testFig.y = 200;

    this.fig = testFig;
    this.addChild(this.fig);

    let testFig2: Graphics = testFig.clone();
    testFig2.beginFill(0xFF0F0A);
    testFig2.drawCircle(200,200,30);
    testFig2.x = 400;
    testFig2.y = 600;

    this.addChild(testFig2);
  }

  private makeColorShapes(colors: number[]): void {
    let shape1: Graphics = new Graphics();
    let shape2: Graphics = new Graphics();
    let shape3: Graphics = new Graphics();
    let shapes: Graphics[] = [shape1, shape2, shape3];

    console.log(colors);
    console.log(shapes);

    for (let i = 0; i < colors.length; i++) {
      for (let j = 0; j < shapes.length; j++) {
        let card1: Graphics = new Graphics();
        card1.beginFill(colors[i]);
        card1.lineStyle(5, colors[i], 1);
        card1.drawEllipse(0, 0, 100, 40);
        card1.endFill();
        this.colorShapes.push(card1);

        let card2: Graphics = new Graphics();
        card2.beginFill(0xFFFFFF);
        card2.lineStyle(5, colors[i], 1);
        card2.endFill();
        this.colorShapes.push(card2);

        let card3: Graphics = new Graphics()
        this.colorShapes.push(card2);
        this.colorShapes.push(card3);
      }
    }
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

let board: Board = new Board();
app.stage.addChild(board);
