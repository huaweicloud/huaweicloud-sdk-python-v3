# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkOrdersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'count': 'int',
        'work_orders': 'list[WorkOrderVo]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'count': 'count',
        'work_orders': 'work_orders'
    }

    def __init__(self, limit=None, offset=None, count=None, work_orders=None):
        r"""ListWorkOrdersResponse

        The model defined in huaweicloud sdk

        :param limit: 每页的记录数
        :type limit: int
        :param offset: 页码，最小值是1，最大值为1000000。默认值是1.
        :type offset: int
        :param count: 记录总数
        :type count: int
        :param work_orders: 业务受理单列表
        :type work_orders: list[:class:`huaweicloudsdkgsl.v3.WorkOrderVo`]
        """
        
        super(ListWorkOrdersResponse, self).__init__()

        self._limit = None
        self._offset = None
        self._count = None
        self._work_orders = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if count is not None:
            self.count = count
        if work_orders is not None:
            self.work_orders = work_orders

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkOrdersResponse.

        每页的记录数

        :return: The limit of this ListWorkOrdersResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkOrdersResponse.

        每页的记录数

        :param limit: The limit of this ListWorkOrdersResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkOrdersResponse.

        页码，最小值是1，最大值为1000000。默认值是1.

        :return: The offset of this ListWorkOrdersResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkOrdersResponse.

        页码，最小值是1，最大值为1000000。默认值是1.

        :param offset: The offset of this ListWorkOrdersResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def count(self):
        r"""Gets the count of this ListWorkOrdersResponse.

        记录总数

        :return: The count of this ListWorkOrdersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListWorkOrdersResponse.

        记录总数

        :param count: The count of this ListWorkOrdersResponse.
        :type count: int
        """
        self._count = count

    @property
    def work_orders(self):
        r"""Gets the work_orders of this ListWorkOrdersResponse.

        业务受理单列表

        :return: The work_orders of this ListWorkOrdersResponse.
        :rtype: list[:class:`huaweicloudsdkgsl.v3.WorkOrderVo`]
        """
        return self._work_orders

    @work_orders.setter
    def work_orders(self, work_orders):
        r"""Sets the work_orders of this ListWorkOrdersResponse.

        业务受理单列表

        :param work_orders: The work_orders of this ListWorkOrdersResponse.
        :type work_orders: list[:class:`huaweicloudsdkgsl.v3.WorkOrderVo`]
        """
        self._work_orders = work_orders

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
        if not isinstance(other, ListWorkOrdersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
