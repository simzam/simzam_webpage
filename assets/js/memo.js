import { Application, Graphics} from 'pixi.js';

// The application will create a renderer using WebGL, if possible,
// with a fallback to a canvas render. It will also setup the ticker
// and the root stage PIXI.Container.
// TODO: WEBgl
const app = new Application({
    view: document.getElementById('pixi-canvas'),
    resolution: window.devicePixelRatio || 1,
    antialias: true,
    backgroundAlpha: 0,
    width: 1400,
    height: 900, //parent.innerHeigth,

    // resizeTo: window
});


function generateCards() {
    return false;
}

const graphics = new Graphics();

// Rectangle
graphics.beginFill(0xDE3249);
graphics.drawRect(50, 50, 100, 100);
graphics.endFill();

app.stage.addChild(graphics);
//document.body.appendChild(app.view);
