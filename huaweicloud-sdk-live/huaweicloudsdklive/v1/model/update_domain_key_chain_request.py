# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainKeyChainRequest:

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
        'body': 'KeyChainInfo'
    }

    attribute_map = {
        'domain': 'domain',
        'body': 'body'
    }

    def __init__(self, domain=None, body=None):
        """UpdateDomainKeyChainRequest

        The model defined in huaweicloud sdk

        :param domain: 直播域名，包括推流域名和播放域名
        :type domain: str
        :param body: Body of the UpdateDomainKeyChainRequest
        :type body: :class:`huaweicloudsdklive.v1.KeyChainInfo`
        """
        
        

        self._domain = None
        self._body = None
        self.discriminator = None

        self.domain = domain
        if body is not None:
            self.body = body

    @property
    def domain(self):
        """Gets the domain of this UpdateDomainKeyChainRequest.

        直播域名，包括推流域名和播放域名

        :return: The domain of this UpdateDomainKeyChainRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this UpdateDomainKeyChainRequest.

        直播域名，包括推流域名和播放域名

        :param domain: The domain of this UpdateDomainKeyChainRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def body(self):
        """Gets the body of this UpdateDomainKeyChainRequest.

        :return: The body of this UpdateDomainKeyChainRequest.
        :rtype: :class:`huaweicloudsdklive.v1.KeyChainInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDomainKeyChainRequest.

        :param body: The body of this UpdateDomainKeyChainRequest.
        :type body: :class:`huaweicloudsdklive.v1.KeyChainInfo`
        """
        self._body = body

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
        if not isinstance(other, UpdateDomainKeyChainRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
