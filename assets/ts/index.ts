import { Application, Sprite, Container } from "pixi.js"

const app = new Application({
  view: document.getElementById("pixi-canvas") as HTMLCanvasElement,
  resolution: window.devicePixelRatio || 1,
  autoDensity: true,
  backgroundColor: 0x6495ed,
  width: 1200,
  height: 800
});

class Board extends Container {
  constructor(app: Application) {
    super();
    const clampy: Sprite = Sprite.from("../static/images/clampy.png");
    const dimmy: Sprite = Sprite.from("../static/images/dimzam.png");
    clampy.x = 100;
    clampy.y = 0;

    // dimmy.anchor.set(0.5);

    dimmy.x = 0;
    dimmy.y = 0;

    dimmy.addChild(clampy);
    app.stage.addChild(dimmy);
    console.log(app.screen);
  }
  dummy() {
    let t: Number = 4;
    console.log('rude!', t);
  }
}

// clampy.anchor.set(0.5);
// DOIES A COMMENT CHENAGE ANYTHING

// app.stage.addChild(clampy);
// MAKING CHANGES

new Board(app);
