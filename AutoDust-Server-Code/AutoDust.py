from Server import Server
from classifiers import ImageClassifier

def get_category(objects):
    biodegradable = "bird.cat.dog.horse.sheep.cow.elephant.bear.zebra.giraffe.banana.apple.sandwich.orange.broccoli.carrot.hot dog.pizza.donut.cake.chair.sofa.pottedplant".split(".")
    non_biodegradable = "bench.parking meter.stop sign.fire hydrant.traffic light.boat.truck.train.bus.aeroplane.motorbike.car.bicycle.backpack.umbrella.handbag.tie.suitcase.frisbee.skis.snowboard.sports ball.kite.baseball bat.baseball glove.skateboard.surfboard.tennis racket.bottle.wine glass.cup.fork.knife.spoon.bowl.bed.diningtable.toilet.tvmonitor.laptop.mouse.remote.keyboard.cell phone.microwave.oven.toaster.sink.refrigerator.book.clock.vase.scissors.teddy bear.hair drier.toothbrush".split(".")
    detected = []
    for obj in objects:
        if obj == 'person':
            continue
        try:
            if obj in biodegradable:
                detected.append(0)            
            else:
                detected.append(1)
        except:
            detected.append(1)
    return detected 


host = '192.168.0.100'
port = 8080
server = Server(host, port)
clf = ImageClassifier.ObjectDetection()
print("Service Started")
running = True
while running:
    res = server.receive_image("img.jpg")
    img = clf.load("img.jpg")
    res = clf.classify(img)
    clf.save(res["image_data"], 'img.jpg')
    detections = res["detections"]
    category = get_category(detections)
    if len(category) > 0:
        status_code = category[0]
    else:
        status_code = 2
    server.send_cmd(status_code) 
    if status_code == 2:
        running = False
server.conn.close()
print("Service stopped")
        
