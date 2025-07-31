# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeAppWhitelistPolicyRequestInfo:

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
        'learning_days': 'int',
        'specified_dir': 'bool',
        'intercept': 'bool',
        'auto_confirm': 'bool',
        'auto_detect': 'bool',
        'dir_list': 'list[str]',
        'ext_list': 'list[str]',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'policy_type': 'policy_type',
        'learning_days': 'learning_days',
        'specified_dir': 'specified_dir',
        'intercept': 'intercept',
        'auto_confirm': 'auto_confirm',
        'auto_detect': 'auto_detect',
        'dir_list': 'dir_list',
        'ext_list': 'ext_list',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, policy_id=None, policy_name=None, policy_type=None, learning_days=None, specified_dir=None, intercept=None, auto_confirm=None, auto_detect=None, dir_list=None, ext_list=None, host_id_list=None):
        r"""ChangeAppWhitelistPolicyRequestInfo

        The model defined in huaweicloud sdk

        :param policy_id: 策略ID
        :type policy_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_type: **参数解释**： 进程白名单策略类型进程白名单策略类型 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行 
        :type policy_type: str
        :param learning_days: **参数解释**: 策略学习天数 **取值范围**: 最小值1，最大值1000 
        :type learning_days: int
        :param specified_dir: **参数解释**： 是否指定学习目录 **约束限制**： 不涉及 **取值范围**: - true：是 - false：否 **默认取值**： 不涉及 
        :type specified_dir: bool
        :param intercept: **参数解释**： 是否开启阻断 **取值范围**: - true：是 - false：否 
        :type intercept: bool
        :param auto_confirm: **参数解释**： 是否自动确认学习结果 **取值范围**: - true：是 - false：否 
        :type auto_confirm: bool
        :param auto_detect: **参数解释**： 是否自动开启检测 **取值范围**: - true：是 - false：否 
        :type auto_detect: bool
        :param dir_list: 监控目录列表
        :type dir_list: list[str]
        :param ext_list: 监控文件后缀名列表
        :type ext_list: list[str]
        :param host_id_list: 主机id列表
        :type host_id_list: list[str]
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._policy_type = None
        self._learning_days = None
        self._specified_dir = None
        self._intercept = None
        self._auto_confirm = None
        self._auto_detect = None
        self._dir_list = None
        self._ext_list = None
        self._host_id_list = None
        self.discriminator = None

        self.policy_id = policy_id
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.learning_days = learning_days
        if specified_dir is not None:
            self.specified_dir = specified_dir
        self.intercept = intercept
        self.auto_confirm = auto_confirm
        self.auto_detect = auto_detect
        if dir_list is not None:
            self.dir_list = dir_list
        if ext_list is not None:
            self.ext_list = ext_list
        self.host_id_list = host_id_list

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ChangeAppWhitelistPolicyRequestInfo.

        策略ID

        :return: The policy_id of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ChangeAppWhitelistPolicyRequestInfo.

        策略ID

        :param policy_id: The policy_id of this ChangeAppWhitelistPolicyRequestInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ChangeAppWhitelistPolicyRequestInfo.

        策略名称

        :return: The policy_name of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ChangeAppWhitelistPolicyRequestInfo.

        策略名称

        :param policy_name: The policy_name of this ChangeAppWhitelistPolicyRequestInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_type(self):
        r"""Gets the policy_type of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**： 进程白名单策略类型进程白名单策略类型 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行 

        :return: The policy_type of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**： 进程白名单策略类型进程白名单策略类型 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行 

        :param policy_type: The policy_type of this ChangeAppWhitelistPolicyRequestInfo.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def learning_days(self):
        r"""Gets the learning_days of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**: 策略学习天数 **取值范围**: 最小值1，最大值1000 

        :return: The learning_days of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: int
        """
        return self._learning_days

    @learning_days.setter
    def learning_days(self, learning_days):
        r"""Sets the learning_days of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**: 策略学习天数 **取值范围**: 最小值1，最大值1000 

        :param learning_days: The learning_days of this ChangeAppWhitelistPolicyRequestInfo.
        :type learning_days: int
        """
        self._learning_days = learning_days

    @property
    def specified_dir(self):
        r"""Gets the specified_dir of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**： 是否指定学习目录 **约束限制**： 不涉及 **取值范围**: - true：是 - false：否 **默认取值**： 不涉及 

        :return: The specified_dir of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: bool
        """
        return self._specified_dir

    @specified_dir.setter
    def specified_dir(self, specified_dir):
        r"""Sets the specified_dir of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**： 是否指定学习目录 **约束限制**： 不涉及 **取值范围**: - true：是 - false：否 **默认取值**： 不涉及 

        :param specified_dir: The specified_dir of this ChangeAppWhitelistPolicyRequestInfo.
        :type specified_dir: bool
        """
        self._specified_dir = specified_dir

    @property
    def intercept(self):
        r"""Gets the intercept of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**： 是否开启阻断 **取值范围**: - true：是 - false：否 

        :return: The intercept of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: bool
        """
        return self._intercept

    @intercept.setter
    def intercept(self, intercept):
        r"""Sets the intercept of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**： 是否开启阻断 **取值范围**: - true：是 - false：否 

        :param intercept: The intercept of this ChangeAppWhitelistPolicyRequestInfo.
        :type intercept: bool
        """
        self._intercept = intercept

    @property
    def auto_confirm(self):
        r"""Gets the auto_confirm of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**： 是否自动确认学习结果 **取值范围**: - true：是 - false：否 

        :return: The auto_confirm of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: bool
        """
        return self._auto_confirm

    @auto_confirm.setter
    def auto_confirm(self, auto_confirm):
        r"""Sets the auto_confirm of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**： 是否自动确认学习结果 **取值范围**: - true：是 - false：否 

        :param auto_confirm: The auto_confirm of this ChangeAppWhitelistPolicyRequestInfo.
        :type auto_confirm: bool
        """
        self._auto_confirm = auto_confirm

    @property
    def auto_detect(self):
        r"""Gets the auto_detect of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**： 是否自动开启检测 **取值范围**: - true：是 - false：否 

        :return: The auto_detect of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: bool
        """
        return self._auto_detect

    @auto_detect.setter
    def auto_detect(self, auto_detect):
        r"""Sets the auto_detect of this ChangeAppWhitelistPolicyRequestInfo.

        **参数解释**： 是否自动开启检测 **取值范围**: - true：是 - false：否 

        :param auto_detect: The auto_detect of this ChangeAppWhitelistPolicyRequestInfo.
        :type auto_detect: bool
        """
        self._auto_detect = auto_detect

    @property
    def dir_list(self):
        r"""Gets the dir_list of this ChangeAppWhitelistPolicyRequestInfo.

        监控目录列表

        :return: The dir_list of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: list[str]
        """
        return self._dir_list

    @dir_list.setter
    def dir_list(self, dir_list):
        r"""Sets the dir_list of this ChangeAppWhitelistPolicyRequestInfo.

        监控目录列表

        :param dir_list: The dir_list of this ChangeAppWhitelistPolicyRequestInfo.
        :type dir_list: list[str]
        """
        self._dir_list = dir_list

    @property
    def ext_list(self):
        r"""Gets the ext_list of this ChangeAppWhitelistPolicyRequestInfo.

        监控文件后缀名列表

        :return: The ext_list of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: list[str]
        """
        return self._ext_list

    @ext_list.setter
    def ext_list(self, ext_list):
        r"""Sets the ext_list of this ChangeAppWhitelistPolicyRequestInfo.

        监控文件后缀名列表

        :param ext_list: The ext_list of this ChangeAppWhitelistPolicyRequestInfo.
        :type ext_list: list[str]
        """
        self._ext_list = ext_list

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this ChangeAppWhitelistPolicyRequestInfo.

        主机id列表

        :return: The host_id_list of this ChangeAppWhitelistPolicyRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this ChangeAppWhitelistPolicyRequestInfo.

        主机id列表

        :param host_id_list: The host_id_list of this ChangeAppWhitelistPolicyRequestInfo.
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
        if not isinstance(other, ChangeAppWhitelistPolicyRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
