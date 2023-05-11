# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceAuthInfoDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_type': 'str',
        'fingerprint': 'str',
        'local_path': 'CertificateLocalPathDTO'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'fingerprint': 'fingerprint',
        'local_path': 'local_path'
    }

    def __init__(self, auth_type=None, fingerprint=None, local_path=None):
        """DeviceAuthInfoDTO

        The model defined in huaweicloud sdk

        :param auth_type: 边缘节点认证方式，不填默认为密钥认证接入方式(SECRET)。
        :type auth_type: str
        :param fingerprint: 证书指纹，认证类型使用证书认证接入(CERTIFICATES)需填写该字段。
        :type fingerprint: str
        :param local_path: 
        :type local_path: :class:`huaweicloudsdkiotedge.v2.CertificateLocalPathDTO`
        """
        
        

        self._auth_type = None
        self._fingerprint = None
        self._local_path = None
        self.discriminator = None

        self.auth_type = auth_type
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if local_path is not None:
            self.local_path = local_path

    @property
    def auth_type(self):
        """Gets the auth_type of this DeviceAuthInfoDTO.

        边缘节点认证方式，不填默认为密钥认证接入方式(SECRET)。

        :return: The auth_type of this DeviceAuthInfoDTO.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this DeviceAuthInfoDTO.

        边缘节点认证方式，不填默认为密钥认证接入方式(SECRET)。

        :param auth_type: The auth_type of this DeviceAuthInfoDTO.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def fingerprint(self):
        """Gets the fingerprint of this DeviceAuthInfoDTO.

        证书指纹，认证类型使用证书认证接入(CERTIFICATES)需填写该字段。

        :return: The fingerprint of this DeviceAuthInfoDTO.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this DeviceAuthInfoDTO.

        证书指纹，认证类型使用证书认证接入(CERTIFICATES)需填写该字段。

        :param fingerprint: The fingerprint of this DeviceAuthInfoDTO.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def local_path(self):
        """Gets the local_path of this DeviceAuthInfoDTO.

        :return: The local_path of this DeviceAuthInfoDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.CertificateLocalPathDTO`
        """
        return self._local_path

    @local_path.setter
    def local_path(self, local_path):
        """Sets the local_path of this DeviceAuthInfoDTO.

        :param local_path: The local_path of this DeviceAuthInfoDTO.
        :type local_path: :class:`huaweicloudsdkiotedge.v2.CertificateLocalPathDTO`
        """
        self._local_path = local_path

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
        if not isinstance(other, DeviceAuthInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
