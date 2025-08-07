# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBusinessPartnersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_partners': 'list[BusinessPartner]',
        'total_count': 'int'
    }

    attribute_map = {
        'business_partners': 'business_partners',
        'total_count': 'total_count'
    }

    def __init__(self, business_partners=None, total_count=None):
        r"""ListBusinessPartnersResponse

        The model defined in huaweicloud sdk

        :param business_partners: 服务商列表。
        :type business_partners: list[:class:`huaweicloudsdkrds.v3.BusinessPartner`]
        :param total_count: 总服务商数。
        :type total_count: int
        """
        
        super(ListBusinessPartnersResponse, self).__init__()

        self._business_partners = None
        self._total_count = None
        self.discriminator = None

        if business_partners is not None:
            self.business_partners = business_partners
        if total_count is not None:
            self.total_count = total_count

    @property
    def business_partners(self):
        r"""Gets the business_partners of this ListBusinessPartnersResponse.

        服务商列表。

        :return: The business_partners of this ListBusinessPartnersResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.BusinessPartner`]
        """
        return self._business_partners

    @business_partners.setter
    def business_partners(self, business_partners):
        r"""Sets the business_partners of this ListBusinessPartnersResponse.

        服务商列表。

        :param business_partners: The business_partners of this ListBusinessPartnersResponse.
        :type business_partners: list[:class:`huaweicloudsdkrds.v3.BusinessPartner`]
        """
        self._business_partners = business_partners

    @property
    def total_count(self):
        r"""Gets the total_count of this ListBusinessPartnersResponse.

        总服务商数。

        :return: The total_count of this ListBusinessPartnersResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListBusinessPartnersResponse.

        总服务商数。

        :param total_count: The total_count of this ListBusinessPartnersResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListBusinessPartnersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
