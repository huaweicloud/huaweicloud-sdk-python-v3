# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'count': 'int'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'count': 'count'
    }

    def __init__(self, metric_name=None, count=None):
        r"""DiagnosisInfo

        The model defined in huaweicloud sdk

        :param metric_name: 指标名称。
        :type metric_name: str
        :param count: 实例数量。
        :type count: int
        """
        
        

        self._metric_name = None
        self._count = None
        self.discriminator = None

        self.metric_name = metric_name
        self.count = count

    @property
    def metric_name(self):
        r"""Gets the metric_name of this DiagnosisInfo.

        指标名称。

        :return: The metric_name of this DiagnosisInfo.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this DiagnosisInfo.

        指标名称。

        :param metric_name: The metric_name of this DiagnosisInfo.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def count(self):
        r"""Gets the count of this DiagnosisInfo.

        实例数量。

        :return: The count of this DiagnosisInfo.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this DiagnosisInfo.

        实例数量。

        :param count: The count of this DiagnosisInfo.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, DiagnosisInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
