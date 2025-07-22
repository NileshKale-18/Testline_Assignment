import fitz  
import os
import json

def extract_pdf_content(pdf_path, output_image_dir):
    os.makedirs(output_image_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    result = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_text = page.get_text().strip()
        page_images = []

        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"page{page_num+1}_image{img_index+1}.{image_ext}"
            image_path = os.path.join(output_image_dir, image_filename)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            page_images.append(image_path)

        result.append({
            "page": page_num + 1,
            "text": page_text,
            "images": page_images
        })

    return result

def save_as_json(data, json_path):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
