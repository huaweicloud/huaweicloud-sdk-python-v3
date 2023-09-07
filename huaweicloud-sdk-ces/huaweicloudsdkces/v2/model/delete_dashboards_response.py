# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDashboardsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dashboards': 'list[BatchDeleteDashboardRespInfo]'
    }

    attribute_map = {
        'dashboards': 'dashboards'
    }

    def __init__(self, dashboards=None):
        """DeleteDashboardsResponse

        The model defined in huaweicloud sdk

        :param dashboards: 批量删除监控看板返回结果
        :type dashboards: list[:class:`huaweicloudsdkces.v2.BatchDeleteDashboardRespInfo`]
        """
        
        super(DeleteDashboardsResponse, self).__init__()

        self._dashboards = None
        self.discriminator = None

        if dashboards is not None:
            self.dashboards = dashboards

    @property
    def dashboards(self):
        """Gets the dashboards of this DeleteDashboardsResponse.

        批量删除监控看板返回结果

        :return: The dashboards of this DeleteDashboardsResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.BatchDeleteDashboardRespInfo`]
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """Sets the dashboards of this DeleteDashboardsResponse.

        批量删除监控看板返回结果

        :param dashboards: The dashboards of this DeleteDashboardsResponse.
        :type dashboards: list[:class:`huaweicloudsdkces.v2.BatchDeleteDashboardRespInfo`]
        """
        self._dashboards = dashboards

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
        if not isinstance(other, DeleteDashboardsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
