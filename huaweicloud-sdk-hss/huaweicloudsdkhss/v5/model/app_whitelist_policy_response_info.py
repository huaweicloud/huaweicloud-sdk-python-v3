# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppWhitelistPolicyResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'policy_name': 'str',
        'policy_type': 'str',
        'learning_status': 'str',
        'learning_days': 'int',
        'specified_dir': 'bool',
        'dir_list': 'list[str]',
        'file_extension_list': 'list[str]',
        'intercept': 'bool',
        'auto_detect': 'bool',
        'not_effect_host_num': 'int',
        'effect_host_num': 'int',
        'trust_num': 'int',
        'suspicious_num': 'int',
        'malicious_num': 'int',
        'unknown_num': 'int',
        'abnormal_info_list': 'list[AppWhitelistAbnormalInfo]',
        'auto_confirm': 'bool',
        'default_policy': 'bool',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'policy_type': 'policy_type',
        'learning_status': 'learning_status',
        'learning_days': 'learning_days',
        'specified_dir': 'specified_dir',
        'dir_list': 'dir_list',
        'file_extension_list': 'file_extension_list',
        'intercept': 'intercept',
        'auto_detect': 'auto_detect',
        'not_effect_host_num': 'not_effect_host_num',
        'effect_host_num': 'effect_host_num',
        'trust_num': 'trust_num',
        'suspicious_num': 'suspicious_num',
        'malicious_num': 'malicious_num',
        'unknown_num': 'unknown_num',
        'abnormal_info_list': 'abnormal_info_list',
        'auto_confirm': 'auto_confirm',
        'default_policy': 'default_policy',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, policy_id=None, policy_name=None, policy_type=None, learning_status=None, learning_days=None, specified_dir=None, dir_list=None, file_extension_list=None, intercept=None, auto_detect=None, not_effect_host_num=None, effect_host_num=None, trust_num=None, suspicious_num=None, malicious_num=None, unknown_num=None, abnormal_info_list=None, auto_confirm=None, default_policy=None, host_id_list=None):
        r"""AppWhitelistPolicyResponseInfo

        The model defined in huaweicloud sdk

        :param policy_id: 策略ID
        :type policy_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_type: **参数解释**： 进程白名单策略类型 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行 
        :type policy_type: str
        :param learning_status: **参数解释**： 服务器名称 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 
        :type learning_status: str
        :param learning_days: **参数解释**: 策略学习天数 **取值范围**: 最小值1，最大值1000 
        :type learning_days: int
        :param specified_dir: **参数解释**： 是否指定学习目录 **约束限制**： 不涉及 **取值范围**: - true：是 - false：否 **默认取值**： 不涉及 
        :type specified_dir: bool
        :param dir_list: 监控目录列表
        :type dir_list: list[str]
        :param file_extension_list: 监控文件后缀名列表
        :type file_extension_list: list[str]
        :param intercept: **参数解释**： 是否开启阻断 **取值范围**: - true：是 - false：否 
        :type intercept: bool
        :param auto_detect: **参数解释**： 是否自动开启检测 **取值范围**: - true：是 - false：否 
        :type auto_detect: bool
        :param not_effect_host_num: **参数解释**: 学习完成策略未生效主机数 **取值范围**: 最小值0，最大值2147483647 
        :type not_effect_host_num: int
        :param effect_host_num: **参数解释**: 学习完成策略已生效主机数 **取值范围**: 最小值0，最大值2147483647 
        :type effect_host_num: int
        :param trust_num: **参数解释**: 识别可信进程数 **取值范围**: 最小值0，最大值2147483647 
        :type trust_num: int
        :param suspicious_num: **参数解释**: 识别可疑进程数 **取值范围**: 最小值0，最大值2147483647 
        :type suspicious_num: int
        :param malicious_num: **参数解释**: 识别恶意进程数 **取值范围**: 最小值0，最大值2147483647 
        :type malicious_num: int
        :param unknown_num: **参数解释**: 识别未知进程数 **取值范围**: 最小值0，最大值2147483647 
        :type unknown_num: int
        :param abnormal_info_list: 学习异常原因列表
        :type abnormal_info_list: list[:class:`huaweicloudsdkhss.v5.AppWhitelistAbnormalInfo`]
        :param auto_confirm: **参数解释**： 是否自动确认学习结果 **取值范围**: - true：是 - false：否 
        :type auto_confirm: bool
        :param default_policy: **参数解释**： 默认进程白名单策略 **取值范围**: - true：是 - false：否 
        :type default_policy: bool
        :param host_id_list: 主机id集合
        :type host_id_list: list[str]
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._policy_type = None
        self._learning_status = None
        self._learning_days = None
        self._specified_dir = None
        self._dir_list = None
        self._file_extension_list = None
        self._intercept = None
        self._auto_detect = None
        self._not_effect_host_num = None
        self._effect_host_num = None
        self._trust_num = None
        self._suspicious_num = None
        self._malicious_num = None
        self._unknown_num = None
        self._abnormal_info_list = None
        self._auto_confirm = None
        self._default_policy = None
        self._host_id_list = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_type is not None:
            self.policy_type = policy_type
        if learning_status is not None:
            self.learning_status = learning_status
        if learning_days is not None:
            self.learning_days = learning_days
        if specified_dir is not None:
            self.specified_dir = specified_dir
        if dir_list is not None:
            self.dir_list = dir_list
        if file_extension_list is not None:
            self.file_extension_list = file_extension_list
        if intercept is not None:
            self.intercept = intercept
        if auto_detect is not None:
            self.auto_detect = auto_detect
        if not_effect_host_num is not None:
            self.not_effect_host_num = not_effect_host_num
        if effect_host_num is not None:
            self.effect_host_num = effect_host_num
        if trust_num is not None:
            self.trust_num = trust_num
        if suspicious_num is not None:
            self.suspicious_num = suspicious_num
        if malicious_num is not None:
            self.malicious_num = malicious_num
        if unknown_num is not None:
            self.unknown_num = unknown_num
        if abnormal_info_list is not None:
            self.abnormal_info_list = abnormal_info_list
        if auto_confirm is not None:
            self.auto_confirm = auto_confirm
        if default_policy is not None:
            self.default_policy = default_policy
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AppWhitelistPolicyResponseInfo.

        策略ID

        :return: The policy_id of this AppWhitelistPolicyResponseInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AppWhitelistPolicyResponseInfo.

        策略ID

        :param policy_id: The policy_id of this AppWhitelistPolicyResponseInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AppWhitelistPolicyResponseInfo.

        策略名称

        :return: The policy_name of this AppWhitelistPolicyResponseInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AppWhitelistPolicyResponseInfo.

        策略名称

        :param policy_name: The policy_name of this AppWhitelistPolicyResponseInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_type(self):
        r"""Gets the policy_type of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 进程白名单策略类型 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行 

        :return: The policy_type of this AppWhitelistPolicyResponseInfo.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 进程白名单策略类型 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行 

        :param policy_type: The policy_type of this AppWhitelistPolicyResponseInfo.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def learning_status(self):
        r"""Gets the learning_status of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 服务器名称 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 

        :return: The learning_status of this AppWhitelistPolicyResponseInfo.
        :rtype: str
        """
        return self._learning_status

    @learning_status.setter
    def learning_status(self, learning_status):
        r"""Sets the learning_status of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 服务器名称 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 

        :param learning_status: The learning_status of this AppWhitelistPolicyResponseInfo.
        :type learning_status: str
        """
        self._learning_status = learning_status

    @property
    def learning_days(self):
        r"""Gets the learning_days of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 策略学习天数 **取值范围**: 最小值1，最大值1000 

        :return: The learning_days of this AppWhitelistPolicyResponseInfo.
        :rtype: int
        """
        return self._learning_days

    @learning_days.setter
    def learning_days(self, learning_days):
        r"""Sets the learning_days of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 策略学习天数 **取值范围**: 最小值1，最大值1000 

        :param learning_days: The learning_days of this AppWhitelistPolicyResponseInfo.
        :type learning_days: int
        """
        self._learning_days = learning_days

    @property
    def specified_dir(self):
        r"""Gets the specified_dir of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 是否指定学习目录 **约束限制**： 不涉及 **取值范围**: - true：是 - false：否 **默认取值**： 不涉及 

        :return: The specified_dir of this AppWhitelistPolicyResponseInfo.
        :rtype: bool
        """
        return self._specified_dir

    @specified_dir.setter
    def specified_dir(self, specified_dir):
        r"""Sets the specified_dir of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 是否指定学习目录 **约束限制**： 不涉及 **取值范围**: - true：是 - false：否 **默认取值**： 不涉及 

        :param specified_dir: The specified_dir of this AppWhitelistPolicyResponseInfo.
        :type specified_dir: bool
        """
        self._specified_dir = specified_dir

    @property
    def dir_list(self):
        r"""Gets the dir_list of this AppWhitelistPolicyResponseInfo.

        监控目录列表

        :return: The dir_list of this AppWhitelistPolicyResponseInfo.
        :rtype: list[str]
        """
        return self._dir_list

    @dir_list.setter
    def dir_list(self, dir_list):
        r"""Sets the dir_list of this AppWhitelistPolicyResponseInfo.

        监控目录列表

        :param dir_list: The dir_list of this AppWhitelistPolicyResponseInfo.
        :type dir_list: list[str]
        """
        self._dir_list = dir_list

    @property
    def file_extension_list(self):
        r"""Gets the file_extension_list of this AppWhitelistPolicyResponseInfo.

        监控文件后缀名列表

        :return: The file_extension_list of this AppWhitelistPolicyResponseInfo.
        :rtype: list[str]
        """
        return self._file_extension_list

    @file_extension_list.setter
    def file_extension_list(self, file_extension_list):
        r"""Sets the file_extension_list of this AppWhitelistPolicyResponseInfo.

        监控文件后缀名列表

        :param file_extension_list: The file_extension_list of this AppWhitelistPolicyResponseInfo.
        :type file_extension_list: list[str]
        """
        self._file_extension_list = file_extension_list

    @property
    def intercept(self):
        r"""Gets the intercept of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 是否开启阻断 **取值范围**: - true：是 - false：否 

        :return: The intercept of this AppWhitelistPolicyResponseInfo.
        :rtype: bool
        """
        return self._intercept

    @intercept.setter
    def intercept(self, intercept):
        r"""Sets the intercept of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 是否开启阻断 **取值范围**: - true：是 - false：否 

        :param intercept: The intercept of this AppWhitelistPolicyResponseInfo.
        :type intercept: bool
        """
        self._intercept = intercept

    @property
    def auto_detect(self):
        r"""Gets the auto_detect of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 是否自动开启检测 **取值范围**: - true：是 - false：否 

        :return: The auto_detect of this AppWhitelistPolicyResponseInfo.
        :rtype: bool
        """
        return self._auto_detect

    @auto_detect.setter
    def auto_detect(self, auto_detect):
        r"""Sets the auto_detect of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 是否自动开启检测 **取值范围**: - true：是 - false：否 

        :param auto_detect: The auto_detect of this AppWhitelistPolicyResponseInfo.
        :type auto_detect: bool
        """
        self._auto_detect = auto_detect

    @property
    def not_effect_host_num(self):
        r"""Gets the not_effect_host_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 学习完成策略未生效主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The not_effect_host_num of this AppWhitelistPolicyResponseInfo.
        :rtype: int
        """
        return self._not_effect_host_num

    @not_effect_host_num.setter
    def not_effect_host_num(self, not_effect_host_num):
        r"""Sets the not_effect_host_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 学习完成策略未生效主机数 **取值范围**: 最小值0，最大值2147483647 

        :param not_effect_host_num: The not_effect_host_num of this AppWhitelistPolicyResponseInfo.
        :type not_effect_host_num: int
        """
        self._not_effect_host_num = not_effect_host_num

    @property
    def effect_host_num(self):
        r"""Gets the effect_host_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 学习完成策略已生效主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The effect_host_num of this AppWhitelistPolicyResponseInfo.
        :rtype: int
        """
        return self._effect_host_num

    @effect_host_num.setter
    def effect_host_num(self, effect_host_num):
        r"""Sets the effect_host_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 学习完成策略已生效主机数 **取值范围**: 最小值0，最大值2147483647 

        :param effect_host_num: The effect_host_num of this AppWhitelistPolicyResponseInfo.
        :type effect_host_num: int
        """
        self._effect_host_num = effect_host_num

    @property
    def trust_num(self):
        r"""Gets the trust_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 识别可信进程数 **取值范围**: 最小值0，最大值2147483647 

        :return: The trust_num of this AppWhitelistPolicyResponseInfo.
        :rtype: int
        """
        return self._trust_num

    @trust_num.setter
    def trust_num(self, trust_num):
        r"""Sets the trust_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 识别可信进程数 **取值范围**: 最小值0，最大值2147483647 

        :param trust_num: The trust_num of this AppWhitelistPolicyResponseInfo.
        :type trust_num: int
        """
        self._trust_num = trust_num

    @property
    def suspicious_num(self):
        r"""Gets the suspicious_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 识别可疑进程数 **取值范围**: 最小值0，最大值2147483647 

        :return: The suspicious_num of this AppWhitelistPolicyResponseInfo.
        :rtype: int
        """
        return self._suspicious_num

    @suspicious_num.setter
    def suspicious_num(self, suspicious_num):
        r"""Sets the suspicious_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 识别可疑进程数 **取值范围**: 最小值0，最大值2147483647 

        :param suspicious_num: The suspicious_num of this AppWhitelistPolicyResponseInfo.
        :type suspicious_num: int
        """
        self._suspicious_num = suspicious_num

    @property
    def malicious_num(self):
        r"""Gets the malicious_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 识别恶意进程数 **取值范围**: 最小值0，最大值2147483647 

        :return: The malicious_num of this AppWhitelistPolicyResponseInfo.
        :rtype: int
        """
        return self._malicious_num

    @malicious_num.setter
    def malicious_num(self, malicious_num):
        r"""Sets the malicious_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 识别恶意进程数 **取值范围**: 最小值0，最大值2147483647 

        :param malicious_num: The malicious_num of this AppWhitelistPolicyResponseInfo.
        :type malicious_num: int
        """
        self._malicious_num = malicious_num

    @property
    def unknown_num(self):
        r"""Gets the unknown_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 识别未知进程数 **取值范围**: 最小值0，最大值2147483647 

        :return: The unknown_num of this AppWhitelistPolicyResponseInfo.
        :rtype: int
        """
        return self._unknown_num

    @unknown_num.setter
    def unknown_num(self, unknown_num):
        r"""Sets the unknown_num of this AppWhitelistPolicyResponseInfo.

        **参数解释**: 识别未知进程数 **取值范围**: 最小值0，最大值2147483647 

        :param unknown_num: The unknown_num of this AppWhitelistPolicyResponseInfo.
        :type unknown_num: int
        """
        self._unknown_num = unknown_num

    @property
    def abnormal_info_list(self):
        r"""Gets the abnormal_info_list of this AppWhitelistPolicyResponseInfo.

        学习异常原因列表

        :return: The abnormal_info_list of this AppWhitelistPolicyResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AppWhitelistAbnormalInfo`]
        """
        return self._abnormal_info_list

    @abnormal_info_list.setter
    def abnormal_info_list(self, abnormal_info_list):
        r"""Sets the abnormal_info_list of this AppWhitelistPolicyResponseInfo.

        学习异常原因列表

        :param abnormal_info_list: The abnormal_info_list of this AppWhitelistPolicyResponseInfo.
        :type abnormal_info_list: list[:class:`huaweicloudsdkhss.v5.AppWhitelistAbnormalInfo`]
        """
        self._abnormal_info_list = abnormal_info_list

    @property
    def auto_confirm(self):
        r"""Gets the auto_confirm of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 是否自动确认学习结果 **取值范围**: - true：是 - false：否 

        :return: The auto_confirm of this AppWhitelistPolicyResponseInfo.
        :rtype: bool
        """
        return self._auto_confirm

    @auto_confirm.setter
    def auto_confirm(self, auto_confirm):
        r"""Sets the auto_confirm of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 是否自动确认学习结果 **取值范围**: - true：是 - false：否 

        :param auto_confirm: The auto_confirm of this AppWhitelistPolicyResponseInfo.
        :type auto_confirm: bool
        """
        self._auto_confirm = auto_confirm

    @property
    def default_policy(self):
        r"""Gets the default_policy of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 默认进程白名单策略 **取值范围**: - true：是 - false：否 

        :return: The default_policy of this AppWhitelistPolicyResponseInfo.
        :rtype: bool
        """
        return self._default_policy

    @default_policy.setter
    def default_policy(self, default_policy):
        r"""Sets the default_policy of this AppWhitelistPolicyResponseInfo.

        **参数解释**： 默认进程白名单策略 **取值范围**: - true：是 - false：否 

        :param default_policy: The default_policy of this AppWhitelistPolicyResponseInfo.
        :type default_policy: bool
        """
        self._default_policy = default_policy

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this AppWhitelistPolicyResponseInfo.

        主机id集合

        :return: The host_id_list of this AppWhitelistPolicyResponseInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this AppWhitelistPolicyResponseInfo.

        主机id集合

        :param host_id_list: The host_id_list of this AppWhitelistPolicyResponseInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, AppWhitelistPolicyResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
