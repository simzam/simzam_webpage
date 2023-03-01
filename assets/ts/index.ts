import { Application, Sprite } from "pixi.js"

const app = new Application({
    view: document.getElementById("pixi-canvas") as HTMLCanvasElement,
    resolution: window.devicePixelRatio || 1,
    autoDensity: true,
    backgroundColor: 0x6495ed,
    width: 2000,
    height: 1000
});

const clampy: Sprite = Sprite.from("../static/images/dimzam.png");
const dimmy: Sprite = Sprite.from("../static/images/clampy.png");

clampy.anchor.set(0.5);

clampy.x = app.screen.width / 2;
clampy.y = app.screen.height / 2;

app.stage.addChild(clampy)


dimmy.anchor.set(0.5);

dimmy.x = app.screen.width / 2;
dimmy.y = app.screen.height / 2;

app.stage.addChild(dimmy);
