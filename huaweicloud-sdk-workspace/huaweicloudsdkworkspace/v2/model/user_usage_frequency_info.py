# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserUsageFrequencyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'use_count': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'use_count': 'use_count'
    }

    def __init__(self, user_name=None, use_count=None):
        r"""UserUsageFrequencyInfo

        The model defined in huaweicloud sdk

        :param user_name: 桌面用户名。
        :type user_name: str
        :param use_count: 用户使用次数。
        :type use_count: int
        """
        
        

        self._user_name = None
        self._use_count = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if use_count is not None:
            self.use_count = use_count

    @property
    def user_name(self):
        r"""Gets the user_name of this UserUsageFrequencyInfo.

        桌面用户名。

        :return: The user_name of this UserUsageFrequencyInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UserUsageFrequencyInfo.

        桌面用户名。

        :param user_name: The user_name of this UserUsageFrequencyInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def use_count(self):
        r"""Gets the use_count of this UserUsageFrequencyInfo.

        用户使用次数。

        :return: The use_count of this UserUsageFrequencyInfo.
        :rtype: int
        """
        return self._use_count

    @use_count.setter
    def use_count(self, use_count):
        r"""Sets the use_count of this UserUsageFrequencyInfo.

        用户使用次数。

        :param use_count: The use_count of this UserUsageFrequencyInfo.
        :type use_count: int
        """
        self._use_count = use_count

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
        if not isinstance(other, UserUsageFrequencyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
