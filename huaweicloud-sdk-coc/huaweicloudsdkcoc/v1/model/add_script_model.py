# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddScriptModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'properties': 'ScriptPropertiesModel',
        'description': 'str',
        'type': 'str',
        'content': 'str',
        'enterprise_project_id': 'str',
        'script_params': 'list[ScriptParamDefine]'
    }

    attribute_map = {
        'name': 'name',
        'properties': 'properties',
        'description': 'description',
        'type': 'type',
        'content': 'content',
        'enterprise_project_id': 'enterprise_project_id',
        'script_params': 'script_params'
    }

    def __init__(self, name=None, properties=None, description=None, type=None, content=None, enterprise_project_id=None, script_params=None):
        r"""AddScriptModel

        The model defined in huaweicloud sdk

        :param name: 脚本名称：只能包含中文、英文、数字、下划线
        :type name: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        :param description: 脚本描述
        :type description: str
        :param type: 脚本类型: 对于脚本后缀： SHELL:.sh PYTHON:.py BAT:.bat
        :type type: str
        :param content: 脚本内容
        :type content: str
        :param enterprise_project_id: 企业项目ID，默认为：0
        :type enterprise_project_id: str
        :param script_params: 脚本入参
        :type script_params: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        """
        
        

        self._name = None
        self._properties = None
        self._description = None
        self._type = None
        self._content = None
        self._enterprise_project_id = None
        self._script_params = None
        self.discriminator = None

        self.name = name
        self.properties = properties
        self.description = description
        self.type = type
        self.content = content
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if script_params is not None:
            self.script_params = script_params

    @property
    def name(self):
        r"""Gets the name of this AddScriptModel.

        脚本名称：只能包含中文、英文、数字、下划线

        :return: The name of this AddScriptModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddScriptModel.

        脚本名称：只能包含中文、英文、数字、下划线

        :param name: The name of this AddScriptModel.
        :type name: str
        """
        self._name = name

    @property
    def properties(self):
        r"""Gets the properties of this AddScriptModel.

        :return: The properties of this AddScriptModel.
        :rtype: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this AddScriptModel.

        :param properties: The properties of this AddScriptModel.
        :type properties: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        """
        self._properties = properties

    @property
    def description(self):
        r"""Gets the description of this AddScriptModel.

        脚本描述

        :return: The description of this AddScriptModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddScriptModel.

        脚本描述

        :param description: The description of this AddScriptModel.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this AddScriptModel.

        脚本类型: 对于脚本后缀： SHELL:.sh PYTHON:.py BAT:.bat

        :return: The type of this AddScriptModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AddScriptModel.

        脚本类型: 对于脚本后缀： SHELL:.sh PYTHON:.py BAT:.bat

        :param type: The type of this AddScriptModel.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        r"""Gets the content of this AddScriptModel.

        脚本内容

        :return: The content of this AddScriptModel.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this AddScriptModel.

        脚本内容

        :param content: The content of this AddScriptModel.
        :type content: str
        """
        self._content = content

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AddScriptModel.

        企业项目ID，默认为：0

        :return: The enterprise_project_id of this AddScriptModel.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AddScriptModel.

        企业项目ID，默认为：0

        :param enterprise_project_id: The enterprise_project_id of this AddScriptModel.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def script_params(self):
        r"""Gets the script_params of this AddScriptModel.

        脚本入参

        :return: The script_params of this AddScriptModel.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        r"""Sets the script_params of this AddScriptModel.

        脚本入参

        :param script_params: The script_params of this AddScriptModel.
        :type script_params: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        """
        self._script_params = script_params

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
        if not isinstance(other, AddScriptModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
