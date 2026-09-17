# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityConfigurationParameter:

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
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):
        r"""SecurityConfigurationParameter

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 参数名。 **取值范围**： audit_dml_state：审计dml操作开关； audit_system_object：审计DDL操作、其它操作； audit_adm：安全管理员用户名； audit_exec_status：审计执行结果； audit_operation_checked：审计DML操作、审计其它操作的具体勾选项； enableSeparationOfDuty：三权分立开关； audit_user_violation：越权访问操作； ssl：ssl开关； require_ssl：是否校验ssl； audit_function_exec：审计存储过程执行操作； audit_copy_exec：对COPY操作进行记录； audit_resource_policy：日志保留策略； audit_file_remain_time：时间策略下的最少保留天数，已废弃； audit_dml_state_select：审计SELECT操作； security_adm：安全管理员； audit_dump_switch：日志转储开关； kernel_audit_dump_switch：内核日志转储开关； audit_system_object_detail：审计DDL操作、其它操作的具体勾选项；
        :type name: str
        :param value: **参数解释**： 参数值。 **取值范围**： 不涉及。
        :type value: str
        """
        
        

        self._name = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def name(self):
        r"""Gets the name of this SecurityConfigurationParameter.

        **参数解释**： 参数名。 **取值范围**： audit_dml_state：审计dml操作开关； audit_system_object：审计DDL操作、其它操作； audit_adm：安全管理员用户名； audit_exec_status：审计执行结果； audit_operation_checked：审计DML操作、审计其它操作的具体勾选项； enableSeparationOfDuty：三权分立开关； audit_user_violation：越权访问操作； ssl：ssl开关； require_ssl：是否校验ssl； audit_function_exec：审计存储过程执行操作； audit_copy_exec：对COPY操作进行记录； audit_resource_policy：日志保留策略； audit_file_remain_time：时间策略下的最少保留天数，已废弃； audit_dml_state_select：审计SELECT操作； security_adm：安全管理员； audit_dump_switch：日志转储开关； kernel_audit_dump_switch：内核日志转储开关； audit_system_object_detail：审计DDL操作、其它操作的具体勾选项；

        :return: The name of this SecurityConfigurationParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SecurityConfigurationParameter.

        **参数解释**： 参数名。 **取值范围**： audit_dml_state：审计dml操作开关； audit_system_object：审计DDL操作、其它操作； audit_adm：安全管理员用户名； audit_exec_status：审计执行结果； audit_operation_checked：审计DML操作、审计其它操作的具体勾选项； enableSeparationOfDuty：三权分立开关； audit_user_violation：越权访问操作； ssl：ssl开关； require_ssl：是否校验ssl； audit_function_exec：审计存储过程执行操作； audit_copy_exec：对COPY操作进行记录； audit_resource_policy：日志保留策略； audit_file_remain_time：时间策略下的最少保留天数，已废弃； audit_dml_state_select：审计SELECT操作； security_adm：安全管理员； audit_dump_switch：日志转储开关； kernel_audit_dump_switch：内核日志转储开关； audit_system_object_detail：审计DDL操作、其它操作的具体勾选项；

        :param name: The name of this SecurityConfigurationParameter.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this SecurityConfigurationParameter.

        **参数解释**： 参数值。 **取值范围**： 不涉及。

        :return: The value of this SecurityConfigurationParameter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this SecurityConfigurationParameter.

        **参数解释**： 参数值。 **取值范围**： 不涉及。

        :param value: The value of this SecurityConfigurationParameter.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, SecurityConfigurationParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
