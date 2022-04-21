# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInvoicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'invoices': 'list[InvoiceRequestInfoIntl]'
    }

    attribute_map = {
        'count': 'count',
        'invoices': 'invoices'
    }

    def __init__(self, count=None, invoices=None):
        """ListInvoicesResponse

        The model defined in huaweicloud sdk

        :param count: 记录数，只有成功的时候才返回这个字段
        :type count: int
        :param invoices: 发票信息列表，参见表2。
        :type invoices: list[:class:`huaweicloudsdkbssintl.v2.InvoiceRequestInfoIntl`]
        """
        
        super(ListInvoicesResponse, self).__init__()

        self._count = None
        self._invoices = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if invoices is not None:
            self.invoices = invoices

    @property
    def count(self):
        """Gets the count of this ListInvoicesResponse.

        记录数，只有成功的时候才返回这个字段

        :return: The count of this ListInvoicesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListInvoicesResponse.

        记录数，只有成功的时候才返回这个字段

        :param count: The count of this ListInvoicesResponse.
        :type count: int
        """
        self._count = count

    @property
    def invoices(self):
        """Gets the invoices of this ListInvoicesResponse.

        发票信息列表，参见表2。

        :return: The invoices of this ListInvoicesResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.InvoiceRequestInfoIntl`]
        """
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        """Sets the invoices of this ListInvoicesResponse.

        发票信息列表，参见表2。

        :param invoices: The invoices of this ListInvoicesResponse.
        :type invoices: list[:class:`huaweicloudsdkbssintl.v2.InvoiceRequestInfoIntl`]
        """
        self._invoices = invoices

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
        if not isinstance(other, ListInvoicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
