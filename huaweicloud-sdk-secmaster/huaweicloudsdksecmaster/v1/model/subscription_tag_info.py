# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionTagInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, key=None, value=None, create_time=None, update_time=None):
        r"""SubscriptionTagInfo

        The model defined in huaweicloud sdk

        :param key: 键。 最大长度36个字符。 字符集：A-Z，a-z ， 0-9，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）
        :type key: str
        :param value: 值。 最大长度43个字符，可以为空字符串。 字符集：A-Z，a-z ， 0-9，‘.’，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）
        :type value: str
        :param create_time: 创建时间戳
        :type create_time: int
        :param update_time: 更新时间戳
        :type update_time: int
        """
        
        

        self._key = None
        self._value = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def key(self):
        r"""Gets the key of this SubscriptionTagInfo.

        键。 最大长度36个字符。 字符集：A-Z，a-z ， 0-9，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）

        :return: The key of this SubscriptionTagInfo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SubscriptionTagInfo.

        键。 最大长度36个字符。 字符集：A-Z，a-z ， 0-9，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）

        :param key: The key of this SubscriptionTagInfo.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this SubscriptionTagInfo.

        值。 最大长度43个字符，可以为空字符串。 字符集：A-Z，a-z ， 0-9，‘.’，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）

        :return: The value of this SubscriptionTagInfo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this SubscriptionTagInfo.

        值。 最大长度43个字符，可以为空字符串。 字符集：A-Z，a-z ， 0-9，‘.’，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）

        :param value: The value of this SubscriptionTagInfo.
        :type value: str
        """
        self._value = value

    @property
    def create_time(self):
        r"""Gets the create_time of this SubscriptionTagInfo.

        创建时间戳

        :return: The create_time of this SubscriptionTagInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SubscriptionTagInfo.

        创建时间戳

        :param create_time: The create_time of this SubscriptionTagInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this SubscriptionTagInfo.

        更新时间戳

        :return: The update_time of this SubscriptionTagInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SubscriptionTagInfo.

        更新时间戳

        :param update_time: The update_time of this SubscriptionTagInfo.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, SubscriptionTagInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
