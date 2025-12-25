# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'operation_state': 'str',
        'error': 'ErrorStatus'
    }

    attribute_map = {
        'state': 'state',
        'operation_state': 'operation_state',
        'error': 'error'
    }

    def __init__(self, state=None, operation_state=None, error=None):
        r"""ShowInstanceStatusResponse

        The model defined in huaweicloud sdk

        :param state: **参数解释**： 实例状态 **约束限制**： 不涉及 **取值范围**： - pending：实例正在启动（分配资源/启动操作系统） - running：实例正常运行（可接受SSH/RDP连接） - stopping：实例正在关闭（停止/休眠过渡状态） - stopped： 实例已完全关闭（存储卷保留） - reinstalling：实例正在重装中 - shutting-down：实例正在终止（删除流程中） - terminated：实例已终止（资源完全删除，不可恢复） - failed：实例处于失败状态，对于reinstall操作可重试，其它操作不可重试并清除相关资源 - modifyIping：实例正在修改ip中 - switch-installing：实例正在切换系统中  &#x60;&#x60;&#x60;mermaid stateDiagram-v2      [*] --&gt; pending : RunInstances/CreateInstance     pending --&gt; running : Provision Finished     reinstalling --&gt; running : Provision Finished     running --&gt; stopping : PowerOff/PowerReboot     stopping --&gt; stopped : PowerOff Finished     stopped --&gt; running : PowerOn | ModifyIP     stopped --&gt; stopped : ChangePassword     pending --&gt; shutting_down : Abort by DeleteInstance     running --&gt; shutting_down : DeleteInstance     running --&gt; switch-installing : SwitchOS     switch-installing --&gt; running : SwitchOS finished     switch-installing --&gt; failed : SwitchOS failed     stopped --&gt; shutting_down : DeleteInstance     stopped --&gt; reinstalling : ReinstallOS     shutting_down --&gt;terminated: DeleteInstance Finished     pending --&gt; failed : Error     shutting_down --&gt; failed : Error     reinstalling --&gt; failed : Error     failed --&gt; reinstalling: Retry     running --&gt; modifyIping : Modify Ip     modifyIping --&gt; running : Modify Ip finished     modifyIping --&gt; failed : Modify Ip failed     failed --&gt; modifyIping : Retrey &#x60;&#x60;&#x60;    **默认取值**：   不涉及 
        :type state: str
        :param operation_state: **参数解释**:  操作状态 **约束限制**:  不涉及 **取值范围**:  - install-processing: 安装OS中 - install-succeed: 安装OS成功 - install-failed: 安装OS失败 - reinstall-processing: 重装OS中 - reinstall-succeed: 重装OS成功 - reinstall-failed: 重装OS失败 - switch-install-processing: 切换OS中 - switch-install-succeed: 切换OS成功 - switch-install-failed: 切换OS失败 - modify-ip-processing: 修改IP地址中 - modify-ip-succeed: 修改IP地址成功 - modify-ip-failed: 修改IP地址失败 - uninstall-processing: 卸载OS中 - uninstall-succeed: 卸载OS成功 - uninstall-failed: 卸载OS失败  **默认取值**:  不涉及
        :type operation_state: str
        :param error: 
        :type error: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        
        super().__init__()

        self._state = None
        self._operation_state = None
        self._error = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if operation_state is not None:
            self.operation_state = operation_state
        if error is not None:
            self.error = error

    @property
    def state(self):
        r"""Gets the state of this ShowInstanceStatusResponse.

        **参数解释**： 实例状态 **约束限制**： 不涉及 **取值范围**： - pending：实例正在启动（分配资源/启动操作系统） - running：实例正常运行（可接受SSH/RDP连接） - stopping：实例正在关闭（停止/休眠过渡状态） - stopped： 实例已完全关闭（存储卷保留） - reinstalling：实例正在重装中 - shutting-down：实例正在终止（删除流程中） - terminated：实例已终止（资源完全删除，不可恢复） - failed：实例处于失败状态，对于reinstall操作可重试，其它操作不可重试并清除相关资源 - modifyIping：实例正在修改ip中 - switch-installing：实例正在切换系统中  ```mermaid stateDiagram-v2      [*] --> pending : RunInstances/CreateInstance     pending --> running : Provision Finished     reinstalling --> running : Provision Finished     running --> stopping : PowerOff/PowerReboot     stopping --> stopped : PowerOff Finished     stopped --> running : PowerOn | ModifyIP     stopped --> stopped : ChangePassword     pending --> shutting_down : Abort by DeleteInstance     running --> shutting_down : DeleteInstance     running --> switch-installing : SwitchOS     switch-installing --> running : SwitchOS finished     switch-installing --> failed : SwitchOS failed     stopped --> shutting_down : DeleteInstance     stopped --> reinstalling : ReinstallOS     shutting_down -->terminated: DeleteInstance Finished     pending --> failed : Error     shutting_down --> failed : Error     reinstalling --> failed : Error     failed --> reinstalling: Retry     running --> modifyIping : Modify Ip     modifyIping --> running : Modify Ip finished     modifyIping --> failed : Modify Ip failed     failed --> modifyIping : Retrey ```    **默认取值**：   不涉及 

        :return: The state of this ShowInstanceStatusResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowInstanceStatusResponse.

        **参数解释**： 实例状态 **约束限制**： 不涉及 **取值范围**： - pending：实例正在启动（分配资源/启动操作系统） - running：实例正常运行（可接受SSH/RDP连接） - stopping：实例正在关闭（停止/休眠过渡状态） - stopped： 实例已完全关闭（存储卷保留） - reinstalling：实例正在重装中 - shutting-down：实例正在终止（删除流程中） - terminated：实例已终止（资源完全删除，不可恢复） - failed：实例处于失败状态，对于reinstall操作可重试，其它操作不可重试并清除相关资源 - modifyIping：实例正在修改ip中 - switch-installing：实例正在切换系统中  ```mermaid stateDiagram-v2      [*] --> pending : RunInstances/CreateInstance     pending --> running : Provision Finished     reinstalling --> running : Provision Finished     running --> stopping : PowerOff/PowerReboot     stopping --> stopped : PowerOff Finished     stopped --> running : PowerOn | ModifyIP     stopped --> stopped : ChangePassword     pending --> shutting_down : Abort by DeleteInstance     running --> shutting_down : DeleteInstance     running --> switch-installing : SwitchOS     switch-installing --> running : SwitchOS finished     switch-installing --> failed : SwitchOS failed     stopped --> shutting_down : DeleteInstance     stopped --> reinstalling : ReinstallOS     shutting_down -->terminated: DeleteInstance Finished     pending --> failed : Error     shutting_down --> failed : Error     reinstalling --> failed : Error     failed --> reinstalling: Retry     running --> modifyIping : Modify Ip     modifyIping --> running : Modify Ip finished     modifyIping --> failed : Modify Ip failed     failed --> modifyIping : Retrey ```    **默认取值**：   不涉及 

        :param state: The state of this ShowInstanceStatusResponse.
        :type state: str
        """
        self._state = state

    @property
    def operation_state(self):
        r"""Gets the operation_state of this ShowInstanceStatusResponse.

        **参数解释**:  操作状态 **约束限制**:  不涉及 **取值范围**:  - install-processing: 安装OS中 - install-succeed: 安装OS成功 - install-failed: 安装OS失败 - reinstall-processing: 重装OS中 - reinstall-succeed: 重装OS成功 - reinstall-failed: 重装OS失败 - switch-install-processing: 切换OS中 - switch-install-succeed: 切换OS成功 - switch-install-failed: 切换OS失败 - modify-ip-processing: 修改IP地址中 - modify-ip-succeed: 修改IP地址成功 - modify-ip-failed: 修改IP地址失败 - uninstall-processing: 卸载OS中 - uninstall-succeed: 卸载OS成功 - uninstall-failed: 卸载OS失败  **默认取值**:  不涉及

        :return: The operation_state of this ShowInstanceStatusResponse.
        :rtype: str
        """
        return self._operation_state

    @operation_state.setter
    def operation_state(self, operation_state):
        r"""Sets the operation_state of this ShowInstanceStatusResponse.

        **参数解释**:  操作状态 **约束限制**:  不涉及 **取值范围**:  - install-processing: 安装OS中 - install-succeed: 安装OS成功 - install-failed: 安装OS失败 - reinstall-processing: 重装OS中 - reinstall-succeed: 重装OS成功 - reinstall-failed: 重装OS失败 - switch-install-processing: 切换OS中 - switch-install-succeed: 切换OS成功 - switch-install-failed: 切换OS失败 - modify-ip-processing: 修改IP地址中 - modify-ip-succeed: 修改IP地址成功 - modify-ip-failed: 修改IP地址失败 - uninstall-processing: 卸载OS中 - uninstall-succeed: 卸载OS成功 - uninstall-failed: 卸载OS失败  **默认取值**:  不涉及

        :param operation_state: The operation_state of this ShowInstanceStatusResponse.
        :type operation_state: str
        """
        self._operation_state = operation_state

    @property
    def error(self):
        r"""Gets the error of this ShowInstanceStatusResponse.

        :return: The error of this ShowInstanceStatusResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ShowInstanceStatusResponse.

        :param error: The error of this ShowInstanceStatusResponse.
        :type error: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        self._error = error

    def to_dict(self):
        import warnings
        warnings.warn("ShowInstanceStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowInstanceStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
