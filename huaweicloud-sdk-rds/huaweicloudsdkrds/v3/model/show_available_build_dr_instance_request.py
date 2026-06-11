# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAvailableBuildDrInstanceRequest:

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
        'x_language': 'str'
    }

    attribute_map = {
        'type': 'type',
        'x_language': 'X-Language'
    }

    def __init__(self, type=None, x_language=None):
        r"""ShowAvailableBuildDrInstanceRequest

        The model defined in huaweicloud sdk

        :param type: 要查询的实例类型 master：主实例。 slave：灾备实例。
        :type type: str
        :param x_language: 语言。默认en-us。
        :type x_language: str
        """
        
        

        self._type = None
        self._x_language = None
        self.discriminator = None

        self.type = type
        if x_language is not None:
            self.x_language = x_language

    @property
    def type(self):
        r"""Gets the type of this ShowAvailableBuildDrInstanceRequest.

        要查询的实例类型 master：主实例。 slave：灾备实例。

        :return: The type of this ShowAvailableBuildDrInstanceRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowAvailableBuildDrInstanceRequest.

        要查询的实例类型 master：主实例。 slave：灾备实例。

        :param type: The type of this ShowAvailableBuildDrInstanceRequest.
        :type type: str
        """
        self._type = type

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowAvailableBuildDrInstanceRequest.

        语言。默认en-us。

        :return: The x_language of this ShowAvailableBuildDrInstanceRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowAvailableBuildDrInstanceRequest.

        语言。默认en-us。

        :param x_language: The x_language of this ShowAvailableBuildDrInstanceRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowAvailableBuildDrInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
