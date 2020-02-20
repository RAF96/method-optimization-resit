from src.main.functions.interface_function import InterfaceFunction


class Linear(InterfaceFunction):

    def __init__(self):
        super().__init__()

    def _function(self, w, X):
        return X.dot(w)

    def _loss(self, w, X, y):
        S = X.shape[0]
        diff = X.dot(w) - y  # Size (S, 1)
        main = diff.T.dot(diff) / S
        total = main + self._loss_regularization_part(w)
        return total

    def _loss_gradient(self, w, X, y):
        S = X.shape[0]
        diff = X.dot(w) - y
        coef = 2 / S
        main = coef * X.T * diff
        total = main + self._loss_gradient_regularization_part(w)
        return total

    def _loss_hessian(self, w, X, y):
        S = X.shape[0]
        coef = 2 / S
        main = coef * X.T.dot(X)
        total = main + self._loss_hessian_regularization_part(w)
        return total
