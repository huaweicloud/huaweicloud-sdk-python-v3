# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'favourite': 'bool',
        'uuid': 'str',
        'type': 'str',
        'name': 'str',
        'weight': 'float',
        'scope': 'str',
        'description': 'str',
        'nick_name': 'str',
        'public': 'bool',
        'tool_type': 'str',
        'template': 'QueryTemplate',
        'parameters': 'list[Parameter]'
    }

    attribute_map = {
        'language': 'language',
        'favourite': 'favourite',
        'uuid': 'uuid',
        'type': 'type',
        'name': 'name',
        'weight': 'weight',
        'scope': 'scope',
        'description': 'description',
        'nick_name': 'nick_name',
        'public': 'public',
        'tool_type': 'tool_type',
        'template': 'template',
        'parameters': 'parameters'
    }

    def __init__(self, language=None, favourite=None, uuid=None, type=None, name=None, weight=None, scope=None, description=None, nick_name=None, public=None, tool_type=None, template=None, parameters=None):
        r"""TemplateList

        The model defined in huaweicloud sdk

        :param language: 模版支持的语言
        :type language: str
        :param favourite: 是否收藏模板
        :type favourite: bool
        :param uuid: uuid
        :type uuid: str
        :param type: 模板类别
        :type type: str
        :param name: 模板命名
        :type name: str
        :param weight: 权重
        :type weight: float
        :param scope: 模板范围，自定义模板默认为：custom,官方模版为：official
        :type scope: str
        :param description: 模板说明
        :type description: str
        :param nick_name: 昵称
        :type nick_name: str
        :param public: 模板是否公开
        :type public: bool
        :param tool_type: 构建工具类型，mono、npm、maven等
        :type tool_type: str
        :param template: 
        :type template: :class:`huaweicloudsdkcodeartsbuild.v3.QueryTemplate`
        :param parameters: 构建执行参数列表
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.Parameter`]
        """
        
        

        self._language = None
        self._favourite = None
        self._uuid = None
        self._type = None
        self._name = None
        self._weight = None
        self._scope = None
        self._description = None
        self._nick_name = None
        self._public = None
        self._tool_type = None
        self._template = None
        self._parameters = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if favourite is not None:
            self.favourite = favourite
        if uuid is not None:
            self.uuid = uuid
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight
        if scope is not None:
            self.scope = scope
        if description is not None:
            self.description = description
        if nick_name is not None:
            self.nick_name = nick_name
        if public is not None:
            self.public = public
        if tool_type is not None:
            self.tool_type = tool_type
        if template is not None:
            self.template = template
        if parameters is not None:
            self.parameters = parameters

    @property
    def language(self):
        r"""Gets the language of this TemplateList.

        模版支持的语言

        :return: The language of this TemplateList.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this TemplateList.

        模版支持的语言

        :param language: The language of this TemplateList.
        :type language: str
        """
        self._language = language

    @property
    def favourite(self):
        r"""Gets the favourite of this TemplateList.

        是否收藏模板

        :return: The favourite of this TemplateList.
        :rtype: bool
        """
        return self._favourite

    @favourite.setter
    def favourite(self, favourite):
        r"""Sets the favourite of this TemplateList.

        是否收藏模板

        :param favourite: The favourite of this TemplateList.
        :type favourite: bool
        """
        self._favourite = favourite

    @property
    def uuid(self):
        r"""Gets the uuid of this TemplateList.

        uuid

        :return: The uuid of this TemplateList.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this TemplateList.

        uuid

        :param uuid: The uuid of this TemplateList.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def type(self):
        r"""Gets the type of this TemplateList.

        模板类别

        :return: The type of this TemplateList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TemplateList.

        模板类别

        :param type: The type of this TemplateList.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this TemplateList.

        模板命名

        :return: The name of this TemplateList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TemplateList.

        模板命名

        :param name: The name of this TemplateList.
        :type name: str
        """
        self._name = name

    @property
    def weight(self):
        r"""Gets the weight of this TemplateList.

        权重

        :return: The weight of this TemplateList.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this TemplateList.

        权重

        :param weight: The weight of this TemplateList.
        :type weight: float
        """
        self._weight = weight

    @property
    def scope(self):
        r"""Gets the scope of this TemplateList.

        模板范围，自定义模板默认为：custom,官方模版为：official

        :return: The scope of this TemplateList.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this TemplateList.

        模板范围，自定义模板默认为：custom,官方模版为：official

        :param scope: The scope of this TemplateList.
        :type scope: str
        """
        self._scope = scope

    @property
    def description(self):
        r"""Gets the description of this TemplateList.

        模板说明

        :return: The description of this TemplateList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TemplateList.

        模板说明

        :param description: The description of this TemplateList.
        :type description: str
        """
        self._description = description

    @property
    def nick_name(self):
        r"""Gets the nick_name of this TemplateList.

        昵称

        :return: The nick_name of this TemplateList.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this TemplateList.

        昵称

        :param nick_name: The nick_name of this TemplateList.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def public(self):
        r"""Gets the public of this TemplateList.

        模板是否公开

        :return: The public of this TemplateList.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        r"""Sets the public of this TemplateList.

        模板是否公开

        :param public: The public of this TemplateList.
        :type public: bool
        """
        self._public = public

    @property
    def tool_type(self):
        r"""Gets the tool_type of this TemplateList.

        构建工具类型，mono、npm、maven等

        :return: The tool_type of this TemplateList.
        :rtype: str
        """
        return self._tool_type

    @tool_type.setter
    def tool_type(self, tool_type):
        r"""Sets the tool_type of this TemplateList.

        构建工具类型，mono、npm、maven等

        :param tool_type: The tool_type of this TemplateList.
        :type tool_type: str
        """
        self._tool_type = tool_type

    @property
    def template(self):
        r"""Gets the template of this TemplateList.

        :return: The template of this TemplateList.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.QueryTemplate`
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this TemplateList.

        :param template: The template of this TemplateList.
        :type template: :class:`huaweicloudsdkcodeartsbuild.v3.QueryTemplate`
        """
        self._template = template

    @property
    def parameters(self):
        r"""Gets the parameters of this TemplateList.

        构建执行参数列表

        :return: The parameters of this TemplateList.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.Parameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this TemplateList.

        构建执行参数列表

        :param parameters: The parameters of this TemplateList.
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.Parameter`]
        """
        self._parameters = parameters

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
        if not isinstance(other, TemplateList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
