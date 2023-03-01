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
    // width: window.innerWidth - 20,
    // height: window.innerHeight - 100, //parent.innerHeigth,
    autoResize: true,
    //resizeTo: parent,
});

// ALL cards are represented
class Game extends Container {
    constructor(screenWidth, screenHeight) {
        super();
        this.width = screenWidth;
        this.height = screenHeight;

        this.gridSize = this.setGridSize();
        this.cardSize = this.setCardSize();
        this.offset = this.setOffset();
    }

    setGridSize() {
        var cols;
        var rows;
        if (this.width > this.heigth) {
            cols = 4;
            rows = 3;
        } else {
            cols = 3;
            rows = 4;
        }
        return [cols, rows];
    }

    setOffset() {
        return 1;
    }

    setCardSize() {
        let cardWidth = this.width / this.gridSize[0];
        let cardHeight = this.height / this.gridSize[1];
        console.log("card size: ", cardWidth, cardHeight);
    }
}

function makeExampleCard(x1, y1, x2, y2) {
    const ex = new Graphics();

    ex.beginFill(0xFFFFFF);
    ex.lineStyle(6, 0X000000, 1);

    ex.drawRoundedRect(x1, y1, x2, y2, 20);

    ex.endFill();
    return ex
}

function drawGrid(width, height) {
    const ex = new Graphics();

    let cols = 4;
    let rows = 3;
    if (width < height) {
        let tmp = cols;
        cols = rows;
        rows = tmp;
    }
    console.log("hei");
    ex.lineStyle(5, 0x0FBF3A, 1);
    let cardBoxWidth = width / cols;
    let cardBoxHeight = height / rows;

    let i = 1;
    for (i = 1; i < cols; i++) {
        let x = i * cardBoxWidth;
        ex.moveTo(x, 0);
        ex.lineTo(x, height);
    }

    for (let j = 1; j < rows; j++) {
        let y = j * cardBoxHeight;
        ex.moveTo(0, y);
        ex.lineTo(width, y);
    }
    
    console.log(cardBoxWidth, cardBoxHeight);
    return ex;
}

//app.stage.addChild (makeExampleCard(240, 0, 160, 240));
//app.stage.addChild (makeExampleCard(0, 280, 160, 240));

//app.stage.addChild (makeExampleCard(240, 500, 160, 240));

// console.log(app.screen.height, app.screen.width);

//let width = app.screen.width;
//let heigth = app.screen.height;

//app.stage.addChild(drawGrid(width, heigth));

new Game(app.screen.width, app.screen.heigth);

//app.stage.addChild (makeExampleCard(10, 10, 90, 120));
//app.stage.addChild (makeExampleCard(10, 830, 90, 120));
