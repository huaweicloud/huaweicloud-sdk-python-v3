# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerResponse(SdkResponse):

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
        'domain_id': 'str',
        'manage_state': 'str',
        'power_state': 'str',
        'operation_state': 'str',
        'health_state': 'str',
        'onboard_time': 'str',
        'location': 'Location',
        'hardware_attributes': 'HardwareSummary',
        'tags': 'list[Tag]',
        'error': 'ErrorStatus'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'manage_state': 'manage_state',
        'power_state': 'power_state',
        'operation_state': 'operation_state',
        'health_state': 'health_state',
        'onboard_time': 'onboard_time',
        'location': 'location',
        'hardware_attributes': 'hardware_attributes',
        'tags': 'tags',
        'error': 'error'
    }

    def __init__(self, id=None, name=None, project_id=None, domain_id=None, manage_state=None, power_state=None, operation_state=None, health_state=None, onboard_time=None, location=None, hardware_attributes=None, tags=None, error=None):
        r"""ShowServerResponse

        The model defined in huaweicloud sdk

        :param id: UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type id: str
        :param name: Resource Name Type
        :type name: str
        :param project_id: project id
        :type project_id: str
        :param domain_id: domain id
        :type domain_id: str
        :param manage_state: **参数解释**： 服务器管理状态 **约束限制**： 不涉及 **取值范围** - onboard：上架中，用户下单，完成LLD设计。 - ready：交付完成，完成硬装、网调、服务器初始化、软调及转维验收。 - in-use：使用中，用户发放裸机。 - frozen：冻结，因欠费导致资源冻结。 - offboarding：下架中。  &#x60;&#x60;&#x60;mermaid stateDiagram-v2    [*] --&gt; onboard : 完成LLD设计   onboard --&gt; ready : 完成网调、服务器初始化、软调及转维验收   ready --&gt; in_use : 发放裸机实例   ready --&gt; offboarding : 请求下架   ready --&gt; frozen : 欠费      in_use --&gt; ready : 删除裸机实例   in_use --&gt; frozen : 欠费    frozen --&gt; offboarding : 请求下架   in_use --&gt; offboarding : 请求下架   offboarding --&gt; [*] : 完成下架   state \&quot;in-use\&quot; as in_use &#x60;&#x60;&#x60; **默认取值**： 不涉及
        :type manage_state: str
        :param power_state: **参数解释**： 电源状态 power_state 会根据不同的操作和事件发生转换，常见的状态转换流程如下：   - 开机流程：off -&gt; powering-on -&gt; on   - 关机流程：on -&gt; powering-off -&gt; off   - 重启流程：on -&gt; rebooting -&gt; on  **约束限制**： 不涉及 **取值范围**： - on：表示节点的电源已开启，硬件处于通电状态，操作系统正在运行或者可以正常启动。这意味着节点能够执行计算任务，为上层应用提供服务。 示例场景：当用户在 Ironic 中创建并激活一个节点，或者手动开启节点电源后，节点的 power_state 会变为 power on。 - off：表明节点的电源已关闭，硬件停止供电，所有组件处于非工作状态，无法执行任何计算任务。 示例场景：在维护节点或者不需要使用节点资源时，管理员可以将节点的电源关闭，此时 power_state 变为 power off。 - rebooting：节点正在进行重启操作，即先关闭电源，然后再重新开启。在这个过程中，节点会经历硬件初始化和操作系统启动等步骤。   示例场景：当管理员通过 Ironic API 发送重启节点的指令后，节点的 power_state 会暂时变为 rebooting，直到重启完成。 - powering-on：节点正在开启电源的过程中，此时硬件开始通电，但操作系统可能还未完全启动。 示例场景：当管理员发送开机指令后，节点会进入 powering on 状态，直到操作系统成功启动，power_state 变为 power on。 - powering-off：节点正在关闭电源的过程中，操作系统会进行一些清理工作，如保存数据、关闭服务等，然后切断硬件的电源供应。  示例场景：当管理员发送关机指令后，节点会进入 powering off 状态，直到电源完全关闭，power_state 变为  off。  **默认取值**： 不涉及 
        :type power_state: str
        :param operation_state: **约束限制**： 不涉及 **取值范围**： - power-on-processing: 节点正在开启电源的过程中，此时硬件开始通电，但操作系统可能还未完全启动。 - power-on-succeed: 开启电源成功。 - power-on-failed: 开启电源失败。 - power-off-processing: 节点正在关闭电源的过程中，操作系统会进行一些清理工作，如保存数据、关闭服务等，然后切断硬件的电源供应。 - power-off-succeed: 关闭电源成功。 - power-off-failed: 关闭电源失败。 - reboot-processing: 节点正在进行重启操作，即先关闭电源，然后再重新开启。在这个过程中，节点会经历硬件初始化和操作系统启动等步骤。 - reboot-succeed: 重启操作成功。 - reboot-failed: 重启操作失败。  **默认取值**： 不涉及 
        :type operation_state: str
        :param health_state: 硬件健康状态： OK：健康 Warning：警告 Critical：严重 Unknown：未知
        :type health_state: str
        :param onboard_time: 上架时间
        :type onboard_time: str
        :param location: 
        :type location: :class:`huaweicloudsdkclouddc.v1.Location`
        :param hardware_attributes: 
        :type hardware_attributes: :class:`huaweicloudsdkclouddc.v1.HardwareSummary`
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        :param error: 
        :type error: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._project_id = None
        self._domain_id = None
        self._manage_state = None
        self._power_state = None
        self._operation_state = None
        self._health_state = None
        self._onboard_time = None
        self._location = None
        self._hardware_attributes = None
        self._tags = None
        self._error = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if manage_state is not None:
            self.manage_state = manage_state
        if power_state is not None:
            self.power_state = power_state
        if operation_state is not None:
            self.operation_state = operation_state
        if health_state is not None:
            self.health_state = health_state
        if onboard_time is not None:
            self.onboard_time = onboard_time
        if location is not None:
            self.location = location
        if hardware_attributes is not None:
            self.hardware_attributes = hardware_attributes
        if tags is not None:
            self.tags = tags
        if error is not None:
            self.error = error

    @property
    def id(self):
        r"""Gets the id of this ShowServerResponse.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :return: The id of this ShowServerResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowServerResponse.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :param id: The id of this ShowServerResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowServerResponse.

        Resource Name Type

        :return: The name of this ShowServerResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowServerResponse.

        Resource Name Type

        :param name: The name of this ShowServerResponse.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowServerResponse.

        project id

        :return: The project_id of this ShowServerResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowServerResponse.

        project id

        :param project_id: The project_id of this ShowServerResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowServerResponse.

        domain id

        :return: The domain_id of this ShowServerResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowServerResponse.

        domain id

        :param domain_id: The domain_id of this ShowServerResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def manage_state(self):
        r"""Gets the manage_state of this ShowServerResponse.

        **参数解释**： 服务器管理状态 **约束限制**： 不涉及 **取值范围** - onboard：上架中，用户下单，完成LLD设计。 - ready：交付完成，完成硬装、网调、服务器初始化、软调及转维验收。 - in-use：使用中，用户发放裸机。 - frozen：冻结，因欠费导致资源冻结。 - offboarding：下架中。  ```mermaid stateDiagram-v2    [*] --> onboard : 完成LLD设计   onboard --> ready : 完成网调、服务器初始化、软调及转维验收   ready --> in_use : 发放裸机实例   ready --> offboarding : 请求下架   ready --> frozen : 欠费      in_use --> ready : 删除裸机实例   in_use --> frozen : 欠费    frozen --> offboarding : 请求下架   in_use --> offboarding : 请求下架   offboarding --> [*] : 完成下架   state \"in-use\" as in_use ``` **默认取值**： 不涉及

        :return: The manage_state of this ShowServerResponse.
        :rtype: str
        """
        return self._manage_state

    @manage_state.setter
    def manage_state(self, manage_state):
        r"""Sets the manage_state of this ShowServerResponse.

        **参数解释**： 服务器管理状态 **约束限制**： 不涉及 **取值范围** - onboard：上架中，用户下单，完成LLD设计。 - ready：交付完成，完成硬装、网调、服务器初始化、软调及转维验收。 - in-use：使用中，用户发放裸机。 - frozen：冻结，因欠费导致资源冻结。 - offboarding：下架中。  ```mermaid stateDiagram-v2    [*] --> onboard : 完成LLD设计   onboard --> ready : 完成网调、服务器初始化、软调及转维验收   ready --> in_use : 发放裸机实例   ready --> offboarding : 请求下架   ready --> frozen : 欠费      in_use --> ready : 删除裸机实例   in_use --> frozen : 欠费    frozen --> offboarding : 请求下架   in_use --> offboarding : 请求下架   offboarding --> [*] : 完成下架   state \"in-use\" as in_use ``` **默认取值**： 不涉及

        :param manage_state: The manage_state of this ShowServerResponse.
        :type manage_state: str
        """
        self._manage_state = manage_state

    @property
    def power_state(self):
        r"""Gets the power_state of this ShowServerResponse.

        **参数解释**： 电源状态 power_state 会根据不同的操作和事件发生转换，常见的状态转换流程如下：   - 开机流程：off -> powering-on -> on   - 关机流程：on -> powering-off -> off   - 重启流程：on -> rebooting -> on  **约束限制**： 不涉及 **取值范围**： - on：表示节点的电源已开启，硬件处于通电状态，操作系统正在运行或者可以正常启动。这意味着节点能够执行计算任务，为上层应用提供服务。 示例场景：当用户在 Ironic 中创建并激活一个节点，或者手动开启节点电源后，节点的 power_state 会变为 power on。 - off：表明节点的电源已关闭，硬件停止供电，所有组件处于非工作状态，无法执行任何计算任务。 示例场景：在维护节点或者不需要使用节点资源时，管理员可以将节点的电源关闭，此时 power_state 变为 power off。 - rebooting：节点正在进行重启操作，即先关闭电源，然后再重新开启。在这个过程中，节点会经历硬件初始化和操作系统启动等步骤。   示例场景：当管理员通过 Ironic API 发送重启节点的指令后，节点的 power_state 会暂时变为 rebooting，直到重启完成。 - powering-on：节点正在开启电源的过程中，此时硬件开始通电，但操作系统可能还未完全启动。 示例场景：当管理员发送开机指令后，节点会进入 powering on 状态，直到操作系统成功启动，power_state 变为 power on。 - powering-off：节点正在关闭电源的过程中，操作系统会进行一些清理工作，如保存数据、关闭服务等，然后切断硬件的电源供应。  示例场景：当管理员发送关机指令后，节点会进入 powering off 状态，直到电源完全关闭，power_state 变为  off。  **默认取值**： 不涉及 

        :return: The power_state of this ShowServerResponse.
        :rtype: str
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        r"""Sets the power_state of this ShowServerResponse.

        **参数解释**： 电源状态 power_state 会根据不同的操作和事件发生转换，常见的状态转换流程如下：   - 开机流程：off -> powering-on -> on   - 关机流程：on -> powering-off -> off   - 重启流程：on -> rebooting -> on  **约束限制**： 不涉及 **取值范围**： - on：表示节点的电源已开启，硬件处于通电状态，操作系统正在运行或者可以正常启动。这意味着节点能够执行计算任务，为上层应用提供服务。 示例场景：当用户在 Ironic 中创建并激活一个节点，或者手动开启节点电源后，节点的 power_state 会变为 power on。 - off：表明节点的电源已关闭，硬件停止供电，所有组件处于非工作状态，无法执行任何计算任务。 示例场景：在维护节点或者不需要使用节点资源时，管理员可以将节点的电源关闭，此时 power_state 变为 power off。 - rebooting：节点正在进行重启操作，即先关闭电源，然后再重新开启。在这个过程中，节点会经历硬件初始化和操作系统启动等步骤。   示例场景：当管理员通过 Ironic API 发送重启节点的指令后，节点的 power_state 会暂时变为 rebooting，直到重启完成。 - powering-on：节点正在开启电源的过程中，此时硬件开始通电，但操作系统可能还未完全启动。 示例场景：当管理员发送开机指令后，节点会进入 powering on 状态，直到操作系统成功启动，power_state 变为 power on。 - powering-off：节点正在关闭电源的过程中，操作系统会进行一些清理工作，如保存数据、关闭服务等，然后切断硬件的电源供应。  示例场景：当管理员发送关机指令后，节点会进入 powering off 状态，直到电源完全关闭，power_state 变为  off。  **默认取值**： 不涉及 

        :param power_state: The power_state of this ShowServerResponse.
        :type power_state: str
        """
        self._power_state = power_state

    @property
    def operation_state(self):
        r"""Gets the operation_state of this ShowServerResponse.

        **约束限制**： 不涉及 **取值范围**： - power-on-processing: 节点正在开启电源的过程中，此时硬件开始通电，但操作系统可能还未完全启动。 - power-on-succeed: 开启电源成功。 - power-on-failed: 开启电源失败。 - power-off-processing: 节点正在关闭电源的过程中，操作系统会进行一些清理工作，如保存数据、关闭服务等，然后切断硬件的电源供应。 - power-off-succeed: 关闭电源成功。 - power-off-failed: 关闭电源失败。 - reboot-processing: 节点正在进行重启操作，即先关闭电源，然后再重新开启。在这个过程中，节点会经历硬件初始化和操作系统启动等步骤。 - reboot-succeed: 重启操作成功。 - reboot-failed: 重启操作失败。  **默认取值**： 不涉及 

        :return: The operation_state of this ShowServerResponse.
        :rtype: str
        """
        return self._operation_state

    @operation_state.setter
    def operation_state(self, operation_state):
        r"""Sets the operation_state of this ShowServerResponse.

        **约束限制**： 不涉及 **取值范围**： - power-on-processing: 节点正在开启电源的过程中，此时硬件开始通电，但操作系统可能还未完全启动。 - power-on-succeed: 开启电源成功。 - power-on-failed: 开启电源失败。 - power-off-processing: 节点正在关闭电源的过程中，操作系统会进行一些清理工作，如保存数据、关闭服务等，然后切断硬件的电源供应。 - power-off-succeed: 关闭电源成功。 - power-off-failed: 关闭电源失败。 - reboot-processing: 节点正在进行重启操作，即先关闭电源，然后再重新开启。在这个过程中，节点会经历硬件初始化和操作系统启动等步骤。 - reboot-succeed: 重启操作成功。 - reboot-failed: 重启操作失败。  **默认取值**： 不涉及 

        :param operation_state: The operation_state of this ShowServerResponse.
        :type operation_state: str
        """
        self._operation_state = operation_state

    @property
    def health_state(self):
        r"""Gets the health_state of this ShowServerResponse.

        硬件健康状态： OK：健康 Warning：警告 Critical：严重 Unknown：未知

        :return: The health_state of this ShowServerResponse.
        :rtype: str
        """
        return self._health_state

    @health_state.setter
    def health_state(self, health_state):
        r"""Sets the health_state of this ShowServerResponse.

        硬件健康状态： OK：健康 Warning：警告 Critical：严重 Unknown：未知

        :param health_state: The health_state of this ShowServerResponse.
        :type health_state: str
        """
        self._health_state = health_state

    @property
    def onboard_time(self):
        r"""Gets the onboard_time of this ShowServerResponse.

        上架时间

        :return: The onboard_time of this ShowServerResponse.
        :rtype: str
        """
        return self._onboard_time

    @onboard_time.setter
    def onboard_time(self, onboard_time):
        r"""Sets the onboard_time of this ShowServerResponse.

        上架时间

        :param onboard_time: The onboard_time of this ShowServerResponse.
        :type onboard_time: str
        """
        self._onboard_time = onboard_time

    @property
    def location(self):
        r"""Gets the location of this ShowServerResponse.

        :return: The location of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.Location`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ShowServerResponse.

        :param location: The location of this ShowServerResponse.
        :type location: :class:`huaweicloudsdkclouddc.v1.Location`
        """
        self._location = location

    @property
    def hardware_attributes(self):
        r"""Gets the hardware_attributes of this ShowServerResponse.

        :return: The hardware_attributes of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.HardwareSummary`
        """
        return self._hardware_attributes

    @hardware_attributes.setter
    def hardware_attributes(self, hardware_attributes):
        r"""Sets the hardware_attributes of this ShowServerResponse.

        :param hardware_attributes: The hardware_attributes of this ShowServerResponse.
        :type hardware_attributes: :class:`huaweicloudsdkclouddc.v1.HardwareSummary`
        """
        self._hardware_attributes = hardware_attributes

    @property
    def tags(self):
        r"""Gets the tags of this ShowServerResponse.

        标签

        :return: The tags of this ShowServerResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowServerResponse.

        标签

        :param tags: The tags of this ShowServerResponse.
        :type tags: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        """
        self._tags = tags

    @property
    def error(self):
        r"""Gets the error of this ShowServerResponse.

        :return: The error of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ShowServerResponse.

        :param error: The error of this ShowServerResponse.
        :type error: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        self._error = error

    def to_dict(self):
        import warnings
        warnings.warn("ShowServerResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
