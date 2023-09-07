# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_count': 'int',
        'actions': 'list[ActionBaseInfo]',
        'auth_content': 'object',
        'auth_id': 'str',
        'category': 'str',
        'created_time': 'datetime',
        'description': 'str',
        'favorite': 'bool',
        'icon': 'str',
        'id': 'str',
        'name': 'str',
        'need_auth': 'bool',
        'provider_name': 'str',
        'release_version': 'str',
        'runtime_permissions': 'list[RuntimePermission]',
        'status': 'str',
        'swagger': 'object',
        'swagger_version_id': 'str',
        'trigger_count': 'int',
        'triggers': 'list[TriggerBaseInfo]',
        'type': 'str',
        'updated_time': 'datetime',
        'version': 'object'
    }

    attribute_map = {
        'action_count': 'action_count',
        'actions': 'actions',
        'auth_content': 'auth_content',
        'auth_id': 'auth_id',
        'category': 'category',
        'created_time': 'created_time',
        'description': 'description',
        'favorite': 'favorite',
        'icon': 'icon',
        'id': 'id',
        'name': 'name',
        'need_auth': 'need_auth',
        'provider_name': 'provider_name',
        'release_version': 'release_version',
        'runtime_permissions': 'runtime_permissions',
        'status': 'status',
        'swagger': 'swagger',
        'swagger_version_id': 'swagger_version_id',
        'trigger_count': 'trigger_count',
        'triggers': 'triggers',
        'type': 'type',
        'updated_time': 'updated_time',
        'version': 'version'
    }

    def __init__(self, action_count=None, actions=None, auth_content=None, auth_id=None, category=None, created_time=None, description=None, favorite=None, icon=None, id=None, name=None, need_auth=None, provider_name=None, release_version=None, runtime_permissions=None, status=None, swagger=None, swagger_version_id=None, trigger_count=None, triggers=None, type=None, updated_time=None, version=None):
        """ConnectorInfo

        The model defined in huaweicloud sdk

        :param action_count: 执行动作数量
        :type action_count: int
        :param actions: 触发事件数量
        :type actions: list[:class:`huaweicloudsdkmssi.v1.ActionBaseInfo`]
        :param auth_content: 安全认证配置内容
        :type auth_content: object
        :param auth_id: 认证配置ID
        :type auth_id: str
        :param category: 自定义连接器种类（连接器市场的tab分类）
        :type category: str
        :param created_time: 创建时间
        :type created_time: datetime
        :param description: 自定义连接器描述
        :type description: str
        :param favorite: 是否收藏
        :type favorite: bool
        :param icon: logo base64编码
        :type icon: str
        :param id: 自定义连接器ID
        :type id: str
        :param name: 自定义连接器名称
        :type name: str
        :param need_auth: 是否需要验证
        :type need_auth: bool
        :param provider_name: 服务提供商
        :type provider_name: str
        :param release_version: 发布版本
        :type release_version: str
        :param runtime_permissions: 权限
        :type runtime_permissions: list[:class:`huaweicloudsdkmssi.v1.RuntimePermission`]
        :param status: 状态(dev：草稿、released：已发布、onboard：已上架)
        :type status: str
        :param swagger: swagger文档（只包含基本信息+认证信息）
        :type swagger: object
        :param swagger_version_id: 版本id
        :type swagger_version_id: str
        :param trigger_count: 触发事件数量
        :type trigger_count: int
        :param triggers: 触发事件数量
        :type triggers: list[:class:`huaweicloudsdkmssi.v1.TriggerBaseInfo`]
        :param type: 自定义连接器类型
        :type type: str
        :param updated_time: 修改时间
        :type updated_time: datetime
        :param version: 版本号
        :type version: object
        """
        
        

        self._action_count = None
        self._actions = None
        self._auth_content = None
        self._auth_id = None
        self._category = None
        self._created_time = None
        self._description = None
        self._favorite = None
        self._icon = None
        self._id = None
        self._name = None
        self._need_auth = None
        self._provider_name = None
        self._release_version = None
        self._runtime_permissions = None
        self._status = None
        self._swagger = None
        self._swagger_version_id = None
        self._trigger_count = None
        self._triggers = None
        self._type = None
        self._updated_time = None
        self._version = None
        self.discriminator = None

        if action_count is not None:
            self.action_count = action_count
        if actions is not None:
            self.actions = actions
        if auth_content is not None:
            self.auth_content = auth_content
        if auth_id is not None:
            self.auth_id = auth_id
        if category is not None:
            self.category = category
        if created_time is not None:
            self.created_time = created_time
        if description is not None:
            self.description = description
        if favorite is not None:
            self.favorite = favorite
        if icon is not None:
            self.icon = icon
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if need_auth is not None:
            self.need_auth = need_auth
        if provider_name is not None:
            self.provider_name = provider_name
        if release_version is not None:
            self.release_version = release_version
        if runtime_permissions is not None:
            self.runtime_permissions = runtime_permissions
        if status is not None:
            self.status = status
        if swagger is not None:
            self.swagger = swagger
        if swagger_version_id is not None:
            self.swagger_version_id = swagger_version_id
        if trigger_count is not None:
            self.trigger_count = trigger_count
        if triggers is not None:
            self.triggers = triggers
        if type is not None:
            self.type = type
        if updated_time is not None:
            self.updated_time = updated_time
        if version is not None:
            self.version = version

    @property
    def action_count(self):
        """Gets the action_count of this ConnectorInfo.

        执行动作数量

        :return: The action_count of this ConnectorInfo.
        :rtype: int
        """
        return self._action_count

    @action_count.setter
    def action_count(self, action_count):
        """Sets the action_count of this ConnectorInfo.

        执行动作数量

        :param action_count: The action_count of this ConnectorInfo.
        :type action_count: int
        """
        self._action_count = action_count

    @property
    def actions(self):
        """Gets the actions of this ConnectorInfo.

        触发事件数量

        :return: The actions of this ConnectorInfo.
        :rtype: list[:class:`huaweicloudsdkmssi.v1.ActionBaseInfo`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ConnectorInfo.

        触发事件数量

        :param actions: The actions of this ConnectorInfo.
        :type actions: list[:class:`huaweicloudsdkmssi.v1.ActionBaseInfo`]
        """
        self._actions = actions

    @property
    def auth_content(self):
        """Gets the auth_content of this ConnectorInfo.

        安全认证配置内容

        :return: The auth_content of this ConnectorInfo.
        :rtype: object
        """
        return self._auth_content

    @auth_content.setter
    def auth_content(self, auth_content):
        """Sets the auth_content of this ConnectorInfo.

        安全认证配置内容

        :param auth_content: The auth_content of this ConnectorInfo.
        :type auth_content: object
        """
        self._auth_content = auth_content

    @property
    def auth_id(self):
        """Gets the auth_id of this ConnectorInfo.

        认证配置ID

        :return: The auth_id of this ConnectorInfo.
        :rtype: str
        """
        return self._auth_id

    @auth_id.setter
    def auth_id(self, auth_id):
        """Sets the auth_id of this ConnectorInfo.

        认证配置ID

        :param auth_id: The auth_id of this ConnectorInfo.
        :type auth_id: str
        """
        self._auth_id = auth_id

    @property
    def category(self):
        """Gets the category of this ConnectorInfo.

        自定义连接器种类（连接器市场的tab分类）

        :return: The category of this ConnectorInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ConnectorInfo.

        自定义连接器种类（连接器市场的tab分类）

        :param category: The category of this ConnectorInfo.
        :type category: str
        """
        self._category = category

    @property
    def created_time(self):
        """Gets the created_time of this ConnectorInfo.

        创建时间

        :return: The created_time of this ConnectorInfo.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ConnectorInfo.

        创建时间

        :param created_time: The created_time of this ConnectorInfo.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def description(self):
        """Gets the description of this ConnectorInfo.

        自定义连接器描述

        :return: The description of this ConnectorInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConnectorInfo.

        自定义连接器描述

        :param description: The description of this ConnectorInfo.
        :type description: str
        """
        self._description = description

    @property
    def favorite(self):
        """Gets the favorite of this ConnectorInfo.

        是否收藏

        :return: The favorite of this ConnectorInfo.
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this ConnectorInfo.

        是否收藏

        :param favorite: The favorite of this ConnectorInfo.
        :type favorite: bool
        """
        self._favorite = favorite

    @property
    def icon(self):
        """Gets the icon of this ConnectorInfo.

        logo base64编码

        :return: The icon of this ConnectorInfo.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ConnectorInfo.

        logo base64编码

        :param icon: The icon of this ConnectorInfo.
        :type icon: str
        """
        self._icon = icon

    @property
    def id(self):
        """Gets the id of this ConnectorInfo.

        自定义连接器ID

        :return: The id of this ConnectorInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectorInfo.

        自定义连接器ID

        :param id: The id of this ConnectorInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ConnectorInfo.

        自定义连接器名称

        :return: The name of this ConnectorInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectorInfo.

        自定义连接器名称

        :param name: The name of this ConnectorInfo.
        :type name: str
        """
        self._name = name

    @property
    def need_auth(self):
        """Gets the need_auth of this ConnectorInfo.

        是否需要验证

        :return: The need_auth of this ConnectorInfo.
        :rtype: bool
        """
        return self._need_auth

    @need_auth.setter
    def need_auth(self, need_auth):
        """Sets the need_auth of this ConnectorInfo.

        是否需要验证

        :param need_auth: The need_auth of this ConnectorInfo.
        :type need_auth: bool
        """
        self._need_auth = need_auth

    @property
    def provider_name(self):
        """Gets the provider_name of this ConnectorInfo.

        服务提供商

        :return: The provider_name of this ConnectorInfo.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this ConnectorInfo.

        服务提供商

        :param provider_name: The provider_name of this ConnectorInfo.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def release_version(self):
        """Gets the release_version of this ConnectorInfo.

        发布版本

        :return: The release_version of this ConnectorInfo.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """Sets the release_version of this ConnectorInfo.

        发布版本

        :param release_version: The release_version of this ConnectorInfo.
        :type release_version: str
        """
        self._release_version = release_version

    @property
    def runtime_permissions(self):
        """Gets the runtime_permissions of this ConnectorInfo.

        权限

        :return: The runtime_permissions of this ConnectorInfo.
        :rtype: list[:class:`huaweicloudsdkmssi.v1.RuntimePermission`]
        """
        return self._runtime_permissions

    @runtime_permissions.setter
    def runtime_permissions(self, runtime_permissions):
        """Sets the runtime_permissions of this ConnectorInfo.

        权限

        :param runtime_permissions: The runtime_permissions of this ConnectorInfo.
        :type runtime_permissions: list[:class:`huaweicloudsdkmssi.v1.RuntimePermission`]
        """
        self._runtime_permissions = runtime_permissions

    @property
    def status(self):
        """Gets the status of this ConnectorInfo.

        状态(dev：草稿、released：已发布、onboard：已上架)

        :return: The status of this ConnectorInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectorInfo.

        状态(dev：草稿、released：已发布、onboard：已上架)

        :param status: The status of this ConnectorInfo.
        :type status: str
        """
        self._status = status

    @property
    def swagger(self):
        """Gets the swagger of this ConnectorInfo.

        swagger文档（只包含基本信息+认证信息）

        :return: The swagger of this ConnectorInfo.
        :rtype: object
        """
        return self._swagger

    @swagger.setter
    def swagger(self, swagger):
        """Sets the swagger of this ConnectorInfo.

        swagger文档（只包含基本信息+认证信息）

        :param swagger: The swagger of this ConnectorInfo.
        :type swagger: object
        """
        self._swagger = swagger

    @property
    def swagger_version_id(self):
        """Gets the swagger_version_id of this ConnectorInfo.

        版本id

        :return: The swagger_version_id of this ConnectorInfo.
        :rtype: str
        """
        return self._swagger_version_id

    @swagger_version_id.setter
    def swagger_version_id(self, swagger_version_id):
        """Sets the swagger_version_id of this ConnectorInfo.

        版本id

        :param swagger_version_id: The swagger_version_id of this ConnectorInfo.
        :type swagger_version_id: str
        """
        self._swagger_version_id = swagger_version_id

    @property
    def trigger_count(self):
        """Gets the trigger_count of this ConnectorInfo.

        触发事件数量

        :return: The trigger_count of this ConnectorInfo.
        :rtype: int
        """
        return self._trigger_count

    @trigger_count.setter
    def trigger_count(self, trigger_count):
        """Sets the trigger_count of this ConnectorInfo.

        触发事件数量

        :param trigger_count: The trigger_count of this ConnectorInfo.
        :type trigger_count: int
        """
        self._trigger_count = trigger_count

    @property
    def triggers(self):
        """Gets the triggers of this ConnectorInfo.

        触发事件数量

        :return: The triggers of this ConnectorInfo.
        :rtype: list[:class:`huaweicloudsdkmssi.v1.TriggerBaseInfo`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this ConnectorInfo.

        触发事件数量

        :param triggers: The triggers of this ConnectorInfo.
        :type triggers: list[:class:`huaweicloudsdkmssi.v1.TriggerBaseInfo`]
        """
        self._triggers = triggers

    @property
    def type(self):
        """Gets the type of this ConnectorInfo.

        自定义连接器类型

        :return: The type of this ConnectorInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConnectorInfo.

        自定义连接器类型

        :param type: The type of this ConnectorInfo.
        :type type: str
        """
        self._type = type

    @property
    def updated_time(self):
        """Gets the updated_time of this ConnectorInfo.

        修改时间

        :return: The updated_time of this ConnectorInfo.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ConnectorInfo.

        修改时间

        :param updated_time: The updated_time of this ConnectorInfo.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

    @property
    def version(self):
        """Gets the version of this ConnectorInfo.

        版本号

        :return: The version of this ConnectorInfo.
        :rtype: object
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ConnectorInfo.

        版本号

        :param version: The version of this ConnectorInfo.
        :type version: object
        """
        self._version = version

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
        if not isinstance(other, ConnectorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
