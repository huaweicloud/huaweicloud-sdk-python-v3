# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DashBoardsFolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created': 'int',
        'updated': 'int',
        'created_by': 'str',
        'dashboard_ids': 'list[str]',
        'display': 'bool',
        'enterprise_project_id': 'str',
        'folder_id': 'str',
        'folder_title': 'str',
        'folder_title_en': 'str',
        'is_template': 'bool'
    }

    attribute_map = {
        'created': 'created',
        'updated': 'updated',
        'created_by': 'created_by',
        'dashboard_ids': 'dashboard_ids',
        'display': 'display',
        'enterprise_project_id': 'enterprise_project_id',
        'folder_id': 'folder_id',
        'folder_title': 'folder_title',
        'folder_title_en': 'folder_title_en',
        'is_template': 'is_template'
    }

    def __init__(self, created=None, updated=None, created_by=None, dashboard_ids=None, display=None, enterprise_project_id=None, folder_id=None, folder_title=None, folder_title_en=None, is_template=None):
        r"""DashBoardsFolder

        The model defined in huaweicloud sdk

        :param created: 仪表盘分组创建时间。
        :type created: int
        :param updated: 仪表盘分组更新时间。
        :type updated: int
        :param created_by: 仪表盘分组创建账号。
        :type created_by: str
        :param dashboard_ids: 仪表盘分组下仪表盘id列表。
        :type dashboard_ids: list[str]
        :param display: 是否展示仪表盘分组。
        :type display: bool
        :param enterprise_project_id: 企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。
        :type enterprise_project_id: str
        :param folder_id: 仪表盘分组id。
        :type folder_id: str
        :param folder_title: 仪表盘分组名称。
        :type folder_title: str
        :param folder_title_en: 仪表盘分组英文名称。
        :type folder_title_en: str
        :param is_template: 仪表盘分组是否为默认仪表盘分组。
        :type is_template: bool
        """
        
        

        self._created = None
        self._updated = None
        self._created_by = None
        self._dashboard_ids = None
        self._display = None
        self._enterprise_project_id = None
        self._folder_id = None
        self._folder_title = None
        self._folder_title_en = None
        self._is_template = None
        self.discriminator = None

        self.created = created
        self.updated = updated
        self.created_by = created_by
        self.dashboard_ids = dashboard_ids
        self.display = display
        self.enterprise_project_id = enterprise_project_id
        self.folder_id = folder_id
        self.folder_title = folder_title
        if folder_title_en is not None:
            self.folder_title_en = folder_title_en
        self.is_template = is_template

    @property
    def created(self):
        r"""Gets the created of this DashBoardsFolder.

        仪表盘分组创建时间。

        :return: The created of this DashBoardsFolder.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this DashBoardsFolder.

        仪表盘分组创建时间。

        :param created: The created of this DashBoardsFolder.
        :type created: int
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this DashBoardsFolder.

        仪表盘分组更新时间。

        :return: The updated of this DashBoardsFolder.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this DashBoardsFolder.

        仪表盘分组更新时间。

        :param updated: The updated of this DashBoardsFolder.
        :type updated: int
        """
        self._updated = updated

    @property
    def created_by(self):
        r"""Gets the created_by of this DashBoardsFolder.

        仪表盘分组创建账号。

        :return: The created_by of this DashBoardsFolder.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this DashBoardsFolder.

        仪表盘分组创建账号。

        :param created_by: The created_by of this DashBoardsFolder.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def dashboard_ids(self):
        r"""Gets the dashboard_ids of this DashBoardsFolder.

        仪表盘分组下仪表盘id列表。

        :return: The dashboard_ids of this DashBoardsFolder.
        :rtype: list[str]
        """
        return self._dashboard_ids

    @dashboard_ids.setter
    def dashboard_ids(self, dashboard_ids):
        r"""Sets the dashboard_ids of this DashBoardsFolder.

        仪表盘分组下仪表盘id列表。

        :param dashboard_ids: The dashboard_ids of this DashBoardsFolder.
        :type dashboard_ids: list[str]
        """
        self._dashboard_ids = dashboard_ids

    @property
    def display(self):
        r"""Gets the display of this DashBoardsFolder.

        是否展示仪表盘分组。

        :return: The display of this DashBoardsFolder.
        :rtype: bool
        """
        return self._display

    @display.setter
    def display(self, display):
        r"""Sets the display of this DashBoardsFolder.

        是否展示仪表盘分组。

        :param display: The display of this DashBoardsFolder.
        :type display: bool
        """
        self._display = display

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this DashBoardsFolder.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。

        :return: The enterprise_project_id of this DashBoardsFolder.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this DashBoardsFolder.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。

        :param enterprise_project_id: The enterprise_project_id of this DashBoardsFolder.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def folder_id(self):
        r"""Gets the folder_id of this DashBoardsFolder.

        仪表盘分组id。

        :return: The folder_id of this DashBoardsFolder.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        r"""Sets the folder_id of this DashBoardsFolder.

        仪表盘分组id。

        :param folder_id: The folder_id of this DashBoardsFolder.
        :type folder_id: str
        """
        self._folder_id = folder_id

    @property
    def folder_title(self):
        r"""Gets the folder_title of this DashBoardsFolder.

        仪表盘分组名称。

        :return: The folder_title of this DashBoardsFolder.
        :rtype: str
        """
        return self._folder_title

    @folder_title.setter
    def folder_title(self, folder_title):
        r"""Sets the folder_title of this DashBoardsFolder.

        仪表盘分组名称。

        :param folder_title: The folder_title of this DashBoardsFolder.
        :type folder_title: str
        """
        self._folder_title = folder_title

    @property
    def folder_title_en(self):
        r"""Gets the folder_title_en of this DashBoardsFolder.

        仪表盘分组英文名称。

        :return: The folder_title_en of this DashBoardsFolder.
        :rtype: str
        """
        return self._folder_title_en

    @folder_title_en.setter
    def folder_title_en(self, folder_title_en):
        r"""Sets the folder_title_en of this DashBoardsFolder.

        仪表盘分组英文名称。

        :param folder_title_en: The folder_title_en of this DashBoardsFolder.
        :type folder_title_en: str
        """
        self._folder_title_en = folder_title_en

    @property
    def is_template(self):
        r"""Gets the is_template of this DashBoardsFolder.

        仪表盘分组是否为默认仪表盘分组。

        :return: The is_template of this DashBoardsFolder.
        :rtype: bool
        """
        return self._is_template

    @is_template.setter
    def is_template(self, is_template):
        r"""Sets the is_template of this DashBoardsFolder.

        仪表盘分组是否为默认仪表盘分组。

        :param is_template: The is_template of this DashBoardsFolder.
        :type is_template: bool
        """
        self._is_template = is_template

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
        if not isinstance(other, DashBoardsFolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
