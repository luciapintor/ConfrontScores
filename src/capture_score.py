# by Lucia Pintor
from sklearn.metrics import completeness_score, v_measure_score
from sklearn.metrics.cluster import homogeneity_score


class CaptureScore:

    def __init__(self, capture_id):
        self.capture_id = capture_id

        self.devices_true = None
        self.devices_count = None
        self.devices_error = None

        self.discarded = None
        self.samples = None

        self.homogeneity = None
        self.completeness = None
        self.v_measure = None

        self.score = 0

    def calculate_error(self, devices_true, devices_count):
        self.devices_true = devices_true
        self.devices_count = devices_count
        self.devices_error = abs(self.devices_count - self.devices_count)

    def calculate_v_measure(self, true_labels, calculated_labels):
        if len(true_labels) == len(calculated_labels):
            self.homogeneity = homogeneity_score(labels_true=true_labels, labels_pred=calculated_labels)
            self.completeness = completeness_score(labels_true=true_labels, labels_pred=calculated_labels)
            self.v_measure = v_measure_score(labels_true=true_labels, labels_pred=calculated_labels, beta=1.0)
        else:
            print("Labels arrays have different sizes in capture {}".format(self.capture_id))

    def calculate_score(self):
        discarded_percentage = (self.samples - self.discarded) / self.samples * 100

        if self.capture_id == "C":
            self.score = (self.devices_count - self.devices_error) / self.devices_count * discarded_percentage

        else:
            if self.v_measure is not None:
                self.score = self.v_measure * discarded_percentage
            else:
                print("v-measure is not available")

