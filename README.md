# Airbnb Databricks Pipeline

Projet de **Data Pipeline** end-to-end sur **Databricks** utilisant l'architecture **Medallion** (Bronze / Silver / Gold) pour traiter les données Airbnb (listings, calendriers, reviews, etc.).

Objectif : ingérer, nettoyer, transformer et rendre les données exploitables pour de l'analyse, du reporting ou du machine learning (ex. : prédiction de prix, segmentation d'hôtes, optimisation de disponibilités).

## Architecture globale (Medallion)

- **Bronze** : Données brutes telles qu'ingérées (raw JSON/CSV, historique conservé, pas de transformation majeure)
- **Silver** : Données nettoyées, validées, dédupliquées, typées correctement, avec quelques enrichissements légers
- **Gold** : Tables business-ready, agrégées, jointes, prêtes pour BI / ML / dashboards (ex. : prix moyen par ville, taux d'occupation, etc.)

## Structure du repository

```text
airbnb-databricks-pipeline/
│
├── utils/                  # Fonctions réutilisables (config, helpers Spark, logging...)
│   └── download_utils.py   # Scripts pour télécharger datasets Airbnb (ex. Inside Airbnb)
│
├── ingestion/              # Notebooks / Jobs d'ingestion (Auto Loader, COPY INTO...)
│
├── bronze/                 # Notebooks / SQL pour créer & charger la couche Bronze
│
├── silver/                 # Nettoyage, validation, qualité des données → Silver
│
├── gold/                   # Agrégations, jointures, tables analytiques → Gold
│
├── README.md
└── requirements.txt        # (optionnel) Dépendances Python si besoin hors Databricks
