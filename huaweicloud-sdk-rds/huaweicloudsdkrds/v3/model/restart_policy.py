# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestartPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period': 'list[str]',
        'utc_offset': 'str'
    }

    attribute_map = {
        'period': 'period',
        'utc_offset': 'utc_offset'
    }

    def __init__(self, period=None, utc_offset=None):
        r"""RestartPolicy

        The model defined in huaweicloud sdk

        :param period: 重启周期配置，在重启周期内的可维护时间窗进行重启，时区为UTC，取值范围： begin: 每月的第一天 middle：每月的15号 end：每月的最后一天 空列表，表示该功能关闭。
        :type period: list[str]
        :param utc_offset: 所在时区相较于UTC时间的偏移量，取值范围：格式必须为+hh:mm，或者-hh:mm，例如+08:00。
        :type utc_offset: str
        """
        
        

        self._period = None
        self._utc_offset = None
        self.discriminator = None

        if period is not None:
            self.period = period
        if utc_offset is not None:
            self.utc_offset = utc_offset

    @property
    def period(self):
        r"""Gets the period of this RestartPolicy.

        重启周期配置，在重启周期内的可维护时间窗进行重启，时区为UTC，取值范围： begin: 每月的第一天 middle：每月的15号 end：每月的最后一天 空列表，表示该功能关闭。

        :return: The period of this RestartPolicy.
        :rtype: list[str]
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this RestartPolicy.

        重启周期配置，在重启周期内的可维护时间窗进行重启，时区为UTC，取值范围： begin: 每月的第一天 middle：每月的15号 end：每月的最后一天 空列表，表示该功能关闭。

        :param period: The period of this RestartPolicy.
        :type period: list[str]
        """
        self._period = period

    @property
    def utc_offset(self):
        r"""Gets the utc_offset of this RestartPolicy.

        所在时区相较于UTC时间的偏移量，取值范围：格式必须为+hh:mm，或者-hh:mm，例如+08:00。

        :return: The utc_offset of this RestartPolicy.
        :rtype: str
        """
        return self._utc_offset

    @utc_offset.setter
    def utc_offset(self, utc_offset):
        r"""Sets the utc_offset of this RestartPolicy.

        所在时区相较于UTC时间的偏移量，取值范围：格式必须为+hh:mm，或者-hh:mm，例如+08:00。

        :param utc_offset: The utc_offset of this RestartPolicy.
        :type utc_offset: str
        """
        self._utc_offset = utc_offset

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
        if not isinstance(other, RestartPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
