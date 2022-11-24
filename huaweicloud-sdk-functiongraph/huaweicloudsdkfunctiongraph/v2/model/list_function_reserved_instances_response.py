# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionReservedInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reservedinstances': 'list[FuncReservedInstance]',
        'page_info': 'PageInfo',
        'count': 'int'
    }

    attribute_map = {
        'reservedinstances': 'reservedinstances',
        'page_info': 'page_info',
        'count': 'count'
    }

    def __init__(self, reservedinstances=None, page_info=None, count=None):
        """ListFunctionReservedInstancesResponse

        The model defined in huaweicloud sdk

        :param reservedinstances: 函数预留实例列表
        :type reservedinstances: list[:class:`huaweicloudsdkfunctiongraph.v2.FuncReservedInstance`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkfunctiongraph.v2.PageInfo`
        :param count: 函数个数
        :type count: int
        """
        
        super(ListFunctionReservedInstancesResponse, self).__init__()

        self._reservedinstances = None
        self._page_info = None
        self._count = None
        self.discriminator = None

        if reservedinstances is not None:
            self.reservedinstances = reservedinstances
        if page_info is not None:
            self.page_info = page_info
        if count is not None:
            self.count = count

    @property
    def reservedinstances(self):
        """Gets the reservedinstances of this ListFunctionReservedInstancesResponse.

        函数预留实例列表

        :return: The reservedinstances of this ListFunctionReservedInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.FuncReservedInstance`]
        """
        return self._reservedinstances

    @reservedinstances.setter
    def reservedinstances(self, reservedinstances):
        """Sets the reservedinstances of this ListFunctionReservedInstancesResponse.

        函数预留实例列表

        :param reservedinstances: The reservedinstances of this ListFunctionReservedInstancesResponse.
        :type reservedinstances: list[:class:`huaweicloudsdkfunctiongraph.v2.FuncReservedInstance`]
        """
        self._reservedinstances = reservedinstances

    @property
    def page_info(self):
        """Gets the page_info of this ListFunctionReservedInstancesResponse.

        :return: The page_info of this ListFunctionReservedInstancesResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListFunctionReservedInstancesResponse.

        :param page_info: The page_info of this ListFunctionReservedInstancesResponse.
        :type page_info: :class:`huaweicloudsdkfunctiongraph.v2.PageInfo`
        """
        self._page_info = page_info

    @property
    def count(self):
        """Gets the count of this ListFunctionReservedInstancesResponse.

        函数个数

        :return: The count of this ListFunctionReservedInstancesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListFunctionReservedInstancesResponse.

        函数个数

        :param count: The count of this ListFunctionReservedInstancesResponse.
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
        if not isinstance(other, ListFunctionReservedInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
