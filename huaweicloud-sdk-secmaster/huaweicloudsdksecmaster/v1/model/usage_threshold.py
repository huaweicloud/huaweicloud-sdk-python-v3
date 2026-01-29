# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UsageThreshold:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'source_resource_spec_code': 'str',
        'threshold': 'float',
        'unit': 'str',
        'enable': 'bool'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'source_resource_spec_code': 'source_resource_spec_code',
        'threshold': 'threshold',
        'unit': 'unit',
        'enable': 'enable'
    }

    def __init__(self, resource_spec_code=None, source_resource_spec_code=None, threshold=None, unit=None, enable=None):
        r"""UsageThreshold

        The model defined in huaweicloud sdk

        :param resource_spec_code: 资源类型
        :type resource_spec_code: str
        :param source_resource_spec_code: 原始资源类型
        :type source_resource_spec_code: str
        :param threshold: 阈值
        :type threshold: float
        :param unit: 阈值对应的单位,%,MB,GB 如果%，对应的阈值最大为95
        :type unit: str
        :param enable: 开启或关闭当前资源类型的告警设置
        :type enable: bool
        """
        
        

        self._resource_spec_code = None
        self._source_resource_spec_code = None
        self._threshold = None
        self._unit = None
        self._enable = None
        self.discriminator = None

        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if source_resource_spec_code is not None:
            self.source_resource_spec_code = source_resource_spec_code
        self.threshold = threshold
        self.unit = unit
        if enable is not None:
            self.enable = enable

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this UsageThreshold.

        资源类型

        :return: The resource_spec_code of this UsageThreshold.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this UsageThreshold.

        资源类型

        :param resource_spec_code: The resource_spec_code of this UsageThreshold.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def source_resource_spec_code(self):
        r"""Gets the source_resource_spec_code of this UsageThreshold.

        原始资源类型

        :return: The source_resource_spec_code of this UsageThreshold.
        :rtype: str
        """
        return self._source_resource_spec_code

    @source_resource_spec_code.setter
    def source_resource_spec_code(self, source_resource_spec_code):
        r"""Sets the source_resource_spec_code of this UsageThreshold.

        原始资源类型

        :param source_resource_spec_code: The source_resource_spec_code of this UsageThreshold.
        :type source_resource_spec_code: str
        """
        self._source_resource_spec_code = source_resource_spec_code

    @property
    def threshold(self):
        r"""Gets the threshold of this UsageThreshold.

        阈值

        :return: The threshold of this UsageThreshold.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this UsageThreshold.

        阈值

        :param threshold: The threshold of this UsageThreshold.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def unit(self):
        r"""Gets the unit of this UsageThreshold.

        阈值对应的单位,%,MB,GB 如果%，对应的阈值最大为95

        :return: The unit of this UsageThreshold.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this UsageThreshold.

        阈值对应的单位,%,MB,GB 如果%，对应的阈值最大为95

        :param unit: The unit of this UsageThreshold.
        :type unit: str
        """
        self._unit = unit

    @property
    def enable(self):
        r"""Gets the enable of this UsageThreshold.

        开启或关闭当前资源类型的告警设置

        :return: The enable of this UsageThreshold.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this UsageThreshold.

        开启或关闭当前资源类型的告警设置

        :param enable: The enable of this UsageThreshold.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, UsageThreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
