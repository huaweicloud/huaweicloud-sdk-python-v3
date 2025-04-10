# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiSetMetricCodeThresholdReq:

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
        'datastore_type': 'str',
        'new_threshold': 'float'
    }

    attribute_map = {
        'metric_code': 'metric_code',
        'datastore_type': 'datastore_type',
        'new_threshold': 'new_threshold'
    }

    def __init__(self, metric_code=None, datastore_type=None, new_threshold=None):
        r"""ApiSetMetricCodeThresholdReq

        The model defined in huaweicloud sdk

        :param metric_code: 指标码
        :type metric_code: str
        :param datastore_type: 数据库类型
        :type datastore_type: str
        :param new_threshold: 新阈值
        :type new_threshold: float
        """
        
        

        self._metric_code = None
        self._datastore_type = None
        self._new_threshold = None
        self.discriminator = None

        self.metric_code = metric_code
        self.datastore_type = datastore_type
        self.new_threshold = new_threshold

    @property
    def metric_code(self):
        r"""Gets the metric_code of this ApiSetMetricCodeThresholdReq.

        指标码

        :return: The metric_code of this ApiSetMetricCodeThresholdReq.
        :rtype: str
        """
        return self._metric_code

    @metric_code.setter
    def metric_code(self, metric_code):
        r"""Sets the metric_code of this ApiSetMetricCodeThresholdReq.

        指标码

        :param metric_code: The metric_code of this ApiSetMetricCodeThresholdReq.
        :type metric_code: str
        """
        self._metric_code = metric_code

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ApiSetMetricCodeThresholdReq.

        数据库类型

        :return: The datastore_type of this ApiSetMetricCodeThresholdReq.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ApiSetMetricCodeThresholdReq.

        数据库类型

        :param datastore_type: The datastore_type of this ApiSetMetricCodeThresholdReq.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def new_threshold(self):
        r"""Gets the new_threshold of this ApiSetMetricCodeThresholdReq.

        新阈值

        :return: The new_threshold of this ApiSetMetricCodeThresholdReq.
        :rtype: float
        """
        return self._new_threshold

    @new_threshold.setter
    def new_threshold(self, new_threshold):
        r"""Sets the new_threshold of this ApiSetMetricCodeThresholdReq.

        新阈值

        :param new_threshold: The new_threshold of this ApiSetMetricCodeThresholdReq.
        :type new_threshold: float
        """
        self._new_threshold = new_threshold

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiSetMetricCodeThresholdReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
