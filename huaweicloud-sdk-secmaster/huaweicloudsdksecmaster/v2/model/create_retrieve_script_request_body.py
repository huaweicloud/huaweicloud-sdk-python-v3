# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRetrieveScriptRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_id': 'str',
        'script_name': 'str',
        'category': 'str',
        'directory': 'str',
        'description': 'str',
        'script': 'str'
    }

    attribute_map = {
        'table_id': 'table_id',
        'script_name': 'script_name',
        'category': 'category',
        'directory': 'directory',
        'description': 'description',
        'script': 'script'
    }

    def __init__(self, table_id=None, script_name=None, category=None, directory=None, description=None, script=None):
        r"""CreateRetrieveScriptRequestBody

        The model defined in huaweicloud sdk

        :param table_id: UUID
        :type table_id: str
        :param script_name: 脚本名称
        :type script_name: str
        :param category: **参数解释**: 脚本分类 - RETRIEVE 检索 - ANALYSIS 分析  **约束限制** 不涉及 **取值范围**: - RETRIEVE - ANALYSIS  **默认值** 不涉及          
        :type category: str
        :param directory: 脚本目录分组名称，长度在1到256个字符之间。
        :type directory: str
        :param description: 脚本的相关描述信息，长度在1到1024个字符之间。
        :type description: str
        :param script: 脚本内容，长度在1到10240个字符之间。
        :type script: str
        """
        
        

        self._table_id = None
        self._script_name = None
        self._category = None
        self._directory = None
        self._description = None
        self._script = None
        self.discriminator = None

        self.table_id = table_id
        self.script_name = script_name
        self.category = category
        if directory is not None:
            self.directory = directory
        if description is not None:
            self.description = description
        self.script = script

    @property
    def table_id(self):
        r"""Gets the table_id of this CreateRetrieveScriptRequestBody.

        UUID

        :return: The table_id of this CreateRetrieveScriptRequestBody.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this CreateRetrieveScriptRequestBody.

        UUID

        :param table_id: The table_id of this CreateRetrieveScriptRequestBody.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def script_name(self):
        r"""Gets the script_name of this CreateRetrieveScriptRequestBody.

        脚本名称

        :return: The script_name of this CreateRetrieveScriptRequestBody.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this CreateRetrieveScriptRequestBody.

        脚本名称

        :param script_name: The script_name of this CreateRetrieveScriptRequestBody.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def category(self):
        r"""Gets the category of this CreateRetrieveScriptRequestBody.

        **参数解释**: 脚本分类 - RETRIEVE 检索 - ANALYSIS 分析  **约束限制** 不涉及 **取值范围**: - RETRIEVE - ANALYSIS  **默认值** 不涉及          

        :return: The category of this CreateRetrieveScriptRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateRetrieveScriptRequestBody.

        **参数解释**: 脚本分类 - RETRIEVE 检索 - ANALYSIS 分析  **约束限制** 不涉及 **取值范围**: - RETRIEVE - ANALYSIS  **默认值** 不涉及          

        :param category: The category of this CreateRetrieveScriptRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def directory(self):
        r"""Gets the directory of this CreateRetrieveScriptRequestBody.

        脚本目录分组名称，长度在1到256个字符之间。

        :return: The directory of this CreateRetrieveScriptRequestBody.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this CreateRetrieveScriptRequestBody.

        脚本目录分组名称，长度在1到256个字符之间。

        :param directory: The directory of this CreateRetrieveScriptRequestBody.
        :type directory: str
        """
        self._directory = directory

    @property
    def description(self):
        r"""Gets the description of this CreateRetrieveScriptRequestBody.

        脚本的相关描述信息，长度在1到1024个字符之间。

        :return: The description of this CreateRetrieveScriptRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateRetrieveScriptRequestBody.

        脚本的相关描述信息，长度在1到1024个字符之间。

        :param description: The description of this CreateRetrieveScriptRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def script(self):
        r"""Gets the script of this CreateRetrieveScriptRequestBody.

        脚本内容，长度在1到10240个字符之间。

        :return: The script of this CreateRetrieveScriptRequestBody.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this CreateRetrieveScriptRequestBody.

        脚本内容，长度在1到10240个字符之间。

        :param script: The script of this CreateRetrieveScriptRequestBody.
        :type script: str
        """
        self._script = script

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
        if not isinstance(other, CreateRetrieveScriptRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
