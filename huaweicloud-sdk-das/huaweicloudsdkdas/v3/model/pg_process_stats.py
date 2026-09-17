# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PgProcessStats:

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
        'active_count': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'active_count': 'active_count',
        'total_count': 'total_count'
    }

    def __init__(self, key=None, value=None, active_count=None, total_count=None):
        r"""PgProcessStats

        The model defined in huaweicloud sdk

        :param key: 参数名
        :type key: str
        :param value: 参数值
        :type value: str
        :param active_count: 活跃数
        :type active_count: int
        :param total_count: 总数
        :type total_count: int
        """
        
        

        self._key = None
        self._value = None
        self._active_count = None
        self._total_count = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if active_count is not None:
            self.active_count = active_count
        if total_count is not None:
            self.total_count = total_count

    @property
    def key(self):
        r"""Gets the key of this PgProcessStats.

        参数名

        :return: The key of this PgProcessStats.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this PgProcessStats.

        参数名

        :param key: The key of this PgProcessStats.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this PgProcessStats.

        参数值

        :return: The value of this PgProcessStats.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this PgProcessStats.

        参数值

        :param value: The value of this PgProcessStats.
        :type value: str
        """
        self._value = value

    @property
    def active_count(self):
        r"""Gets the active_count of this PgProcessStats.

        活跃数

        :return: The active_count of this PgProcessStats.
        :rtype: int
        """
        return self._active_count

    @active_count.setter
    def active_count(self, active_count):
        r"""Sets the active_count of this PgProcessStats.

        活跃数

        :param active_count: The active_count of this PgProcessStats.
        :type active_count: int
        """
        self._active_count = active_count

    @property
    def total_count(self):
        r"""Gets the total_count of this PgProcessStats.

        总数

        :return: The total_count of this PgProcessStats.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this PgProcessStats.

        总数

        :param total_count: The total_count of this PgProcessStats.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, PgProcessStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
