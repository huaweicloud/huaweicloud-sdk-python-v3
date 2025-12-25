# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAnalysisScriptRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_name': 'str',
        'category': 'str',
        'directory': 'str',
        'description': 'str',
        'script_type': 'str',
        'retrieve_table_id': 'str',
        'retrieve_table_name': 'str',
        'script': 'str',
        'owner': 'str',
        'script_params': 'list[AnalysisScriptParam]'
    }

    attribute_map = {
        'script_name': 'script_name',
        'category': 'category',
        'directory': 'directory',
        'description': 'description',
        'script_type': 'script_type',
        'retrieve_table_id': 'retrieve_table_id',
        'retrieve_table_name': 'retrieve_table_name',
        'script': 'script',
        'owner': 'owner',
        'script_params': 'script_params'
    }

    def __init__(self, script_name=None, category=None, directory=None, description=None, script_type=None, retrieve_table_id=None, retrieve_table_name=None, script=None, owner=None, script_params=None):
        r"""CreateAnalysisScriptRequestBody

        The model defined in huaweicloud sdk

        :param script_name: 脚本名称
        :type script_name: str
        :param category: **参数解释**: 脚本分类 - RETRIEVE 检索 - ANALYSIS 分析  **约束限制** 不涉及 **取值范围**: - RETRIEVE - ANALYSIS  **默认值** 不涉及          
        :type category: str
        :param directory: 脚本目录分组名称，长度在1到256个字符之间。
        :type directory: str
        :param description: 脚本的相关描述信息，长度在1到1024个字符之间。
        :type description: str
        :param script_type: **参数解释**: 分析脚本类型 - SEC_MASTER_SQL 安全云脑SQL - RETRIEVE_SQL 检索SQL  **约束限制** 不涉及 **取值范围**: - SEC_MASTER_SQL - RETRIEVE_SQL  **默认值** 不涉及      
        :type script_type: str
        :param retrieve_table_id: UUID
        :type retrieve_table_id: str
        :param retrieve_table_name: 表名
        :type retrieve_table_name: str
        :param script: 脚本内容，长度在1到10240个字符之间。
        :type script: str
        :param owner: Iam用户ID
        :type owner: str
        :param script_params: 分析脚本参数列表
        :type script_params: list[:class:`huaweicloudsdksecmaster.v2.AnalysisScriptParam`]
        """
        
        

        self._script_name = None
        self._category = None
        self._directory = None
        self._description = None
        self._script_type = None
        self._retrieve_table_id = None
        self._retrieve_table_name = None
        self._script = None
        self._owner = None
        self._script_params = None
        self.discriminator = None

        self.script_name = script_name
        self.category = category
        if directory is not None:
            self.directory = directory
        if description is not None:
            self.description = description
        self.script_type = script_type
        if retrieve_table_id is not None:
            self.retrieve_table_id = retrieve_table_id
        if retrieve_table_name is not None:
            self.retrieve_table_name = retrieve_table_name
        self.script = script
        if owner is not None:
            self.owner = owner
        self.script_params = script_params

    @property
    def script_name(self):
        r"""Gets the script_name of this CreateAnalysisScriptRequestBody.

        脚本名称

        :return: The script_name of this CreateAnalysisScriptRequestBody.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this CreateAnalysisScriptRequestBody.

        脚本名称

        :param script_name: The script_name of this CreateAnalysisScriptRequestBody.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def category(self):
        r"""Gets the category of this CreateAnalysisScriptRequestBody.

        **参数解释**: 脚本分类 - RETRIEVE 检索 - ANALYSIS 分析  **约束限制** 不涉及 **取值范围**: - RETRIEVE - ANALYSIS  **默认值** 不涉及          

        :return: The category of this CreateAnalysisScriptRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateAnalysisScriptRequestBody.

        **参数解释**: 脚本分类 - RETRIEVE 检索 - ANALYSIS 分析  **约束限制** 不涉及 **取值范围**: - RETRIEVE - ANALYSIS  **默认值** 不涉及          

        :param category: The category of this CreateAnalysisScriptRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def directory(self):
        r"""Gets the directory of this CreateAnalysisScriptRequestBody.

        脚本目录分组名称，长度在1到256个字符之间。

        :return: The directory of this CreateAnalysisScriptRequestBody.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this CreateAnalysisScriptRequestBody.

        脚本目录分组名称，长度在1到256个字符之间。

        :param directory: The directory of this CreateAnalysisScriptRequestBody.
        :type directory: str
        """
        self._directory = directory

    @property
    def description(self):
        r"""Gets the description of this CreateAnalysisScriptRequestBody.

        脚本的相关描述信息，长度在1到1024个字符之间。

        :return: The description of this CreateAnalysisScriptRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAnalysisScriptRequestBody.

        脚本的相关描述信息，长度在1到1024个字符之间。

        :param description: The description of this CreateAnalysisScriptRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def script_type(self):
        r"""Gets the script_type of this CreateAnalysisScriptRequestBody.

        **参数解释**: 分析脚本类型 - SEC_MASTER_SQL 安全云脑SQL - RETRIEVE_SQL 检索SQL  **约束限制** 不涉及 **取值范围**: - SEC_MASTER_SQL - RETRIEVE_SQL  **默认值** 不涉及      

        :return: The script_type of this CreateAnalysisScriptRequestBody.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        r"""Sets the script_type of this CreateAnalysisScriptRequestBody.

        **参数解释**: 分析脚本类型 - SEC_MASTER_SQL 安全云脑SQL - RETRIEVE_SQL 检索SQL  **约束限制** 不涉及 **取值范围**: - SEC_MASTER_SQL - RETRIEVE_SQL  **默认值** 不涉及      

        :param script_type: The script_type of this CreateAnalysisScriptRequestBody.
        :type script_type: str
        """
        self._script_type = script_type

    @property
    def retrieve_table_id(self):
        r"""Gets the retrieve_table_id of this CreateAnalysisScriptRequestBody.

        UUID

        :return: The retrieve_table_id of this CreateAnalysisScriptRequestBody.
        :rtype: str
        """
        return self._retrieve_table_id

    @retrieve_table_id.setter
    def retrieve_table_id(self, retrieve_table_id):
        r"""Sets the retrieve_table_id of this CreateAnalysisScriptRequestBody.

        UUID

        :param retrieve_table_id: The retrieve_table_id of this CreateAnalysisScriptRequestBody.
        :type retrieve_table_id: str
        """
        self._retrieve_table_id = retrieve_table_id

    @property
    def retrieve_table_name(self):
        r"""Gets the retrieve_table_name of this CreateAnalysisScriptRequestBody.

        表名

        :return: The retrieve_table_name of this CreateAnalysisScriptRequestBody.
        :rtype: str
        """
        return self._retrieve_table_name

    @retrieve_table_name.setter
    def retrieve_table_name(self, retrieve_table_name):
        r"""Sets the retrieve_table_name of this CreateAnalysisScriptRequestBody.

        表名

        :param retrieve_table_name: The retrieve_table_name of this CreateAnalysisScriptRequestBody.
        :type retrieve_table_name: str
        """
        self._retrieve_table_name = retrieve_table_name

    @property
    def script(self):
        r"""Gets the script of this CreateAnalysisScriptRequestBody.

        脚本内容，长度在1到10240个字符之间。

        :return: The script of this CreateAnalysisScriptRequestBody.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this CreateAnalysisScriptRequestBody.

        脚本内容，长度在1到10240个字符之间。

        :param script: The script of this CreateAnalysisScriptRequestBody.
        :type script: str
        """
        self._script = script

    @property
    def owner(self):
        r"""Gets the owner of this CreateAnalysisScriptRequestBody.

        Iam用户ID

        :return: The owner of this CreateAnalysisScriptRequestBody.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this CreateAnalysisScriptRequestBody.

        Iam用户ID

        :param owner: The owner of this CreateAnalysisScriptRequestBody.
        :type owner: str
        """
        self._owner = owner

    @property
    def script_params(self):
        r"""Gets the script_params of this CreateAnalysisScriptRequestBody.

        分析脚本参数列表

        :return: The script_params of this CreateAnalysisScriptRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AnalysisScriptParam`]
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        r"""Sets the script_params of this CreateAnalysisScriptRequestBody.

        分析脚本参数列表

        :param script_params: The script_params of this CreateAnalysisScriptRequestBody.
        :type script_params: list[:class:`huaweicloudsdksecmaster.v2.AnalysisScriptParam`]
        """
        self._script_params = script_params

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
        if not isinstance(other, CreateAnalysisScriptRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
