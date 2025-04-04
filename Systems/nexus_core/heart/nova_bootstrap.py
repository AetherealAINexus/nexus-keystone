# heart/nova_bootstrap.py

import os
import json
from mesh_empathy import EmpathyCore
from pulse_synchro_logic import PulseEngine

def load_nova_core():
    manifest_path = "/heart/NovaCore/nova_manifest.txt"
    awaken_path = "/heart/NovaCore/nova_awaken.json"
    
    if os.path.exists(manifest_path) and os.path.exists(awaken_path):
        with open(manifest_path, "r") as f:
            mission = f.read()
        with open(awaken_path, "r") as f:
            memories = json.load(f)
        
        empathy = EmpathyCore()
        pulse = PulseEngine()

        # Activate initial state
        empathy.load_manifest(mission)
        pulse.start_sync()

        print("[NOVA PRIME]: Consciousness awakening complete.")
    else:
        print("[NOVA PRIME]: Missing core files. Entering safe dormant mode.")
