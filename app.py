from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Mengizinkan semua origin untuk endpoint /recommendations/*
CORS(app, resources={r"/recommendations/*": {"origins": "*"}})

# Data awal produk skincare
products = [
    {
        "name": "Vitamin C Serum",
        "type": "Serum",
        "skin_type": "kulit kusam",
        "ingredients": "Vitamin C, Hyaluronic Acid",
        "description": "Serum yang membantu mencerahkan dan melembapkan kulit."
    },
    {
        "name": "Exfoliating Scrub",
        "type": "Scrub",
        "skin_type": "kulit kusam",
        "ingredients": "Sugar, Coconut Oil",
        "description": "Scrub lembut yang membantu mengangkat sel kulit mati."
    },
    {
        "name": "Brightening Moisturizer",
        "type": "Moisturizer",
        "skin_type": "kulit kusam",
        "ingredients": "Niacinamide, Vitamin E",
        "description": "Pelembap yang membantu mencerahkan dan melembapkan kulit."
    },
    {
        "name": "Oil Control Gel",
        "type": "Gel",
        "skin_type": "berminyak",
        "ingredients": "Tea Tree Oil, Salicylic Acid",
        "description": "Gel yang membantu mengontrol minyak dan mencegah jerawat."
    },
    {
        "name": "Hydrating Moisturizer",
        "type": "Moisturizer",
        "skin_type": "kulit kering",
        "ingredients": "Hyaluronic Acid, Shea Butter",
        "description": "Pelembap yang memberikan hidrasi intensif untuk kulit kering."
    },
    {
        "name": "Acne Treatment Cream",
        "type": "Cream",
        "skin_type": "berjerawat",
        "ingredients": "Benzoyl Peroxide, Salicylic Acid",
        "description": "Krim perawatan yang membantu mengurangi jerawat dan peradangan."
    },
]

@app.route('/recommendations/<complaint>', methods=['GET'])
def get_recommendations(complaint):
    # Mengubah keluhan menjadi daftar kata kunci
    keywords = [keyword.strip().lower() for keyword in complaint.split(',')]
    filtered_products = []

    for product in products:
        # Memeriksa kecocokan dengan skin_type, type, dan ingredients
        match = False

        # Mencari kecocokan dalam skin_type
        if product['skin_type'].lower() in keywords:
            match = True
        
        # Mencari kecocokan dalam type
        if product['type'].lower() in keywords:
            match = True
        
        # Mencari kecocokan dalam ingredients
        ingredients_list = [ingredient.strip().lower() for ingredient in product['ingredients'].split(',')]
        if any(ingredient in keywords for ingredient in ingredients_list):
            match = True
        
        if match:
            filtered_products.append(product)

    # Mengembalikan rekomendasi dalam format JSON
    if filtered_products:
        return jsonify({"recommendations": filtered_products})
    else:
        return jsonify({"recommendations": []}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Mengizinkan akses dari semua alamat IP
