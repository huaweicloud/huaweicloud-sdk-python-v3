# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVendorResponse(SdkResponse):

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
        'vendors': 'list[VendorDto]'
    }

    attribute_map = {
        'count': 'count',
        'vendors': 'vendors'
    }

    def __init__(self, count=None, vendors=None):
        """ListVendorResponse

        The model defined in huaweicloud sdk

        :param count: 供应商个数
        :type count: int
        :param vendors: 供应商列表
        :type vendors: list[:class:`huaweicloudsdkeihealth.v1.VendorDto`]
        """
        
        super(ListVendorResponse, self).__init__()

        self._count = None
        self._vendors = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if vendors is not None:
            self.vendors = vendors

    @property
    def count(self):
        """Gets the count of this ListVendorResponse.

        供应商个数

        :return: The count of this ListVendorResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListVendorResponse.

        供应商个数

        :param count: The count of this ListVendorResponse.
        :type count: int
        """
        self._count = count

    @property
    def vendors(self):
        """Gets the vendors of this ListVendorResponse.

        供应商列表

        :return: The vendors of this ListVendorResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.VendorDto`]
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        """Sets the vendors of this ListVendorResponse.

        供应商列表

        :param vendors: The vendors of this ListVendorResponse.
        :type vendors: list[:class:`huaweicloudsdkeihealth.v1.VendorDto`]
        """
        self._vendors = vendors

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
        if not isinstance(other, ListVendorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
