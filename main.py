from pdf_extractor import extract_pdf_content, save_as_json

def main():
    PDF_PATH = "input/IMO_Grade1_1-2.pdf"  #give the path for the pdf here
    IMAGE_DIR = "output/images"
    OUTPUT_JSON = "output/extracted_content.json"

    print("🔍 Extracting PDF content...")
    content = extract_pdf_content(PDF_PATH, IMAGE_DIR)

    print("💾 Saving JSON...")
    save_as_json(content, OUTPUT_JSON)

    print("✅ Done! JSON saved to:", OUTPUT_JSON)

if __name__ == "__main__":
    main()
