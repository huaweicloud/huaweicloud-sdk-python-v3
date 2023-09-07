# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DashBoardNameItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dashboard_name': 'str'
    }

    attribute_map = {
        'dashboard_name': 'dashboard_name'
    }

    def __init__(self, dashboard_name=None):
        """DashBoardNameItem

        The model defined in huaweicloud sdk

        :param dashboard_name: 自定义监控看板名称
        :type dashboard_name: str
        """
        
        

        self._dashboard_name = None
        self.discriminator = None

        if dashboard_name is not None:
            self.dashboard_name = dashboard_name

    @property
    def dashboard_name(self):
        """Gets the dashboard_name of this DashBoardNameItem.

        自定义监控看板名称

        :return: The dashboard_name of this DashBoardNameItem.
        :rtype: str
        """
        return self._dashboard_name

    @dashboard_name.setter
    def dashboard_name(self, dashboard_name):
        """Sets the dashboard_name of this DashBoardNameItem.

        自定义监控看板名称

        :param dashboard_name: The dashboard_name of this DashBoardNameItem.
        :type dashboard_name: str
        """
        self._dashboard_name = dashboard_name

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
        if not isinstance(other, DashBoardNameItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
