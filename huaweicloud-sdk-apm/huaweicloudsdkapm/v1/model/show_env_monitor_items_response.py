# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEnvMonitorItemsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category_info_list': 'list[CollectorCategoryInfo]',
        'monitor_item_info_list': 'list[MonitorItemEntity]'
    }

    attribute_map = {
        'category_info_list': 'category_info_list',
        'monitor_item_info_list': 'monitor_item_info_list'
    }

    def __init__(self, category_info_list=None, monitor_item_info_list=None):
        """ShowEnvMonitorItemsResponse

        The model defined in huaweicloud sdk

        :param category_info_list: 采集器类别集合。
        :type category_info_list: list[:class:`huaweicloudsdkapm.v1.CollectorCategoryInfo`]
        :param monitor_item_info_list: 监控项集合。
        :type monitor_item_info_list: list[:class:`huaweicloudsdkapm.v1.MonitorItemEntity`]
        """
        
        super(ShowEnvMonitorItemsResponse, self).__init__()

        self._category_info_list = None
        self._monitor_item_info_list = None
        self.discriminator = None

        if category_info_list is not None:
            self.category_info_list = category_info_list
        if monitor_item_info_list is not None:
            self.monitor_item_info_list = monitor_item_info_list

    @property
    def category_info_list(self):
        """Gets the category_info_list of this ShowEnvMonitorItemsResponse.

        采集器类别集合。

        :return: The category_info_list of this ShowEnvMonitorItemsResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.CollectorCategoryInfo`]
        """
        return self._category_info_list

    @category_info_list.setter
    def category_info_list(self, category_info_list):
        """Sets the category_info_list of this ShowEnvMonitorItemsResponse.

        采集器类别集合。

        :param category_info_list: The category_info_list of this ShowEnvMonitorItemsResponse.
        :type category_info_list: list[:class:`huaweicloudsdkapm.v1.CollectorCategoryInfo`]
        """
        self._category_info_list = category_info_list

    @property
    def monitor_item_info_list(self):
        """Gets the monitor_item_info_list of this ShowEnvMonitorItemsResponse.

        监控项集合。

        :return: The monitor_item_info_list of this ShowEnvMonitorItemsResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.MonitorItemEntity`]
        """
        return self._monitor_item_info_list

    @monitor_item_info_list.setter
    def monitor_item_info_list(self, monitor_item_info_list):
        """Sets the monitor_item_info_list of this ShowEnvMonitorItemsResponse.

        监控项集合。

        :param monitor_item_info_list: The monitor_item_info_list of this ShowEnvMonitorItemsResponse.
        :type monitor_item_info_list: list[:class:`huaweicloudsdkapm.v1.MonitorItemEntity`]
        """
        self._monitor_item_info_list = monitor_item_info_list

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
        if not isinstance(other, ShowEnvMonitorItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
