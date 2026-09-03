# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CedarPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statement': 'str'
    }

    attribute_map = {
        'statement': 'statement'
    }

    def __init__(self, statement=None):
        r"""CedarPolicy

        The model defined in huaweicloud sdk

        :param statement: The Cedar policy statement that defines the authorization logic. This statement follows Cedar syntax and specifies principals, actions, resources, and conditions for fine-grained access control.
        :type statement: str
        """
        
        

        self._statement = None
        self.discriminator = None

        self.statement = statement

    @property
    def statement(self):
        r"""Gets the statement of this CedarPolicy.

        The Cedar policy statement that defines the authorization logic. This statement follows Cedar syntax and specifies principals, actions, resources, and conditions for fine-grained access control.

        :return: The statement of this CedarPolicy.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this CedarPolicy.

        The Cedar policy statement that defines the authorization logic. This statement follows Cedar syntax and specifies principals, actions, resources, and conditions for fine-grained access control.

        :param statement: The statement of this CedarPolicy.
        :type statement: str
        """
        self._statement = statement

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
        if not isinstance(other, CedarPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
