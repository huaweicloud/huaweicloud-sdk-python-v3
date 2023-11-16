# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplatesItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'favourite': 'bool',
        'id': 'str',
        'uuid': 'str',
        'template': 'QueryTemplate',
        'type': 'str',
        'public': 'bool',
        'name': 'str',
        'create_time': 'str',
        'domain_id': 'str',
        'weight': 'float',
        'user_id': 'str',
        'user_name': 'str',
        'domain_name': 'str',
        'scope': 'str',
        'description': 'str',
        'tool_type': 'str',
        'intl_description': 'object',
        'parameters': 'list[CreateBuildJobParameter]',
        'i18n': 'object'
    }

    attribute_map = {
        'favourite': 'favourite',
        'id': 'id',
        'uuid': 'uuid',
        'template': 'template',
        'type': 'type',
        'public': 'public',
        'name': 'name',
        'create_time': 'create_time',
        'domain_id': 'domain_id',
        'weight': 'weight',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'domain_name': 'domain_name',
        'scope': 'scope',
        'description': 'description',
        'tool_type': 'tool_type',
        'intl_description': 'intl_description',
        'parameters': 'parameters',
        'i18n': 'i18n'
    }

    def __init__(self, favourite=None, id=None, uuid=None, template=None, type=None, public=None, name=None, create_time=None, domain_id=None, weight=None, user_id=None, user_name=None, domain_name=None, scope=None, description=None, tool_type=None, intl_description=None, parameters=None, i18n=None):
        """CreateTemplatesItems

        The model defined in huaweicloud sdk

        :param favourite: 是否收藏模板
        :type favourite: bool
        :param id: 数据库中id
        :type id: str
        :param uuid: uuid
        :type uuid: str
        :param template: 
        :type template: :class:`huaweicloudsdkcodeartsbuild.v3.QueryTemplate`
        :param type: 模板类别
        :type type: str
        :param public: 模板是否公开
        :type public: bool
        :param name: 模板命名
        :type name: str
        :param create_time: 创建时间
        :type create_time: str
        :param domain_id: domainId
        :type domain_id: str
        :param weight: 权重
        :type weight: float
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param domain_name: domain名字
        :type domain_name: str
        :param scope: 模板范围，自定义模板默认为custom
        :type scope: str
        :param description: 模板说明
        :type description: str
        :param tool_type: 构建工具类型，yaml构建还是action构建
        :type tool_type: str
        :param intl_description: intl说明
        :type intl_description: object
        :param parameters: 构建执行参数列表
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        :param i18n: i18n
        :type i18n: object
        """
        
        

        self._favourite = None
        self._id = None
        self._uuid = None
        self._template = None
        self._type = None
        self._public = None
        self._name = None
        self._create_time = None
        self._domain_id = None
        self._weight = None
        self._user_id = None
        self._user_name = None
        self._domain_name = None
        self._scope = None
        self._description = None
        self._tool_type = None
        self._intl_description = None
        self._parameters = None
        self._i18n = None
        self.discriminator = None

        if favourite is not None:
            self.favourite = favourite
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid
        if template is not None:
            self.template = template
        if type is not None:
            self.type = type
        if public is not None:
            self.public = public
        if name is not None:
            self.name = name
        if create_time is not None:
            self.create_time = create_time
        if domain_id is not None:
            self.domain_id = domain_id
        if weight is not None:
            self.weight = weight
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if domain_name is not None:
            self.domain_name = domain_name
        if scope is not None:
            self.scope = scope
        if description is not None:
            self.description = description
        if tool_type is not None:
            self.tool_type = tool_type
        if intl_description is not None:
            self.intl_description = intl_description
        if parameters is not None:
            self.parameters = parameters
        if i18n is not None:
            self.i18n = i18n

    @property
    def favourite(self):
        """Gets the favourite of this CreateTemplatesItems.

        是否收藏模板

        :return: The favourite of this CreateTemplatesItems.
        :rtype: bool
        """
        return self._favourite

    @favourite.setter
    def favourite(self, favourite):
        """Sets the favourite of this CreateTemplatesItems.

        是否收藏模板

        :param favourite: The favourite of this CreateTemplatesItems.
        :type favourite: bool
        """
        self._favourite = favourite

    @property
    def id(self):
        """Gets the id of this CreateTemplatesItems.

        数据库中id

        :return: The id of this CreateTemplatesItems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateTemplatesItems.

        数据库中id

        :param id: The id of this CreateTemplatesItems.
        :type id: str
        """
        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this CreateTemplatesItems.

        uuid

        :return: The uuid of this CreateTemplatesItems.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this CreateTemplatesItems.

        uuid

        :param uuid: The uuid of this CreateTemplatesItems.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def template(self):
        """Gets the template of this CreateTemplatesItems.

        :return: The template of this CreateTemplatesItems.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.QueryTemplate`
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this CreateTemplatesItems.

        :param template: The template of this CreateTemplatesItems.
        :type template: :class:`huaweicloudsdkcodeartsbuild.v3.QueryTemplate`
        """
        self._template = template

    @property
    def type(self):
        """Gets the type of this CreateTemplatesItems.

        模板类别

        :return: The type of this CreateTemplatesItems.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateTemplatesItems.

        模板类别

        :param type: The type of this CreateTemplatesItems.
        :type type: str
        """
        self._type = type

    @property
    def public(self):
        """Gets the public of this CreateTemplatesItems.

        模板是否公开

        :return: The public of this CreateTemplatesItems.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this CreateTemplatesItems.

        模板是否公开

        :param public: The public of this CreateTemplatesItems.
        :type public: bool
        """
        self._public = public

    @property
    def name(self):
        """Gets the name of this CreateTemplatesItems.

        模板命名

        :return: The name of this CreateTemplatesItems.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTemplatesItems.

        模板命名

        :param name: The name of this CreateTemplatesItems.
        :type name: str
        """
        self._name = name

    @property
    def create_time(self):
        """Gets the create_time of this CreateTemplatesItems.

        创建时间

        :return: The create_time of this CreateTemplatesItems.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateTemplatesItems.

        创建时间

        :param create_time: The create_time of this CreateTemplatesItems.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateTemplatesItems.

        domainId

        :return: The domain_id of this CreateTemplatesItems.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateTemplatesItems.

        domainId

        :param domain_id: The domain_id of this CreateTemplatesItems.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def weight(self):
        """Gets the weight of this CreateTemplatesItems.

        权重

        :return: The weight of this CreateTemplatesItems.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateTemplatesItems.

        权重

        :param weight: The weight of this CreateTemplatesItems.
        :type weight: float
        """
        self._weight = weight

    @property
    def user_id(self):
        """Gets the user_id of this CreateTemplatesItems.

        用户id

        :return: The user_id of this CreateTemplatesItems.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateTemplatesItems.

        用户id

        :param user_id: The user_id of this CreateTemplatesItems.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this CreateTemplatesItems.

        用户名

        :return: The user_name of this CreateTemplatesItems.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateTemplatesItems.

        用户名

        :param user_name: The user_name of this CreateTemplatesItems.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain_name(self):
        """Gets the domain_name of this CreateTemplatesItems.

        domain名字

        :return: The domain_name of this CreateTemplatesItems.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CreateTemplatesItems.

        domain名字

        :param domain_name: The domain_name of this CreateTemplatesItems.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def scope(self):
        """Gets the scope of this CreateTemplatesItems.

        模板范围，自定义模板默认为custom

        :return: The scope of this CreateTemplatesItems.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CreateTemplatesItems.

        模板范围，自定义模板默认为custom

        :param scope: The scope of this CreateTemplatesItems.
        :type scope: str
        """
        self._scope = scope

    @property
    def description(self):
        """Gets the description of this CreateTemplatesItems.

        模板说明

        :return: The description of this CreateTemplatesItems.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTemplatesItems.

        模板说明

        :param description: The description of this CreateTemplatesItems.
        :type description: str
        """
        self._description = description

    @property
    def tool_type(self):
        """Gets the tool_type of this CreateTemplatesItems.

        构建工具类型，yaml构建还是action构建

        :return: The tool_type of this CreateTemplatesItems.
        :rtype: str
        """
        return self._tool_type

    @tool_type.setter
    def tool_type(self, tool_type):
        """Sets the tool_type of this CreateTemplatesItems.

        构建工具类型，yaml构建还是action构建

        :param tool_type: The tool_type of this CreateTemplatesItems.
        :type tool_type: str
        """
        self._tool_type = tool_type

    @property
    def intl_description(self):
        """Gets the intl_description of this CreateTemplatesItems.

        intl说明

        :return: The intl_description of this CreateTemplatesItems.
        :rtype: object
        """
        return self._intl_description

    @intl_description.setter
    def intl_description(self, intl_description):
        """Sets the intl_description of this CreateTemplatesItems.

        intl说明

        :param intl_description: The intl_description of this CreateTemplatesItems.
        :type intl_description: object
        """
        self._intl_description = intl_description

    @property
    def parameters(self):
        """Gets the parameters of this CreateTemplatesItems.

        构建执行参数列表

        :return: The parameters of this CreateTemplatesItems.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this CreateTemplatesItems.

        构建执行参数列表

        :param parameters: The parameters of this CreateTemplatesItems.
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        self._parameters = parameters

    @property
    def i18n(self):
        """Gets the i18n of this CreateTemplatesItems.

        i18n

        :return: The i18n of this CreateTemplatesItems.
        :rtype: object
        """
        return self._i18n

    @i18n.setter
    def i18n(self, i18n):
        """Sets the i18n of this CreateTemplatesItems.

        i18n

        :param i18n: The i18n of this CreateTemplatesItems.
        :type i18n: object
        """
        self._i18n = i18n

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
        if not isinstance(other, CreateTemplatesItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
