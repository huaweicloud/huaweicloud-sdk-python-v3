# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecretVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secret_name': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'secret_name': 'secret_name',
        'version_id': 'version_id'
    }

    def __init__(self, secret_name=None, version_id=None):
        """ShowSecretVersionRequest

        The model defined in huaweicloud sdk

        :param secret_name: 凭据名称。
        :type secret_name: str
        :param version_id: 凭据的版本标识符。
        :type version_id: str
        """
        
        

        self._secret_name = None
        self._version_id = None
        self.discriminator = None

        self.secret_name = secret_name
        self.version_id = version_id

    @property
    def secret_name(self):
        """Gets the secret_name of this ShowSecretVersionRequest.

        凭据名称。

        :return: The secret_name of this ShowSecretVersionRequest.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this ShowSecretVersionRequest.

        凭据名称。

        :param secret_name: The secret_name of this ShowSecretVersionRequest.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def version_id(self):
        """Gets the version_id of this ShowSecretVersionRequest.

        凭据的版本标识符。

        :return: The version_id of this ShowSecretVersionRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ShowSecretVersionRequest.

        凭据的版本标识符。

        :param version_id: The version_id of this ShowSecretVersionRequest.
        :type version_id: str
        """
        self._version_id = version_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowSecretVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
