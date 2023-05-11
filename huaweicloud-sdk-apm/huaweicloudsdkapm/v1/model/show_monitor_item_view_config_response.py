# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonitorItemViewConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'collector_name': 'str',
        'view_row_list': 'list[ViewRow]',
        'style': 'str'
    }

    attribute_map = {
        'title': 'title',
        'collector_name': 'collector_name',
        'view_row_list': 'view_row_list',
        'style': 'style'
    }

    def __init__(self, title=None, collector_name=None, view_row_list=None, style=None):
        """ShowMonitorItemViewConfigResponse

        The model defined in huaweicloud sdk

        :param title: 标题。
        :type title: str
        :param collector_name: 采集器名称。
        :type collector_name: str
        :param view_row_list: 视图的列表，内部每个List代表的是一行图表。
        :type view_row_list: list[:class:`huaweicloudsdkapm.v1.ViewRow`]
        :param style: 类型。
        :type style: str
        """
        
        super(ShowMonitorItemViewConfigResponse, self).__init__()

        self._title = None
        self._collector_name = None
        self._view_row_list = None
        self._style = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if collector_name is not None:
            self.collector_name = collector_name
        if view_row_list is not None:
            self.view_row_list = view_row_list
        if style is not None:
            self.style = style

    @property
    def title(self):
        """Gets the title of this ShowMonitorItemViewConfigResponse.

        标题。

        :return: The title of this ShowMonitorItemViewConfigResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ShowMonitorItemViewConfigResponse.

        标题。

        :param title: The title of this ShowMonitorItemViewConfigResponse.
        :type title: str
        """
        self._title = title

    @property
    def collector_name(self):
        """Gets the collector_name of this ShowMonitorItemViewConfigResponse.

        采集器名称。

        :return: The collector_name of this ShowMonitorItemViewConfigResponse.
        :rtype: str
        """
        return self._collector_name

    @collector_name.setter
    def collector_name(self, collector_name):
        """Sets the collector_name of this ShowMonitorItemViewConfigResponse.

        采集器名称。

        :param collector_name: The collector_name of this ShowMonitorItemViewConfigResponse.
        :type collector_name: str
        """
        self._collector_name = collector_name

    @property
    def view_row_list(self):
        """Gets the view_row_list of this ShowMonitorItemViewConfigResponse.

        视图的列表，内部每个List代表的是一行图表。

        :return: The view_row_list of this ShowMonitorItemViewConfigResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.ViewRow`]
        """
        return self._view_row_list

    @view_row_list.setter
    def view_row_list(self, view_row_list):
        """Sets the view_row_list of this ShowMonitorItemViewConfigResponse.

        视图的列表，内部每个List代表的是一行图表。

        :param view_row_list: The view_row_list of this ShowMonitorItemViewConfigResponse.
        :type view_row_list: list[:class:`huaweicloudsdkapm.v1.ViewRow`]
        """
        self._view_row_list = view_row_list

    @property
    def style(self):
        """Gets the style of this ShowMonitorItemViewConfigResponse.

        类型。

        :return: The style of this ShowMonitorItemViewConfigResponse.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this ShowMonitorItemViewConfigResponse.

        类型。

        :param style: The style of this ShowMonitorItemViewConfigResponse.
        :type style: str
        """
        self._style = style

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
        if not isinstance(other, ShowMonitorItemViewConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
