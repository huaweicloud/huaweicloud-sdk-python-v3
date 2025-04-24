# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainMultiCertificatesResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'status': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'status': 'status',
        'reason': 'reason'
    }

    def __init__(self, domain_name=None, status=None, reason=None):
        r"""UpdateDomainMultiCertificatesResponseBodyResult

        The model defined in huaweicloud sdk

        :param domain_name: 域名名称
        :type domain_name: str
        :param status: 执行结果，success，fail
        :type status: str
        :param reason: 失败原因
        :type reason: str
        """
        
        

        self._domain_name = None
        self._status = None
        self._reason = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UpdateDomainMultiCertificatesResponseBodyResult.

        域名名称

        :return: The domain_name of this UpdateDomainMultiCertificatesResponseBodyResult.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UpdateDomainMultiCertificatesResponseBodyResult.

        域名名称

        :param domain_name: The domain_name of this UpdateDomainMultiCertificatesResponseBodyResult.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def status(self):
        r"""Gets the status of this UpdateDomainMultiCertificatesResponseBodyResult.

        执行结果，success，fail

        :return: The status of this UpdateDomainMultiCertificatesResponseBodyResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateDomainMultiCertificatesResponseBodyResult.

        执行结果，success，fail

        :param status: The status of this UpdateDomainMultiCertificatesResponseBodyResult.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this UpdateDomainMultiCertificatesResponseBodyResult.

        失败原因

        :return: The reason of this UpdateDomainMultiCertificatesResponseBodyResult.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this UpdateDomainMultiCertificatesResponseBodyResult.

        失败原因

        :param reason: The reason of this UpdateDomainMultiCertificatesResponseBodyResult.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, UpdateDomainMultiCertificatesResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
