# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDashboardWidgetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'widget_ids': 'list[str]'
    }

    attribute_map = {
        'widget_ids': 'widget_ids'
    }

    def __init__(self, widget_ids=None):
        r"""CreateDashboardWidgetsResponse

        The model defined in huaweicloud sdk

        :param widget_ids: 批量创建监控视图返回结果
        :type widget_ids: list[str]
        """
        
        super(CreateDashboardWidgetsResponse, self).__init__()

        self._widget_ids = None
        self.discriminator = None

        if widget_ids is not None:
            self.widget_ids = widget_ids

    @property
    def widget_ids(self):
        r"""Gets the widget_ids of this CreateDashboardWidgetsResponse.

        批量创建监控视图返回结果

        :return: The widget_ids of this CreateDashboardWidgetsResponse.
        :rtype: list[str]
        """
        return self._widget_ids

    @widget_ids.setter
    def widget_ids(self, widget_ids):
        r"""Sets the widget_ids of this CreateDashboardWidgetsResponse.

        批量创建监控视图返回结果

        :param widget_ids: The widget_ids of this CreateDashboardWidgetsResponse.
        :type widget_ids: list[str]
        """
        self._widget_ids = widget_ids

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
        if not isinstance(other, CreateDashboardWidgetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
