# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppWhitelistPolicyResponse(SdkResponse):

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
        'intercept': 'bool',
        'update_time': 'int',
        'total_num': 'int',
        'unconfirmed_num': 'int',
        'trust_num': 'int',
        'suspicious_num': 'int',
        'malicious_num': 'int',
        'unknown_num': 'int',
        'auto_apply': 'bool'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'policy_type': 'policy_type',
        'intercept': 'intercept',
        'update_time': 'update_time',
        'total_num': 'total_num',
        'unconfirmed_num': 'unconfirmed_num',
        'trust_num': 'trust_num',
        'suspicious_num': 'suspicious_num',
        'malicious_num': 'malicious_num',
        'unknown_num': 'unknown_num',
        'auto_apply': 'auto_apply'
    }

    def __init__(self, policy_id=None, policy_name=None, policy_type=None, intercept=None, update_time=None, total_num=None, unconfirmed_num=None, trust_num=None, suspicious_num=None, malicious_num=None, unknown_num=None, auto_apply=None):
        r"""ShowAppWhitelistPolicyResponse

        The model defined in huaweicloud sdk

        :param policy_id: 策略ID
        :type policy_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_type: **参数解释**： 进程白名单策略类型 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行 
        :type policy_type: str
        :param intercept: **参数解释**： 是否开启阻断 **取值范围**: - true：是 - false：否 
        :type intercept: bool
        :param update_time: 更新时间，毫秒
        :type update_time: int
        :param total_num: **参数解释**: 进程总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_num: int
        :param unconfirmed_num: **参数解释**: 待确认进程数 **取值范围**: 最小值0，最大值2147483647 
        :type unconfirmed_num: int
        :param trust_num: **参数解释**: 识别可信进程数 **取值范围**: 最小值0，最大值2147483647 
        :type trust_num: int
        :param suspicious_num: **参数解释**: 识别可疑进程数 **取值范围**: 最小值0，最大值2147483647 
        :type suspicious_num: int
        :param malicious_num: **参数解释**: 识别恶意进程数 **取值范围**: 最小值0，最大值2147483647 
        :type malicious_num: int
        :param unknown_num: **参数解释**: 识别未知进程数 **取值范围**: 最小值0，最大值2147483647 
        :type unknown_num: int
        :param auto_apply: **参数解释**： 是否自动应用策略 **取值范围**: - true：是 - false：否 
        :type auto_apply: bool
        """
        
        super(ShowAppWhitelistPolicyResponse, self).__init__()

        self._policy_id = None
        self._policy_name = None
        self._policy_type = None
        self._intercept = None
        self._update_time = None
        self._total_num = None
        self._unconfirmed_num = None
        self._trust_num = None
        self._suspicious_num = None
        self._malicious_num = None
        self._unknown_num = None
        self._auto_apply = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_type is not None:
            self.policy_type = policy_type
        if intercept is not None:
            self.intercept = intercept
        if update_time is not None:
            self.update_time = update_time
        if total_num is not None:
            self.total_num = total_num
        if unconfirmed_num is not None:
            self.unconfirmed_num = unconfirmed_num
        if trust_num is not None:
            self.trust_num = trust_num
        if suspicious_num is not None:
            self.suspicious_num = suspicious_num
        if malicious_num is not None:
            self.malicious_num = malicious_num
        if unknown_num is not None:
            self.unknown_num = unknown_num
        if auto_apply is not None:
            self.auto_apply = auto_apply

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowAppWhitelistPolicyResponse.

        策略ID

        :return: The policy_id of this ShowAppWhitelistPolicyResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowAppWhitelistPolicyResponse.

        策略ID

        :param policy_id: The policy_id of this ShowAppWhitelistPolicyResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ShowAppWhitelistPolicyResponse.

        策略名称

        :return: The policy_name of this ShowAppWhitelistPolicyResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ShowAppWhitelistPolicyResponse.

        策略名称

        :param policy_name: The policy_name of this ShowAppWhitelistPolicyResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_type(self):
        r"""Gets the policy_type of this ShowAppWhitelistPolicyResponse.

        **参数解释**： 进程白名单策略类型 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行 

        :return: The policy_type of this ShowAppWhitelistPolicyResponse.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this ShowAppWhitelistPolicyResponse.

        **参数解释**： 进程白名单策略类型 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行 

        :param policy_type: The policy_type of this ShowAppWhitelistPolicyResponse.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def intercept(self):
        r"""Gets the intercept of this ShowAppWhitelistPolicyResponse.

        **参数解释**： 是否开启阻断 **取值范围**: - true：是 - false：否 

        :return: The intercept of this ShowAppWhitelistPolicyResponse.
        :rtype: bool
        """
        return self._intercept

    @intercept.setter
    def intercept(self, intercept):
        r"""Sets the intercept of this ShowAppWhitelistPolicyResponse.

        **参数解释**： 是否开启阻断 **取值范围**: - true：是 - false：否 

        :param intercept: The intercept of this ShowAppWhitelistPolicyResponse.
        :type intercept: bool
        """
        self._intercept = intercept

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowAppWhitelistPolicyResponse.

        更新时间，毫秒

        :return: The update_time of this ShowAppWhitelistPolicyResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowAppWhitelistPolicyResponse.

        更新时间，毫秒

        :param update_time: The update_time of this ShowAppWhitelistPolicyResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 进程总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_num of this ShowAppWhitelistPolicyResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 进程总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_num: The total_num of this ShowAppWhitelistPolicyResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def unconfirmed_num(self):
        r"""Gets the unconfirmed_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 待确认进程数 **取值范围**: 最小值0，最大值2147483647 

        :return: The unconfirmed_num of this ShowAppWhitelistPolicyResponse.
        :rtype: int
        """
        return self._unconfirmed_num

    @unconfirmed_num.setter
    def unconfirmed_num(self, unconfirmed_num):
        r"""Sets the unconfirmed_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 待确认进程数 **取值范围**: 最小值0，最大值2147483647 

        :param unconfirmed_num: The unconfirmed_num of this ShowAppWhitelistPolicyResponse.
        :type unconfirmed_num: int
        """
        self._unconfirmed_num = unconfirmed_num

    @property
    def trust_num(self):
        r"""Gets the trust_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 识别可信进程数 **取值范围**: 最小值0，最大值2147483647 

        :return: The trust_num of this ShowAppWhitelistPolicyResponse.
        :rtype: int
        """
        return self._trust_num

    @trust_num.setter
    def trust_num(self, trust_num):
        r"""Sets the trust_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 识别可信进程数 **取值范围**: 最小值0，最大值2147483647 

        :param trust_num: The trust_num of this ShowAppWhitelistPolicyResponse.
        :type trust_num: int
        """
        self._trust_num = trust_num

    @property
    def suspicious_num(self):
        r"""Gets the suspicious_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 识别可疑进程数 **取值范围**: 最小值0，最大值2147483647 

        :return: The suspicious_num of this ShowAppWhitelistPolicyResponse.
        :rtype: int
        """
        return self._suspicious_num

    @suspicious_num.setter
    def suspicious_num(self, suspicious_num):
        r"""Sets the suspicious_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 识别可疑进程数 **取值范围**: 最小值0，最大值2147483647 

        :param suspicious_num: The suspicious_num of this ShowAppWhitelistPolicyResponse.
        :type suspicious_num: int
        """
        self._suspicious_num = suspicious_num

    @property
    def malicious_num(self):
        r"""Gets the malicious_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 识别恶意进程数 **取值范围**: 最小值0，最大值2147483647 

        :return: The malicious_num of this ShowAppWhitelistPolicyResponse.
        :rtype: int
        """
        return self._malicious_num

    @malicious_num.setter
    def malicious_num(self, malicious_num):
        r"""Sets the malicious_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 识别恶意进程数 **取值范围**: 最小值0，最大值2147483647 

        :param malicious_num: The malicious_num of this ShowAppWhitelistPolicyResponse.
        :type malicious_num: int
        """
        self._malicious_num = malicious_num

    @property
    def unknown_num(self):
        r"""Gets the unknown_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 识别未知进程数 **取值范围**: 最小值0，最大值2147483647 

        :return: The unknown_num of this ShowAppWhitelistPolicyResponse.
        :rtype: int
        """
        return self._unknown_num

    @unknown_num.setter
    def unknown_num(self, unknown_num):
        r"""Sets the unknown_num of this ShowAppWhitelistPolicyResponse.

        **参数解释**: 识别未知进程数 **取值范围**: 最小值0，最大值2147483647 

        :param unknown_num: The unknown_num of this ShowAppWhitelistPolicyResponse.
        :type unknown_num: int
        """
        self._unknown_num = unknown_num

    @property
    def auto_apply(self):
        r"""Gets the auto_apply of this ShowAppWhitelistPolicyResponse.

        **参数解释**： 是否自动应用策略 **取值范围**: - true：是 - false：否 

        :return: The auto_apply of this ShowAppWhitelistPolicyResponse.
        :rtype: bool
        """
        return self._auto_apply

    @auto_apply.setter
    def auto_apply(self, auto_apply):
        r"""Sets the auto_apply of this ShowAppWhitelistPolicyResponse.

        **参数解释**： 是否自动应用策略 **取值范围**: - true：是 - false：否 

        :param auto_apply: The auto_apply of this ShowAppWhitelistPolicyResponse.
        :type auto_apply: bool
        """
        self._auto_apply = auto_apply

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
        if not isinstance(other, ShowAppWhitelistPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
