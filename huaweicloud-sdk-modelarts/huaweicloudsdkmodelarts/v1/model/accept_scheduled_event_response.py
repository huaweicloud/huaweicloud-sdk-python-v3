# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AcceptScheduledEventResponse(SdkResponse):

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
        'catalog': 'str',
        'type': 'str',
        'description': 'str',
        'state': 'str',
        'instance_type': 'str',
        'instance_id': 'str',
        'node_name': 'str',
        'pool_name': 'str',
        'pool_display_name': 'str',
        'publish_time': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'not_before': 'str',
        'probe_msg': 'str',
        'redeploy_type': 'list[str]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'catalog': 'catalog',
        'type': 'type',
        'description': 'description',
        'state': 'state',
        'instance_type': 'instanceType',
        'instance_id': 'instanceId',
        'node_name': 'nodeName',
        'pool_name': 'poolName',
        'pool_display_name': 'poolDisplayName',
        'publish_time': 'publishTime',
        'start_time': 'startTime',
        'finish_time': 'finishTime',
        'not_before': 'notBefore',
        'probe_msg': 'probeMsg',
        'redeploy_type': 'redeployType',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, id=None, catalog=None, type=None, description=None, state=None, instance_type=None, instance_id=None, node_name=None, pool_name=None, pool_display_name=None, publish_time=None, start_time=None, finish_time=None, not_before=None, probe_msg=None, redeploy_type=None, x_request_id=None):
        r"""AcceptScheduledEventResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：计划事件ID，取值查询计划事件列表接口的event_id字段。 系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63。 **取值范围**：不涉及。
        :type id: str
        :param catalog: **参数解释**：事件分类。 **取值范围**：可选值如下： - hardware：硬件维修。 - software：软件维修。
        :type catalog: str
        :param type: **参数解释**：事件类型。 **取值范围**：可选值如下： - system-maintenance：系统维护 - localdisk-recovery：本地盘恢复 - node_reboot：节点重启 - operation-request：运维授权 - node_maintenance：超节点维护 - node_redeploy：超节点重部署 - node_localdisk_recovery 超节点本地盘恢复。
        :type type: str
        :param description: **参数解释**：对计划事件的描述信息。系统自动生成。 **取值范围**：不涉及。
        :type description: str
        :param state: **参数解释**：事件状态。 **取值范围**：可选择值如下： - inquiring: 待授权, - scheduled: 待执行, - executing: 执行中, - completed: 执行成功 - failed: 执行失败 - canceled: 取消
        :type state: str
        :param instance_type: **参数解释**：节点类型归属。 **取值范围**可选择值如下： - devserver：lite-server节点 - lite-cluster lite池 - standard 标准池
        :type instance_type: str
        :param instance_id: **参数解释**：服务器ID。计算服务系统自动生成的实例ID，长度小于63。 **取值范围**：不涉及。
        :type instance_id: str
        :param node_name: **参数解释**：节点名称，取值自节点详情的metadata.name字段。系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。
        :type node_name: str
        :param pool_name: **参数解释**：资源池名称, lite-cluster、standard才具有，取值自资源池详情的metadata.name字段。系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。
        :type pool_name: str
        :param pool_display_name: **参数解释**：资源池对外显示的名称, lite-cluster、standard才具有，取值自资源池详情的metadata.name字段。只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为[36-63]个字符。 **取值范围**：不涉及。
        :type pool_display_name: str
        :param publish_time: **参数解释**：事件发布时间。 **约束限制**：格式为UTC时间字符串：2025-09-15T07:02:30Z。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type publish_time: str
        :param start_time: **参数解释**：事件开始时间。 **约束限制**：格式为UTC时间字符串：2025-09-15T07:02:30Z。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type start_time: str
        :param finish_time: **参数解释**：事件完成时间。 **约束限制**：格式为UTC时间字符串：2025-09-15T07:02:30Z。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type finish_time: str
        :param not_before: **参数解释**：事件计划执行开始时间，格式为UTC时间字符串：2025-09-15T07:02:30Z。 **约束限制**：大于当前时间。 **取值范围**：不涉及。 **默认取值**：不填表示立即执行。
        :type not_before: str
        :param probe_msg: **参数解释**：提示信息。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type probe_msg: str
        :param redeploy_type: **参数解释**：节点的重部署类型。 **约束限制**：不涉及。 **取值范围**：可选值如下：- HARD：表示支持强制重部署, - SOFT：表示支持重部署 **默认取值**：不涉及。
        :type redeploy_type: list[str]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._id = None
        self._catalog = None
        self._type = None
        self._description = None
        self._state = None
        self._instance_type = None
        self._instance_id = None
        self._node_name = None
        self._pool_name = None
        self._pool_display_name = None
        self._publish_time = None
        self._start_time = None
        self._finish_time = None
        self._not_before = None
        self._probe_msg = None
        self._redeploy_type = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if catalog is not None:
            self.catalog = catalog
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if state is not None:
            self.state = state
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_id is not None:
            self.instance_id = instance_id
        if node_name is not None:
            self.node_name = node_name
        if pool_name is not None:
            self.pool_name = pool_name
        if pool_display_name is not None:
            self.pool_display_name = pool_display_name
        if publish_time is not None:
            self.publish_time = publish_time
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if not_before is not None:
            self.not_before = not_before
        if probe_msg is not None:
            self.probe_msg = probe_msg
        if redeploy_type is not None:
            self.redeploy_type = redeploy_type
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this AcceptScheduledEventResponse.

        **参数解释**：计划事件ID，取值查询计划事件列表接口的event_id字段。 系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63。 **取值范围**：不涉及。

        :return: The id of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AcceptScheduledEventResponse.

        **参数解释**：计划事件ID，取值查询计划事件列表接口的event_id字段。 系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63。 **取值范围**：不涉及。

        :param id: The id of this AcceptScheduledEventResponse.
        :type id: str
        """
        self._id = id

    @property
    def catalog(self):
        r"""Gets the catalog of this AcceptScheduledEventResponse.

        **参数解释**：事件分类。 **取值范围**：可选值如下： - hardware：硬件维修。 - software：软件维修。

        :return: The catalog of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        r"""Sets the catalog of this AcceptScheduledEventResponse.

        **参数解释**：事件分类。 **取值范围**：可选值如下： - hardware：硬件维修。 - software：软件维修。

        :param catalog: The catalog of this AcceptScheduledEventResponse.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def type(self):
        r"""Gets the type of this AcceptScheduledEventResponse.

        **参数解释**：事件类型。 **取值范围**：可选值如下： - system-maintenance：系统维护 - localdisk-recovery：本地盘恢复 - node_reboot：节点重启 - operation-request：运维授权 - node_maintenance：超节点维护 - node_redeploy：超节点重部署 - node_localdisk_recovery 超节点本地盘恢复。

        :return: The type of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AcceptScheduledEventResponse.

        **参数解释**：事件类型。 **取值范围**：可选值如下： - system-maintenance：系统维护 - localdisk-recovery：本地盘恢复 - node_reboot：节点重启 - operation-request：运维授权 - node_maintenance：超节点维护 - node_redeploy：超节点重部署 - node_localdisk_recovery 超节点本地盘恢复。

        :param type: The type of this AcceptScheduledEventResponse.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this AcceptScheduledEventResponse.

        **参数解释**：对计划事件的描述信息。系统自动生成。 **取值范围**：不涉及。

        :return: The description of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AcceptScheduledEventResponse.

        **参数解释**：对计划事件的描述信息。系统自动生成。 **取值范围**：不涉及。

        :param description: The description of this AcceptScheduledEventResponse.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        r"""Gets the state of this AcceptScheduledEventResponse.

        **参数解释**：事件状态。 **取值范围**：可选择值如下： - inquiring: 待授权, - scheduled: 待执行, - executing: 执行中, - completed: 执行成功 - failed: 执行失败 - canceled: 取消

        :return: The state of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this AcceptScheduledEventResponse.

        **参数解释**：事件状态。 **取值范围**：可选择值如下： - inquiring: 待授权, - scheduled: 待执行, - executing: 执行中, - completed: 执行成功 - failed: 执行失败 - canceled: 取消

        :param state: The state of this AcceptScheduledEventResponse.
        :type state: str
        """
        self._state = state

    @property
    def instance_type(self):
        r"""Gets the instance_type of this AcceptScheduledEventResponse.

        **参数解释**：节点类型归属。 **取值范围**可选择值如下： - devserver：lite-server节点 - lite-cluster lite池 - standard 标准池

        :return: The instance_type of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this AcceptScheduledEventResponse.

        **参数解释**：节点类型归属。 **取值范围**可选择值如下： - devserver：lite-server节点 - lite-cluster lite池 - standard 标准池

        :param instance_type: The instance_type of this AcceptScheduledEventResponse.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AcceptScheduledEventResponse.

        **参数解释**：服务器ID。计算服务系统自动生成的实例ID，长度小于63。 **取值范围**：不涉及。

        :return: The instance_id of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AcceptScheduledEventResponse.

        **参数解释**：服务器ID。计算服务系统自动生成的实例ID，长度小于63。 **取值范围**：不涉及。

        :param instance_id: The instance_id of this AcceptScheduledEventResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_name(self):
        r"""Gets the node_name of this AcceptScheduledEventResponse.

        **参数解释**：节点名称，取值自节点详情的metadata.name字段。系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。

        :return: The node_name of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this AcceptScheduledEventResponse.

        **参数解释**：节点名称，取值自节点详情的metadata.name字段。系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。

        :param node_name: The node_name of this AcceptScheduledEventResponse.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def pool_name(self):
        r"""Gets the pool_name of this AcceptScheduledEventResponse.

        **参数解释**：资源池名称, lite-cluster、standard才具有，取值自资源池详情的metadata.name字段。系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。

        :return: The pool_name of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this AcceptScheduledEventResponse.

        **参数解释**：资源池名称, lite-cluster、standard才具有，取值自资源池详情的metadata.name字段。系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，小于63个字符。 **取值范围**：不涉及。

        :param pool_name: The pool_name of this AcceptScheduledEventResponse.
        :type pool_name: str
        """
        self._pool_name = pool_name

    @property
    def pool_display_name(self):
        r"""Gets the pool_display_name of this AcceptScheduledEventResponse.

        **参数解释**：资源池对外显示的名称, lite-cluster、standard才具有，取值自资源池详情的metadata.name字段。只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为[36-63]个字符。 **取值范围**：不涉及。

        :return: The pool_display_name of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._pool_display_name

    @pool_display_name.setter
    def pool_display_name(self, pool_display_name):
        r"""Sets the pool_display_name of this AcceptScheduledEventResponse.

        **参数解释**：资源池对外显示的名称, lite-cluster、standard才具有，取值自资源池详情的metadata.name字段。只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为[36-63]个字符。 **取值范围**：不涉及。

        :param pool_display_name: The pool_display_name of this AcceptScheduledEventResponse.
        :type pool_display_name: str
        """
        self._pool_display_name = pool_display_name

    @property
    def publish_time(self):
        r"""Gets the publish_time of this AcceptScheduledEventResponse.

        **参数解释**：事件发布时间。 **约束限制**：格式为UTC时间字符串：2025-09-15T07:02:30Z。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The publish_time of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        r"""Sets the publish_time of this AcceptScheduledEventResponse.

        **参数解释**：事件发布时间。 **约束限制**：格式为UTC时间字符串：2025-09-15T07:02:30Z。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param publish_time: The publish_time of this AcceptScheduledEventResponse.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def start_time(self):
        r"""Gets the start_time of this AcceptScheduledEventResponse.

        **参数解释**：事件开始时间。 **约束限制**：格式为UTC时间字符串：2025-09-15T07:02:30Z。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The start_time of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AcceptScheduledEventResponse.

        **参数解释**：事件开始时间。 **约束限制**：格式为UTC时间字符串：2025-09-15T07:02:30Z。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param start_time: The start_time of this AcceptScheduledEventResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this AcceptScheduledEventResponse.

        **参数解释**：事件完成时间。 **约束限制**：格式为UTC时间字符串：2025-09-15T07:02:30Z。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The finish_time of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this AcceptScheduledEventResponse.

        **参数解释**：事件完成时间。 **约束限制**：格式为UTC时间字符串：2025-09-15T07:02:30Z。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param finish_time: The finish_time of this AcceptScheduledEventResponse.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def not_before(self):
        r"""Gets the not_before of this AcceptScheduledEventResponse.

        **参数解释**：事件计划执行开始时间，格式为UTC时间字符串：2025-09-15T07:02:30Z。 **约束限制**：大于当前时间。 **取值范围**：不涉及。 **默认取值**：不填表示立即执行。

        :return: The not_before of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        r"""Sets the not_before of this AcceptScheduledEventResponse.

        **参数解释**：事件计划执行开始时间，格式为UTC时间字符串：2025-09-15T07:02:30Z。 **约束限制**：大于当前时间。 **取值范围**：不涉及。 **默认取值**：不填表示立即执行。

        :param not_before: The not_before of this AcceptScheduledEventResponse.
        :type not_before: str
        """
        self._not_before = not_before

    @property
    def probe_msg(self):
        r"""Gets the probe_msg of this AcceptScheduledEventResponse.

        **参数解释**：提示信息。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The probe_msg of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._probe_msg

    @probe_msg.setter
    def probe_msg(self, probe_msg):
        r"""Sets the probe_msg of this AcceptScheduledEventResponse.

        **参数解释**：提示信息。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param probe_msg: The probe_msg of this AcceptScheduledEventResponse.
        :type probe_msg: str
        """
        self._probe_msg = probe_msg

    @property
    def redeploy_type(self):
        r"""Gets the redeploy_type of this AcceptScheduledEventResponse.

        **参数解释**：节点的重部署类型。 **约束限制**：不涉及。 **取值范围**：可选值如下：- HARD：表示支持强制重部署, - SOFT：表示支持重部署 **默认取值**：不涉及。

        :return: The redeploy_type of this AcceptScheduledEventResponse.
        :rtype: list[str]
        """
        return self._redeploy_type

    @redeploy_type.setter
    def redeploy_type(self, redeploy_type):
        r"""Sets the redeploy_type of this AcceptScheduledEventResponse.

        **参数解释**：节点的重部署类型。 **约束限制**：不涉及。 **取值范围**：可选值如下：- HARD：表示支持强制重部署, - SOFT：表示支持重部署 **默认取值**：不涉及。

        :param redeploy_type: The redeploy_type of this AcceptScheduledEventResponse.
        :type redeploy_type: list[str]
        """
        self._redeploy_type = redeploy_type

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this AcceptScheduledEventResponse.

        :return: The x_request_id of this AcceptScheduledEventResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this AcceptScheduledEventResponse.

        :param x_request_id: The x_request_id of this AcceptScheduledEventResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("AcceptScheduledEventResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, AcceptScheduledEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
