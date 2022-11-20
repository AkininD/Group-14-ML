from PIL import Image, ImageDraw, ImageFont
import torch
import detrd
import helpers
import torchvision.transforms as T
import io
import streamlit as st

torch.set_grad_enabled(False);


# TODO: константу COLORS, CLASSES вынести в отдельный файл и импортировать в файл main.py
# COCO classes
CLASSES = [
    'N/A', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A',
    'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse',
    'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack',
    'umbrella', 'N/A', 'N/A', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis',
    'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove',
    'skateboard', 'surfboard', 'tennis racket', 'bottle', 'N/A', 'wine glass',
    'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich',
    'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake',
    'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table', 'N/A',
    'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard',
    'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A',
    'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier',
    'toothbrush'
]


COLORS = [(46,139,87), (128,0,0), (220,20,60), (255,99,71), (205,92,92), (255,160,122),
          (128,128,0), (107,142,35), (0,128,0), (34,139,34), (32,178,170), (255,140,0),
          (0,128,128), (95,158,160), (30,144,255), (0,0,128), (65,105,225), (186,85,211)]

transform = T.Compose([
    T.Resize(800),
    T.ToTensor(),
    T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


@st.cache(allow_output_mutation=True)
def load_model():
    detr = detrd.Detr(num_classes=91)
    state_dict = torch.hub.load_state_dict_from_url(
        url='https://dl.fbaipublicfiles.com/detr/detr_demo-da2a99e9.pth',
        map_location='cpu', check_hash=True)
    detr.load_state_dict(state_dict)
    detr.eval();
    return detr


def detect_objects(image_data):
    image =  Image.open(io.BytesIO(image_data))
    scores, boxes = helpers.detect(image, model, transform)
    for p, (xmin, ymin, xmax, ymax), c in zip(scores, boxes.tolist(), COLORS * 100):
        cl = p.argmax()
        text = f'{CLASSES[cl]}: {p[cl]:0.2f}'
        draw = ImageDraw.Draw(image)
        draw.rectangle(((xmin, ymin), (xmax, ymax)), fill=None, outline=c, width=2)
        font = ImageFont.truetype("./assets/roboto.ttf", 14)
        left, top, right, bottom = draw.textbbox((xmin, ymin), text, font=font)
        draw.rectangle((left-5, top-5, right+5, bottom+5), fill="yellow")
        draw.text((xmin, ymin), text, font=font, fill="black")
    return image


def load_image():
    """Создание формы для загрузки изображения"""
    # Форма для загрузки изображения средствами Streamlit
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        # Получение загруженного изображения
        image_data = uploaded_file.getvalue()
        return image_data
    else:
        return None


# Вызываем функцию загрузки модели распознавания
model = load_model()


def main():
    # Выводим заголовок страницы средствами Streamlit
    st.title('Распознавание объектов на изображении')
    # Вызываем функцию создания формы загрузки изображения
    img = load_image()

    if img is not None:
        btn = st.button("Распознать объекты")
        try:
            st.image(img, use_column_width=True)
            if btn:
                with st.spinner('Распознаем картинку...'):
                    result_image = detect_objects(img)
                st.title('Распознанное изображение')
                st.success('Сделано!')
                st.image(result_image, use_column_width=True)
        except:
                st.error('Ошибка! Некорректный формат файла!')


if __name__ == "__main__":
    main()
