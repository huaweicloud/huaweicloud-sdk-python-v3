# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserResetPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'reset_count_per_day': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'reset_count_per_day': 'reset_count_per_day'
    }

    def __init__(self, enable=None, reset_count_per_day=None):
        r"""UserResetPolicy

        The model defined in huaweicloud sdk

        :param enable: 开关
        :type enable: bool
        :param reset_count_per_day: 用户每天自动重试次数,重置次数每天0点刷新。
        :type reset_count_per_day: int
        """
        
        

        self._enable = None
        self._reset_count_per_day = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if reset_count_per_day is not None:
            self.reset_count_per_day = reset_count_per_day

    @property
    def enable(self):
        r"""Gets the enable of this UserResetPolicy.

        开关

        :return: The enable of this UserResetPolicy.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this UserResetPolicy.

        开关

        :param enable: The enable of this UserResetPolicy.
        :type enable: bool
        """
        self._enable = enable

    @property
    def reset_count_per_day(self):
        r"""Gets the reset_count_per_day of this UserResetPolicy.

        用户每天自动重试次数,重置次数每天0点刷新。

        :return: The reset_count_per_day of this UserResetPolicy.
        :rtype: int
        """
        return self._reset_count_per_day

    @reset_count_per_day.setter
    def reset_count_per_day(self, reset_count_per_day):
        r"""Sets the reset_count_per_day of this UserResetPolicy.

        用户每天自动重试次数,重置次数每天0点刷新。

        :param reset_count_per_day: The reset_count_per_day of this UserResetPolicy.
        :type reset_count_per_day: int
        """
        self._reset_count_per_day = reset_count_per_day

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
        if not isinstance(other, UserResetPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
