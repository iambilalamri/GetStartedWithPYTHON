# GetStartedWithPYTHON

PYTHON

## Execution Python

To Execute python file, use the dependance code runner to simplify the execution of python code use the cmd : ctrl + alt + n

## Implementation CPython(c) vs Jython(java) ve Pypy(subset of python) vs ironPython(c#)

## GUI:

1. pyQt: fournit des bindings Python pour le framework Qt.
2. PyGObject: fournit des bindings Python, qui donnent un accès complet à la plate-forme logicielle GNOME. Il est entièrement compatible avec GTK+ 3. Remplace actuellement PyGTK. Voir tutoriel.
3. wxPython: boîte à outils d’interface graphique pour le langage de programmation Python, basé sur wxWidgets.
4. Kivy: bibliothèque Python pour le développement d’applications riches en média supportant le multi-touch. Écrit en Python, basé sur OpenGL (accélération GPU) et supporte les différents dispositifs d’entrée tels que: souris, la souris double, TUIO, WiiMote, WM_TOUCH, HIDtouch, les produits d’Apple et ainsi de suite. Fonctionne sur toutes les principales plateformes (Linux, OSX, Windows, Android).
5. Tk: Tkinter est une mince couche orientée par dessus Tcl/Tk. Il a l’avantage d’être inclus dans la bibliothèque standard Python, ce qui le rend la boîte à outils la plus pratique et compatible pour programmer.

## Pour internet:

Tweepy: pour se connecter à l’API de Twitter. Voir article sur ce site.
Facebook Python SDK: la même chose, mais pour facebook.
Gestion des images:

Python Imaging Library (ou PIL): une des bibliothèques de base pour la manipulation d’images en Python.Pillow est un fork beaucoup plus récent et actif.
OpenCV: OpenSource Computer Vision, librairies plus avancée de manipulation et de traitement d’images que PIL. Est aussi utilisée dans le cadre de la reconnaissance automatique en IA. Voir cette série de tutoriels.
Pour la science:

NumPy: bibliothèque de bas niveau écrite en C (et FORTRAN) pour les fonctions mathématiques de haut niveau. Fait partie du projet SciPy (ci-après). Numba est un compilateur Python de NumPy qui traduit le code en LLVM (plus rapide à l’exécution).
SciPy: bibliothèque qui utilise NumPy, avec des modules pour la programmation scientifique, incluant l’algèbre linéaire, le calcul intégral (calcul différentiel), la résolution d’équation différentielle ordinaire et le traitement du signal.
Matplotlib: bibliothèque de création de diagrammes flexible pour créer des diagrammes 2D et 3D interactifs. L’API reflète de plusieurs façons celle de MATLAB, facilitant la transition des utilisateurs MATLAB à Python. De nombreux exemples, avec le code source pour les recréer, sont disponibles dans la galerie de matplotlib.
Rpy2: Binding pour le logiciel statistique R permettant l’exécution de fonctions de R depuis Python et transmettant les données dans les deux sens entre les deux environnements. Rpy2 est l’implémentation orientée objet des bindings Rpy.
PsychoPy: Bibliothèque pour la psychologie cognitive et les expérimentations en neuroscience. La bibliothèque gère la présentation des stimuli, le scripting de conception expérimentale et la collecte de données.
A noter qu’Anaconda est une distribution qui inclue tous les paquets Python scientifiques les plus courants, ainsi que de nombreux paquets liés à l’analyse de données et au big data. Je l’ai utilisée pour ce MOOC.

## Pour l’IA:

Toutes les librairies pour l’IA (à détailler plus tard) sur le site officiel.

1. Theano: librairie open-source créée pour le deep learning utilisant une syntaxe proche de Numpy et optimisée pour le calcul GPU (Github) — Voir page dédiée.
2. Pour la Cryptographie:

- Cryptography: bibliothèque développée activement qui fournit des recettes et des primitives cryptographiques.
- PyCrypto: autre bibliothèque, qui fournit des fonctions de hash sécurisées et différents algorithmes de chiffrement.

3. Pour la connexion avec d’autres langages:

- SWIG: outil pour générer des bindings pour les langages interprétés à partir des fichiers d’en-tête C/C++. Il suffit de définir un fichier d’interface, inclure les en-têtes C/C ++ nécessaires, et exécuter l’outil de build sur eux. Très puissant, il expose beaucoup de fonctionnalités pour Python avec peu d’effort.
- ctypes: bibliothèque pour l’interfaçage avec C/C ++ depuis CPython, fournit non seulement un accès complet à l’interface C native de la plupart des principaux systèmes d’exploitation mais fournit également le support pour le chargement et l’interfaçage avec des bibliothèques dynamiques, telles que les DLL ou les objets partagés (Shared Objects ou SO) lors de l’exécution.
