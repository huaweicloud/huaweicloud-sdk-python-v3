# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteDashboardRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dashboard_ids': 'list[str]'
    }

    attribute_map = {
        'dashboard_ids': 'dashboard_ids'
    }

    def __init__(self, dashboard_ids=None):
        """BatchDeleteDashboardRequestBody

        The model defined in huaweicloud sdk

        :param dashboard_ids: 监控看板id列表
        :type dashboard_ids: list[str]
        """
        
        

        self._dashboard_ids = None
        self.discriminator = None

        if dashboard_ids is not None:
            self.dashboard_ids = dashboard_ids

    @property
    def dashboard_ids(self):
        """Gets the dashboard_ids of this BatchDeleteDashboardRequestBody.

        监控看板id列表

        :return: The dashboard_ids of this BatchDeleteDashboardRequestBody.
        :rtype: list[str]
        """
        return self._dashboard_ids

    @dashboard_ids.setter
    def dashboard_ids(self, dashboard_ids):
        """Sets the dashboard_ids of this BatchDeleteDashboardRequestBody.

        监控看板id列表

        :param dashboard_ids: The dashboard_ids of this BatchDeleteDashboardRequestBody.
        :type dashboard_ids: list[str]
        """
        self._dashboard_ids = dashboard_ids

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
        if not isinstance(other, BatchDeleteDashboardRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
