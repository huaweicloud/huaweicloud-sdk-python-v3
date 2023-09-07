# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDashboardRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dashboard_name': 'str',
        'is_favorite': 'bool',
        'row_widget_num': 'int'
    }

    attribute_map = {
        'dashboard_name': 'dashboard_name',
        'is_favorite': 'is_favorite',
        'row_widget_num': 'row_widget_num'
    }

    def __init__(self, dashboard_name=None, is_favorite=None, row_widget_num=None):
        """UpdateDashboardRequestBody

        The model defined in huaweicloud sdk

        :param dashboard_name: 自定义监控看板名称
        :type dashboard_name: str
        :param is_favorite: 监控看板是否标记收藏, true: 收藏, false: 未收藏
        :type is_favorite: bool
        :param row_widget_num: 监控视图展示模式，0表示自定义坐标，1代表每行一个
        :type row_widget_num: int
        """
        
        

        self._dashboard_name = None
        self._is_favorite = None
        self._row_widget_num = None
        self.discriminator = None

        if dashboard_name is not None:
            self.dashboard_name = dashboard_name
        if is_favorite is not None:
            self.is_favorite = is_favorite
        if row_widget_num is not None:
            self.row_widget_num = row_widget_num

    @property
    def dashboard_name(self):
        """Gets the dashboard_name of this UpdateDashboardRequestBody.

        自定义监控看板名称

        :return: The dashboard_name of this UpdateDashboardRequestBody.
        :rtype: str
        """
        return self._dashboard_name

    @dashboard_name.setter
    def dashboard_name(self, dashboard_name):
        """Sets the dashboard_name of this UpdateDashboardRequestBody.

        自定义监控看板名称

        :param dashboard_name: The dashboard_name of this UpdateDashboardRequestBody.
        :type dashboard_name: str
        """
        self._dashboard_name = dashboard_name

    @property
    def is_favorite(self):
        """Gets the is_favorite of this UpdateDashboardRequestBody.

        监控看板是否标记收藏, true: 收藏, false: 未收藏

        :return: The is_favorite of this UpdateDashboardRequestBody.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """Sets the is_favorite of this UpdateDashboardRequestBody.

        监控看板是否标记收藏, true: 收藏, false: 未收藏

        :param is_favorite: The is_favorite of this UpdateDashboardRequestBody.
        :type is_favorite: bool
        """
        self._is_favorite = is_favorite

    @property
    def row_widget_num(self):
        """Gets the row_widget_num of this UpdateDashboardRequestBody.

        监控视图展示模式，0表示自定义坐标，1代表每行一个

        :return: The row_widget_num of this UpdateDashboardRequestBody.
        :rtype: int
        """
        return self._row_widget_num

    @row_widget_num.setter
    def row_widget_num(self, row_widget_num):
        """Sets the row_widget_num of this UpdateDashboardRequestBody.

        监控视图展示模式，0表示自定义坐标，1代表每行一个

        :param row_widget_num: The row_widget_num of this UpdateDashboardRequestBody.
        :type row_widget_num: int
        """
        self._row_widget_num = row_widget_num

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
        if not isinstance(other, UpdateDashboardRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
