import * as PIXI from 'pixi.js';

// The application will create a renderer using WebGL, if possible,
// with a fallback to a canvas render. It will also setup the ticker
// and the root stage PIXI.Container.
const app = new PIXI.Application({
    view: document.getElementById('pixi-canvas'),
    resolution: window.devicePixelRatio || 1,
    antialias: true,
    backgroundAlpha: 0,
    resizeTo: window
});

const graphics = new PIXI.Graphics();

// Rectangle
graphics.beginFill(0xDE3249);
graphics.drawRect(50, 50, 100, 100);
graphics.endFill();

// Rectangle + line style 1
graphics.lineStyle(2, 0xFEEB77, 1);
graphics.beginFill(0x650A5A);
graphics.drawRect(200, 50, 100, 100);
graphics.endFill();

// Rectangle + line style 2
graphics.lineStyle(10, 0xFFBD01, 1);
graphics.beginFill(0xC34288);
graphics.drawRect(350, 50, 100, 100);
graphics.endFill();

// Rectangle 2
graphics.lineStyle(2, 0xFFFFFF, 1);
graphics.beginFill(0xAA4F08);
graphics.drawRect(530, 50, 140, 100);
graphics.endFill();

// Circle
graphics.lineStyle(0); // draw a circle, set the lineStyle to zero so the circle doesn't have an outline
graphics.beginFill(0xDE3249, 1);
graphics.drawCircle(100, 250, 50);
graphics.endFill();

// Circle
// draw polygon
const path = [600, 370, 700, 460, 780, 420, 730, 570, 590, 520];

graphics.lineStyle(0);
graphics.beginFill(0x3500FA, 1);
graphics.drawPolygon(path);
graphics.endFill();

app.stage.addChild(graphics);
//document.body.appendChild(app.view);
