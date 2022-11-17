# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConsumeSubCustomersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_customers': 'list[SubCustomerInfoV3]',
        'total_count': 'int'
    }

    attribute_map = {
        'sub_customers': 'sub_customers',
        'total_count': 'total_count'
    }

    def __init__(self, sub_customers=None, total_count=None):
        """ListConsumeSubCustomersResponse

        The model defined in huaweicloud sdk

        :param sub_customers: 子客户列表。 具体请参见表SubCustomerInfo。
        :type sub_customers: list[:class:`huaweicloudsdkbss.v2.SubCustomerInfoV3`]
        :param total_count: 结果集数量，只有成功才返回这个参数。
        :type total_count: int
        """
        
        super(ListConsumeSubCustomersResponse, self).__init__()

        self._sub_customers = None
        self._total_count = None
        self.discriminator = None

        if sub_customers is not None:
            self.sub_customers = sub_customers
        if total_count is not None:
            self.total_count = total_count

    @property
    def sub_customers(self):
        """Gets the sub_customers of this ListConsumeSubCustomersResponse.

        子客户列表。 具体请参见表SubCustomerInfo。

        :return: The sub_customers of this ListConsumeSubCustomersResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.SubCustomerInfoV3`]
        """
        return self._sub_customers

    @sub_customers.setter
    def sub_customers(self, sub_customers):
        """Sets the sub_customers of this ListConsumeSubCustomersResponse.

        子客户列表。 具体请参见表SubCustomerInfo。

        :param sub_customers: The sub_customers of this ListConsumeSubCustomersResponse.
        :type sub_customers: list[:class:`huaweicloudsdkbss.v2.SubCustomerInfoV3`]
        """
        self._sub_customers = sub_customers

    @property
    def total_count(self):
        """Gets the total_count of this ListConsumeSubCustomersResponse.

        结果集数量，只有成功才返回这个参数。

        :return: The total_count of this ListConsumeSubCustomersResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListConsumeSubCustomersResponse.

        结果集数量，只有成功才返回这个参数。

        :param total_count: The total_count of this ListConsumeSubCustomersResponse.
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
        if not isinstance(other, ListConsumeSubCustomersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
