# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDashBoardResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charts': 'list[str]',
        'filters': 'list[str]',
        'group_name': 'str',
        'id': 'str',
        'last_update_time': 'int',
        'project_id': 'str',
        'title': 'str',
        'use_system_template': 'bool'
    }

    attribute_map = {
        'charts': 'charts',
        'filters': 'filters',
        'group_name': 'group_name',
        'id': 'id',
        'last_update_time': 'last_update_time',
        'project_id': 'project_id',
        'title': 'title',
        'use_system_template': 'useSystemTemplate'
    }

    def __init__(self, charts=None, filters=None, group_name=None, id=None, last_update_time=None, project_id=None, title=None, use_system_template=None):
        """CreateDashBoardResponse

        The model defined in huaweicloud sdk

        :param charts: 仪表盘图表
        :type charts: list[str]
        :param filters: 过滤条件
        :type filters: list[str]
        :param group_name: 日志组名称
        :type group_name: str
        :param id: 仪表盘id
        :type id: str
        :param last_update_time: 最近修改时间
        :type last_update_time: int
        :param project_id: 项目id
        :type project_id: str
        :param title: 仪表盘名称
        :type title: str
        :param use_system_template: 是否使用模板
        :type use_system_template: bool
        """
        
        super(CreateDashBoardResponse, self).__init__()

        self._charts = None
        self._filters = None
        self._group_name = None
        self._id = None
        self._last_update_time = None
        self._project_id = None
        self._title = None
        self._use_system_template = None
        self.discriminator = None

        if charts is not None:
            self.charts = charts
        if filters is not None:
            self.filters = filters
        if group_name is not None:
            self.group_name = group_name
        if id is not None:
            self.id = id
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if project_id is not None:
            self.project_id = project_id
        if title is not None:
            self.title = title
        if use_system_template is not None:
            self.use_system_template = use_system_template

    @property
    def charts(self):
        """Gets the charts of this CreateDashBoardResponse.

        仪表盘图表

        :return: The charts of this CreateDashBoardResponse.
        :rtype: list[str]
        """
        return self._charts

    @charts.setter
    def charts(self, charts):
        """Sets the charts of this CreateDashBoardResponse.

        仪表盘图表

        :param charts: The charts of this CreateDashBoardResponse.
        :type charts: list[str]
        """
        self._charts = charts

    @property
    def filters(self):
        """Gets the filters of this CreateDashBoardResponse.

        过滤条件

        :return: The filters of this CreateDashBoardResponse.
        :rtype: list[str]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this CreateDashBoardResponse.

        过滤条件

        :param filters: The filters of this CreateDashBoardResponse.
        :type filters: list[str]
        """
        self._filters = filters

    @property
    def group_name(self):
        """Gets the group_name of this CreateDashBoardResponse.

        日志组名称

        :return: The group_name of this CreateDashBoardResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this CreateDashBoardResponse.

        日志组名称

        :param group_name: The group_name of this CreateDashBoardResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def id(self):
        """Gets the id of this CreateDashBoardResponse.

        仪表盘id

        :return: The id of this CreateDashBoardResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateDashBoardResponse.

        仪表盘id

        :param id: The id of this CreateDashBoardResponse.
        :type id: str
        """
        self._id = id

    @property
    def last_update_time(self):
        """Gets the last_update_time of this CreateDashBoardResponse.

        最近修改时间

        :return: The last_update_time of this CreateDashBoardResponse.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this CreateDashBoardResponse.

        最近修改时间

        :param last_update_time: The last_update_time of this CreateDashBoardResponse.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def project_id(self):
        """Gets the project_id of this CreateDashBoardResponse.

        项目id

        :return: The project_id of this CreateDashBoardResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateDashBoardResponse.

        项目id

        :param project_id: The project_id of this CreateDashBoardResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def title(self):
        """Gets the title of this CreateDashBoardResponse.

        仪表盘名称

        :return: The title of this CreateDashBoardResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateDashBoardResponse.

        仪表盘名称

        :param title: The title of this CreateDashBoardResponse.
        :type title: str
        """
        self._title = title

    @property
    def use_system_template(self):
        """Gets the use_system_template of this CreateDashBoardResponse.

        是否使用模板

        :return: The use_system_template of this CreateDashBoardResponse.
        :rtype: bool
        """
        return self._use_system_template

    @use_system_template.setter
    def use_system_template(self, use_system_template):
        """Sets the use_system_template of this CreateDashBoardResponse.

        是否使用模板

        :param use_system_template: The use_system_template of this CreateDashBoardResponse.
        :type use_system_template: bool
        """
        self._use_system_template = use_system_template

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
        if not isinstance(other, CreateDashBoardResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
