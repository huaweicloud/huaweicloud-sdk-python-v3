# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditScriptModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'content': 'str',
        'properties': 'ScriptPropertiesModel',
        'script_params': 'list[ScriptParamDefine]'
    }

    attribute_map = {
        'description': 'description',
        'content': 'content',
        'properties': 'properties',
        'script_params': 'script_params'
    }

    def __init__(self, description=None, content=None, properties=None, script_params=None):
        r"""EditScriptModel

        The model defined in huaweicloud sdk

        :param description: 脚本描述
        :type description: str
        :param content: 脚本内容
        :type content: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        :param script_params: 脚本入参
        :type script_params: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        """
        
        

        self._description = None
        self._content = None
        self._properties = None
        self._script_params = None
        self.discriminator = None

        self.description = description
        self.content = content
        if properties is not None:
            self.properties = properties
        if script_params is not None:
            self.script_params = script_params

    @property
    def description(self):
        r"""Gets the description of this EditScriptModel.

        脚本描述

        :return: The description of this EditScriptModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EditScriptModel.

        脚本描述

        :param description: The description of this EditScriptModel.
        :type description: str
        """
        self._description = description

    @property
    def content(self):
        r"""Gets the content of this EditScriptModel.

        脚本内容

        :return: The content of this EditScriptModel.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this EditScriptModel.

        脚本内容

        :param content: The content of this EditScriptModel.
        :type content: str
        """
        self._content = content

    @property
    def properties(self):
        r"""Gets the properties of this EditScriptModel.

        :return: The properties of this EditScriptModel.
        :rtype: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this EditScriptModel.

        :param properties: The properties of this EditScriptModel.
        :type properties: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        """
        self._properties = properties

    @property
    def script_params(self):
        r"""Gets the script_params of this EditScriptModel.

        脚本入参

        :return: The script_params of this EditScriptModel.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        r"""Sets the script_params of this EditScriptModel.

        脚本入参

        :param script_params: The script_params of this EditScriptModel.
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
        if not isinstance(other, EditScriptModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
