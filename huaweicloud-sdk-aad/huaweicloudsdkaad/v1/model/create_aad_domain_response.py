# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAadDomainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cname': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'cname': 'cname',
        'domain_id': 'domainId'
    }

    def __init__(self, cname=None, domain_id=None):
        """CreateAadDomainResponse

        The model defined in huaweicloud sdk

        :param cname: 高防提供的CNAME地址
        :type cname: str
        :param domain_id: 域名id
        :type domain_id: str
        """
        
        super(CreateAadDomainResponse, self).__init__()

        self._cname = None
        self._domain_id = None
        self.discriminator = None

        if cname is not None:
            self.cname = cname
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def cname(self):
        """Gets the cname of this CreateAadDomainResponse.

        高防提供的CNAME地址

        :return: The cname of this CreateAadDomainResponse.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this CreateAadDomainResponse.

        高防提供的CNAME地址

        :param cname: The cname of this CreateAadDomainResponse.
        :type cname: str
        """
        self._cname = cname

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateAadDomainResponse.

        域名id

        :return: The domain_id of this CreateAadDomainResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateAadDomainResponse.

        域名id

        :param domain_id: The domain_id of this CreateAadDomainResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, CreateAadDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
