# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDashboardRequestBody:

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
        'enterprise_id': 'str',
        'dashboard_id': 'str',
        'row_widget_num': 'int'
    }

    attribute_map = {
        'dashboard_name': 'dashboard_name',
        'enterprise_id': 'enterprise_id',
        'dashboard_id': 'dashboard_id',
        'row_widget_num': 'row_widget_num'
    }

    def __init__(self, dashboard_name=None, enterprise_id=None, dashboard_id=None, row_widget_num=None):
        """CreateDashboardRequestBody

        The model defined in huaweicloud sdk

        :param dashboard_name: 自定义监控看板名称
        :type dashboard_name: str
        :param enterprise_id: 企业项目Id
        :type enterprise_id: str
        :param dashboard_id: 监控看板id
        :type dashboard_id: str
        :param row_widget_num: 监控视图展示模式，0表示自定义坐标，1代表每行一个
        :type row_widget_num: int
        """
        
        

        self._dashboard_name = None
        self._enterprise_id = None
        self._dashboard_id = None
        self._row_widget_num = None
        self.discriminator = None

        if dashboard_name is not None:
            self.dashboard_name = dashboard_name
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if row_widget_num is not None:
            self.row_widget_num = row_widget_num

    @property
    def dashboard_name(self):
        """Gets the dashboard_name of this CreateDashboardRequestBody.

        自定义监控看板名称

        :return: The dashboard_name of this CreateDashboardRequestBody.
        :rtype: str
        """
        return self._dashboard_name

    @dashboard_name.setter
    def dashboard_name(self, dashboard_name):
        """Sets the dashboard_name of this CreateDashboardRequestBody.

        自定义监控看板名称

        :param dashboard_name: The dashboard_name of this CreateDashboardRequestBody.
        :type dashboard_name: str
        """
        self._dashboard_name = dashboard_name

    @property
    def enterprise_id(self):
        """Gets the enterprise_id of this CreateDashboardRequestBody.

        企业项目Id

        :return: The enterprise_id of this CreateDashboardRequestBody.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        """Sets the enterprise_id of this CreateDashboardRequestBody.

        企业项目Id

        :param enterprise_id: The enterprise_id of this CreateDashboardRequestBody.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this CreateDashboardRequestBody.

        监控看板id

        :return: The dashboard_id of this CreateDashboardRequestBody.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this CreateDashboardRequestBody.

        监控看板id

        :param dashboard_id: The dashboard_id of this CreateDashboardRequestBody.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

    @property
    def row_widget_num(self):
        """Gets the row_widget_num of this CreateDashboardRequestBody.

        监控视图展示模式，0表示自定义坐标，1代表每行一个

        :return: The row_widget_num of this CreateDashboardRequestBody.
        :rtype: int
        """
        return self._row_widget_num

    @row_widget_num.setter
    def row_widget_num(self, row_widget_num):
        """Sets the row_widget_num of this CreateDashboardRequestBody.

        监控视图展示模式，0表示自定义坐标，1代表每行一个

        :param row_widget_num: The row_widget_num of this CreateDashboardRequestBody.
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
        if not isinstance(other, CreateDashboardRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
