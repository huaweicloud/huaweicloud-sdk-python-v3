# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicScriptDetailModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_uuid': 'str',
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'content': 'str',
        'script_params': 'list[ScriptParamDefine]',
        'gmt_created': 'int',
        'properties': 'PublicScriptPropertiesModel'
    }

    attribute_map = {
        'script_uuid': 'script_uuid',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'content': 'content',
        'script_params': 'script_params',
        'gmt_created': 'gmt_created',
        'properties': 'properties'
    }

    def __init__(self, script_uuid=None, name=None, description=None, type=None, content=None, script_params=None, gmt_created=None, properties=None):
        r"""PublicScriptDetailModel

        The model defined in huaweicloud sdk

        :param script_uuid: 脚本uuid
        :type script_uuid: str
        :param name: 脚本名称
        :type name: str
        :param description: 脚本描述
        :type description: str
        :param type: 脚本类型 SHELL:shell脚本， PYTHON:Python脚本， BAT:Bat脚本，
        :type type: str
        :param content: 脚本内容
        :type content: str
        :param script_params: 脚本入参
        :type script_params: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        :param gmt_created: 创建时间
        :type gmt_created: int
        :param properties: 
        :type properties: :class:`huaweicloudsdkcoc.v1.PublicScriptPropertiesModel`
        """
        
        

        self._script_uuid = None
        self._name = None
        self._description = None
        self._type = None
        self._content = None
        self._script_params = None
        self._gmt_created = None
        self._properties = None
        self.discriminator = None

        self.script_uuid = script_uuid
        self.name = name
        self.description = description
        self.type = type
        self.content = content
        if script_params is not None:
            self.script_params = script_params
        self.gmt_created = gmt_created
        self.properties = properties

    @property
    def script_uuid(self):
        r"""Gets the script_uuid of this PublicScriptDetailModel.

        脚本uuid

        :return: The script_uuid of this PublicScriptDetailModel.
        :rtype: str
        """
        return self._script_uuid

    @script_uuid.setter
    def script_uuid(self, script_uuid):
        r"""Sets the script_uuid of this PublicScriptDetailModel.

        脚本uuid

        :param script_uuid: The script_uuid of this PublicScriptDetailModel.
        :type script_uuid: str
        """
        self._script_uuid = script_uuid

    @property
    def name(self):
        r"""Gets the name of this PublicScriptDetailModel.

        脚本名称

        :return: The name of this PublicScriptDetailModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PublicScriptDetailModel.

        脚本名称

        :param name: The name of this PublicScriptDetailModel.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this PublicScriptDetailModel.

        脚本描述

        :return: The description of this PublicScriptDetailModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PublicScriptDetailModel.

        脚本描述

        :param description: The description of this PublicScriptDetailModel.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this PublicScriptDetailModel.

        脚本类型 SHELL:shell脚本， PYTHON:Python脚本， BAT:Bat脚本，

        :return: The type of this PublicScriptDetailModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PublicScriptDetailModel.

        脚本类型 SHELL:shell脚本， PYTHON:Python脚本， BAT:Bat脚本，

        :param type: The type of this PublicScriptDetailModel.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        r"""Gets the content of this PublicScriptDetailModel.

        脚本内容

        :return: The content of this PublicScriptDetailModel.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this PublicScriptDetailModel.

        脚本内容

        :param content: The content of this PublicScriptDetailModel.
        :type content: str
        """
        self._content = content

    @property
    def script_params(self):
        r"""Gets the script_params of this PublicScriptDetailModel.

        脚本入参

        :return: The script_params of this PublicScriptDetailModel.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        r"""Sets the script_params of this PublicScriptDetailModel.

        脚本入参

        :param script_params: The script_params of this PublicScriptDetailModel.
        :type script_params: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        """
        self._script_params = script_params

    @property
    def gmt_created(self):
        r"""Gets the gmt_created of this PublicScriptDetailModel.

        创建时间

        :return: The gmt_created of this PublicScriptDetailModel.
        :rtype: int
        """
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, gmt_created):
        r"""Sets the gmt_created of this PublicScriptDetailModel.

        创建时间

        :param gmt_created: The gmt_created of this PublicScriptDetailModel.
        :type gmt_created: int
        """
        self._gmt_created = gmt_created

    @property
    def properties(self):
        r"""Gets the properties of this PublicScriptDetailModel.

        :return: The properties of this PublicScriptDetailModel.
        :rtype: :class:`huaweicloudsdkcoc.v1.PublicScriptPropertiesModel`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this PublicScriptDetailModel.

        :param properties: The properties of this PublicScriptDetailModel.
        :type properties: :class:`huaweicloudsdkcoc.v1.PublicScriptPropertiesModel`
        """
        self._properties = properties

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
        if not isinstance(other, PublicScriptDetailModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
