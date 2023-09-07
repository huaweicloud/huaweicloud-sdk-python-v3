# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDashboardWidgetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dashboard_id': 'str'
    }

    attribute_map = {
        'dashboard_id': 'dashboard_id'
    }

    def __init__(self, dashboard_id=None):
        """ListDashboardWidgetsRequest

        The model defined in huaweicloud sdk

        :param dashboard_id: 监控看板id，以db开头，包含22个字母和数字例：db16564943172807wjOmoLyn&#39;
        :type dashboard_id: str
        """
        
        

        self._dashboard_id = None
        self.discriminator = None

        self.dashboard_id = dashboard_id

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this ListDashboardWidgetsRequest.

        监控看板id，以db开头，包含22个字母和数字例：db16564943172807wjOmoLyn'

        :return: The dashboard_id of this ListDashboardWidgetsRequest.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this ListDashboardWidgetsRequest.

        监控看板id，以db开头，包含22个字母和数字例：db16564943172807wjOmoLyn'

        :param dashboard_id: The dashboard_id of this ListDashboardWidgetsRequest.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

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
        if not isinstance(other, ListDashboardWidgetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
