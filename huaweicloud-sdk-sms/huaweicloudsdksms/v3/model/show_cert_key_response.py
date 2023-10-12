# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert': 'str',
        'private_key': 'str',
        'ca': 'str',
        'target_mgmt_cert': 'str',
        'target_mgmt_private_key': 'str',
        'target_data_cert': 'str',
        'target_data_private_key': 'str'
    }

    attribute_map = {
        'cert': 'cert',
        'private_key': 'private_key',
        'ca': 'ca',
        'target_mgmt_cert': 'target_mgmt_cert',
        'target_mgmt_private_key': 'target_mgmt_private_key',
        'target_data_cert': 'target_data_cert',
        'target_data_private_key': 'target_data_private_key'
    }

    def __init__(self, cert=None, private_key=None, ca=None, target_mgmt_cert=None, target_mgmt_private_key=None, target_data_cert=None, target_data_private_key=None):
        """ShowCertKeyResponse

        The model defined in huaweicloud sdk

        :param cert: 源端证书
        :type cert: str
        :param private_key: 源端私钥
        :type private_key: str
        :param ca: ca证书
        :type ca: str
        :param target_mgmt_cert: 目的端管理层证书
        :type target_mgmt_cert: str
        :param target_mgmt_private_key: 目的端管理层私钥
        :type target_mgmt_private_key: str
        :param target_data_cert: 目的端数据层证书
        :type target_data_cert: str
        :param target_data_private_key: 目的端数据层私钥
        :type target_data_private_key: str
        """
        
        super(ShowCertKeyResponse, self).__init__()

        self._cert = None
        self._private_key = None
        self._ca = None
        self._target_mgmt_cert = None
        self._target_mgmt_private_key = None
        self._target_data_cert = None
        self._target_data_private_key = None
        self.discriminator = None

        if cert is not None:
            self.cert = cert
        if private_key is not None:
            self.private_key = private_key
        if ca is not None:
            self.ca = ca
        if target_mgmt_cert is not None:
            self.target_mgmt_cert = target_mgmt_cert
        if target_mgmt_private_key is not None:
            self.target_mgmt_private_key = target_mgmt_private_key
        if target_data_cert is not None:
            self.target_data_cert = target_data_cert
        if target_data_private_key is not None:
            self.target_data_private_key = target_data_private_key

    @property
    def cert(self):
        """Gets the cert of this ShowCertKeyResponse.

        源端证书

        :return: The cert of this ShowCertKeyResponse.
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this ShowCertKeyResponse.

        源端证书

        :param cert: The cert of this ShowCertKeyResponse.
        :type cert: str
        """
        self._cert = cert

    @property
    def private_key(self):
        """Gets the private_key of this ShowCertKeyResponse.

        源端私钥

        :return: The private_key of this ShowCertKeyResponse.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this ShowCertKeyResponse.

        源端私钥

        :param private_key: The private_key of this ShowCertKeyResponse.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def ca(self):
        """Gets the ca of this ShowCertKeyResponse.

        ca证书

        :return: The ca of this ShowCertKeyResponse.
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this ShowCertKeyResponse.

        ca证书

        :param ca: The ca of this ShowCertKeyResponse.
        :type ca: str
        """
        self._ca = ca

    @property
    def target_mgmt_cert(self):
        """Gets the target_mgmt_cert of this ShowCertKeyResponse.

        目的端管理层证书

        :return: The target_mgmt_cert of this ShowCertKeyResponse.
        :rtype: str
        """
        return self._target_mgmt_cert

    @target_mgmt_cert.setter
    def target_mgmt_cert(self, target_mgmt_cert):
        """Sets the target_mgmt_cert of this ShowCertKeyResponse.

        目的端管理层证书

        :param target_mgmt_cert: The target_mgmt_cert of this ShowCertKeyResponse.
        :type target_mgmt_cert: str
        """
        self._target_mgmt_cert = target_mgmt_cert

    @property
    def target_mgmt_private_key(self):
        """Gets the target_mgmt_private_key of this ShowCertKeyResponse.

        目的端管理层私钥

        :return: The target_mgmt_private_key of this ShowCertKeyResponse.
        :rtype: str
        """
        return self._target_mgmt_private_key

    @target_mgmt_private_key.setter
    def target_mgmt_private_key(self, target_mgmt_private_key):
        """Sets the target_mgmt_private_key of this ShowCertKeyResponse.

        目的端管理层私钥

        :param target_mgmt_private_key: The target_mgmt_private_key of this ShowCertKeyResponse.
        :type target_mgmt_private_key: str
        """
        self._target_mgmt_private_key = target_mgmt_private_key

    @property
    def target_data_cert(self):
        """Gets the target_data_cert of this ShowCertKeyResponse.

        目的端数据层证书

        :return: The target_data_cert of this ShowCertKeyResponse.
        :rtype: str
        """
        return self._target_data_cert

    @target_data_cert.setter
    def target_data_cert(self, target_data_cert):
        """Sets the target_data_cert of this ShowCertKeyResponse.

        目的端数据层证书

        :param target_data_cert: The target_data_cert of this ShowCertKeyResponse.
        :type target_data_cert: str
        """
        self._target_data_cert = target_data_cert

    @property
    def target_data_private_key(self):
        """Gets the target_data_private_key of this ShowCertKeyResponse.

        目的端数据层私钥

        :return: The target_data_private_key of this ShowCertKeyResponse.
        :rtype: str
        """
        return self._target_data_private_key

    @target_data_private_key.setter
    def target_data_private_key(self, target_data_private_key):
        """Sets the target_data_private_key of this ShowCertKeyResponse.

        目的端数据层私钥

        :param target_data_private_key: The target_data_private_key of this ShowCertKeyResponse.
        :type target_data_private_key: str
        """
        self._target_data_private_key = target_data_private_key

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
        if not isinstance(other, ShowCertKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
