#  Modélisation Épidémique SIRD – Analyse Numérique du COVID-19 au Maroc

## Contexte

L’analyse numérique est un pilier des mathématiques appliquées, offrant des outils puissants pour résoudre des problèmes complexes lorsque les solutions analytiques sont inaccessibles.  
Dans un monde confronté à des défis scientifiques et techniques croissants, cette discipline joue un rôle crucial dans de nombreux domaines — ingénierie, physique, économie et surtout **santé publique**.

L’émergence de pandémies telles que la **COVID-19** a mis en évidence l’importance de développer des **modèles mathématiques robustes** pour prédire et contrôler la propagation des virus.  

Ce **mini-projet** s’inscrit dans cette perspective, en explorant la modélisation de la dynamique épidémique via le **modèle SIRD (Susceptible – Infecté – Rétabli – Décédé)**, une extension du modèle classique **SIR**, à l’aide de **Python** et d’outils numériques.

---

## Objectifs

Appliquer les techniques d’**analyse numérique** pour étudier la propagation du **COVID-19** à partir de **données réelles**.

Les méthodes utilisées permettent de :
- Estimer l’évolution des cas **infectés**, **guéris** et **décédés**.  
- Prédire des indicateurs critiques comme le **pic épidémique** et le **seuil d’immunité collective**.  
- Évaluer l’efficacité des **mesures sanitaires** : confinement, vaccination, restrictions de mobilité, etc.

---

## Méthodes Numériques Utilisées

| Technique | Objectif |
|------------|-----------|
| **Interpolation** | Approximation des courbes épidémiques à partir de données réelles |
| **Résolution d’équations non linéaires** | Détermination du pic épidémique et du seuil d’immunité collective |
| **Dérivation numérique** | Estimation des taux de transmission et de croissance |
| **Intégration numérique** | Calcul des cas cumulés et de la durée de propagation |
| **Résolution d’équations différentielles** | Simulation complète de la dynamique SIRD |

---

## Données et Contexte de l’Étude

**Virus étudié :** COVID-19  
**Zone géographique :** Maroc  
**Période :** du **1er mars 2020** au **13 juillet 2021** (≈ 500 jours)  
**Population totale considérée :** ~36 millions d’habitants  

Les données couvrent :
- Le **début de la propagation** du virus au Maroc  
- La **montée en flèche des cas**  
- Les **effets des mesures sanitaires** décidées par les autorités

---

## Technologies et Librairies

- **Langage :** Python 3  
- **Librairies principales :**
  - `numpy` – calcul numérique  
  - `matplotlib` – visualisation graphique  
  - `scipy` – intégration et équations différentielles  
  - `pandas` – manipulation de données  

