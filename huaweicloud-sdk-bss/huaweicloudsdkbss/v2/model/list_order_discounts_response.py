# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrderDiscountsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'discounts': 'list[DiscountInfoV3]'
    }

    attribute_map = {
        'discounts': 'discounts'
    }

    def __init__(self, discounts=None):
        """ListOrderDiscountsResponse

        The model defined in huaweicloud sdk

        :param discounts: 可用的折扣列表。 具体请参见表2。
        :type discounts: list[:class:`huaweicloudsdkbss.v2.DiscountInfoV3`]
        """
        
        super(ListOrderDiscountsResponse, self).__init__()

        self._discounts = None
        self.discriminator = None

        if discounts is not None:
            self.discounts = discounts

    @property
    def discounts(self):
        """Gets the discounts of this ListOrderDiscountsResponse.

        可用的折扣列表。 具体请参见表2。

        :return: The discounts of this ListOrderDiscountsResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.DiscountInfoV3`]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this ListOrderDiscountsResponse.

        可用的折扣列表。 具体请参见表2。

        :param discounts: The discounts of this ListOrderDiscountsResponse.
        :type discounts: list[:class:`huaweicloudsdkbss.v2.DiscountInfoV3`]
        """
        self._discounts = discounts

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
        if not isinstance(other, ListOrderDiscountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
