# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'state': 'list[str]',
        'type': 'list[str]',
        'id': 'str',
        'node_name': 'str',
        'pool_name': 'str',
        'publish_start_time': 'str',
        'publish_end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'workspace_id': 'workspaceId',
        'state': 'state',
        'type': 'type',
        'id': 'id',
        'node_name': 'nodeName',
        'pool_name': 'poolName',
        'publish_start_time': 'publishStartTime',
        'publish_end_time': 'publishEndTime',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, workspace_id=None, state=None, type=None, id=None, node_name=None, pool_name=None, publish_start_time=None, publish_end_time=None, offset=None, limit=None):
        r"""ListScheduledEventsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间ID，默认值为0，取值于查询workspaces列表的接口的id字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type workspace_id: str
        :param state: **参数解释**：事件状态。 **约束限制**：不涉及。 **取值范围**：可选择值如下： - inquiring: 待授权, - scheduled: 待执行 - executing: 执行中 - completed: 执行成功 - failed: 执行失败 - canceled: 取消 **默认取值**：不涉及。
        :type state: list[str]
        :param type: **参数解释**：事件类型。 **约束限制**：不涉及。 **取值范围**：可选择值如下： - system-maintenance：系统维护 - localdisk-recovery：本地盘恢复 - node_reboot：节点重启 - operation-request：运维授权 - node_maintenance：超节点维护 - node_redeploy：超节点重部署 - node_localdisk_recovery 超节点本地盘恢复 **默认取值**：不涉及。
        :type type: list[str]
        :param id: **参数解释**：计划事件ID，取值查询计划事件列表接口的event_id字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type id: str
        :param node_name: **参数解释**：节点名称，取值自节点详情的metadata.name字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type node_name: str
        :param pool_name: **参数解释**：资源池名称, lite-cluster、standard才具有，取值自资源池详情的metadata.name字段。查询指定standard cluster和lite cluster下节点的计划事件时可传递该参数。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type pool_name: str
        :param publish_start_time: **参数解释**：事件发布开始时间,按照时间范围过滤。 **约束限制**：按照ISO8601标准表示，并使用UTC +0时间，格式为yyyy-MM-ddTHH:mm:ssZ。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type publish_start_time: str
        :param publish_end_time: **参数解释**：事件发布结束时间,按照时间范围过滤。 **约束限制**：按照ISO8601标准表示，并使用UTC +0时间，格式为yyyy-MM-ddTHH:mm:ssZ。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type publish_end_time: str
        :param offset: **参数解释**：偏移量,表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：[0,1000000000]。 **默认取值**：0。
        :type offset: int
        :param limit: **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：[1,100]。 **默认取值**：100。
        :type limit: int
        """
        
        

        self._workspace_id = None
        self._state = None
        self._type = None
        self._id = None
        self._node_name = None
        self._pool_name = None
        self._publish_start_time = None
        self._publish_end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if node_name is not None:
            self.node_name = node_name
        if pool_name is not None:
            self.pool_name = pool_name
        if publish_start_time is not None:
            self.publish_start_time = publish_start_time
        if publish_end_time is not None:
            self.publish_end_time = publish_end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListScheduledEventsRequest.

        **参数解释**：工作空间ID，默认值为0，取值于查询workspaces列表的接口的id字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The workspace_id of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListScheduledEventsRequest.

        **参数解释**：工作空间ID，默认值为0，取值于查询workspaces列表的接口的id字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListScheduledEventsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def state(self):
        r"""Gets the state of this ListScheduledEventsRequest.

        **参数解释**：事件状态。 **约束限制**：不涉及。 **取值范围**：可选择值如下： - inquiring: 待授权, - scheduled: 待执行 - executing: 执行中 - completed: 执行成功 - failed: 执行失败 - canceled: 取消 **默认取值**：不涉及。

        :return: The state of this ListScheduledEventsRequest.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListScheduledEventsRequest.

        **参数解释**：事件状态。 **约束限制**：不涉及。 **取值范围**：可选择值如下： - inquiring: 待授权, - scheduled: 待执行 - executing: 执行中 - completed: 执行成功 - failed: 执行失败 - canceled: 取消 **默认取值**：不涉及。

        :param state: The state of this ListScheduledEventsRequest.
        :type state: list[str]
        """
        self._state = state

    @property
    def type(self):
        r"""Gets the type of this ListScheduledEventsRequest.

        **参数解释**：事件类型。 **约束限制**：不涉及。 **取值范围**：可选择值如下： - system-maintenance：系统维护 - localdisk-recovery：本地盘恢复 - node_reboot：节点重启 - operation-request：运维授权 - node_maintenance：超节点维护 - node_redeploy：超节点重部署 - node_localdisk_recovery 超节点本地盘恢复 **默认取值**：不涉及。

        :return: The type of this ListScheduledEventsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListScheduledEventsRequest.

        **参数解释**：事件类型。 **约束限制**：不涉及。 **取值范围**：可选择值如下： - system-maintenance：系统维护 - localdisk-recovery：本地盘恢复 - node_reboot：节点重启 - operation-request：运维授权 - node_maintenance：超节点维护 - node_redeploy：超节点重部署 - node_localdisk_recovery 超节点本地盘恢复 **默认取值**：不涉及。

        :param type: The type of this ListScheduledEventsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def id(self):
        r"""Gets the id of this ListScheduledEventsRequest.

        **参数解释**：计划事件ID，取值查询计划事件列表接口的event_id字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The id of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListScheduledEventsRequest.

        **参数解释**：计划事件ID，取值查询计划事件列表接口的event_id字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param id: The id of this ListScheduledEventsRequest.
        :type id: str
        """
        self._id = id

    @property
    def node_name(self):
        r"""Gets the node_name of this ListScheduledEventsRequest.

        **参数解释**：节点名称，取值自节点详情的metadata.name字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The node_name of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ListScheduledEventsRequest.

        **参数解释**：节点名称，取值自节点详情的metadata.name字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param node_name: The node_name of this ListScheduledEventsRequest.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def pool_name(self):
        r"""Gets the pool_name of this ListScheduledEventsRequest.

        **参数解释**：资源池名称, lite-cluster、standard才具有，取值自资源池详情的metadata.name字段。查询指定standard cluster和lite cluster下节点的计划事件时可传递该参数。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The pool_name of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this ListScheduledEventsRequest.

        **参数解释**：资源池名称, lite-cluster、standard才具有，取值自资源池详情的metadata.name字段。查询指定standard cluster和lite cluster下节点的计划事件时可传递该参数。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param pool_name: The pool_name of this ListScheduledEventsRequest.
        :type pool_name: str
        """
        self._pool_name = pool_name

    @property
    def publish_start_time(self):
        r"""Gets the publish_start_time of this ListScheduledEventsRequest.

        **参数解释**：事件发布开始时间,按照时间范围过滤。 **约束限制**：按照ISO8601标准表示，并使用UTC +0时间，格式为yyyy-MM-ddTHH:mm:ssZ。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The publish_start_time of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, publish_start_time):
        r"""Sets the publish_start_time of this ListScheduledEventsRequest.

        **参数解释**：事件发布开始时间,按照时间范围过滤。 **约束限制**：按照ISO8601标准表示，并使用UTC +0时间，格式为yyyy-MM-ddTHH:mm:ssZ。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param publish_start_time: The publish_start_time of this ListScheduledEventsRequest.
        :type publish_start_time: str
        """
        self._publish_start_time = publish_start_time

    @property
    def publish_end_time(self):
        r"""Gets the publish_end_time of this ListScheduledEventsRequest.

        **参数解释**：事件发布结束时间,按照时间范围过滤。 **约束限制**：按照ISO8601标准表示，并使用UTC +0时间，格式为yyyy-MM-ddTHH:mm:ssZ。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The publish_end_time of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, publish_end_time):
        r"""Sets the publish_end_time of this ListScheduledEventsRequest.

        **参数解释**：事件发布结束时间,按照时间范围过滤。 **约束限制**：按照ISO8601标准表示，并使用UTC +0时间，格式为yyyy-MM-ddTHH:mm:ssZ。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param publish_end_time: The publish_end_time of this ListScheduledEventsRequest.
        :type publish_end_time: str
        """
        self._publish_end_time = publish_end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListScheduledEventsRequest.

        **参数解释**：偏移量,表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：[0,1000000000]。 **默认取值**：0。

        :return: The offset of this ListScheduledEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScheduledEventsRequest.

        **参数解释**：偏移量,表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：[0,1000000000]。 **默认取值**：0。

        :param offset: The offset of this ListScheduledEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduledEventsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：[1,100]。 **默认取值**：100。

        :return: The limit of this ListScheduledEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduledEventsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：[1,100]。 **默认取值**：100。

        :param limit: The limit of this ListScheduledEventsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListScheduledEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
