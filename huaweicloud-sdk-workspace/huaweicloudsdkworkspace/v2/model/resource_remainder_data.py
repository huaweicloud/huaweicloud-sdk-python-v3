# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceRemainderData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'remainder': 'int',
        'need': 'int',
        'volume_type': 'str'
    }

    attribute_map = {
        'type': 'type',
        'remainder': 'remainder',
        'need': 'need',
        'volume_type': 'volume_type'
    }

    def __init__(self, type=None, remainder=None, need=None, volume_type=None):
        r"""ResourceRemainderData

        The model defined in huaweicloud sdk

        :param type: 资源类型。
        :type type: str
        :param remainder: 剩余数量。
        :type remainder: int
        :param need: 所需资源。
        :type need: int
        :param volume_type: 磁盘类型。type为volume_gigabytes时，会返回该字段。
        :type volume_type: str
        """
        
        

        self._type = None
        self._remainder = None
        self._need = None
        self._volume_type = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if remainder is not None:
            self.remainder = remainder
        if need is not None:
            self.need = need
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def type(self):
        r"""Gets the type of this ResourceRemainderData.

        资源类型。

        :return: The type of this ResourceRemainderData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceRemainderData.

        资源类型。

        :param type: The type of this ResourceRemainderData.
        :type type: str
        """
        self._type = type

    @property
    def remainder(self):
        r"""Gets the remainder of this ResourceRemainderData.

        剩余数量。

        :return: The remainder of this ResourceRemainderData.
        :rtype: int
        """
        return self._remainder

    @remainder.setter
    def remainder(self, remainder):
        r"""Sets the remainder of this ResourceRemainderData.

        剩余数量。

        :param remainder: The remainder of this ResourceRemainderData.
        :type remainder: int
        """
        self._remainder = remainder

    @property
    def need(self):
        r"""Gets the need of this ResourceRemainderData.

        所需资源。

        :return: The need of this ResourceRemainderData.
        :rtype: int
        """
        return self._need

    @need.setter
    def need(self, need):
        r"""Sets the need of this ResourceRemainderData.

        所需资源。

        :param need: The need of this ResourceRemainderData.
        :type need: int
        """
        self._need = need

    @property
    def volume_type(self):
        r"""Gets the volume_type of this ResourceRemainderData.

        磁盘类型。type为volume_gigabytes时，会返回该字段。

        :return: The volume_type of this ResourceRemainderData.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this ResourceRemainderData.

        磁盘类型。type为volume_gigabytes时，会返回该字段。

        :param volume_type: The volume_type of this ResourceRemainderData.
        :type volume_type: str
        """
        self._volume_type = volume_type

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
        if not isinstance(other, ResourceRemainderData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
