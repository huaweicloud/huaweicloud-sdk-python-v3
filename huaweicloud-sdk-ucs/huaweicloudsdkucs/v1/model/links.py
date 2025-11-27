# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Links:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_self': 'str',
        'next': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'next': 'next'
    }

    def __init__(self, _self=None, next=None):
        r"""Links

        The model defined in huaweicloud sdk

        :param _self: object信息
        :type _self: str
        :param next: Next信息
        :type next: str
        """
        
        

        self.__self = None
        self._next = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if next is not None:
            self.next = next

    @property
    def _self(self):
        r"""Gets the _self of this Links.

        object信息

        :return: The _self of this Links.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        r"""Sets the _self of this Links.

        object信息

        :param _self: The _self of this Links.
        :type _self: str
        """
        self.__self = _self

    @property
    def next(self):
        r"""Gets the next of this Links.

        Next信息

        :return: The next of this Links.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        r"""Sets the next of this Links.

        Next信息

        :param next: The next of this Links.
        :type next: str
        """
        self._next = next

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
        if not isinstance(other, Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
