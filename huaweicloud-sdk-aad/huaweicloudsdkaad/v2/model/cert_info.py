# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_name': 'str',
        'id': 'str',
        'apply_domain': 'str',
        'expire_time': 'int',
        'expire_status': 'int'
    }

    attribute_map = {
        'cert_name': 'cert_name',
        'id': 'id',
        'apply_domain': 'apply_domain',
        'expire_time': 'expire_time',
        'expire_status': 'expire_status'
    }

    def __init__(self, cert_name=None, id=None, apply_domain=None, expire_time=None, expire_status=None):
        r"""CertInfo

        The model defined in huaweicloud sdk

        :param cert_name: 证书名称
        :type cert_name: str
        :param id: 证书id
        :type id: str
        :param apply_domain: 适用域名
        :type apply_domain: str
        :param expire_time: 过期时间
        :type expire_time: int
        :param expire_status: 过期状态
        :type expire_status: int
        """
        
        

        self._cert_name = None
        self._id = None
        self._apply_domain = None
        self._expire_time = None
        self._expire_status = None
        self.discriminator = None

        self.cert_name = cert_name
        self.id = id
        self.apply_domain = apply_domain
        self.expire_time = expire_time
        self.expire_status = expire_status

    @property
    def cert_name(self):
        r"""Gets the cert_name of this CertInfo.

        证书名称

        :return: The cert_name of this CertInfo.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this CertInfo.

        证书名称

        :param cert_name: The cert_name of this CertInfo.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def id(self):
        r"""Gets the id of this CertInfo.

        证书id

        :return: The id of this CertInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CertInfo.

        证书id

        :param id: The id of this CertInfo.
        :type id: str
        """
        self._id = id

    @property
    def apply_domain(self):
        r"""Gets the apply_domain of this CertInfo.

        适用域名

        :return: The apply_domain of this CertInfo.
        :rtype: str
        """
        return self._apply_domain

    @apply_domain.setter
    def apply_domain(self, apply_domain):
        r"""Sets the apply_domain of this CertInfo.

        适用域名

        :param apply_domain: The apply_domain of this CertInfo.
        :type apply_domain: str
        """
        self._apply_domain = apply_domain

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CertInfo.

        过期时间

        :return: The expire_time of this CertInfo.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CertInfo.

        过期时间

        :param expire_time: The expire_time of this CertInfo.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def expire_status(self):
        r"""Gets the expire_status of this CertInfo.

        过期状态

        :return: The expire_status of this CertInfo.
        :rtype: int
        """
        return self._expire_status

    @expire_status.setter
    def expire_status(self, expire_status):
        r"""Sets the expire_status of this CertInfo.

        过期状态

        :param expire_status: The expire_status of this CertInfo.
        :type expire_status: int
        """
        self._expire_status = expire_status

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
        if not isinstance(other, CertInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
