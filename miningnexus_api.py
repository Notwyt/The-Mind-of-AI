from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  

@app.route("/reward", methods=["POST"])
def claim_rewards():
    try:
        data = request.json
        user_public_key = data.get("userPublicKey")
        
        reward_data = pd.DataFrame({"user": [user_public_key], "reward": [100]})
        optimized_reward = reward_data["reward"].mean()

        return jsonify({
            "success": True,
            "message": f"Rewarded {optimized_reward} tokens to {user_public_key}"
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)