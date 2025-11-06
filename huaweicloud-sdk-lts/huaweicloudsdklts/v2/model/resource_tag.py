# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTag:

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
        'tags_to_streams_enable': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'tags_to_streams_enable': 'tags_to_streams_enable'
    }

    def __init__(self, key=None, value=None, tags_to_streams_enable=None):
        r"""ResourceTag

        The model defined in huaweicloud sdk

        :param key: 标签的key
        :type key: str
        :param value: 标签的value
        :type value: str
        :param tags_to_streams_enable: 是否启用日志流标签
        :type tags_to_streams_enable: str
        """
        
        

        self._key = None
        self._value = None
        self._tags_to_streams_enable = None
        self.discriminator = None

        self.key = key
        self.value = value
        self.tags_to_streams_enable = tags_to_streams_enable

    @property
    def key(self):
        r"""Gets the key of this ResourceTag.

        标签的key

        :return: The key of this ResourceTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ResourceTag.

        标签的key

        :param key: The key of this ResourceTag.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this ResourceTag.

        标签的value

        :return: The value of this ResourceTag.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ResourceTag.

        标签的value

        :param value: The value of this ResourceTag.
        :type value: str
        """
        self._value = value

    @property
    def tags_to_streams_enable(self):
        r"""Gets the tags_to_streams_enable of this ResourceTag.

        是否启用日志流标签

        :return: The tags_to_streams_enable of this ResourceTag.
        :rtype: str
        """
        return self._tags_to_streams_enable

    @tags_to_streams_enable.setter
    def tags_to_streams_enable(self, tags_to_streams_enable):
        r"""Sets the tags_to_streams_enable of this ResourceTag.

        是否启用日志流标签

        :param tags_to_streams_enable: The tags_to_streams_enable of this ResourceTag.
        :type tags_to_streams_enable: str
        """
        self._tags_to_streams_enable = tags_to_streams_enable

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
        if not isinstance(other, ResourceTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
