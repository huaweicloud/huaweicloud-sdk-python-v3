# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopicsWithAssociatedResourcesItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'name': 'str',
        'display_name': 'str',
        'push_policy': 'int',
        'enterprise_project_id': 'str',
        'topic_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'tags': 'list[ResourceTag]',
        'attributes': 'TopicAccessPolicyAttribute',
        'logtanks': 'list[LogtankItem]'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'name': 'name',
        'display_name': 'display_name',
        'push_policy': 'push_policy',
        'enterprise_project_id': 'enterprise_project_id',
        'topic_id': 'topic_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'tags': 'tags',
        'attributes': 'attributes',
        'logtanks': 'logtanks'
    }

    def __init__(self, topic_urn=None, name=None, display_name=None, push_policy=None, enterprise_project_id=None, topic_id=None, create_time=None, update_time=None, tags=None, attributes=None, logtanks=None):
        r"""ListTopicsWithAssociatedResourcesItem

        The model defined in huaweicloud sdk

        :param topic_urn: Topic的唯一的资源标识。
        :type topic_urn: str
        :param name: 创建topic的名字。
        :type name: str
        :param display_name: Topic的显示名，推送邮件消息时，作为邮件发件人显示。
        :type display_name: str
        :param push_policy: 消息推送的策略，该属性目前不支持修改，后续将支持修改。0表示发送失败，保留到失败队列，1表示直接丢弃发送失败的消息。
        :type push_policy: int
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param topic_id: 主题ID。
        :type topic_id: str
        :param create_time: 创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type create_time: str
        :param update_time: 更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type update_time: str
        :param tags: 资源标签列表。
        :type tags: list[:class:`huaweicloudsdksmn.v2.ResourceTag`]
        :param attributes: 
        :type attributes: :class:`huaweicloudsdksmn.v2.TopicAccessPolicyAttribute`
        :param logtanks: 云日志信息列表。
        :type logtanks: list[:class:`huaweicloudsdksmn.v2.LogtankItem`]
        """
        
        

        self._topic_urn = None
        self._name = None
        self._display_name = None
        self._push_policy = None
        self._enterprise_project_id = None
        self._topic_id = None
        self._create_time = None
        self._update_time = None
        self._tags = None
        self._attributes = None
        self._logtanks = None
        self.discriminator = None

        self.topic_urn = topic_urn
        self.name = name
        self.display_name = display_name
        self.push_policy = push_policy
        self.enterprise_project_id = enterprise_project_id
        self.topic_id = topic_id
        self.create_time = create_time
        self.update_time = update_time
        self.tags = tags
        self.attributes = attributes
        self.logtanks = logtanks

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ListTopicsWithAssociatedResourcesItem.

        Topic的唯一的资源标识。

        :return: The topic_urn of this ListTopicsWithAssociatedResourcesItem.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ListTopicsWithAssociatedResourcesItem.

        Topic的唯一的资源标识。

        :param topic_urn: The topic_urn of this ListTopicsWithAssociatedResourcesItem.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def name(self):
        r"""Gets the name of this ListTopicsWithAssociatedResourcesItem.

        创建topic的名字。

        :return: The name of this ListTopicsWithAssociatedResourcesItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTopicsWithAssociatedResourcesItem.

        创建topic的名字。

        :param name: The name of this ListTopicsWithAssociatedResourcesItem.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this ListTopicsWithAssociatedResourcesItem.

        Topic的显示名，推送邮件消息时，作为邮件发件人显示。

        :return: The display_name of this ListTopicsWithAssociatedResourcesItem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ListTopicsWithAssociatedResourcesItem.

        Topic的显示名，推送邮件消息时，作为邮件发件人显示。

        :param display_name: The display_name of this ListTopicsWithAssociatedResourcesItem.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def push_policy(self):
        r"""Gets the push_policy of this ListTopicsWithAssociatedResourcesItem.

        消息推送的策略，该属性目前不支持修改，后续将支持修改。0表示发送失败，保留到失败队列，1表示直接丢弃发送失败的消息。

        :return: The push_policy of this ListTopicsWithAssociatedResourcesItem.
        :rtype: int
        """
        return self._push_policy

    @push_policy.setter
    def push_policy(self, push_policy):
        r"""Sets the push_policy of this ListTopicsWithAssociatedResourcesItem.

        消息推送的策略，该属性目前不支持修改，后续将支持修改。0表示发送失败，保留到失败队列，1表示直接丢弃发送失败的消息。

        :param push_policy: The push_policy of this ListTopicsWithAssociatedResourcesItem.
        :type push_policy: int
        """
        self._push_policy = push_policy

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListTopicsWithAssociatedResourcesItem.

        企业项目ID。

        :return: The enterprise_project_id of this ListTopicsWithAssociatedResourcesItem.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListTopicsWithAssociatedResourcesItem.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListTopicsWithAssociatedResourcesItem.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def topic_id(self):
        r"""Gets the topic_id of this ListTopicsWithAssociatedResourcesItem.

        主题ID。

        :return: The topic_id of this ListTopicsWithAssociatedResourcesItem.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        r"""Sets the topic_id of this ListTopicsWithAssociatedResourcesItem.

        主题ID。

        :param topic_id: The topic_id of this ListTopicsWithAssociatedResourcesItem.
        :type topic_id: str
        """
        self._topic_id = topic_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ListTopicsWithAssociatedResourcesItem.

        创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The create_time of this ListTopicsWithAssociatedResourcesItem.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListTopicsWithAssociatedResourcesItem.

        创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param create_time: The create_time of this ListTopicsWithAssociatedResourcesItem.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListTopicsWithAssociatedResourcesItem.

        更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The update_time of this ListTopicsWithAssociatedResourcesItem.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListTopicsWithAssociatedResourcesItem.

        更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param update_time: The update_time of this ListTopicsWithAssociatedResourcesItem.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def tags(self):
        r"""Gets the tags of this ListTopicsWithAssociatedResourcesItem.

        资源标签列表。

        :return: The tags of this ListTopicsWithAssociatedResourcesItem.
        :rtype: list[:class:`huaweicloudsdksmn.v2.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListTopicsWithAssociatedResourcesItem.

        资源标签列表。

        :param tags: The tags of this ListTopicsWithAssociatedResourcesItem.
        :type tags: list[:class:`huaweicloudsdksmn.v2.ResourceTag`]
        """
        self._tags = tags

    @property
    def attributes(self):
        r"""Gets the attributes of this ListTopicsWithAssociatedResourcesItem.

        :return: The attributes of this ListTopicsWithAssociatedResourcesItem.
        :rtype: :class:`huaweicloudsdksmn.v2.TopicAccessPolicyAttribute`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this ListTopicsWithAssociatedResourcesItem.

        :param attributes: The attributes of this ListTopicsWithAssociatedResourcesItem.
        :type attributes: :class:`huaweicloudsdksmn.v2.TopicAccessPolicyAttribute`
        """
        self._attributes = attributes

    @property
    def logtanks(self):
        r"""Gets the logtanks of this ListTopicsWithAssociatedResourcesItem.

        云日志信息列表。

        :return: The logtanks of this ListTopicsWithAssociatedResourcesItem.
        :rtype: list[:class:`huaweicloudsdksmn.v2.LogtankItem`]
        """
        return self._logtanks

    @logtanks.setter
    def logtanks(self, logtanks):
        r"""Sets the logtanks of this ListTopicsWithAssociatedResourcesItem.

        云日志信息列表。

        :param logtanks: The logtanks of this ListTopicsWithAssociatedResourcesItem.
        :type logtanks: list[:class:`huaweicloudsdksmn.v2.LogtankItem`]
        """
        self._logtanks = logtanks

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
        if not isinstance(other, ListTopicsWithAssociatedResourcesItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
