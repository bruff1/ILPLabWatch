class Observable():
    """Erbt eine Klasse von Observable, so kann sie von Observern beobachtet werden."""
    observers = []

    # Fügt einen neuen Observer (Beobachter) hinzu.
    def addObserver(self, observer):
        if not (observer in self.observers):
            self.observers.append(observer)

    # Entfernt einen Observer
    def removeObserver(self, observer):
        self.observers.remove(observer)

    def removeAllObservers(self):
        """Entfernt alle Observer"""
        for observer in self.observers:
            self.removeObserver(observer)

    # informiert alle Observer über eine Änderung
    def informObserver(self):
        for observer in self.observers:
            observer.observableChanged(self)

    # informiert nur die observer, welche vom typ type sind. (klappt auc für subtypen.)
    def informObserverOfType(self, type):
        observers = list(filter(lambda object: isinstance(object, type), self.observers))
        for observer in observers:
            observer.observableChanged(self)
