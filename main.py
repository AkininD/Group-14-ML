from PIL import Image, ImageDraw, ImageFont
import torch
import detrd
import helpers
import torchvision.transforms as T
import io
import uuid
import awesome_log
import yaml
from pathlib import Path
from dotenv import dotenv_values
env = dotenv_values(".env")
# load config file
config_path = Path(__file__).parent / "config.yaml"
with open(config_path, "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

logger = awesome_log.Logger(__name__)
a_log = logger.printer()

torch.set_grad_enabled(False)

# COCO classes
CLASSES = config["classes"]

COLORS = [(46, 139, 87), (128, 0, 0), (220, 20, 60),
          (255, 99, 71), (205, 92, 92), (255, 160, 122),
          (128, 128, 0), (107, 142, 35), (0, 128, 0),
          (34, 139, 34), (32, 178, 170), (255, 140, 0),
          (0, 128, 128), (95, 158, 160), (30, 144, 255),
          (0, 0, 128), (65, 105, 225), (186, 85, 211)]

transform = T.Compose([
    T.Resize(800),
    T.ToTensor(),
    T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


# @st.cache(allow_output_mutation=True)
def load_model():
    a_log.info('Model loading...')
    detr = detrd.Detr(num_classes=91)
    state_dict = torch.hub.load_state_dict_from_url(
        url=config["model_url"],
        map_location='cpu', check_hash=True)
    detr.load_state_dict(state_dict)
    detr.eval()
    return detr


def creating_frame(prep_d, img):
    res = list()
    for p, (xmin, ymin, xmax, ymax), c in prep_d:
        cl = p.argmax()
        class_name = f'{CLASSES[cl]}: {p[cl]:0.2f}'
        res.append({CLASSES[cl]: f'{p[cl]:0.2f}'})
        draw = ImageDraw.Draw(img)
        draw.rectangle(((xmin, ymin), (xmax, ymax)),
                       fill=None, outline=c, width=2)
        font = ImageFont.truetype("./assets/roboto.ttf", 14)
        left, top, right, bottom = draw.textbbox((xmin, ymin), class_name, font=font)
        draw.rectangle((left - 5, top - 5, right + 5, bottom + 5),
                       fill="yellow")
        draw.text((xmin, ymin), class_name, font=font, fill="black")
    return res


def detect_objects(image_data, name):
    a_log.info('Object detection starting...')
    image = Image.open(io.BytesIO(image_data))
    scores, boxes = helpers.detect(image, load_model(), transform)
    prepared_data = zip(scores, boxes.tolist(), COLORS * 100)
    result = creating_frame(prepared_data, image)
    filename = f'{uuid.uuid4()}_{name}'
    image.save(f'./static/{filename}')
    result.append({'image_url': f'{env["BASE_URL"]}/static/{filename}'})
    return result
