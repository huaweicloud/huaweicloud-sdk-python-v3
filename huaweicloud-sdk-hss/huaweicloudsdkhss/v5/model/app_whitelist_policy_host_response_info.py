# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppWhitelistPolicyHostResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'asset_value': 'str',
        'policy_name': 'str',
        'event_num': 'int',
        'os_type': 'str',
        'learning_status': 'str',
        'apply_status': 'bool',
        'intercept': 'bool',
        'policy_id': 'str',
        'policy_type': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'asset_value': 'asset_value',
        'policy_name': 'policy_name',
        'event_num': 'event_num',
        'os_type': 'os_type',
        'learning_status': 'learning_status',
        'apply_status': 'apply_status',
        'intercept': 'intercept',
        'policy_id': 'policy_id',
        'policy_type': 'policy_type'
    }

    def __init__(self, host_id=None, host_name=None, public_ip=None, private_ip=None, asset_value=None, policy_name=None, event_num=None, os_type=None, learning_status=None, apply_status=None, intercept=None, policy_id=None, policy_type=None):
        r"""AppWhitelistPolicyHostResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param event_num: **参数解释**: 主机发生事件数 **取值范围**: 最小值0，最大值2147483647 
        :type event_num: int
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param learning_status: **参数解释**： 服务器名称 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 
        :type learning_status: str
        :param apply_status: **参数解释**： 是否应用 **取值范围**: - true：是 - false：否 
        :type apply_status: bool
        :param intercept: 是否开启阻断
        :type intercept: bool
        :param policy_id: 策略ID
        :type policy_id: str
        :param policy_type: 策略类型
        :type policy_type: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._asset_value = None
        self._policy_name = None
        self._event_num = None
        self._os_type = None
        self._learning_status = None
        self._apply_status = None
        self._intercept = None
        self._policy_id = None
        self._policy_type = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if asset_value is not None:
            self.asset_value = asset_value
        if policy_name is not None:
            self.policy_name = policy_name
        if event_num is not None:
            self.event_num = event_num
        if os_type is not None:
            self.os_type = os_type
        if learning_status is not None:
            self.learning_status = learning_status
        if apply_status is not None:
            self.apply_status = apply_status
        if intercept is not None:
            self.intercept = intercept
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_type is not None:
            self.policy_type = policy_type

    @property
    def host_id(self):
        r"""Gets the host_id of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this AppWhitelistPolicyHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this AppWhitelistPolicyHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this AppWhitelistPolicyHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this AppWhitelistPolicyHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this AppWhitelistPolicyHostResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this AppWhitelistPolicyHostResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this AppWhitelistPolicyHostResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this AppWhitelistPolicyHostResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this AppWhitelistPolicyHostResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this AppWhitelistPolicyHostResponseInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this AppWhitelistPolicyHostResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this AppWhitelistPolicyHostResponseInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AppWhitelistPolicyHostResponseInfo.

        策略名称

        :return: The policy_name of this AppWhitelistPolicyHostResponseInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AppWhitelistPolicyHostResponseInfo.

        策略名称

        :param policy_name: The policy_name of this AppWhitelistPolicyHostResponseInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def event_num(self):
        r"""Gets the event_num of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**: 主机发生事件数 **取值范围**: 最小值0，最大值2147483647 

        :return: The event_num of this AppWhitelistPolicyHostResponseInfo.
        :rtype: int
        """
        return self._event_num

    @event_num.setter
    def event_num(self, event_num):
        r"""Sets the event_num of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**: 主机发生事件数 **取值范围**: 最小值0，最大值2147483647 

        :param event_num: The event_num of this AppWhitelistPolicyHostResponseInfo.
        :type event_num: int
        """
        self._event_num = event_num

    @property
    def os_type(self):
        r"""Gets the os_type of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this AppWhitelistPolicyHostResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this AppWhitelistPolicyHostResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def learning_status(self):
        r"""Gets the learning_status of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 服务器名称 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 

        :return: The learning_status of this AppWhitelistPolicyHostResponseInfo.
        :rtype: str
        """
        return self._learning_status

    @learning_status.setter
    def learning_status(self, learning_status):
        r"""Sets the learning_status of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 服务器名称 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 

        :param learning_status: The learning_status of this AppWhitelistPolicyHostResponseInfo.
        :type learning_status: str
        """
        self._learning_status = learning_status

    @property
    def apply_status(self):
        r"""Gets the apply_status of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 是否应用 **取值范围**: - true：是 - false：否 

        :return: The apply_status of this AppWhitelistPolicyHostResponseInfo.
        :rtype: bool
        """
        return self._apply_status

    @apply_status.setter
    def apply_status(self, apply_status):
        r"""Sets the apply_status of this AppWhitelistPolicyHostResponseInfo.

        **参数解释**： 是否应用 **取值范围**: - true：是 - false：否 

        :param apply_status: The apply_status of this AppWhitelistPolicyHostResponseInfo.
        :type apply_status: bool
        """
        self._apply_status = apply_status

    @property
    def intercept(self):
        r"""Gets the intercept of this AppWhitelistPolicyHostResponseInfo.

        是否开启阻断

        :return: The intercept of this AppWhitelistPolicyHostResponseInfo.
        :rtype: bool
        """
        return self._intercept

    @intercept.setter
    def intercept(self, intercept):
        r"""Sets the intercept of this AppWhitelistPolicyHostResponseInfo.

        是否开启阻断

        :param intercept: The intercept of this AppWhitelistPolicyHostResponseInfo.
        :type intercept: bool
        """
        self._intercept = intercept

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AppWhitelistPolicyHostResponseInfo.

        策略ID

        :return: The policy_id of this AppWhitelistPolicyHostResponseInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AppWhitelistPolicyHostResponseInfo.

        策略ID

        :param policy_id: The policy_id of this AppWhitelistPolicyHostResponseInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_type(self):
        r"""Gets the policy_type of this AppWhitelistPolicyHostResponseInfo.

        策略类型

        :return: The policy_type of this AppWhitelistPolicyHostResponseInfo.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this AppWhitelistPolicyHostResponseInfo.

        策略类型

        :param policy_type: The policy_type of this AppWhitelistPolicyHostResponseInfo.
        :type policy_type: str
        """
        self._policy_type = policy_type

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
        if not isinstance(other, AppWhitelistPolicyHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
