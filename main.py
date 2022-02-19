@namespace
class StatusBarKind:
    Nectar = StatusBarKind.create()

def on_a_pressed():
    Bee.say_text(list2[randint(0, len(list2) - 1)], 30000, True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    Beenergy.value = 100
    info.change_score_by(Nectergy.value)
    if Nectergy.value == Nectergy.max:
        info.change_score_by(Nectergy.max)
    Nectergy.value = 0
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

def on_status_reached_comparison_eq_type_fixed(status):
    game.over(False)
statusbars.on_status_reached(StatusBarKind.health,
    statusbars.StatusComparison.EQ,
    statusbars.ComparisonType.FIXED,
    0,
    on_status_reached_comparison_eq_type_fixed)

def on_countdown_end():
    game.over(True)
info.on_countdown_end(on_countdown_end)

def on_hit_wall(sprite2, location2):
    sprite2.destroy()
scene.on_hit_wall(SpriteKind.enemy, on_hit_wall)

def on_on_overlap(sprite3, otherSprite):
    if Nectergy.value < Nectergy.max:
        otherSprite.destroy(effects.fountain, 500)
        Nectergy.value += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_b_pressed():
    global Music_On
    if Music_On == 1:
        Music_On = 0
    else:
        Music_On = 1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap2(sprite4, otherSprite2):
    Bee.destroy(effects.ashes, 500)
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

BöseMiezekatze: Sprite = None
Flower: Sprite = None
BöserPiepmatz: Sprite = None
list2: List[str] = []
Music_On = 0
Nectergy: StatusBarSprite = None
Beenergy: StatusBarSprite = None
Bee: Sprite = None
game.splash("Bienen sind beeutiful !!!",
    "Wenn du mehr erfahren willst drücke die A Taste während des Spiels.")
Bee = sprites.create(assets.image("""
    Bee
"""), SpriteKind.player)
controller.move_sprite(Bee)
tiles.set_tilemap(tilemap("""
    Level1
"""))
scene.camera_follow_sprite(Bee)
Beenergy = statusbars.create(20, 4, StatusBarKind.health)
Beenergy.attach_to_sprite(Bee, -24, 0)
Beenergy.set_color(8, 2)
Nectergy = statusbars.create(20, 4, StatusBarKind.Nectar)
Nectergy.attach_to_sprite(Bee, -28, 0)
Nectergy.set_color(4, 3)
Nectergy.max = 5
Nectergy.value = 0
info.start_countdown(180)
Music_On = 1
Enemy_Wait = 1
list2 = []
list2.append("Bienen gehören zu den Insekten und haben sechs Beine, vier Flügel und einen Panzer. Der Panzer besteht aus Chitin. Er ist sozusagen das Skelett der Bienen. Weibliche Bienen haben am Hinterleib einen Stachel.")
list2.append("Bei den meisten Bienenarten lebt jedes Tier für sich allein. Man nennt sie Solitärbienen. Sie kümmern sich nur um ihre eigenen Jungtiere. Die Gruppe der Kuckucksbienen legt ihre Eier in fremde Nester, wie eben der Vogel Kuckuck und überlässt die Aufzucht der Jungtiere den fremden Eltern.")
list2.append("Manche Bienenarten leben in einem Volk zusammen, der auch Staat genannt wird. Sie heißen deshalb staatenbildende Arten. Dazu gehört auch die Honigbiene. Sie wird in vielen Ländern gezüchtet und ist deshalb weit verbreitet. Bienenzüchter heißen in der Fachsprache \"Imker\".")
list2.append("Die Honigbiene ist dunkelbraun und am Körper behaart. Sie wird etwa eineinhalb Zentimeter groß und fliegt bis zu 25 Kilometer pro Stunde schnell. Das ist also ungefähr so schnell, wie ein flotter Radfahrer fährt.")
list2.append("Jedes Volk von Honigbienen baut sein eigenes Nest. Die Bienen nutzen dazu oft eine Baumhöhle. In ihrem Bauch haben sie besondere Drüsen. Das sind kleine Organe, die Wachs hergeben. Damit bauen sie sechseckige Kamqmern. Man nennt sie auch \"Waben\".")
list2.append("Zu einem Bienenvolk gehört eine Königin. Sie kann als einzige Eier legen. Zur Fortpflanzung fliegt die Königin aus und paart sich mit etwa 20 Männchen aus einem anderen Bienenvolk. Die Männchen sterben dann.")
list2.append("Die Königin legt ihre Eier, und zwar bis zu 2.000 Stück am Tag. Aus ihnen entwickeln sich dann in den Waben die Larven. Aus befruchteten Eiern entstehen Arbeiterinnen, und zwar ungefähr 40.000 bis 60.000 Stück. Aus unbefruchteten Eiern entstehen Männchen, die heißen Drohnen. Von ihnen gibt es etwa tausend.")
list2.append("Aus den Eiern werden Larven, dann Bienen. Eine einzige Larve wird besonders gefüttert, daraus wird eine Königin. Wenn das Bienenvolk zu groß wird, fliegt die junge Königin mit einem Teil der Arbeiterinnen aus und bildet einen eigenen Bienenstaat. Die Königin wird drei bis fünf Jahre alt, die Arbeiterinnen weniger als ein Jahr.")
list2.append("So lange es irgendwelche Blüten gibt, schwärmen die Bienen aus. Sie sammeln Pollen, Nektar und Honigtau. Pollen nennt man den Blütenstaub von Pflanzen. Nektar ist ein Saft mit viel Zucker, den die Blüten herstellen. Honigtau ist ebenfalls ein süßer Saft, den machen aber kleine Insekten, vor allem Blattläuse. Da Pollen sehr viel Eiweiß enthält, lagern die Bienen diesen um ihre Jungen, zu füttern. Zusammen mit dem Körpersaft der Biene verwandeln sich Nektar und Honigtau in Honig. Diesen lagern sie als Nahrung für sich selbst im Winter in den Waben ein. Im Winter zittern sie mit ihren Muskeln am ganzen Körper und halten sich so warm. Sie ernähren sich vom gesammelten Honig oder von Zucker, den ihnen der Imker gibt.")
list2.append("Honig ist süß und sehr nahrhaft. In der Natur haben es vor allem die Bären darauf abgesehen. Sie rauben gerne Bienennester aus. Die Bienen versuchen zwar, sich mit ihren Stacheln gegen die Bären zu wehren, aber das dichte Fell können sie damit nicht durchdringen.")
list2.append("Auch der Mensch isst schon seit der Steinzeit gerne Bienenhonig. Um an wilden Bienenhonig heranzukommen, muss man erst einmal die Bienen mit Rauch verscheuchen. Aber auch dann geht ein Raubzug kaum ohne Stich ab.")
list2.append("Heute züchten manche Menschen Honigbienen. Sie bauen dazu besondere Kästen aus Holz. Im Winter geben sie den Bienen Zucker zu fressen und behalten den Honig für sich selbst. Wer das macht, ist ein Imker.")
list2.append("Dass wir so viele unterschiedliche Arten von Gemüse, Obst und Blumen haben, haben wir der Biene zu verdanken. Die Biene frisst mit ihrem Rüssel gerne Blumennektar. Während sie für ein paar Sekunden auf einer Blüte sitzt, verfangen sich ein paar Blütenpollen in ihrem Haarkleid. Wenn sie dann zu einer andere Blüte fliegt, streift sie dort ein paar Pollenkörnchen ab. Dadurch wird die andere Blume bestäubt. Tut die Biene das nicht, können keine neuen Pflanzen wachsen.")
list2.append("Bienenkenner sagen, dass es den Honigbienen nicht gut geht. Das hat viele Ursachen. Etwa die Varroa-Milbe. Die ist ein Parasit, das heißt, dass sie sich von den Bienen ernährt, ohne ihr zu nutzen. Sie klammert sich in der Biene fest und saugt ihr Blut. Dadurch entsteht eine offene Bisswunde und die Biene kann schnell krank werden. Auch benutzen viele Gärtner oder Bauern Gifte, um ihre Pflanzen gegen Parasiten zu schützen. Diese Pflanzenschutzmittel sind aber auch für Bienen gefährlich.")
list2.append("Bei einigen Arten dient der Stachel zum Ablegen von Eiern, aus denen sich junge Bienen entwickeln. Andere, so auch die Honigbiene, brauchen den Stachel, um sich gegen Feinde zu wehren. Oft fühlen sie sich schon bedroht, wenn sie sich eingeengt fühlen. Dies geschieht beispielsweise, wenn sie uns unter ein Kleidungsstück geraten. Wenn Bienen stechen, spritzen sie ein Gift in den Körper ihres Gegners. Das beißt uns Menschen gewaltig.")
list2.append("Der Stachel vieler Bienen hat Widerhaken. Sie können damit andere Insekten stechen und ihn aus deren Chitinpanzer wieder herausziehen. Fliegen sie von einem gestochenen Menschen weg, bleibt der Stachel in seiner Haut stecken. Dadurch wird die Biene schwer verletzt und stirbt nach dem Stich bald.")

def on_update_interval():
    global BöserPiepmatz, Enemy_Wait
    if Enemy_Wait > 2:
        BöserPiepmatz = sprites.create(assets.image("""
            Bird
        """), SpriteKind.enemy)
        BöserPiepmatz.y = randint(10, 250)
        BöserPiepmatz.x = 250
        BöserPiepmatz.set_velocity(-50, 0)
    Enemy_Wait += 1
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global Flower
    Flower = sprites.create(assets.image("""
        Flower
    """), SpriteKind.food)
    Flower.set_position(randint(10, 250), randint(10, 250))
game.on_update_interval(5000, on_update_interval2)

def on_forever():
    if Music_On == 1:
        music.set_tempo(18)
        music.set_volume(20)
        music.play_tone(392, music.beat(BeatFraction.EIGHTH))
        music.play_tone(330, music.beat(BeatFraction.EIGHTH))
        music.play_tone(294, music.beat(BeatFraction.EIGHTH))
        music.play_tone(262, music.beat(BeatFraction.EIGHTH))
        music.play_tone(294, music.beat(BeatFraction.EIGHTH))
        music.play_tone(330, music.beat(BeatFraction.EIGHTH))
        music.play_tone(392, music.beat(BeatFraction.EIGHTH))
        music.play_tone(330, music.beat(BeatFraction.EIGHTH))
        music.play_tone(294, music.beat(BeatFraction.EIGHTH))
        music.play_tone(262, music.beat(BeatFraction.EIGHTH))
        music.play_tone(294, music.beat(BeatFraction.SIXTEENTH))
        music.play_tone(330, music.beat(BeatFraction.SIXTEENTH))
        music.play_tone(294, music.beat(BeatFraction.SIXTEENTH))
        music.play_tone(330, music.beat(BeatFraction.SIXTEENTH))
        music.play_tone(392, music.beat(BeatFraction.EIGHTH))
        music.play_tone(330, music.beat(BeatFraction.EIGHTH))
        music.play_tone(392, music.beat(BeatFraction.EIGHTH))
        music.play_tone(440, music.beat(BeatFraction.EIGHTH))
        music.play_tone(330, music.beat(BeatFraction.EIGHTH))
        music.play_tone(440, music.beat(BeatFraction.EIGHTH))
        music.play_tone(392, music.beat(BeatFraction.EIGHTH))
        music.play_tone(330, music.beat(BeatFraction.EIGHTH))
        music.play_tone(294, music.beat(BeatFraction.EIGHTH))
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        pause(400)
forever(on_forever)

def on_update_interval3():
    global BöseMiezekatze, Enemy_Wait
    if Enemy_Wait > 2:
        BöseMiezekatze = sprites.create(assets.image("""
            Cat
        """), SpriteKind.enemy)
        BöseMiezekatze.set_position(randint(10, 250), randint(10, 250))
    Enemy_Wait += 1
game.on_update_interval(30000, on_update_interval3)

def on_update_interval4():
    Beenergy.value += -1
game.on_update_interval(300, on_update_interval4)
