# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DasMetricInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'threshold_index': 'int',
        'instance_status': 'str',
        'timestamp': 'int',
        'metrics': 'object',
        'threshold_metrics': 'object'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'threshold_index': 'threshold_index',
        'instance_status': 'instance_status',
        'timestamp': 'timestamp',
        'metrics': 'metrics',
        'threshold_metrics': 'threshold_metrics'
    }

    def __init__(self, instance_id=None, threshold_index=None, instance_status=None, timestamp=None, metrics=None, threshold_metrics=None):
        r"""DasMetricInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param threshold_index: 阈值索引
        :type threshold_index: int
        :param instance_status: 实例状态
        :type instance_status: str
        :param timestamp: 指标采集时间戳
        :type timestamp: int
        :param metrics: 指标数据
        :type metrics: object
        :param threshold_metrics: 阈值指标数据
        :type threshold_metrics: object
        """
        
        

        self._instance_id = None
        self._threshold_index = None
        self._instance_status = None
        self._timestamp = None
        self._metrics = None
        self._threshold_metrics = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if threshold_index is not None:
            self.threshold_index = threshold_index
        if instance_status is not None:
            self.instance_status = instance_status
        if timestamp is not None:
            self.timestamp = timestamp
        if metrics is not None:
            self.metrics = metrics
        if threshold_metrics is not None:
            self.threshold_metrics = threshold_metrics

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DasMetricInfo.

        实例ID

        :return: The instance_id of this DasMetricInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DasMetricInfo.

        实例ID

        :param instance_id: The instance_id of this DasMetricInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def threshold_index(self):
        r"""Gets the threshold_index of this DasMetricInfo.

        阈值索引

        :return: The threshold_index of this DasMetricInfo.
        :rtype: int
        """
        return self._threshold_index

    @threshold_index.setter
    def threshold_index(self, threshold_index):
        r"""Sets the threshold_index of this DasMetricInfo.

        阈值索引

        :param threshold_index: The threshold_index of this DasMetricInfo.
        :type threshold_index: int
        """
        self._threshold_index = threshold_index

    @property
    def instance_status(self):
        r"""Gets the instance_status of this DasMetricInfo.

        实例状态

        :return: The instance_status of this DasMetricInfo.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this DasMetricInfo.

        实例状态

        :param instance_status: The instance_status of this DasMetricInfo.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def timestamp(self):
        r"""Gets the timestamp of this DasMetricInfo.

        指标采集时间戳

        :return: The timestamp of this DasMetricInfo.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this DasMetricInfo.

        指标采集时间戳

        :param timestamp: The timestamp of this DasMetricInfo.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def metrics(self):
        r"""Gets the metrics of this DasMetricInfo.

        指标数据

        :return: The metrics of this DasMetricInfo.
        :rtype: object
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this DasMetricInfo.

        指标数据

        :param metrics: The metrics of this DasMetricInfo.
        :type metrics: object
        """
        self._metrics = metrics

    @property
    def threshold_metrics(self):
        r"""Gets the threshold_metrics of this DasMetricInfo.

        阈值指标数据

        :return: The threshold_metrics of this DasMetricInfo.
        :rtype: object
        """
        return self._threshold_metrics

    @threshold_metrics.setter
    def threshold_metrics(self, threshold_metrics):
        r"""Sets the threshold_metrics of this DasMetricInfo.

        阈值指标数据

        :param threshold_metrics: The threshold_metrics of this DasMetricInfo.
        :type threshold_metrics: object
        """
        self._threshold_metrics = threshold_metrics

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DasMetricInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
