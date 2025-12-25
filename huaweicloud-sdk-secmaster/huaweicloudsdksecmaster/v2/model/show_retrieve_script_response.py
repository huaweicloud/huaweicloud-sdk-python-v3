# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRetrieveScriptResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_id': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'script_name': 'str',
        'table_id': 'str',
        'category': 'str',
        'directory': 'str',
        'description': 'str',
        'script': 'str',
        'create_by': 'str',
        'create_time': 'int',
        'update_by': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'script_id': 'script_id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'script_name': 'script_name',
        'table_id': 'table_id',
        'category': 'category',
        'directory': 'directory',
        'description': 'description',
        'script': 'script',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'update_by': 'update_by',
        'update_time': 'update_time'
    }

    def __init__(self, script_id=None, project_id=None, workspace_id=None, script_name=None, table_id=None, category=None, directory=None, description=None, script=None, create_by=None, create_time=None, update_by=None, update_time=None):
        r"""ShowRetrieveScriptResponse

        The model defined in huaweicloud sdk

        :param script_id: UUID
        :type script_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param script_name: 脚本名称
        :type script_name: str
        :param table_id: UUID
        :type table_id: str
        :param category: **参数解释**: 脚本分类 - RETRIEVE 检索 - ANALYSIS 分析  **约束限制** 不涉及 **取值范围**: - RETRIEVE - ANALYSIS  **默认值** 不涉及          
        :type category: str
        :param directory: 脚本目录分组名称，长度在1到256个字符之间。
        :type directory: str
        :param description: 脚本的相关描述信息，长度在1到1024个字符之间。
        :type description: str
        :param script: 脚本内容，长度在1到10240个字符之间。
        :type script: str
        :param create_by: Iam用户ID
        :type create_by: str
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param update_by: Iam用户ID
        :type update_by: str
        :param update_time: 毫秒时间戳
        :type update_time: int
        """
        
        super().__init__()

        self._script_id = None
        self._project_id = None
        self._workspace_id = None
        self._script_name = None
        self._table_id = None
        self._category = None
        self._directory = None
        self._description = None
        self._script = None
        self._create_by = None
        self._create_time = None
        self._update_by = None
        self._update_time = None
        self.discriminator = None

        if script_id is not None:
            self.script_id = script_id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if script_name is not None:
            self.script_name = script_name
        if table_id is not None:
            self.table_id = table_id
        if category is not None:
            self.category = category
        if directory is not None:
            self.directory = directory
        if description is not None:
            self.description = description
        if script is not None:
            self.script = script
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time

    @property
    def script_id(self):
        r"""Gets the script_id of this ShowRetrieveScriptResponse.

        UUID

        :return: The script_id of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        r"""Sets the script_id of this ShowRetrieveScriptResponse.

        UUID

        :param script_id: The script_id of this ShowRetrieveScriptResponse.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowRetrieveScriptResponse.

        项目ID

        :return: The project_id of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowRetrieveScriptResponse.

        项目ID

        :param project_id: The project_id of this ShowRetrieveScriptResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowRetrieveScriptResponse.

        工作空间ID

        :return: The workspace_id of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowRetrieveScriptResponse.

        工作空间ID

        :param workspace_id: The workspace_id of this ShowRetrieveScriptResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def script_name(self):
        r"""Gets the script_name of this ShowRetrieveScriptResponse.

        脚本名称

        :return: The script_name of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this ShowRetrieveScriptResponse.

        脚本名称

        :param script_name: The script_name of this ShowRetrieveScriptResponse.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def table_id(self):
        r"""Gets the table_id of this ShowRetrieveScriptResponse.

        UUID

        :return: The table_id of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this ShowRetrieveScriptResponse.

        UUID

        :param table_id: The table_id of this ShowRetrieveScriptResponse.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def category(self):
        r"""Gets the category of this ShowRetrieveScriptResponse.

        **参数解释**: 脚本分类 - RETRIEVE 检索 - ANALYSIS 分析  **约束限制** 不涉及 **取值范围**: - RETRIEVE - ANALYSIS  **默认值** 不涉及          

        :return: The category of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowRetrieveScriptResponse.

        **参数解释**: 脚本分类 - RETRIEVE 检索 - ANALYSIS 分析  **约束限制** 不涉及 **取值范围**: - RETRIEVE - ANALYSIS  **默认值** 不涉及          

        :param category: The category of this ShowRetrieveScriptResponse.
        :type category: str
        """
        self._category = category

    @property
    def directory(self):
        r"""Gets the directory of this ShowRetrieveScriptResponse.

        脚本目录分组名称，长度在1到256个字符之间。

        :return: The directory of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this ShowRetrieveScriptResponse.

        脚本目录分组名称，长度在1到256个字符之间。

        :param directory: The directory of this ShowRetrieveScriptResponse.
        :type directory: str
        """
        self._directory = directory

    @property
    def description(self):
        r"""Gets the description of this ShowRetrieveScriptResponse.

        脚本的相关描述信息，长度在1到1024个字符之间。

        :return: The description of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowRetrieveScriptResponse.

        脚本的相关描述信息，长度在1到1024个字符之间。

        :param description: The description of this ShowRetrieveScriptResponse.
        :type description: str
        """
        self._description = description

    @property
    def script(self):
        r"""Gets the script of this ShowRetrieveScriptResponse.

        脚本内容，长度在1到10240个字符之间。

        :return: The script of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this ShowRetrieveScriptResponse.

        脚本内容，长度在1到10240个字符之间。

        :param script: The script of this ShowRetrieveScriptResponse.
        :type script: str
        """
        self._script = script

    @property
    def create_by(self):
        r"""Gets the create_by of this ShowRetrieveScriptResponse.

        Iam用户ID

        :return: The create_by of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this ShowRetrieveScriptResponse.

        Iam用户ID

        :param create_by: The create_by of this ShowRetrieveScriptResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowRetrieveScriptResponse.

        毫秒时间戳

        :return: The create_time of this ShowRetrieveScriptResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowRetrieveScriptResponse.

        毫秒时间戳

        :param create_time: The create_time of this ShowRetrieveScriptResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        r"""Gets the update_by of this ShowRetrieveScriptResponse.

        Iam用户ID

        :return: The update_by of this ShowRetrieveScriptResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this ShowRetrieveScriptResponse.

        Iam用户ID

        :param update_by: The update_by of this ShowRetrieveScriptResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowRetrieveScriptResponse.

        毫秒时间戳

        :return: The update_time of this ShowRetrieveScriptResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowRetrieveScriptResponse.

        毫秒时间戳

        :param update_time: The update_time of this ShowRetrieveScriptResponse.
        :type update_time: int
        """
        self._update_time = update_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowRetrieveScriptResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowRetrieveScriptResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
