# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachOrDetachCertsReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_ids': 'list[str]',
        'verified_client_certificate_enabled': 'bool'
    }

    attribute_map = {
        'certificate_ids': 'certificate_ids',
        'verified_client_certificate_enabled': 'verified_client_certificate_enabled'
    }

    def __init__(self, certificate_ids=None, verified_client_certificate_enabled=None):
        """AttachOrDetachCertsReqBody

        The model defined in huaweicloud sdk

        :param certificate_ids: 证书的id集合
        :type certificate_ids: list[str]
        :param verified_client_certificate_enabled: 是否开启客户端证书校验。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。
        :type verified_client_certificate_enabled: bool
        """
        
        

        self._certificate_ids = None
        self._verified_client_certificate_enabled = None
        self.discriminator = None

        self.certificate_ids = certificate_ids
        if verified_client_certificate_enabled is not None:
            self.verified_client_certificate_enabled = verified_client_certificate_enabled

    @property
    def certificate_ids(self):
        """Gets the certificate_ids of this AttachOrDetachCertsReqBody.

        证书的id集合

        :return: The certificate_ids of this AttachOrDetachCertsReqBody.
        :rtype: list[str]
        """
        return self._certificate_ids

    @certificate_ids.setter
    def certificate_ids(self, certificate_ids):
        """Sets the certificate_ids of this AttachOrDetachCertsReqBody.

        证书的id集合

        :param certificate_ids: The certificate_ids of this AttachOrDetachCertsReqBody.
        :type certificate_ids: list[str]
        """
        self._certificate_ids = certificate_ids

    @property
    def verified_client_certificate_enabled(self):
        """Gets the verified_client_certificate_enabled of this AttachOrDetachCertsReqBody.

        是否开启客户端证书校验。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :return: The verified_client_certificate_enabled of this AttachOrDetachCertsReqBody.
        :rtype: bool
        """
        return self._verified_client_certificate_enabled

    @verified_client_certificate_enabled.setter
    def verified_client_certificate_enabled(self, verified_client_certificate_enabled):
        """Sets the verified_client_certificate_enabled of this AttachOrDetachCertsReqBody.

        是否开启客户端证书校验。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :param verified_client_certificate_enabled: The verified_client_certificate_enabled of this AttachOrDetachCertsReqBody.
        :type verified_client_certificate_enabled: bool
        """
        self._verified_client_certificate_enabled = verified_client_certificate_enabled

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
        if not isinstance(other, AttachOrDetachCertsReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
