# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectorInfo0:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_content': 'AuthConfigA',
        'auth_id': 'str',
        'auth_type': 'str',
        'category': 'str',
        'created_time': 'datetime',
        'definition_ref': 'str',
        'description': 'str',
        'icon': 'str',
        'id': 'str',
        'name': 'str',
        'need_auth': 'bool',
        'operations': 'list[object]',
        'provider': 'str',
        'swagger': 'str',
        'triggers': 'list[object]',
        'type': 'str',
        'updated_time': 'datetime'
    }

    attribute_map = {
        'auth_content': 'authContent',
        'auth_id': 'authId',
        'auth_type': 'auth_type',
        'category': 'category',
        'created_time': 'created_time',
        'definition_ref': 'definitionRef',
        'description': 'description',
        'icon': 'icon',
        'id': 'id',
        'name': 'name',
        'need_auth': 'needAuth',
        'operations': 'operations',
        'provider': 'provider',
        'swagger': 'swagger',
        'triggers': 'triggers',
        'type': 'type',
        'updated_time': 'updated_time'
    }

    def __init__(self, auth_content=None, auth_id=None, auth_type=None, category=None, created_time=None, definition_ref=None, description=None, icon=None, id=None, name=None, need_auth=None, operations=None, provider=None, swagger=None, triggers=None, type=None, updated_time=None):
        """ConnectorInfo0

        The model defined in huaweicloud sdk

        :param auth_content: 
        :type auth_content: :class:`huaweicloudsdkmssi.v1.AuthConfigA`
        :param auth_id: 认证id
        :type auth_id: str
        :param auth_type: 判断方式
        :type auth_type: str
        :param category: 内置连接器查询
        :type category: str
        :param created_time: 创建时间
        :type created_time: datetime
        :param definition_ref: 连接器
        :type definition_ref: str
        :param description: 连接器描述
        :type description: str
        :param icon: logo base64编码
        :type icon: str
        :param id: 连接器ID
        :type id: str
        :param name: 连接器名称
        :type name: str
        :param need_auth: 是否需要验证
        :type need_auth: bool
        :param operations: 视图数据
        :type operations: list[object]
        :param provider: 供应商
        :type provider: str
        :param swagger: swagger文档，大文本
        :type swagger: str
        :param triggers: 操作json
        :type triggers: list[object]
        :param type: 连接器类型
        :type type: str
        :param updated_time: 修改时间
        :type updated_time: datetime
        """
        
        

        self._auth_content = None
        self._auth_id = None
        self._auth_type = None
        self._category = None
        self._created_time = None
        self._definition_ref = None
        self._description = None
        self._icon = None
        self._id = None
        self._name = None
        self._need_auth = None
        self._operations = None
        self._provider = None
        self._swagger = None
        self._triggers = None
        self._type = None
        self._updated_time = None
        self.discriminator = None

        if auth_content is not None:
            self.auth_content = auth_content
        if auth_id is not None:
            self.auth_id = auth_id
        if auth_type is not None:
            self.auth_type = auth_type
        if category is not None:
            self.category = category
        if created_time is not None:
            self.created_time = created_time
        if definition_ref is not None:
            self.definition_ref = definition_ref
        if description is not None:
            self.description = description
        if icon is not None:
            self.icon = icon
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if need_auth is not None:
            self.need_auth = need_auth
        if operations is not None:
            self.operations = operations
        if provider is not None:
            self.provider = provider
        if swagger is not None:
            self.swagger = swagger
        if triggers is not None:
            self.triggers = triggers
        if type is not None:
            self.type = type
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def auth_content(self):
        """Gets the auth_content of this ConnectorInfo0.

        :return: The auth_content of this ConnectorInfo0.
        :rtype: :class:`huaweicloudsdkmssi.v1.AuthConfigA`
        """
        return self._auth_content

    @auth_content.setter
    def auth_content(self, auth_content):
        """Sets the auth_content of this ConnectorInfo0.

        :param auth_content: The auth_content of this ConnectorInfo0.
        :type auth_content: :class:`huaweicloudsdkmssi.v1.AuthConfigA`
        """
        self._auth_content = auth_content

    @property
    def auth_id(self):
        """Gets the auth_id of this ConnectorInfo0.

        认证id

        :return: The auth_id of this ConnectorInfo0.
        :rtype: str
        """
        return self._auth_id

    @auth_id.setter
    def auth_id(self, auth_id):
        """Sets the auth_id of this ConnectorInfo0.

        认证id

        :param auth_id: The auth_id of this ConnectorInfo0.
        :type auth_id: str
        """
        self._auth_id = auth_id

    @property
    def auth_type(self):
        """Gets the auth_type of this ConnectorInfo0.

        判断方式

        :return: The auth_type of this ConnectorInfo0.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ConnectorInfo0.

        判断方式

        :param auth_type: The auth_type of this ConnectorInfo0.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def category(self):
        """Gets the category of this ConnectorInfo0.

        内置连接器查询

        :return: The category of this ConnectorInfo0.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ConnectorInfo0.

        内置连接器查询

        :param category: The category of this ConnectorInfo0.
        :type category: str
        """
        self._category = category

    @property
    def created_time(self):
        """Gets the created_time of this ConnectorInfo0.

        创建时间

        :return: The created_time of this ConnectorInfo0.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ConnectorInfo0.

        创建时间

        :param created_time: The created_time of this ConnectorInfo0.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def definition_ref(self):
        """Gets the definition_ref of this ConnectorInfo0.

        连接器

        :return: The definition_ref of this ConnectorInfo0.
        :rtype: str
        """
        return self._definition_ref

    @definition_ref.setter
    def definition_ref(self, definition_ref):
        """Sets the definition_ref of this ConnectorInfo0.

        连接器

        :param definition_ref: The definition_ref of this ConnectorInfo0.
        :type definition_ref: str
        """
        self._definition_ref = definition_ref

    @property
    def description(self):
        """Gets the description of this ConnectorInfo0.

        连接器描述

        :return: The description of this ConnectorInfo0.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConnectorInfo0.

        连接器描述

        :param description: The description of this ConnectorInfo0.
        :type description: str
        """
        self._description = description

    @property
    def icon(self):
        """Gets the icon of this ConnectorInfo0.

        logo base64编码

        :return: The icon of this ConnectorInfo0.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ConnectorInfo0.

        logo base64编码

        :param icon: The icon of this ConnectorInfo0.
        :type icon: str
        """
        self._icon = icon

    @property
    def id(self):
        """Gets the id of this ConnectorInfo0.

        连接器ID

        :return: The id of this ConnectorInfo0.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectorInfo0.

        连接器ID

        :param id: The id of this ConnectorInfo0.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ConnectorInfo0.

        连接器名称

        :return: The name of this ConnectorInfo0.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectorInfo0.

        连接器名称

        :param name: The name of this ConnectorInfo0.
        :type name: str
        """
        self._name = name

    @property
    def need_auth(self):
        """Gets the need_auth of this ConnectorInfo0.

        是否需要验证

        :return: The need_auth of this ConnectorInfo0.
        :rtype: bool
        """
        return self._need_auth

    @need_auth.setter
    def need_auth(self, need_auth):
        """Sets the need_auth of this ConnectorInfo0.

        是否需要验证

        :param need_auth: The need_auth of this ConnectorInfo0.
        :type need_auth: bool
        """
        self._need_auth = need_auth

    @property
    def operations(self):
        """Gets the operations of this ConnectorInfo0.

        视图数据

        :return: The operations of this ConnectorInfo0.
        :rtype: list[object]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this ConnectorInfo0.

        视图数据

        :param operations: The operations of this ConnectorInfo0.
        :type operations: list[object]
        """
        self._operations = operations

    @property
    def provider(self):
        """Gets the provider of this ConnectorInfo0.

        供应商

        :return: The provider of this ConnectorInfo0.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ConnectorInfo0.

        供应商

        :param provider: The provider of this ConnectorInfo0.
        :type provider: str
        """
        self._provider = provider

    @property
    def swagger(self):
        """Gets the swagger of this ConnectorInfo0.

        swagger文档，大文本

        :return: The swagger of this ConnectorInfo0.
        :rtype: str
        """
        return self._swagger

    @swagger.setter
    def swagger(self, swagger):
        """Sets the swagger of this ConnectorInfo0.

        swagger文档，大文本

        :param swagger: The swagger of this ConnectorInfo0.
        :type swagger: str
        """
        self._swagger = swagger

    @property
    def triggers(self):
        """Gets the triggers of this ConnectorInfo0.

        操作json

        :return: The triggers of this ConnectorInfo0.
        :rtype: list[object]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this ConnectorInfo0.

        操作json

        :param triggers: The triggers of this ConnectorInfo0.
        :type triggers: list[object]
        """
        self._triggers = triggers

    @property
    def type(self):
        """Gets the type of this ConnectorInfo0.

        连接器类型

        :return: The type of this ConnectorInfo0.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConnectorInfo0.

        连接器类型

        :param type: The type of this ConnectorInfo0.
        :type type: str
        """
        self._type = type

    @property
    def updated_time(self):
        """Gets the updated_time of this ConnectorInfo0.

        修改时间

        :return: The updated_time of this ConnectorInfo0.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ConnectorInfo0.

        修改时间

        :param updated_time: The updated_time of this ConnectorInfo0.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

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
        if not isinstance(other, ConnectorInfo0):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
