# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Secret:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secret_id': 'str',
        'secret_name': 'str'
    }

    attribute_map = {
        'secret_id': 'secret_id',
        'secret_name': 'secret_name'
    }

    def __init__(self, secret_id=None, secret_name=None):
        r"""Secret

        The model defined in huaweicloud sdk

        :param secret_id: The secret identifier.
        :type secret_id: str
        :param secret_name: The secret name.
        :type secret_name: str
        """
        
        

        self._secret_id = None
        self._secret_name = None
        self.discriminator = None

        self.secret_id = secret_id
        self.secret_name = secret_name

    @property
    def secret_id(self):
        r"""Gets the secret_id of this Secret.

        The secret identifier.

        :return: The secret_id of this Secret.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        r"""Sets the secret_id of this Secret.

        The secret identifier.

        :param secret_id: The secret_id of this Secret.
        :type secret_id: str
        """
        self._secret_id = secret_id

    @property
    def secret_name(self):
        r"""Gets the secret_name of this Secret.

        The secret name.

        :return: The secret_name of this Secret.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this Secret.

        The secret name.

        :param secret_name: The secret_name of this Secret.
        :type secret_name: str
        """
        self._secret_name = secret_name

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
        if not isinstance(other, Secret):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
