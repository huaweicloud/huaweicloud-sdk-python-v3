# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_infos': 'list[CustomerInformation]',
        'count': 'int'
    }

    attribute_map = {
        'customer_infos': 'customer_infos',
        'count': 'count'
    }

    def __init__(self, customer_infos=None, count=None):
        r"""ListSubCustomersResponse

        The model defined in huaweicloud sdk

        :param customer_infos: 客户信息列表。 具体请参见表1。
        :type customer_infos: list[:class:`huaweicloudsdkbss.v2.CustomerInformation`]
        :param count: 总记录数。
        :type count: int
        """
        
        super(ListSubCustomersResponse, self).__init__()

        self._customer_infos = None
        self._count = None
        self.discriminator = None

        if customer_infos is not None:
            self.customer_infos = customer_infos
        if count is not None:
            self.count = count

    @property
    def customer_infos(self):
        r"""Gets the customer_infos of this ListSubCustomersResponse.

        客户信息列表。 具体请参见表1。

        :return: The customer_infos of this ListSubCustomersResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.CustomerInformation`]
        """
        return self._customer_infos

    @customer_infos.setter
    def customer_infos(self, customer_infos):
        r"""Sets the customer_infos of this ListSubCustomersResponse.

        客户信息列表。 具体请参见表1。

        :param customer_infos: The customer_infos of this ListSubCustomersResponse.
        :type customer_infos: list[:class:`huaweicloudsdkbss.v2.CustomerInformation`]
        """
        self._customer_infos = customer_infos

    @property
    def count(self):
        r"""Gets the count of this ListSubCustomersResponse.

        总记录数。

        :return: The count of this ListSubCustomersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSubCustomersResponse.

        总记录数。

        :param count: The count of this ListSubCustomersResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListSubCustomersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
