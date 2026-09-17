# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetMetricThresholdNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_code': 'str',
        'engine_type': 'str',
        'new_threshold': 'float'
    }

    attribute_map = {
        'metric_code': 'metric_code',
        'engine_type': 'engine_type',
        'new_threshold': 'new_threshold'
    }

    def __init__(self, metric_code=None, engine_type=None, new_threshold=None):
        r"""SetMetricThresholdNewRequestBody

        The model defined in huaweicloud sdk

        :param metric_code: 指标码
        :type metric_code: str
        :param engine_type: 数据库类型
        :type engine_type: str
        :param new_threshold: 新阈值
        :type new_threshold: float
        """
        
        

        self._metric_code = None
        self._engine_type = None
        self._new_threshold = None
        self.discriminator = None

        self.metric_code = metric_code
        self.engine_type = engine_type
        self.new_threshold = new_threshold

    @property
    def metric_code(self):
        r"""Gets the metric_code of this SetMetricThresholdNewRequestBody.

        指标码

        :return: The metric_code of this SetMetricThresholdNewRequestBody.
        :rtype: str
        """
        return self._metric_code

    @metric_code.setter
    def metric_code(self, metric_code):
        r"""Sets the metric_code of this SetMetricThresholdNewRequestBody.

        指标码

        :param metric_code: The metric_code of this SetMetricThresholdNewRequestBody.
        :type metric_code: str
        """
        self._metric_code = metric_code

    @property
    def engine_type(self):
        r"""Gets the engine_type of this SetMetricThresholdNewRequestBody.

        数据库类型

        :return: The engine_type of this SetMetricThresholdNewRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this SetMetricThresholdNewRequestBody.

        数据库类型

        :param engine_type: The engine_type of this SetMetricThresholdNewRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def new_threshold(self):
        r"""Gets the new_threshold of this SetMetricThresholdNewRequestBody.

        新阈值

        :return: The new_threshold of this SetMetricThresholdNewRequestBody.
        :rtype: float
        """
        return self._new_threshold

    @new_threshold.setter
    def new_threshold(self, new_threshold):
        r"""Sets the new_threshold of this SetMetricThresholdNewRequestBody.

        新阈值

        :param new_threshold: The new_threshold of this SetMetricThresholdNewRequestBody.
        :type new_threshold: float
        """
        self._new_threshold = new_threshold

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
        if not isinstance(other, SetMetricThresholdNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
