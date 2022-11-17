# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainItemDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_item_details': 'DomainItemDetail'
    }

    attribute_map = {
        'domain_item_details': 'domain_item_details'
    }

    def __init__(self, domain_item_details=None):
        """ShowDomainItemDetailsResponse

        The model defined in huaweicloud sdk

        :param domain_item_details: 
        :type domain_item_details: :class:`huaweicloudsdkcdn.v1.DomainItemDetail`
        """
        
        super(ShowDomainItemDetailsResponse, self).__init__()

        self._domain_item_details = None
        self.discriminator = None

        if domain_item_details is not None:
            self.domain_item_details = domain_item_details

    @property
    def domain_item_details(self):
        """Gets the domain_item_details of this ShowDomainItemDetailsResponse.

        :return: The domain_item_details of this ShowDomainItemDetailsResponse.
        :rtype: :class:`huaweicloudsdkcdn.v1.DomainItemDetail`
        """
        return self._domain_item_details

    @domain_item_details.setter
    def domain_item_details(self, domain_item_details):
        """Sets the domain_item_details of this ShowDomainItemDetailsResponse.

        :param domain_item_details: The domain_item_details of this ShowDomainItemDetailsResponse.
        :type domain_item_details: :class:`huaweicloudsdkcdn.v1.DomainItemDetail`
        """
        self._domain_item_details = domain_item_details

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
        if not isinstance(other, ShowDomainItemDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
