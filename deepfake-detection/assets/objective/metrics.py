from sklearn.metrics import log_loss

import substratools as tools


class MnistMetrics(tools.Metrics):
    def score(self, y_true, y_pred):
        """Returns the macro-average recall

        :param y_true: actual values from test data
        :type y_true: pd.DataFrame
        :param y_pred: predicted values from test data
        :type y_pred: pd.DataFrame
        :rtype: float
        """
        #invert predictions for the log_loss function (take the REAL label as reference)
        y_pred_inverted = 1-y_pred
        return log_loss(y_true, y_pred_inverted)


if __name__ == "__main__":
    tools.metrics.execute(MnistMetrics())