# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterEventResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'cluster_name': 'str',
        'cluster_id': 'str',
        'event_name': 'str',
        'event_class_id': 'str',
        'event_id': 'str',
        'event_type': 'int',
        'event_content': 'str',
        'handle_status': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'policy_name': 'str',
        'policy_id': 'str',
        'resource_info': 'ClusterEventResourceResponseInfo'
    }

    attribute_map = {
        'action': 'action',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'event_name': 'event_name',
        'event_class_id': 'event_class_id',
        'event_id': 'event_id',
        'event_type': 'event_type',
        'event_content': 'event_content',
        'handle_status': 'handle_status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'policy_name': 'policy_name',
        'policy_id': 'policy_id',
        'resource_info': 'resource_info'
    }

    def __init__(self, action=None, cluster_name=None, cluster_id=None, event_name=None, event_class_id=None, event_id=None, event_type=None, event_content=None, handle_status=None, create_time=None, update_time=None, project_id=None, enterprise_project_id=None, policy_name=None, policy_id=None, resource_info=None):
        r"""ClusterEventResponseInfo

        The model defined in huaweicloud sdk

        :param action: 阻断动作
        :type action: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群Id
        :type cluster_id: str
        :param event_name: 事件名称
        :type event_name: str
        :param event_class_id: 事件唯一标识
        :type event_class_id: str
        :param event_id: 事件id
        :type event_id: str
        :param event_type: 事件类型
        :type event_type: int
        :param event_content: 事件内容
        :type event_content: str
        :param handle_status: 处理状态，包含如下:   - unhandled：未处理   - handled：已处理
        :type handle_status: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param project_id: 项目ID
        :type project_id: str
        :param enterprise_project_id: 企业ID
        :type enterprise_project_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_id: 策略ID
        :type policy_id: str
        :param resource_info: 
        :type resource_info: :class:`huaweicloudsdkhss.v5.ClusterEventResourceResponseInfo`
        """
        
        

        self._action = None
        self._cluster_name = None
        self._cluster_id = None
        self._event_name = None
        self._event_class_id = None
        self._event_id = None
        self._event_type = None
        self._event_content = None
        self._handle_status = None
        self._create_time = None
        self._update_time = None
        self._project_id = None
        self._enterprise_project_id = None
        self._policy_name = None
        self._policy_id = None
        self._resource_info = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if event_name is not None:
            self.event_name = event_name
        if event_class_id is not None:
            self.event_class_id = event_class_id
        if event_id is not None:
            self.event_id = event_id
        if event_type is not None:
            self.event_type = event_type
        if event_content is not None:
            self.event_content = event_content
        if handle_status is not None:
            self.handle_status = handle_status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_id is not None:
            self.policy_id = policy_id
        if resource_info is not None:
            self.resource_info = resource_info

    @property
    def action(self):
        r"""Gets the action of this ClusterEventResponseInfo.

        阻断动作

        :return: The action of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ClusterEventResponseInfo.

        阻断动作

        :param action: The action of this ClusterEventResponseInfo.
        :type action: str
        """
        self._action = action

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterEventResponseInfo.

        集群名称

        :return: The cluster_name of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterEventResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ClusterEventResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterEventResponseInfo.

        集群Id

        :return: The cluster_id of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterEventResponseInfo.

        集群Id

        :param cluster_id: The cluster_id of this ClusterEventResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def event_name(self):
        r"""Gets the event_name of this ClusterEventResponseInfo.

        事件名称

        :return: The event_name of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ClusterEventResponseInfo.

        事件名称

        :param event_name: The event_name of this ClusterEventResponseInfo.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_class_id(self):
        r"""Gets the event_class_id of this ClusterEventResponseInfo.

        事件唯一标识

        :return: The event_class_id of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._event_class_id

    @event_class_id.setter
    def event_class_id(self, event_class_id):
        r"""Sets the event_class_id of this ClusterEventResponseInfo.

        事件唯一标识

        :param event_class_id: The event_class_id of this ClusterEventResponseInfo.
        :type event_class_id: str
        """
        self._event_class_id = event_class_id

    @property
    def event_id(self):
        r"""Gets the event_id of this ClusterEventResponseInfo.

        事件id

        :return: The event_id of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this ClusterEventResponseInfo.

        事件id

        :param event_id: The event_id of this ClusterEventResponseInfo.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_type(self):
        r"""Gets the event_type of this ClusterEventResponseInfo.

        事件类型

        :return: The event_type of this ClusterEventResponseInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ClusterEventResponseInfo.

        事件类型

        :param event_type: The event_type of this ClusterEventResponseInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def event_content(self):
        r"""Gets the event_content of this ClusterEventResponseInfo.

        事件内容

        :return: The event_content of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._event_content

    @event_content.setter
    def event_content(self, event_content):
        r"""Sets the event_content of this ClusterEventResponseInfo.

        事件内容

        :param event_content: The event_content of this ClusterEventResponseInfo.
        :type event_content: str
        """
        self._event_content = event_content

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ClusterEventResponseInfo.

        处理状态，包含如下:   - unhandled：未处理   - handled：已处理

        :return: The handle_status of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ClusterEventResponseInfo.

        处理状态，包含如下:   - unhandled：未处理   - handled：已处理

        :param handle_status: The handle_status of this ClusterEventResponseInfo.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def create_time(self):
        r"""Gets the create_time of this ClusterEventResponseInfo.

        创建时间

        :return: The create_time of this ClusterEventResponseInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ClusterEventResponseInfo.

        创建时间

        :param create_time: The create_time of this ClusterEventResponseInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ClusterEventResponseInfo.

        更新时间

        :return: The update_time of this ClusterEventResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ClusterEventResponseInfo.

        更新时间

        :param update_time: The update_time of this ClusterEventResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def project_id(self):
        r"""Gets the project_id of this ClusterEventResponseInfo.

        项目ID

        :return: The project_id of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ClusterEventResponseInfo.

        项目ID

        :param project_id: The project_id of this ClusterEventResponseInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ClusterEventResponseInfo.

        企业ID

        :return: The enterprise_project_id of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ClusterEventResponseInfo.

        企业ID

        :param enterprise_project_id: The enterprise_project_id of this ClusterEventResponseInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ClusterEventResponseInfo.

        策略名称

        :return: The policy_name of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ClusterEventResponseInfo.

        策略名称

        :param policy_name: The policy_name of this ClusterEventResponseInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ClusterEventResponseInfo.

        策略ID

        :return: The policy_id of this ClusterEventResponseInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ClusterEventResponseInfo.

        策略ID

        :param policy_id: The policy_id of this ClusterEventResponseInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def resource_info(self):
        r"""Gets the resource_info of this ClusterEventResponseInfo.

        :return: The resource_info of this ClusterEventResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ClusterEventResourceResponseInfo`
        """
        return self._resource_info

    @resource_info.setter
    def resource_info(self, resource_info):
        r"""Sets the resource_info of this ClusterEventResponseInfo.

        :param resource_info: The resource_info of this ClusterEventResponseInfo.
        :type resource_info: :class:`huaweicloudsdkhss.v5.ClusterEventResourceResponseInfo`
        """
        self._resource_info = resource_info

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
        if not isinstance(other, ClusterEventResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
