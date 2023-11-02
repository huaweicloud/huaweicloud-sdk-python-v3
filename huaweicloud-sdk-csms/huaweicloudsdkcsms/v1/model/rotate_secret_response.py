# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RotateSecretResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_id': 'str',
        'secret_name': 'str'
    }

    attribute_map = {
        'version_id': 'version_id',
        'secret_name': 'secret_name'
    }

    def __init__(self, version_id=None, secret_name=None):
        """RotateSecretResponse

        The model defined in huaweicloud sdk

        :param version_id: 凭据的版本号标识符。
        :type version_id: str
        :param secret_name: 凭据的名称。
        :type secret_name: str
        """
        
        super(RotateSecretResponse, self).__init__()

        self._version_id = None
        self._secret_name = None
        self.discriminator = None

        if version_id is not None:
            self.version_id = version_id
        if secret_name is not None:
            self.secret_name = secret_name

    @property
    def version_id(self):
        """Gets the version_id of this RotateSecretResponse.

        凭据的版本号标识符。

        :return: The version_id of this RotateSecretResponse.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this RotateSecretResponse.

        凭据的版本号标识符。

        :param version_id: The version_id of this RotateSecretResponse.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def secret_name(self):
        """Gets the secret_name of this RotateSecretResponse.

        凭据的名称。

        :return: The secret_name of this RotateSecretResponse.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this RotateSecretResponse.

        凭据的名称。

        :param secret_name: The secret_name of this RotateSecretResponse.
        :type secret_name: str
        """
        self._secret_name = secret_name

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
        if not isinstance(other, RotateSecretResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
