# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name_info': 'DomainNameInfo'
    }

    attribute_map = {
        'domain_name_info': 'domain_name_info'
    }

    def __init__(self, domain_name_info=None):
        r"""UpdateDomainNameResponse

        The model defined in huaweicloud sdk

        :param domain_name_info: 
        :type domain_name_info: :class:`huaweicloudsdkswr.v2.DomainNameInfo`
        """
        
        super(UpdateDomainNameResponse, self).__init__()

        self._domain_name_info = None
        self.discriminator = None

        if domain_name_info is not None:
            self.domain_name_info = domain_name_info

    @property
    def domain_name_info(self):
        r"""Gets the domain_name_info of this UpdateDomainNameResponse.

        :return: The domain_name_info of this UpdateDomainNameResponse.
        :rtype: :class:`huaweicloudsdkswr.v2.DomainNameInfo`
        """
        return self._domain_name_info

    @domain_name_info.setter
    def domain_name_info(self, domain_name_info):
        r"""Sets the domain_name_info of this UpdateDomainNameResponse.

        :param domain_name_info: The domain_name_info of this UpdateDomainNameResponse.
        :type domain_name_info: :class:`huaweicloudsdkswr.v2.DomainNameInfo`
        """
        self._domain_name_info = domain_name_info

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
        if not isinstance(other, UpdateDomainNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
