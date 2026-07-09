# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonSettingsResponseLogRetention:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retention_days': 'int',
        'range_days_min': 'int',
        'range_days_max': 'int'
    }

    attribute_map = {
        'retention_days': 'retention_days',
        'range_days_min': 'range_days_min',
        'range_days_max': 'range_days_max'
    }

    def __init__(self, retention_days=None, range_days_min=None, range_days_max=None):
        r"""CommonSettingsResponseLogRetention

        The model defined in huaweicloud sdk

        :param retention_days: 设定的审计日志保存时间
        :type retention_days: int
        :param range_days_min: 审计日志保存时间设置最小时间
        :type range_days_min: int
        :param range_days_max: 审计日志保存时间设置最大时间
        :type range_days_max: int
        """
        
        

        self._retention_days = None
        self._range_days_min = None
        self._range_days_max = None
        self.discriminator = None

        if retention_days is not None:
            self.retention_days = retention_days
        if range_days_min is not None:
            self.range_days_min = range_days_min
        if range_days_max is not None:
            self.range_days_max = range_days_max

    @property
    def retention_days(self):
        r"""Gets the retention_days of this CommonSettingsResponseLogRetention.

        设定的审计日志保存时间

        :return: The retention_days of this CommonSettingsResponseLogRetention.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this CommonSettingsResponseLogRetention.

        设定的审计日志保存时间

        :param retention_days: The retention_days of this CommonSettingsResponseLogRetention.
        :type retention_days: int
        """
        self._retention_days = retention_days

    @property
    def range_days_min(self):
        r"""Gets the range_days_min of this CommonSettingsResponseLogRetention.

        审计日志保存时间设置最小时间

        :return: The range_days_min of this CommonSettingsResponseLogRetention.
        :rtype: int
        """
        return self._range_days_min

    @range_days_min.setter
    def range_days_min(self, range_days_min):
        r"""Sets the range_days_min of this CommonSettingsResponseLogRetention.

        审计日志保存时间设置最小时间

        :param range_days_min: The range_days_min of this CommonSettingsResponseLogRetention.
        :type range_days_min: int
        """
        self._range_days_min = range_days_min

    @property
    def range_days_max(self):
        r"""Gets the range_days_max of this CommonSettingsResponseLogRetention.

        审计日志保存时间设置最大时间

        :return: The range_days_max of this CommonSettingsResponseLogRetention.
        :rtype: int
        """
        return self._range_days_max

    @range_days_max.setter
    def range_days_max(self, range_days_max):
        r"""Sets the range_days_max of this CommonSettingsResponseLogRetention.

        审计日志保存时间设置最大时间

        :param range_days_max: The range_days_max of this CommonSettingsResponseLogRetention.
        :type range_days_max: int
        """
        self._range_days_max = range_days_max

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
        if not isinstance(other, CommonSettingsResponseLogRetention):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
