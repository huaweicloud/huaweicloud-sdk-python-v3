# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateCertificateV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'group_id': 'str',
        'domain_id': 'str',
        'certificate_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group_id': 'group_id',
        'domain_id': 'domain_id',
        'certificate_id': 'certificate_id'
    }

    def __init__(self, instance_id=None, group_id=None, domain_id=None, certificate_id=None):
        r"""DisassociateCertificateV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param group_id: 分组的编号
        :type group_id: str
        :param domain_id: 域名的编号
        :type domain_id: str
        :param certificate_id: 证书的编号
        :type certificate_id: str
        """
        
        

        self._instance_id = None
        self._group_id = None
        self._domain_id = None
        self._certificate_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group_id = group_id
        self.domain_id = domain_id
        self.certificate_id = certificate_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DisassociateCertificateV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this DisassociateCertificateV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DisassociateCertificateV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this DisassociateCertificateV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group_id(self):
        r"""Gets the group_id of this DisassociateCertificateV2Request.

        分组的编号

        :return: The group_id of this DisassociateCertificateV2Request.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DisassociateCertificateV2Request.

        分组的编号

        :param group_id: The group_id of this DisassociateCertificateV2Request.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DisassociateCertificateV2Request.

        域名的编号

        :return: The domain_id of this DisassociateCertificateV2Request.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DisassociateCertificateV2Request.

        域名的编号

        :param domain_id: The domain_id of this DisassociateCertificateV2Request.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this DisassociateCertificateV2Request.

        证书的编号

        :return: The certificate_id of this DisassociateCertificateV2Request.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this DisassociateCertificateV2Request.

        证书的编号

        :param certificate_id: The certificate_id of this DisassociateCertificateV2Request.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

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
        if not isinstance(other, DisassociateCertificateV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
