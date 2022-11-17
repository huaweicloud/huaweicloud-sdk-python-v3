# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKeypairResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'public_key': 'str',
        'private_key': 'str',
        'user_id': 'str',
        'fingerprint': 'str'
    }

    attribute_map = {
        'name': 'name',
        'public_key': 'public_key',
        'private_key': 'private_key',
        'user_id': 'user_id',
        'fingerprint': 'fingerprint'
    }

    def __init__(self, name=None, public_key=None, private_key=None, user_id=None, fingerprint=None):
        """CreateKeypairResponse

        The model defined in huaweicloud sdk

        :param name: 密钥对名称。
        :type name: str
        :param public_key: 公钥。
        :type public_key: str
        :param private_key: 私钥。
        :type private_key: str
        :param user_id: 用户ID。
        :type user_id: str
        :param fingerprint: 指纹。
        :type fingerprint: str
        """
        
        super(CreateKeypairResponse, self).__init__()

        self._name = None
        self._public_key = None
        self._private_key = None
        self._user_id = None
        self._fingerprint = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if public_key is not None:
            self.public_key = public_key
        if private_key is not None:
            self.private_key = private_key
        if user_id is not None:
            self.user_id = user_id
        if fingerprint is not None:
            self.fingerprint = fingerprint

    @property
    def name(self):
        """Gets the name of this CreateKeypairResponse.

        密钥对名称。

        :return: The name of this CreateKeypairResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateKeypairResponse.

        密钥对名称。

        :param name: The name of this CreateKeypairResponse.
        :type name: str
        """
        self._name = name

    @property
    def public_key(self):
        """Gets the public_key of this CreateKeypairResponse.

        公钥。

        :return: The public_key of this CreateKeypairResponse.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this CreateKeypairResponse.

        公钥。

        :param public_key: The public_key of this CreateKeypairResponse.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def private_key(self):
        """Gets the private_key of this CreateKeypairResponse.

        私钥。

        :return: The private_key of this CreateKeypairResponse.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CreateKeypairResponse.

        私钥。

        :param private_key: The private_key of this CreateKeypairResponse.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def user_id(self):
        """Gets the user_id of this CreateKeypairResponse.

        用户ID。

        :return: The user_id of this CreateKeypairResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateKeypairResponse.

        用户ID。

        :param user_id: The user_id of this CreateKeypairResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def fingerprint(self):
        """Gets the fingerprint of this CreateKeypairResponse.

        指纹。

        :return: The fingerprint of this CreateKeypairResponse.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this CreateKeypairResponse.

        指纹。

        :param fingerprint: The fingerprint of this CreateKeypairResponse.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

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
        if not isinstance(other, CreateKeypairResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
