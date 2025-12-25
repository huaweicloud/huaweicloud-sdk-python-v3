# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcRdsVolume:

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
        'size': 'int'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size'
    }

    def __init__(self, type=None, size=None):
        r"""HwcRdsVolume

        The model defined in huaweicloud sdk

        :param type: 磁盘类型。
        :type type: str
        :param size: 磁盘大小。
        :type size: int
        """
        
        

        self._type = None
        self._size = None
        self.discriminator = None

        self.type = type
        self.size = size

    @property
    def type(self):
        r"""Gets the type of this HwcRdsVolume.

        磁盘类型。

        :return: The type of this HwcRdsVolume.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HwcRdsVolume.

        磁盘类型。

        :param type: The type of this HwcRdsVolume.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this HwcRdsVolume.

        磁盘大小。

        :return: The size of this HwcRdsVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this HwcRdsVolume.

        磁盘大小。

        :param size: The size of this HwcRdsVolume.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, HwcRdsVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
