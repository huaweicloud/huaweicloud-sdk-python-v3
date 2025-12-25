# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditDO:

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
        'module': 'str',
        'operation': 'str',
        'time': 'str',
        'info': 'str',
        'data': 'str',
        'reason': 'str',
        'user_agent': 'str',
        'operator': 'str',
        'operator_nick_name': 'str',
        'operator_tenant_name': 'str',
        'ip_source': 'str'
    }

    attribute_map = {
        'id': 'id',
        'module': 'module',
        'operation': 'operation',
        'time': 'time',
        'info': 'info',
        'data': 'data',
        'reason': 'reason',
        'user_agent': 'userAgent',
        'operator': 'operator',
        'operator_nick_name': 'operatorNickName',
        'operator_tenant_name': 'operatorTenantName',
        'ip_source': 'ipSource'
    }

    def __init__(self, id=None, module=None, operation=None, time=None, info=None, data=None, reason=None, user_agent=None, operator=None, operator_nick_name=None, operator_tenant_name=None, ip_source=None):
        r"""AuditDO

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 操作ID。  **取值范围**： 不涉及。id
        :type id: str
        :param module: **参数解释**： 操作模块。  **取值范围**： 不涉及。
        :type module: str
        :param operation: **参数解释**： 操作类型。  **取值范围**： 不涉及。
        :type operation: str
        :param time: **参数解释**： 操作时间。  **取值范围**： 不涉及。
        :type time: str
        :param info: **参数解释**： 操作信息。  **取值范围**： 不涉及。
        :type info: str
        :param data: **参数解释**： 操作数据。  **取值范围**： 不涉及。
        :type data: str
        :param reason: **参数解释**： 原因。  **取值范围**： 不涉及。
        :type reason: str
        :param user_agent: **参数解释**： 操作人客户端类型。  **取值范围**： 不涉及。
        :type user_agent: str
        :param operator: **参数解释**： 操作人。  **取值范围**： 不涉及。
        :type operator: str
        :param operator_nick_name: **参数解释**： 操作人名字。  **取值范围**： 不涉及。
        :type operator_nick_name: str
        :param operator_tenant_name: **参数解释**： 操作人租户名。  **取值范围**： 不涉及。
        :type operator_tenant_name: str
        :param ip_source: **参数解释**： 操作人IP地址。  **取值范围**： 不涉及。
        :type ip_source: str
        """
        
        

        self._id = None
        self._module = None
        self._operation = None
        self._time = None
        self._info = None
        self._data = None
        self._reason = None
        self._user_agent = None
        self._operator = None
        self._operator_nick_name = None
        self._operator_tenant_name = None
        self._ip_source = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if module is not None:
            self.module = module
        if operation is not None:
            self.operation = operation
        if time is not None:
            self.time = time
        if info is not None:
            self.info = info
        if data is not None:
            self.data = data
        if reason is not None:
            self.reason = reason
        if user_agent is not None:
            self.user_agent = user_agent
        if operator is not None:
            self.operator = operator
        if operator_nick_name is not None:
            self.operator_nick_name = operator_nick_name
        if operator_tenant_name is not None:
            self.operator_tenant_name = operator_tenant_name
        if ip_source is not None:
            self.ip_source = ip_source

    @property
    def id(self):
        r"""Gets the id of this AuditDO.

        **参数解释**： 操作ID。  **取值范围**： 不涉及。id

        :return: The id of this AuditDO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AuditDO.

        **参数解释**： 操作ID。  **取值范围**： 不涉及。id

        :param id: The id of this AuditDO.
        :type id: str
        """
        self._id = id

    @property
    def module(self):
        r"""Gets the module of this AuditDO.

        **参数解释**： 操作模块。  **取值范围**： 不涉及。

        :return: The module of this AuditDO.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this AuditDO.

        **参数解释**： 操作模块。  **取值范围**： 不涉及。

        :param module: The module of this AuditDO.
        :type module: str
        """
        self._module = module

    @property
    def operation(self):
        r"""Gets the operation of this AuditDO.

        **参数解释**： 操作类型。  **取值范围**： 不涉及。

        :return: The operation of this AuditDO.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this AuditDO.

        **参数解释**： 操作类型。  **取值范围**： 不涉及。

        :param operation: The operation of this AuditDO.
        :type operation: str
        """
        self._operation = operation

    @property
    def time(self):
        r"""Gets the time of this AuditDO.

        **参数解释**： 操作时间。  **取值范围**： 不涉及。

        :return: The time of this AuditDO.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this AuditDO.

        **参数解释**： 操作时间。  **取值范围**： 不涉及。

        :param time: The time of this AuditDO.
        :type time: str
        """
        self._time = time

    @property
    def info(self):
        r"""Gets the info of this AuditDO.

        **参数解释**： 操作信息。  **取值范围**： 不涉及。

        :return: The info of this AuditDO.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this AuditDO.

        **参数解释**： 操作信息。  **取值范围**： 不涉及。

        :param info: The info of this AuditDO.
        :type info: str
        """
        self._info = info

    @property
    def data(self):
        r"""Gets the data of this AuditDO.

        **参数解释**： 操作数据。  **取值范围**： 不涉及。

        :return: The data of this AuditDO.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this AuditDO.

        **参数解释**： 操作数据。  **取值范围**： 不涉及。

        :param data: The data of this AuditDO.
        :type data: str
        """
        self._data = data

    @property
    def reason(self):
        r"""Gets the reason of this AuditDO.

        **参数解释**： 原因。  **取值范围**： 不涉及。

        :return: The reason of this AuditDO.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this AuditDO.

        **参数解释**： 原因。  **取值范围**： 不涉及。

        :param reason: The reason of this AuditDO.
        :type reason: str
        """
        self._reason = reason

    @property
    def user_agent(self):
        r"""Gets the user_agent of this AuditDO.

        **参数解释**： 操作人客户端类型。  **取值范围**： 不涉及。

        :return: The user_agent of this AuditDO.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        r"""Sets the user_agent of this AuditDO.

        **参数解释**： 操作人客户端类型。  **取值范围**： 不涉及。

        :param user_agent: The user_agent of this AuditDO.
        :type user_agent: str
        """
        self._user_agent = user_agent

    @property
    def operator(self):
        r"""Gets the operator of this AuditDO.

        **参数解释**： 操作人。  **取值范围**： 不涉及。

        :return: The operator of this AuditDO.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this AuditDO.

        **参数解释**： 操作人。  **取值范围**： 不涉及。

        :param operator: The operator of this AuditDO.
        :type operator: str
        """
        self._operator = operator

    @property
    def operator_nick_name(self):
        r"""Gets the operator_nick_name of this AuditDO.

        **参数解释**： 操作人名字。  **取值范围**： 不涉及。

        :return: The operator_nick_name of this AuditDO.
        :rtype: str
        """
        return self._operator_nick_name

    @operator_nick_name.setter
    def operator_nick_name(self, operator_nick_name):
        r"""Sets the operator_nick_name of this AuditDO.

        **参数解释**： 操作人名字。  **取值范围**： 不涉及。

        :param operator_nick_name: The operator_nick_name of this AuditDO.
        :type operator_nick_name: str
        """
        self._operator_nick_name = operator_nick_name

    @property
    def operator_tenant_name(self):
        r"""Gets the operator_tenant_name of this AuditDO.

        **参数解释**： 操作人租户名。  **取值范围**： 不涉及。

        :return: The operator_tenant_name of this AuditDO.
        :rtype: str
        """
        return self._operator_tenant_name

    @operator_tenant_name.setter
    def operator_tenant_name(self, operator_tenant_name):
        r"""Sets the operator_tenant_name of this AuditDO.

        **参数解释**： 操作人租户名。  **取值范围**： 不涉及。

        :param operator_tenant_name: The operator_tenant_name of this AuditDO.
        :type operator_tenant_name: str
        """
        self._operator_tenant_name = operator_tenant_name

    @property
    def ip_source(self):
        r"""Gets the ip_source of this AuditDO.

        **参数解释**： 操作人IP地址。  **取值范围**： 不涉及。

        :return: The ip_source of this AuditDO.
        :rtype: str
        """
        return self._ip_source

    @ip_source.setter
    def ip_source(self, ip_source):
        r"""Sets the ip_source of this AuditDO.

        **参数解释**： 操作人IP地址。  **取值范围**： 不涉及。

        :param ip_source: The ip_source of this AuditDO.
        :type ip_source: str
        """
        self._ip_source = ip_source

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
        if not isinstance(other, AuditDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
