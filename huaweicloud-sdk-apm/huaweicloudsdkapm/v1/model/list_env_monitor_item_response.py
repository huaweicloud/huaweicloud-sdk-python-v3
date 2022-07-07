# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnvMonitorItemResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'monitor_item_list': 'list[MonitorItem]',
        'total_count': 'int',
        'total_page': 'int'
    }

    attribute_map = {
        'monitor_item_list': 'monitor_item_list',
        'total_count': 'total_count',
        'total_page': 'totalPage'
    }

    def __init__(self, monitor_item_list=None, total_count=None, total_page=None):
        """ListEnvMonitorItemResponse

        The model defined in huaweicloud sdk

        :param monitor_item_list: 监控项列表
        :type monitor_item_list: list[:class:`huaweicloudsdkapm.v1.MonitorItem`]
        :param total_count: 总数
        :type total_count: int
        :param total_page: 总页数
        :type total_page: int
        """
        
        super(ListEnvMonitorItemResponse, self).__init__()

        self._monitor_item_list = None
        self._total_count = None
        self._total_page = None
        self.discriminator = None

        if monitor_item_list is not None:
            self.monitor_item_list = monitor_item_list
        if total_count is not None:
            self.total_count = total_count
        if total_page is not None:
            self.total_page = total_page

    @property
    def monitor_item_list(self):
        """Gets the monitor_item_list of this ListEnvMonitorItemResponse.

        监控项列表

        :return: The monitor_item_list of this ListEnvMonitorItemResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.MonitorItem`]
        """
        return self._monitor_item_list

    @monitor_item_list.setter
    def monitor_item_list(self, monitor_item_list):
        """Sets the monitor_item_list of this ListEnvMonitorItemResponse.

        监控项列表

        :param monitor_item_list: The monitor_item_list of this ListEnvMonitorItemResponse.
        :type monitor_item_list: list[:class:`huaweicloudsdkapm.v1.MonitorItem`]
        """
        self._monitor_item_list = monitor_item_list

    @property
    def total_count(self):
        """Gets the total_count of this ListEnvMonitorItemResponse.

        总数

        :return: The total_count of this ListEnvMonitorItemResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListEnvMonitorItemResponse.

        总数

        :param total_count: The total_count of this ListEnvMonitorItemResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def total_page(self):
        """Gets the total_page of this ListEnvMonitorItemResponse.

        总页数

        :return: The total_page of this ListEnvMonitorItemResponse.
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        """Sets the total_page of this ListEnvMonitorItemResponse.

        总页数

        :param total_page: The total_page of this ListEnvMonitorItemResponse.
        :type total_page: int
        """
        self._total_page = total_page

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
        if not isinstance(other, ListEnvMonitorItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
