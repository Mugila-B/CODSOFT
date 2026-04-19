import os
import sys

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = self._original_stdout
        sys.stderr = self._original_stderr


with HiddenPrints():
    from transformers import BlipProcessor, BlipForConditionalGeneration
    from PIL import Image

    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

image = Image.open("sample.jpg")

inputs = processor(image, return_tensors="pt")
output = model.generate(**inputs)

caption = processor.decode(output[0], skip_special_tokens=True)

print("Caption:")
print(caption)
