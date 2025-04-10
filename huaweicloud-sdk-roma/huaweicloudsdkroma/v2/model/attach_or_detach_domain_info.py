# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachOrDetachDomainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'instance_ids': 'list[str]',
        'verified_client_certificate_enabled': 'bool'
    }

    attribute_map = {
        'domain': 'domain',
        'instance_ids': 'instance_ids',
        'verified_client_certificate_enabled': 'verified_client_certificate_enabled'
    }

    def __init__(self, domain=None, instance_ids=None, verified_client_certificate_enabled=None):
        r"""AttachOrDetachDomainInfo

        The model defined in huaweicloud sdk

        :param domain: 域名
        :type domain: str
        :param instance_ids: 实例ID集合
        :type instance_ids: list[str]
        :param verified_client_certificate_enabled: 是否开启客户端证书校验。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。
        :type verified_client_certificate_enabled: bool
        """
        
        

        self._domain = None
        self._instance_ids = None
        self._verified_client_certificate_enabled = None
        self.discriminator = None

        self.domain = domain
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if verified_client_certificate_enabled is not None:
            self.verified_client_certificate_enabled = verified_client_certificate_enabled

    @property
    def domain(self):
        r"""Gets the domain of this AttachOrDetachDomainInfo.

        域名

        :return: The domain of this AttachOrDetachDomainInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this AttachOrDetachDomainInfo.

        域名

        :param domain: The domain of this AttachOrDetachDomainInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this AttachOrDetachDomainInfo.

        实例ID集合

        :return: The instance_ids of this AttachOrDetachDomainInfo.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this AttachOrDetachDomainInfo.

        实例ID集合

        :param instance_ids: The instance_ids of this AttachOrDetachDomainInfo.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def verified_client_certificate_enabled(self):
        r"""Gets the verified_client_certificate_enabled of this AttachOrDetachDomainInfo.

        是否开启客户端证书校验。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :return: The verified_client_certificate_enabled of this AttachOrDetachDomainInfo.
        :rtype: bool
        """
        return self._verified_client_certificate_enabled

    @verified_client_certificate_enabled.setter
    def verified_client_certificate_enabled(self, verified_client_certificate_enabled):
        r"""Sets the verified_client_certificate_enabled of this AttachOrDetachDomainInfo.

        是否开启客户端证书校验。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :param verified_client_certificate_enabled: The verified_client_certificate_enabled of this AttachOrDetachDomainInfo.
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
        if not isinstance(other, AttachOrDetachDomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
