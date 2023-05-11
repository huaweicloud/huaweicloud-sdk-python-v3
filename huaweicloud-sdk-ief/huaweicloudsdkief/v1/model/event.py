# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'description': 'str',
        'in_using': 'bool',
        'events': 'str',
        'target': 'EndpointObjResp',
        'target_resource': 'dict(str, str)',
        'success_messages': 'int',
        'fail_messages': 'int',
        'delete_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'description': 'description',
        'in_using': 'in_using',
        'events': 'events',
        'target': 'target',
        'target_resource': 'target_resource',
        'success_messages': 'success_messages',
        'fail_messages': 'fail_messages',
        'delete_at': 'delete_at'
    }

    def __init__(self, id=None, name=None, project_id=None, created_at=None, updated_at=None, description=None, in_using=None, events=None, target=None, target_resource=None, success_messages=None, fail_messages=None, delete_at=None):
        """Event

        The model defined in huaweicloud sdk

        :param id: 系统订阅事件ID
        :type id: str
        :param name: 系统订阅事件名称。只允许小写英文字符、数字、下划线、中划线，最大长度64，同一个帐号中创建的系统订阅和消息规则名唯一
        :type name: str
        :param project_id: 系统订阅事件所属项目ID
        :type project_id: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param description: 描述，最大长度255，不允许^~#$%&amp;*&lt;&gt;()[]{}&#39;\&quot;\\
        :type description: str
        :param in_using: 是否启用系统订阅规则，默认为true（启用）
        :type in_using: bool
        :param events: 系统订阅事件主题。每个主题由“{边缘资源}/{操作}”组成，多个主题使用逗号（,）进行分隔，支持如下主题： - edgeNode/offline：节点离线 - edgeNode/online：节点上线 - edgeNode/all：节点离线+节点上线 - deployment/created：容器应用创建 - deployment/updated：容器应用更新 - deployment/deleted：容器应用删除 - deployment/all：容器应用创建+更新+删除 - instance/created：应用实例创建 - instance/updated：应用实例更新 - instance/deleted：应用实例删除 - instance/all：应用实例创建+更新+删除
        :type events: str
        :param target: 
        :type target: :class:`huaweicloudsdkief.v1.EndpointObjResp`
        :param target_resource: 目的端点资源属性
        :type target_resource: dict(str, str)
        :param success_messages: 成功次数
        :type success_messages: int
        :param fail_messages: 失败次数
        :type fail_messages: int
        :param delete_at: 删除时间
        :type delete_at: int
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._description = None
        self._in_using = None
        self._events = None
        self._target = None
        self._target_resource = None
        self._success_messages = None
        self._fail_messages = None
        self._delete_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if description is not None:
            self.description = description
        if in_using is not None:
            self.in_using = in_using
        if events is not None:
            self.events = events
        if target is not None:
            self.target = target
        if target_resource is not None:
            self.target_resource = target_resource
        if success_messages is not None:
            self.success_messages = success_messages
        if fail_messages is not None:
            self.fail_messages = fail_messages
        if delete_at is not None:
            self.delete_at = delete_at

    @property
    def id(self):
        """Gets the id of this Event.

        系统订阅事件ID

        :return: The id of this Event.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Event.

        系统订阅事件ID

        :param id: The id of this Event.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Event.

        系统订阅事件名称。只允许小写英文字符、数字、下划线、中划线，最大长度64，同一个帐号中创建的系统订阅和消息规则名唯一

        :return: The name of this Event.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Event.

        系统订阅事件名称。只允许小写英文字符、数字、下划线、中划线，最大长度64，同一个帐号中创建的系统订阅和消息规则名唯一

        :param name: The name of this Event.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this Event.

        系统订阅事件所属项目ID

        :return: The project_id of this Event.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Event.

        系统订阅事件所属项目ID

        :param project_id: The project_id of this Event.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this Event.

        创建时间

        :return: The created_at of this Event.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Event.

        创建时间

        :param created_at: The created_at of this Event.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Event.

        更新时间

        :return: The updated_at of this Event.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Event.

        更新时间

        :param updated_at: The updated_at of this Event.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def description(self):
        """Gets the description of this Event.

        描述，最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :return: The description of this Event.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Event.

        描述，最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :param description: The description of this Event.
        :type description: str
        """
        self._description = description

    @property
    def in_using(self):
        """Gets the in_using of this Event.

        是否启用系统订阅规则，默认为true（启用）

        :return: The in_using of this Event.
        :rtype: bool
        """
        return self._in_using

    @in_using.setter
    def in_using(self, in_using):
        """Sets the in_using of this Event.

        是否启用系统订阅规则，默认为true（启用）

        :param in_using: The in_using of this Event.
        :type in_using: bool
        """
        self._in_using = in_using

    @property
    def events(self):
        """Gets the events of this Event.

        系统订阅事件主题。每个主题由“{边缘资源}/{操作}”组成，多个主题使用逗号（,）进行分隔，支持如下主题： - edgeNode/offline：节点离线 - edgeNode/online：节点上线 - edgeNode/all：节点离线+节点上线 - deployment/created：容器应用创建 - deployment/updated：容器应用更新 - deployment/deleted：容器应用删除 - deployment/all：容器应用创建+更新+删除 - instance/created：应用实例创建 - instance/updated：应用实例更新 - instance/deleted：应用实例删除 - instance/all：应用实例创建+更新+删除

        :return: The events of this Event.
        :rtype: str
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Event.

        系统订阅事件主题。每个主题由“{边缘资源}/{操作}”组成，多个主题使用逗号（,）进行分隔，支持如下主题： - edgeNode/offline：节点离线 - edgeNode/online：节点上线 - edgeNode/all：节点离线+节点上线 - deployment/created：容器应用创建 - deployment/updated：容器应用更新 - deployment/deleted：容器应用删除 - deployment/all：容器应用创建+更新+删除 - instance/created：应用实例创建 - instance/updated：应用实例更新 - instance/deleted：应用实例删除 - instance/all：应用实例创建+更新+删除

        :param events: The events of this Event.
        :type events: str
        """
        self._events = events

    @property
    def target(self):
        """Gets the target of this Event.

        :return: The target of this Event.
        :rtype: :class:`huaweicloudsdkief.v1.EndpointObjResp`
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Event.

        :param target: The target of this Event.
        :type target: :class:`huaweicloudsdkief.v1.EndpointObjResp`
        """
        self._target = target

    @property
    def target_resource(self):
        """Gets the target_resource of this Event.

        目的端点资源属性

        :return: The target_resource of this Event.
        :rtype: dict(str, str)
        """
        return self._target_resource

    @target_resource.setter
    def target_resource(self, target_resource):
        """Sets the target_resource of this Event.

        目的端点资源属性

        :param target_resource: The target_resource of this Event.
        :type target_resource: dict(str, str)
        """
        self._target_resource = target_resource

    @property
    def success_messages(self):
        """Gets the success_messages of this Event.

        成功次数

        :return: The success_messages of this Event.
        :rtype: int
        """
        return self._success_messages

    @success_messages.setter
    def success_messages(self, success_messages):
        """Sets the success_messages of this Event.

        成功次数

        :param success_messages: The success_messages of this Event.
        :type success_messages: int
        """
        self._success_messages = success_messages

    @property
    def fail_messages(self):
        """Gets the fail_messages of this Event.

        失败次数

        :return: The fail_messages of this Event.
        :rtype: int
        """
        return self._fail_messages

    @fail_messages.setter
    def fail_messages(self, fail_messages):
        """Sets the fail_messages of this Event.

        失败次数

        :param fail_messages: The fail_messages of this Event.
        :type fail_messages: int
        """
        self._fail_messages = fail_messages

    @property
    def delete_at(self):
        """Gets the delete_at of this Event.

        删除时间

        :return: The delete_at of this Event.
        :rtype: int
        """
        return self._delete_at

    @delete_at.setter
    def delete_at(self, delete_at):
        """Sets the delete_at of this Event.

        删除时间

        :param delete_at: The delete_at of this Event.
        :type delete_at: int
        """
        self._delete_at = delete_at

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
