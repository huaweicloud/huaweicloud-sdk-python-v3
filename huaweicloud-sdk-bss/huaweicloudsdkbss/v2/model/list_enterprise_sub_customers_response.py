# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseSubCustomersResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'sub_customer_infos': 'list[SubCustomerInfoV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'sub_customer_infos': 'sub_customer_infos'
    }

    def __init__(self, total_count=None, sub_customer_infos=None):
        """ListEnterpriseSubCustomersResponse - a model defined in huaweicloud sdk"""
        
        super(ListEnterpriseSubCustomersResponse, self).__init__()

        self._total_count = None
        self._sub_customer_infos = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if sub_customer_infos is not None:
            self.sub_customer_infos = sub_customer_infos

    @property
    def total_count(self):
        """Gets the total_count of this ListEnterpriseSubCustomersResponse.

        结果集数量，成功才有。

        :return: The total_count of this ListEnterpriseSubCustomersResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListEnterpriseSubCustomersResponse.

        结果集数量，成功才有。

        :param total_count: The total_count of this ListEnterpriseSubCustomersResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def sub_customer_infos(self):
        """Gets the sub_customer_infos of this ListEnterpriseSubCustomersResponse.

        客户信息列表，成功才有。 具体请参见表2。

        :return: The sub_customer_infos of this ListEnterpriseSubCustomersResponse.
        :rtype: list[SubCustomerInfoV2]
        """
        return self._sub_customer_infos

    @sub_customer_infos.setter
    def sub_customer_infos(self, sub_customer_infos):
        """Sets the sub_customer_infos of this ListEnterpriseSubCustomersResponse.

        客户信息列表，成功才有。 具体请参见表2。

        :param sub_customer_infos: The sub_customer_infos of this ListEnterpriseSubCustomersResponse.
        :type: list[SubCustomerInfoV2]
        """
        self._sub_customer_infos = sub_customer_infos

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListEnterpriseSubCustomersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
