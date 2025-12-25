# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeHandlerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'type': 'int'
    }

    attribute_map = {
        'ids': 'ids',
        'type': 'type'
    }

    def __init__(self, ids=None, type=None):
        r"""AuthorizeHandlerRequestBody

        The model defined in huaweicloud sdk

        :param ids: 数据 ID
        :type ids: list[str]
        :param type: 0-同意 2-拒绝 3-取消
        :type type: int
        """
        
        

        self._ids = None
        self._type = None
        self.discriminator = None

        self.ids = ids
        self.type = type

    @property
    def ids(self):
        r"""Gets the ids of this AuthorizeHandlerRequestBody.

        数据 ID

        :return: The ids of this AuthorizeHandlerRequestBody.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this AuthorizeHandlerRequestBody.

        数据 ID

        :param ids: The ids of this AuthorizeHandlerRequestBody.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def type(self):
        r"""Gets the type of this AuthorizeHandlerRequestBody.

        0-同意 2-拒绝 3-取消

        :return: The type of this AuthorizeHandlerRequestBody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AuthorizeHandlerRequestBody.

        0-同意 2-拒绝 3-取消

        :param type: The type of this AuthorizeHandlerRequestBody.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, AuthorizeHandlerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
