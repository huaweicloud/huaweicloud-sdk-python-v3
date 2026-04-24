# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatedBy:

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
        'identifier': 'str'
    }

    attribute_map = {
        'type': 'type',
        'identifier': 'identifier'
    }

    def __init__(self, type=None, identifier=None):
        r"""CreatedBy

        The model defined in huaweicloud sdk

        :param type: 工作负载身份创建者类型
        :type type: str
        :param identifier: 工作负载身份创建者标识
        :type identifier: str
        """
        
        

        self._type = None
        self._identifier = None
        self.discriminator = None

        self.type = type
        self.identifier = identifier

    @property
    def type(self):
        r"""Gets the type of this CreatedBy.

        工作负载身份创建者类型

        :return: The type of this CreatedBy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreatedBy.

        工作负载身份创建者类型

        :param type: The type of this CreatedBy.
        :type type: str
        """
        self._type = type

    @property
    def identifier(self):
        r"""Gets the identifier of this CreatedBy.

        工作负载身份创建者标识

        :return: The identifier of this CreatedBy.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this CreatedBy.

        工作负载身份创建者标识

        :param identifier: The identifier of this CreatedBy.
        :type identifier: str
        """
        self._identifier = identifier

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
        if not isinstance(other, CreatedBy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
