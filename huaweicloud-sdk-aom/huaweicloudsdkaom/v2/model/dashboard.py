# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Dashboard:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'dashboard_type': 'str',
        'dashboard_title': 'str',
        'dashboard_title_en': 'str',
        'dashboard_id': 'str',
        'version': 'str',
        'enterprise_project_id': 'str',
        'folder_name': 'str',
        'folder_id': 'str',
        'sync_data': 'str',
        'is_create_action': 'bool',
        'dashboard_tags': 'list[dict(str, str)]',
        'is_favorite': 'bool',
        'created': 'int',
        'updated': 'int',
        'created_by': 'str',
        'updated_by': 'str',
        'charts': 'object',
        'templating': 'object',
        'display': 'bool',
        'query_count': 'int',
        'time_range': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'dashboard_type': 'dashboard_type',
        'dashboard_title': 'dashboard_title',
        'dashboard_title_en': 'dashboard_title_en',
        'dashboard_id': 'dashboard_id',
        'version': 'version',
        'enterprise_project_id': 'enterprise_project_id',
        'folder_name': 'folder_name',
        'folder_id': 'folder_id',
        'sync_data': 'sync_data',
        'is_create_action': 'is_create_action',
        'dashboard_tags': 'dashboard_tags',
        'is_favorite': 'is_favorite',
        'created': 'created',
        'updated': 'updated',
        'created_by': 'created_by',
        'updated_by': 'updated_by',
        'charts': 'charts',
        'templating': 'templating',
        'display': 'display',
        'query_count': 'query_count',
        'time_range': 'time_range'
    }

    def __init__(self, project_id=None, dashboard_type=None, dashboard_title=None, dashboard_title_en=None, dashboard_id=None, version=None, enterprise_project_id=None, folder_name=None, folder_id=None, sync_data=None, is_create_action=None, dashboard_tags=None, is_favorite=None, created=None, updated=None, created_by=None, updated_by=None, charts=None, templating=None, display=None, query_count=None, time_range=None):
        r"""Dashboard

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，可以从控制台获取，也可以从调用API处获取。获取方式请参见：[获取项目ID](aom_04_0024.xml)。
        :type project_id: str
        :param dashboard_type: 仪表盘类型。
        :type dashboard_type: str
        :param dashboard_title: 仪表盘名称。
        :type dashboard_title: str
        :param dashboard_title_en: 仪表盘英文名称。
        :type dashboard_title_en: str
        :param dashboard_id: 仪表盘id。
        :type dashboard_id: str
        :param version: 仪表盘版本。
        :type version: str
        :param enterprise_project_id: 仪表盘企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。
        :type enterprise_project_id: str
        :param folder_name: 仪表盘分组名称。
        :type folder_name: str
        :param folder_id: 仪表盘分组id。
        :type folder_id: str
        :param sync_data: 待同步的仪表盘数。
        :type sync_data: str
        :param is_create_action: 是否创建 - false：更新 - true：创建
        :type is_create_action: bool
        :param dashboard_tags: 仪表盘标签列表。
        :type dashboard_tags: list[dict(str, str)]
        :param is_favorite: 是否收藏 - true：收藏 - false：不收藏
        :type is_favorite: bool
        :param created: 仪表盘创建时间。
        :type created: int
        :param updated: 仪表盘更新时间。
        :type updated: int
        :param created_by: 创建仪表盘的账号名称。
        :type created_by: str
        :param updated_by: 更新仪表盘的账号名称。
        :type updated_by: str
        :param charts: 仪表盘图表详情。
        :type charts: object
        :param templating: 仪表盘变量列表。
        :type templating: object
        :param display: 是否展示。
        :type display: bool
        :param query_count: 查询总次数。
        :type query_count: int
        :param time_range: 默认查询时间范围。
        :type time_range: str
        """
        
        

        self._project_id = None
        self._dashboard_type = None
        self._dashboard_title = None
        self._dashboard_title_en = None
        self._dashboard_id = None
        self._version = None
        self._enterprise_project_id = None
        self._folder_name = None
        self._folder_id = None
        self._sync_data = None
        self._is_create_action = None
        self._dashboard_tags = None
        self._is_favorite = None
        self._created = None
        self._updated = None
        self._created_by = None
        self._updated_by = None
        self._charts = None
        self._templating = None
        self._display = None
        self._query_count = None
        self._time_range = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if dashboard_type is not None:
            self.dashboard_type = dashboard_type
        if dashboard_title is not None:
            self.dashboard_title = dashboard_title
        if dashboard_title_en is not None:
            self.dashboard_title_en = dashboard_title_en
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if version is not None:
            self.version = version
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if folder_name is not None:
            self.folder_name = folder_name
        if folder_id is not None:
            self.folder_id = folder_id
        if sync_data is not None:
            self.sync_data = sync_data
        if is_create_action is not None:
            self.is_create_action = is_create_action
        if dashboard_tags is not None:
            self.dashboard_tags = dashboard_tags
        if is_favorite is not None:
            self.is_favorite = is_favorite
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if charts is not None:
            self.charts = charts
        if templating is not None:
            self.templating = templating
        if display is not None:
            self.display = display
        if query_count is not None:
            self.query_count = query_count
        if time_range is not None:
            self.time_range = time_range

    @property
    def project_id(self):
        r"""Gets the project_id of this Dashboard.

        项目ID，可以从控制台获取，也可以从调用API处获取。获取方式请参见：[获取项目ID](aom_04_0024.xml)。

        :return: The project_id of this Dashboard.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Dashboard.

        项目ID，可以从控制台获取，也可以从调用API处获取。获取方式请参见：[获取项目ID](aom_04_0024.xml)。

        :param project_id: The project_id of this Dashboard.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def dashboard_type(self):
        r"""Gets the dashboard_type of this Dashboard.

        仪表盘类型。

        :return: The dashboard_type of this Dashboard.
        :rtype: str
        """
        return self._dashboard_type

    @dashboard_type.setter
    def dashboard_type(self, dashboard_type):
        r"""Sets the dashboard_type of this Dashboard.

        仪表盘类型。

        :param dashboard_type: The dashboard_type of this Dashboard.
        :type dashboard_type: str
        """
        self._dashboard_type = dashboard_type

    @property
    def dashboard_title(self):
        r"""Gets the dashboard_title of this Dashboard.

        仪表盘名称。

        :return: The dashboard_title of this Dashboard.
        :rtype: str
        """
        return self._dashboard_title

    @dashboard_title.setter
    def dashboard_title(self, dashboard_title):
        r"""Sets the dashboard_title of this Dashboard.

        仪表盘名称。

        :param dashboard_title: The dashboard_title of this Dashboard.
        :type dashboard_title: str
        """
        self._dashboard_title = dashboard_title

    @property
    def dashboard_title_en(self):
        r"""Gets the dashboard_title_en of this Dashboard.

        仪表盘英文名称。

        :return: The dashboard_title_en of this Dashboard.
        :rtype: str
        """
        return self._dashboard_title_en

    @dashboard_title_en.setter
    def dashboard_title_en(self, dashboard_title_en):
        r"""Sets the dashboard_title_en of this Dashboard.

        仪表盘英文名称。

        :param dashboard_title_en: The dashboard_title_en of this Dashboard.
        :type dashboard_title_en: str
        """
        self._dashboard_title_en = dashboard_title_en

    @property
    def dashboard_id(self):
        r"""Gets the dashboard_id of this Dashboard.

        仪表盘id。

        :return: The dashboard_id of this Dashboard.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        r"""Sets the dashboard_id of this Dashboard.

        仪表盘id。

        :param dashboard_id: The dashboard_id of this Dashboard.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

    @property
    def version(self):
        r"""Gets the version of this Dashboard.

        仪表盘版本。

        :return: The version of this Dashboard.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Dashboard.

        仪表盘版本。

        :param version: The version of this Dashboard.
        :type version: str
        """
        self._version = version

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Dashboard.

        仪表盘企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。

        :return: The enterprise_project_id of this Dashboard.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Dashboard.

        仪表盘企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。

        :param enterprise_project_id: The enterprise_project_id of this Dashboard.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def folder_name(self):
        r"""Gets the folder_name of this Dashboard.

        仪表盘分组名称。

        :return: The folder_name of this Dashboard.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        r"""Sets the folder_name of this Dashboard.

        仪表盘分组名称。

        :param folder_name: The folder_name of this Dashboard.
        :type folder_name: str
        """
        self._folder_name = folder_name

    @property
    def folder_id(self):
        r"""Gets the folder_id of this Dashboard.

        仪表盘分组id。

        :return: The folder_id of this Dashboard.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        r"""Sets the folder_id of this Dashboard.

        仪表盘分组id。

        :param folder_id: The folder_id of this Dashboard.
        :type folder_id: str
        """
        self._folder_id = folder_id

    @property
    def sync_data(self):
        r"""Gets the sync_data of this Dashboard.

        待同步的仪表盘数。

        :return: The sync_data of this Dashboard.
        :rtype: str
        """
        return self._sync_data

    @sync_data.setter
    def sync_data(self, sync_data):
        r"""Sets the sync_data of this Dashboard.

        待同步的仪表盘数。

        :param sync_data: The sync_data of this Dashboard.
        :type sync_data: str
        """
        self._sync_data = sync_data

    @property
    def is_create_action(self):
        r"""Gets the is_create_action of this Dashboard.

        是否创建 - false：更新 - true：创建

        :return: The is_create_action of this Dashboard.
        :rtype: bool
        """
        return self._is_create_action

    @is_create_action.setter
    def is_create_action(self, is_create_action):
        r"""Sets the is_create_action of this Dashboard.

        是否创建 - false：更新 - true：创建

        :param is_create_action: The is_create_action of this Dashboard.
        :type is_create_action: bool
        """
        self._is_create_action = is_create_action

    @property
    def dashboard_tags(self):
        r"""Gets the dashboard_tags of this Dashboard.

        仪表盘标签列表。

        :return: The dashboard_tags of this Dashboard.
        :rtype: list[dict(str, str)]
        """
        return self._dashboard_tags

    @dashboard_tags.setter
    def dashboard_tags(self, dashboard_tags):
        r"""Sets the dashboard_tags of this Dashboard.

        仪表盘标签列表。

        :param dashboard_tags: The dashboard_tags of this Dashboard.
        :type dashboard_tags: list[dict(str, str)]
        """
        self._dashboard_tags = dashboard_tags

    @property
    def is_favorite(self):
        r"""Gets the is_favorite of this Dashboard.

        是否收藏 - true：收藏 - false：不收藏

        :return: The is_favorite of this Dashboard.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        r"""Sets the is_favorite of this Dashboard.

        是否收藏 - true：收藏 - false：不收藏

        :param is_favorite: The is_favorite of this Dashboard.
        :type is_favorite: bool
        """
        self._is_favorite = is_favorite

    @property
    def created(self):
        r"""Gets the created of this Dashboard.

        仪表盘创建时间。

        :return: The created of this Dashboard.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this Dashboard.

        仪表盘创建时间。

        :param created: The created of this Dashboard.
        :type created: int
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this Dashboard.

        仪表盘更新时间。

        :return: The updated of this Dashboard.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this Dashboard.

        仪表盘更新时间。

        :param updated: The updated of this Dashboard.
        :type updated: int
        """
        self._updated = updated

    @property
    def created_by(self):
        r"""Gets the created_by of this Dashboard.

        创建仪表盘的账号名称。

        :return: The created_by of this Dashboard.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this Dashboard.

        创建仪表盘的账号名称。

        :param created_by: The created_by of this Dashboard.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def updated_by(self):
        r"""Gets the updated_by of this Dashboard.

        更新仪表盘的账号名称。

        :return: The updated_by of this Dashboard.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this Dashboard.

        更新仪表盘的账号名称。

        :param updated_by: The updated_by of this Dashboard.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def charts(self):
        r"""Gets the charts of this Dashboard.

        仪表盘图表详情。

        :return: The charts of this Dashboard.
        :rtype: object
        """
        return self._charts

    @charts.setter
    def charts(self, charts):
        r"""Sets the charts of this Dashboard.

        仪表盘图表详情。

        :param charts: The charts of this Dashboard.
        :type charts: object
        """
        self._charts = charts

    @property
    def templating(self):
        r"""Gets the templating of this Dashboard.

        仪表盘变量列表。

        :return: The templating of this Dashboard.
        :rtype: object
        """
        return self._templating

    @templating.setter
    def templating(self, templating):
        r"""Sets the templating of this Dashboard.

        仪表盘变量列表。

        :param templating: The templating of this Dashboard.
        :type templating: object
        """
        self._templating = templating

    @property
    def display(self):
        r"""Gets the display of this Dashboard.

        是否展示。

        :return: The display of this Dashboard.
        :rtype: bool
        """
        return self._display

    @display.setter
    def display(self, display):
        r"""Sets the display of this Dashboard.

        是否展示。

        :param display: The display of this Dashboard.
        :type display: bool
        """
        self._display = display

    @property
    def query_count(self):
        r"""Gets the query_count of this Dashboard.

        查询总次数。

        :return: The query_count of this Dashboard.
        :rtype: int
        """
        return self._query_count

    @query_count.setter
    def query_count(self, query_count):
        r"""Sets the query_count of this Dashboard.

        查询总次数。

        :param query_count: The query_count of this Dashboard.
        :type query_count: int
        """
        self._query_count = query_count

    @property
    def time_range(self):
        r"""Gets the time_range of this Dashboard.

        默认查询时间范围。

        :return: The time_range of this Dashboard.
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        r"""Sets the time_range of this Dashboard.

        默认查询时间范围。

        :param time_range: The time_range of this Dashboard.
        :type time_range: str
        """
        self._time_range = time_range

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Dashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
