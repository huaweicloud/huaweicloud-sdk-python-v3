# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventCreateDetail:

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
        'description': 'str',
        'events': 'str',
        'target': 'str',
        'target_resource': 'EndpointResource'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'events': 'events',
        'target': 'target',
        'target_resource': 'target_resource'
    }

    def __init__(self, name=None, description=None, events=None, target=None, target_resource=None):
        """EventCreateDetail

        The model defined in huaweicloud sdk

        :param name: 系统订阅名称。只允许小写英文字符、数字、下划线、中划线，最大长度64，同一个帐号中创建的系统订阅和消息规则名唯一
        :type name: str
        :param description: 描述。最大长度255，不允许^~#$%&amp;*&lt;&gt;()[]{}&#39;\&quot;\\
        :type description: str
        :param events: 系统订阅主题。每个主题由“{边缘资源}/{操作}”组成，多个主题使用逗号（,）进行分隔，支持如下主题： - edgeNode/offline：节点离线 - edgeNode/online：节点上线 - edgeNode/all：节点离线+节点上线 - deployment/created：容器应用创建 - deployment/updated：容器应用更新 - deployment/deleted：容器应用删除 - deployment/all：容器应用创建+更新+删除 - instance/created：应用实例创建 - instance/updated：应用实例更新 - instance/deleted：应用实例删除 - instance/all：应用实例创建+更新+删除
        :type events: str
        :param target: 目的端点ID
        :type target: str
        :param target_resource: 
        :type target_resource: :class:`huaweicloudsdkief.v1.EndpointResource`
        """
        
        

        self._name = None
        self._description = None
        self._events = None
        self._target = None
        self._target_resource = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if events is not None:
            self.events = events
        if target is not None:
            self.target = target
        if target_resource is not None:
            self.target_resource = target_resource

    @property
    def name(self):
        """Gets the name of this EventCreateDetail.

        系统订阅名称。只允许小写英文字符、数字、下划线、中划线，最大长度64，同一个帐号中创建的系统订阅和消息规则名唯一

        :return: The name of this EventCreateDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventCreateDetail.

        系统订阅名称。只允许小写英文字符、数字、下划线、中划线，最大长度64，同一个帐号中创建的系统订阅和消息规则名唯一

        :param name: The name of this EventCreateDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EventCreateDetail.

        描述。最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :return: The description of this EventCreateDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventCreateDetail.

        描述。最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :param description: The description of this EventCreateDetail.
        :type description: str
        """
        self._description = description

    @property
    def events(self):
        """Gets the events of this EventCreateDetail.

        系统订阅主题。每个主题由“{边缘资源}/{操作}”组成，多个主题使用逗号（,）进行分隔，支持如下主题： - edgeNode/offline：节点离线 - edgeNode/online：节点上线 - edgeNode/all：节点离线+节点上线 - deployment/created：容器应用创建 - deployment/updated：容器应用更新 - deployment/deleted：容器应用删除 - deployment/all：容器应用创建+更新+删除 - instance/created：应用实例创建 - instance/updated：应用实例更新 - instance/deleted：应用实例删除 - instance/all：应用实例创建+更新+删除

        :return: The events of this EventCreateDetail.
        :rtype: str
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this EventCreateDetail.

        系统订阅主题。每个主题由“{边缘资源}/{操作}”组成，多个主题使用逗号（,）进行分隔，支持如下主题： - edgeNode/offline：节点离线 - edgeNode/online：节点上线 - edgeNode/all：节点离线+节点上线 - deployment/created：容器应用创建 - deployment/updated：容器应用更新 - deployment/deleted：容器应用删除 - deployment/all：容器应用创建+更新+删除 - instance/created：应用实例创建 - instance/updated：应用实例更新 - instance/deleted：应用实例删除 - instance/all：应用实例创建+更新+删除

        :param events: The events of this EventCreateDetail.
        :type events: str
        """
        self._events = events

    @property
    def target(self):
        """Gets the target of this EventCreateDetail.

        目的端点ID

        :return: The target of this EventCreateDetail.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this EventCreateDetail.

        目的端点ID

        :param target: The target of this EventCreateDetail.
        :type target: str
        """
        self._target = target

    @property
    def target_resource(self):
        """Gets the target_resource of this EventCreateDetail.

        :return: The target_resource of this EventCreateDetail.
        :rtype: :class:`huaweicloudsdkief.v1.EndpointResource`
        """
        return self._target_resource

    @target_resource.setter
    def target_resource(self, target_resource):
        """Sets the target_resource of this EventCreateDetail.

        :param target_resource: The target_resource of this EventCreateDetail.
        :type target_resource: :class:`huaweicloudsdkief.v1.EndpointResource`
        """
        self._target_resource = target_resource

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
        if not isinstance(other, EventCreateDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
