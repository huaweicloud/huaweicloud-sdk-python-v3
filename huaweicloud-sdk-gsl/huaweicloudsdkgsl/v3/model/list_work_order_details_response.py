# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkOrderDetailsResponse(SdkResponse):

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
        'work_order_details': 'list[WorkOrderDetailVo]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'count': 'count',
        'work_order_details': 'work_order_details'
    }

    def __init__(self, limit=None, offset=None, count=None, work_order_details=None):
        """ListWorkOrderDetailsResponse

        The model defined in huaweicloud sdk

        :param limit: 每页的记录数
        :type limit: int
        :param offset: 页码，最小值是1，最大值为1000000。默认值是1.
        :type offset: int
        :param count: 记录总数
        :type count: int
        :param work_order_details: 业务受理明细列表
        :type work_order_details: list[:class:`huaweicloudsdkgsl.v3.WorkOrderDetailVo`]
        """
        
        super(ListWorkOrderDetailsResponse, self).__init__()

        self._limit = None
        self._offset = None
        self._count = None
        self._work_order_details = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if count is not None:
            self.count = count
        if work_order_details is not None:
            self.work_order_details = work_order_details

    @property
    def limit(self):
        """Gets the limit of this ListWorkOrderDetailsResponse.

        每页的记录数

        :return: The limit of this ListWorkOrderDetailsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWorkOrderDetailsResponse.

        每页的记录数

        :param limit: The limit of this ListWorkOrderDetailsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListWorkOrderDetailsResponse.

        页码，最小值是1，最大值为1000000。默认值是1.

        :return: The offset of this ListWorkOrderDetailsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListWorkOrderDetailsResponse.

        页码，最小值是1，最大值为1000000。默认值是1.

        :param offset: The offset of this ListWorkOrderDetailsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def count(self):
        """Gets the count of this ListWorkOrderDetailsResponse.

        记录总数

        :return: The count of this ListWorkOrderDetailsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListWorkOrderDetailsResponse.

        记录总数

        :param count: The count of this ListWorkOrderDetailsResponse.
        :type count: int
        """
        self._count = count

    @property
    def work_order_details(self):
        """Gets the work_order_details of this ListWorkOrderDetailsResponse.

        业务受理明细列表

        :return: The work_order_details of this ListWorkOrderDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkgsl.v3.WorkOrderDetailVo`]
        """
        return self._work_order_details

    @work_order_details.setter
    def work_order_details(self, work_order_details):
        """Sets the work_order_details of this ListWorkOrderDetailsResponse.

        业务受理明细列表

        :param work_order_details: The work_order_details of this ListWorkOrderDetailsResponse.
        :type work_order_details: list[:class:`huaweicloudsdkgsl.v3.WorkOrderDetailVo`]
        """
        self._work_order_details = work_order_details

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
        if not isinstance(other, ListWorkOrderDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
