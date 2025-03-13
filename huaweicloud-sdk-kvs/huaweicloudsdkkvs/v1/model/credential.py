# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Credential:
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = ["sk"]

    openapi_types = {
        'ak': 'str',
        'sk': 'str',
        'stsToken': 'str'
    }

    attribute_map = {
        'ak': 'ak',
        'sk': 'dk',
        'sts_token': 'stsToken'
    }

    def __init__(self, ak=None, sk=None, sts_token=None):
        """Credential

        The model defined in huaweicloud sdk

        :param ak: accessKey。
        :type ak: str
        :param sk: secretKey。
        :type sk: str
        :param sts_token: securityToken。
        :type sk: str
        """

        self._ak = None
        self._sk = None
        self._sts_token = None
        self.discriminator = None

        self.ak = ak
        self.sk = sk
        self.sts_token = sts_token

    @property
    def ak(self):
        """Gets the ak of this Credential.

         AccessKey

        :return: The ak of this Credential.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this Credential.

        AccessKey.

        :param ak: The ak of this Credential.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this Credential.

        SecurityKey.

        :return: The sk of this Credential.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this Credential.

        SecurityKey.

        :param sk: The sk of this Credential.
        :type sk: str
        """
        self._sk = sk

    @property
    def sts_token(self):
        """Gets the sts_token of this Credential.

        SecurityToken.

        :return: The sts_token of this Credential.
        :rtype: str
        """
        return self._sts_token

    @sts_token.setter
    def sts_token(self, sts_token):
        """Sets the sts_token of this Credential.

        SecurityToken.

        :param sts_token: The sts_token of this Credential.
        :type sts_token: str
        """
        self._sts_token = sts_token

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Credential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
