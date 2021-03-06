from src.main.optim_methods.interface_method_optim import InterfaceMethodOptim, InterfaceOptimAnswer
from src.main.optim_methods.utils import get_lr


class GradientDescent(InterfaceMethodOptim):

    def step(self):
        grad = self._function.loss_gradient(self._w, self._X, self._y)
        assert grad.shape == self._w.shape
        # probably there bounds write like BAD SMELL
        direction = grad
        lr = get_lr(self._w, direction, self._X, self._y, self._function, max_bound=1)
        self._w -= lr * direction
        self._tensorboard_part(lr)

    def get_answer(self):
        return InterfaceOptimAnswer(self._w_start, self._w, self._function)
