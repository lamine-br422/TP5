# 📘 Homework

## 🔧 Ajout des Design Patterns dans le projet

Cette partie du homework améliore le projet de gestion d’association en intégrant deux design patterns : **Factory** et **Observer**, tout en respectant l’architecture MVC.

---

## 🏭 1. Factory Pattern

### Objectif  
Centraliser et uniformiser la création des membres (students / teachers).

### Modifications  
- Création de `factories/member_factory.py`
- Ajout des méthodes `create_student()` et `create_teacher()`
- La GUI utilise la factory au lieu de créer les dictionnaires manuellement
- Le contrôleur passe désormais par la factory

### Résultat  
Une création d’objets cohérente, propre, maintenable et facile à étendre.

---

## 👁️ 2. Observer Pattern

### Objectif  
Mettre à jour automatiquement la GUI après chaque changement de données.

### Modifications  
- Création de `observers/data_observer.py`
- Les contrôleurs deviennent des *Subjects* et notifient la vue
- La GUI implémente *Observer* avec une méthode `update()`
- Rafraîchissement automatique lors :
  - d’ajout/suppression de membres  
  - d’ajout/suppression d’événements  
  - de modifications des abonnements/paiements  

### Résultat  
Une interface dynamique, sans appels manuels à `_refresh_tab()`, et un meilleur respect du MVC.

---

## ✅ Résumé

- **Factory** : centralise la création des objets  
- **Observer** : synchronise automatiquement la Vue et les données  
- Le projet devient plus clair, modulaire et extensible
