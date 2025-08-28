# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppWhitelistPolicyHostRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'policy_name': 'str',
        'learning_status': 'str',
        'apply_status': 'bool',
        'asset_value': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'os_type': 'str',
        'policy_id': 'str',
        'public_ip': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'policy_name': 'policy_name',
        'learning_status': 'learning_status',
        'apply_status': 'apply_status',
        'asset_value': 'asset_value',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'os_type': 'os_type',
        'policy_id': 'policy_id',
        'public_ip': 'public_ip'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, policy_name=None, learning_status=None, apply_status=None, asset_value=None, host_name=None, private_ip=None, os_type=None, policy_id=None, public_ip=None):
        r"""ListAppWhitelistPolicyHostRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param policy_name: 策略名称
        :type policy_name: str
        :param learning_status: **策略学习状态**： 策略学习状态 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 
        :type learning_status: str
        :param apply_status: **策略学习状态**： 策略应用状态 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 
        :type apply_status: bool
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux：Linux。   - Windows：Windows。
        :type os_type: str
        :param policy_id: 策略ID
        :type policy_id: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._policy_name = None
        self._learning_status = None
        self._apply_status = None
        self._asset_value = None
        self._host_name = None
        self._private_ip = None
        self._os_type = None
        self._policy_id = None
        self._public_ip = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if policy_name is not None:
            self.policy_name = policy_name
        if learning_status is not None:
            self.learning_status = learning_status
        if apply_status is not None:
            self.apply_status = apply_status
        if asset_value is not None:
            self.asset_value = asset_value
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if os_type is not None:
            self.os_type = os_type
        if policy_id is not None:
            self.policy_id = policy_id
        if public_ip is not None:
            self.public_ip = public_ip

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAppWhitelistPolicyHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListAppWhitelistPolicyHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAppWhitelistPolicyHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListAppWhitelistPolicyHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAppWhitelistPolicyHostRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListAppWhitelistPolicyHostRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAppWhitelistPolicyHostRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListAppWhitelistPolicyHostRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAppWhitelistPolicyHostRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAppWhitelistPolicyHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAppWhitelistPolicyHostRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAppWhitelistPolicyHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ListAppWhitelistPolicyHostRequest.

        策略名称

        :return: The policy_name of this ListAppWhitelistPolicyHostRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ListAppWhitelistPolicyHostRequest.

        策略名称

        :param policy_name: The policy_name of this ListAppWhitelistPolicyHostRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def learning_status(self):
        r"""Gets the learning_status of this ListAppWhitelistPolicyHostRequest.

        **策略学习状态**： 策略学习状态 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 

        :return: The learning_status of this ListAppWhitelistPolicyHostRequest.
        :rtype: str
        """
        return self._learning_status

    @learning_status.setter
    def learning_status(self, learning_status):
        r"""Sets the learning_status of this ListAppWhitelistPolicyHostRequest.

        **策略学习状态**： 策略学习状态 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 

        :param learning_status: The learning_status of this ListAppWhitelistPolicyHostRequest.
        :type learning_status: str
        """
        self._learning_status = learning_status

    @property
    def apply_status(self):
        r"""Gets the apply_status of this ListAppWhitelistPolicyHostRequest.

        **策略学习状态**： 策略应用状态 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :return: The apply_status of this ListAppWhitelistPolicyHostRequest.
        :rtype: bool
        """
        return self._apply_status

    @apply_status.setter
    def apply_status(self, apply_status):
        r"""Sets the apply_status of this ListAppWhitelistPolicyHostRequest.

        **策略学习状态**： 策略应用状态 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :param apply_status: The apply_status of this ListAppWhitelistPolicyHostRequest.
        :type apply_status: bool
        """
        self._apply_status = apply_status

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListAppWhitelistPolicyHostRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ListAppWhitelistPolicyHostRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListAppWhitelistPolicyHostRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ListAppWhitelistPolicyHostRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def host_name(self):
        r"""Gets the host_name of this ListAppWhitelistPolicyHostRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListAppWhitelistPolicyHostRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListAppWhitelistPolicyHostRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListAppWhitelistPolicyHostRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListAppWhitelistPolicyHostRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListAppWhitelistPolicyHostRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListAppWhitelistPolicyHostRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListAppWhitelistPolicyHostRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def os_type(self):
        r"""Gets the os_type of this ListAppWhitelistPolicyHostRequest.

        操作系统类型，包含如下2种。   - Linux：Linux。   - Windows：Windows。

        :return: The os_type of this ListAppWhitelistPolicyHostRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListAppWhitelistPolicyHostRequest.

        操作系统类型，包含如下2种。   - Linux：Linux。   - Windows：Windows。

        :param os_type: The os_type of this ListAppWhitelistPolicyHostRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListAppWhitelistPolicyHostRequest.

        策略ID

        :return: The policy_id of this ListAppWhitelistPolicyHostRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListAppWhitelistPolicyHostRequest.

        策略ID

        :param policy_id: The policy_id of this ListAppWhitelistPolicyHostRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListAppWhitelistPolicyHostRequest.

        服务器公网IP

        :return: The public_ip of this ListAppWhitelistPolicyHostRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListAppWhitelistPolicyHostRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListAppWhitelistPolicyHostRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

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
        if not isinstance(other, ListAppWhitelistPolicyHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
