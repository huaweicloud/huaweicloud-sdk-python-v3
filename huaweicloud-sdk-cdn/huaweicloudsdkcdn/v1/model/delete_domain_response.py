# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDomainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'DomainsWithPort',
        'x_request_id': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, domain=None, x_request_id=None):
        r"""DeleteDomainResponse

        The model defined in huaweicloud sdk

        :param domain: 
        :type domain: :class:`huaweicloudsdkcdn.v1.DomainsWithPort`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DeleteDomainResponse, self).__init__()

        self._domain = None
        self._x_request_id = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def domain(self):
        r"""Gets the domain of this DeleteDomainResponse.

        :return: The domain of this DeleteDomainResponse.
        :rtype: :class:`huaweicloudsdkcdn.v1.DomainsWithPort`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this DeleteDomainResponse.

        :param domain: The domain of this DeleteDomainResponse.
        :type domain: :class:`huaweicloudsdkcdn.v1.DomainsWithPort`
        """
        self._domain = domain

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this DeleteDomainResponse.

        :return: The x_request_id of this DeleteDomainResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this DeleteDomainResponse.

        :param x_request_id: The x_request_id of this DeleteDomainResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, DeleteDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
