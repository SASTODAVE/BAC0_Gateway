# 🏭 BAC0 Gateway — Serveur BACnet/IP basé sur des APIs de consommation

## 📌 Description

Ce projet implémente un **serveur BACnet/IP** en Python qui expose dynamiquement des objets BACnet créés à partir de données provenant d’APIs externes ou de fichiers JSON locaux.
L’objectif est de transformer des données de consommation (ex. énergie, puissance, etc.) en objets BACnet accessibles par n’importe quel superviseur compatible.

---

## ⚠️ Prérequis

- **Python 3.11 obligatoire** (⚠️ `bacpypes` n’est pas compatible avec Python 3.12+).  
- `pip` version ≥ 24.0
- (Optionnel) `pyenv` pour gérer les versions de Python.

---

## 📂 Architecture du projet

```
bac0_gateway/
│── bacnet/                     # Package principal
│   │── __init__.py             # Exporte les classes/fonctions principales
│   │── api_client.py           # Gestion des appels API et lecture des fichiers JSON
│   │── config_loader.py        # Lecture et parsing du fichier de config (YAML)
│   │── objects.py              # Création automatique d’objets BACnet selon les données
│   │── server.py               # Classe BacnetServer (démarrage/arrêt du serveur)
│   │── updater.py              # Mise à jour continue des objets BACnet avec les nouvelles valeurs
│
│── lib/                        # Données de test
│   │── consommation_30minutes.json
│   │── consommation_quotidienne.json
│
│── tests/                      # Tests unitaires
│   │── read_config.py
│   │── create_objects.py
│
│── utils/                      # Outils divers
│   │── helpers.py
│
│── config.yaml                 # Configuration du serveur et des APIs
│── main.py                     # Script principal de démarrage
│── requirements.txt            # Dépendances Python
│── README.md                   # 📖 
```

---

## ⚙️ Fichier de configuration (`config.yaml`)

Exemple :

```yaml
device:
  name: "RPI_BAC0"
  identifier: 100
  vendor_id: 9999
  ip: "0.0.0.0"

apis:
  - name: "Consommation 30min"
    source: "file"
    path: "lib/consommation_30minutes.json"

  - name: "Consommation quotidienne"
    source: "file"
    path: "lib/consommation_quotidienne.json"

  - name: "API temps réel"
    source: "http"
    path: "https://mon-api.exemple.com/objects"
```

* `device` → décrit l’appareil BACnet local.
* `apis` → liste des sources de données (`file` ou `http`).

---

## 🚀 Installation et exécution

### 1. Cloner le projet

```bash
git clone https://github.com/SASTODAVE/BAC0_Gateway.git
cd bac0_gateway
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 3. Activer l’environnement virtuel

* **macOS / Linux** :

  ```bash
  source .venv/bin/activate
  ```
* **Windows (PowerShell)** :

  ```powershell
  .venv\Scripts\Activate
  ```

### 4. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Lancer le serveur

```bash
python main.py
```

### 6. Arrêter le serveur

Appuie sur `CTRL + C` → le serveur s’arrête proprement.
