namespace StatusBarKind {
    export const Nectar = StatusBarKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    Bee.sayText(list[randint(0, list.length - 1)], 30000, true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite, location) {
    Beenergy.value = 100
    info.changeScoreBy(Nectergy.value)
    if (Nectergy.value == Nectergy.max) {
        info.changeScoreBy(Nectergy.max)
    }
    Nectergy.value = 0
})
statusbars.onStatusReached(StatusBarKind.Health, statusbars.StatusComparison.EQ, statusbars.ComparisonType.Fixed, 0, function (status) {
    game.over(false)
})
info.onCountdownEnd(function () {
    game.over(true)
})
scene.onHitWall(SpriteKind.Enemy, function (sprite, location) {
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    if (Nectergy.value < Nectergy.max) {
        otherSprite.destroy(effects.fountain, 500)
        Nectergy.value += 1
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Music_On == 1) {
        Music_On = 0
    } else {
        Music_On = 1
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    Bee.destroy(effects.ashes, 500)
    game.over(false)
})
let BöseMiezekatze: Sprite = null
let Flower: Sprite = null
let BöserPiepmatz: Sprite = null
let list: string[] = []
let Music_On = 0
let Nectergy: StatusBarSprite = null
let Beenergy: StatusBarSprite = null
let Bee: Sprite = null
game.splash("Bienen sind beeutiful !!!", "Wenn du mehr erfahren willst drücke die A Taste während des Spiels.")
Bee = sprites.create(assets.image`Bee`, SpriteKind.Player)
controller.moveSprite(Bee)
tiles.setTilemap(tilemap`Level1`)
scene.cameraFollowSprite(Bee)
Beenergy = statusbars.create(20, 4, StatusBarKind.Health)
Beenergy.attachToSprite(Bee, -24, 0)
Beenergy.setColor(8, 2)
Nectergy = statusbars.create(20, 4, StatusBarKind.Nectar)
Nectergy.attachToSprite(Bee, -28, 0)
Nectergy.setColor(4, 3)
Nectergy.max = 5
Nectergy.value = 0
info.startCountdown(180)
Music_On = 1
let Enemy_Wait = 1
list = []
list.push("Bienen gehören zu den Insekten und haben sechs Beine, vier Flügel und einen Panzer. Der Panzer besteht aus Chitin. Er ist sozusagen das Skelett der Bienen. Weibliche Bienen haben am Hinterleib einen Stachel.")
list.push("Bei den meisten Bienenarten lebt jedes Tier für sich allein. Man nennt sie Solitärbienen. Sie kümmern sich nur um ihre eigenen Jungtiere. Die Gruppe der Kuckucksbienen legt ihre Eier in fremde Nester, wie eben der Vogel Kuckuck und überlässt die Aufzucht der Jungtiere den fremden Eltern.")
list.push("Manche Bienenarten leben in einem Volk zusammen, der auch Staat genannt wird. Sie heißen deshalb staatenbildende Arten. Dazu gehört auch die Honigbiene. Sie wird in vielen Ländern gezüchtet und ist deshalb weit verbreitet. Bienenzüchter heißen in der Fachsprache \"Imker\".")
list.push("Die Honigbiene ist dunkelbraun und am Körper behaart. Sie wird etwa eineinhalb Zentimeter groß und fliegt bis zu 25 Kilometer pro Stunde schnell. Das ist also ungefähr so schnell, wie ein flotter Radfahrer fährt.")
list.push("Jedes Volk von Honigbienen baut sein eigenes Nest. Die Bienen nutzen dazu oft eine Baumhöhle. In ihrem Bauch haben sie besondere Drüsen. Das sind kleine Organe, die Wachs hergeben. Damit bauen sie sechseckige Kamqmern. Man nennt sie auch \"Waben\".")
list.push("Zu einem Bienenvolk gehört eine Königin. Sie kann als einzige Eier legen. Zur Fortpflanzung fliegt die Königin aus und paart sich mit etwa 20 Männchen aus einem anderen Bienenvolk. Die Männchen sterben dann.")
list.push("Die Königin legt ihre Eier, und zwar bis zu 2.000 Stück am Tag. Aus ihnen entwickeln sich dann in den Waben die Larven. Aus befruchteten Eiern entstehen Arbeiterinnen, und zwar ungefähr 40.000 bis 60.000 Stück. Aus unbefruchteten Eiern entstehen Männchen, die heißen Drohnen. Von ihnen gibt es etwa tausend.")
list.push("Aus den Eiern werden Larven, dann Bienen. Eine einzige Larve wird besonders gefüttert, daraus wird eine Königin. Wenn das Bienenvolk zu groß wird, fliegt die junge Königin mit einem Teil der Arbeiterinnen aus und bildet einen eigenen Bienenstaat. Die Königin wird drei bis fünf Jahre alt, die Arbeiterinnen weniger als ein Jahr.")
list.push("So lange es irgendwelche Blüten gibt, schwärmen die Bienen aus. Sie sammeln Pollen, Nektar und Honigtau. Pollen nennt man den Blütenstaub von Pflanzen. Nektar ist ein Saft mit viel Zucker, den die Blüten herstellen. Honigtau ist ebenfalls ein süßer Saft, den machen aber kleine Insekten, vor allem Blattläuse. Da Pollen sehr viel Eiweiß enthält, lagern die Bienen diesen um ihre Jungen, zu füttern. Zusammen mit dem Körpersaft der Biene verwandeln sich Nektar und Honigtau in Honig. Diesen lagern sie als Nahrung für sich selbst im Winter in den Waben ein. Im Winter zittern sie mit ihren Muskeln am ganzen Körper und halten sich so warm. Sie ernähren sich vom gesammelten Honig oder von Zucker, den ihnen der Imker gibt.")
list.push("Honig ist süß und sehr nahrhaft. In der Natur haben es vor allem die Bären darauf abgesehen. Sie rauben gerne Bienennester aus. Die Bienen versuchen zwar, sich mit ihren Stacheln gegen die Bären zu wehren, aber das dichte Fell können sie damit nicht durchdringen.")
list.push("Auch der Mensch isst schon seit der Steinzeit gerne Bienenhonig. Um an wilden Bienenhonig heranzukommen, muss man erst einmal die Bienen mit Rauch verscheuchen. Aber auch dann geht ein Raubzug kaum ohne Stich ab.")
list.push("Heute züchten manche Menschen Honigbienen. Sie bauen dazu besondere Kästen aus Holz. Im Winter geben sie den Bienen Zucker zu fressen und behalten den Honig für sich selbst. Wer das macht, ist ein Imker.")
list.push("Dass wir so viele unterschiedliche Arten von Gemüse, Obst und Blumen haben, haben wir der Biene zu verdanken. Die Biene frisst mit ihrem Rüssel gerne Blumennektar. Während sie für ein paar Sekunden auf einer Blüte sitzt, verfangen sich ein paar Blütenpollen in ihrem Haarkleid. Wenn sie dann zu einer andere Blüte fliegt, streift sie dort ein paar Pollenkörnchen ab. Dadurch wird die andere Blume bestäubt. Tut die Biene das nicht, können keine neuen Pflanzen wachsen.")
list.push("Bienenkenner sagen, dass es den Honigbienen nicht gut geht. Das hat viele Ursachen. Etwa die Varroa-Milbe. Die ist ein Parasit, das heißt, dass sie sich von den Bienen ernährt, ohne ihr zu nutzen. Sie klammert sich in der Biene fest und saugt ihr Blut. Dadurch entsteht eine offene Bisswunde und die Biene kann schnell krank werden. Auch benutzen viele Gärtner oder Bauern Gifte, um ihre Pflanzen gegen Parasiten zu schützen. Diese Pflanzenschutzmittel sind aber auch für Bienen gefährlich.")
list.push("Bei einigen Arten dient der Stachel zum Ablegen von Eiern, aus denen sich junge Bienen entwickeln. Andere, so auch die Honigbiene, brauchen den Stachel, um sich gegen Feinde zu wehren. Oft fühlen sie sich schon bedroht, wenn sie sich eingeengt fühlen. Dies geschieht beispielsweise, wenn sie uns unter ein Kleidungsstück geraten. Wenn Bienen stechen, spritzen sie ein Gift in den Körper ihres Gegners. Das beißt uns Menschen gewaltig.")
list.push("Der Stachel vieler Bienen hat Widerhaken. Sie können damit andere Insekten stechen und ihn aus deren Chitinpanzer wieder herausziehen. Fliegen sie von einem gestochenen Menschen weg, bleibt der Stachel in seiner Haut stecken. Dadurch wird die Biene schwer verletzt und stirbt nach dem Stich bald.")
game.onUpdateInterval(5000, function () {
    if (Enemy_Wait > 2) {
        BöserPiepmatz = sprites.create(assets.image`Bird`, SpriteKind.Enemy)
        BöserPiepmatz.y = randint(10, 250)
        BöserPiepmatz.x = 250
        BöserPiepmatz.setVelocity(-50, 0)
    }
    Enemy_Wait += 1
})
game.onUpdateInterval(5000, function () {
    Flower = sprites.create(assets.image`Flower`, SpriteKind.Food)
    Flower.setPosition(randint(10, 250), randint(10, 250))
})
forever(function () {
    if (Music_On == 1) {
        music.setTempo(18)
        music.setVolume(20)
        music.playTone(392, music.beat(BeatFraction.Eighth))
        music.playTone(330, music.beat(BeatFraction.Eighth))
        music.playTone(294, music.beat(BeatFraction.Eighth))
        music.playTone(262, music.beat(BeatFraction.Eighth))
        music.playTone(294, music.beat(BeatFraction.Eighth))
        music.playTone(330, music.beat(BeatFraction.Eighth))
        music.playTone(392, music.beat(BeatFraction.Eighth))
        music.playTone(330, music.beat(BeatFraction.Eighth))
        music.playTone(294, music.beat(BeatFraction.Eighth))
        music.playTone(262, music.beat(BeatFraction.Eighth))
        music.playTone(294, music.beat(BeatFraction.Sixteenth))
        music.playTone(330, music.beat(BeatFraction.Sixteenth))
        music.playTone(294, music.beat(BeatFraction.Sixteenth))
        music.playTone(330, music.beat(BeatFraction.Sixteenth))
        music.playTone(392, music.beat(BeatFraction.Eighth))
        music.playTone(330, music.beat(BeatFraction.Eighth))
        music.playTone(392, music.beat(BeatFraction.Eighth))
        music.playTone(440, music.beat(BeatFraction.Eighth))
        music.playTone(330, music.beat(BeatFraction.Eighth))
        music.playTone(440, music.beat(BeatFraction.Eighth))
        music.playTone(392, music.beat(BeatFraction.Eighth))
        music.playTone(330, music.beat(BeatFraction.Eighth))
        music.playTone(294, music.beat(BeatFraction.Eighth))
        music.playTone(262, music.beat(BeatFraction.Quarter))
        pause(400)
    }
})
game.onUpdateInterval(30000, function () {
    if (Enemy_Wait > 2) {
        BöseMiezekatze = sprites.create(assets.image`Cat`, SpriteKind.Enemy)
        BöseMiezekatze.setPosition(randint(10, 250), randint(10, 250))
    }
    Enemy_Wait += 1
})
game.onUpdateInterval(300, function () {
    Beenergy.value += -1
})
