import { Application, Container, Graphics} from 'pixi.js';

// TODO: sizing?


// The application will create a renderer using WebGL, if possible,
// with a fallback to a canvas render. It will also setup the ticker
// and the root stage PIXI.Container.
// TODO: WEBgl
//

var parentElem = document.getElementById('pixi-content');


const app = new Application({
    view: document.getElementById('pixi-canvas'),
    resolution: window.devicePixelRatio || 1,
    antialias: true,
    backgroundAlpha: 0,
    width: window.innerWidth - 80,
    height: window.innerHeight - 200, //parent.innerHeigth,

    // resizeTo: window
});

class Game extends Container {
    constructor(screenWidth, screenHeight) {
        super();
        this.width = screenWidth;
        this._height = screenHeight;

        this.gridSize = this.setGridSize();
        console.log(this.gridSize, screenWidth);
    }
    setGridSize() {
        console.log("Resolution is (width x height):", this.width, this._height);

        return 1;
    }
}

const card1 = new Graphics();
card1.beginFill(0xFFFFFF);
card1.lineStyle(12, 0x000000, 1);
card1.drawRoundedRect(20, 20, 200, 320, 20);
card1.lineStyle(6, 0x000000, 1);
card1.beginFill(0x00F0F0)
card1.drawEllipse(120, 80, 80, 40);

card1.beginFill(0xFF0FF0);
card1.lineStyle(6, 0x000000, 1);
card1.drawEllipse(120, 180, 80, 40);

card1.beginFill(0x0FAFF0);
card1.lineStyle(6, 0x000000, 1);
card1.drawEllipse(120, 280, 80, 40);



card1.endFill();
app.stage.addChild (card1);

console.log(window.innerWidth, window.innerHeight);

const game = new Game(app.width, app.height);
