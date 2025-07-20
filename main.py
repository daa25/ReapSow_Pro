from flask import Flask, request, jsonify
from fulfillment import process_orders
from firebase_init import initialize_firebase

app = Flask(__name__)

# Initialize Firebase
if not initialize_firebase():
    print("❌ Firebase initialization failed.")
else:
    print("✅ Firebase initialized successfully.")

@app.route('/api/fulfill', methods=['POST'])
def route_fulfillment():
    try:
        order_data = request.json
        result = process_orders(order_data)
        return jsonify({"success": True, "result": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/')
def home():
    return "✅ ReapSow API is live."

if __name__ == '__main__':
    app.run(debug=True, port=3000)
