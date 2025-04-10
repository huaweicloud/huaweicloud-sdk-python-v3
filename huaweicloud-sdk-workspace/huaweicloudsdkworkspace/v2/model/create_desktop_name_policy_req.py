# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDesktopNamePolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'name_prefix': 'str',
        'digit_number': 'int',
        'start_number': 'int',
        'single_domain_user_inc': 'int',
        'is_default_policy': 'bool'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'name_prefix': 'name_prefix',
        'digit_number': 'digit_number',
        'start_number': 'start_number',
        'single_domain_user_inc': 'single_domain_user_inc',
        'is_default_policy': 'is_default_policy'
    }

    def __init__(self, policy_name=None, name_prefix=None, digit_number=None, start_number=None, single_domain_user_inc=None, is_default_policy=None):
        r"""CreateDesktopNamePolicyReq

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称，由数字、字母、中文、下划线组成，必须以字母或下划线开头，长度范围为1~30个字符。
        :type policy_name: str
        :param name_prefix: 策略前缀。
        :type name_prefix: str
        :param digit_number: 策略后缀有效位数。
        :type digit_number: int
        :param start_number: 策略后缀起始数字。
        :type start_number: int
        :param single_domain_user_inc: 是否单用户名递增。 - 1 单用户名递增。 - 0 租户递增。
        :type single_domain_user_inc: int
        :param is_default_policy: 是否为默认策略，true默认策略。
        :type is_default_policy: bool
        """
        
        

        self._policy_name = None
        self._name_prefix = None
        self._digit_number = None
        self._start_number = None
        self._single_domain_user_inc = None
        self._is_default_policy = None
        self.discriminator = None

        self.policy_name = policy_name
        self.name_prefix = name_prefix
        self.digit_number = digit_number
        self.start_number = start_number
        self.single_domain_user_inc = single_domain_user_inc
        if is_default_policy is not None:
            self.is_default_policy = is_default_policy

    @property
    def policy_name(self):
        r"""Gets the policy_name of this CreateDesktopNamePolicyReq.

        策略名称，由数字、字母、中文、下划线组成，必须以字母或下划线开头，长度范围为1~30个字符。

        :return: The policy_name of this CreateDesktopNamePolicyReq.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this CreateDesktopNamePolicyReq.

        策略名称，由数字、字母、中文、下划线组成，必须以字母或下划线开头，长度范围为1~30个字符。

        :param policy_name: The policy_name of this CreateDesktopNamePolicyReq.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def name_prefix(self):
        r"""Gets the name_prefix of this CreateDesktopNamePolicyReq.

        策略前缀。

        :return: The name_prefix of this CreateDesktopNamePolicyReq.
        :rtype: str
        """
        return self._name_prefix

    @name_prefix.setter
    def name_prefix(self, name_prefix):
        r"""Sets the name_prefix of this CreateDesktopNamePolicyReq.

        策略前缀。

        :param name_prefix: The name_prefix of this CreateDesktopNamePolicyReq.
        :type name_prefix: str
        """
        self._name_prefix = name_prefix

    @property
    def digit_number(self):
        r"""Gets the digit_number of this CreateDesktopNamePolicyReq.

        策略后缀有效位数。

        :return: The digit_number of this CreateDesktopNamePolicyReq.
        :rtype: int
        """
        return self._digit_number

    @digit_number.setter
    def digit_number(self, digit_number):
        r"""Sets the digit_number of this CreateDesktopNamePolicyReq.

        策略后缀有效位数。

        :param digit_number: The digit_number of this CreateDesktopNamePolicyReq.
        :type digit_number: int
        """
        self._digit_number = digit_number

    @property
    def start_number(self):
        r"""Gets the start_number of this CreateDesktopNamePolicyReq.

        策略后缀起始数字。

        :return: The start_number of this CreateDesktopNamePolicyReq.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        r"""Sets the start_number of this CreateDesktopNamePolicyReq.

        策略后缀起始数字。

        :param start_number: The start_number of this CreateDesktopNamePolicyReq.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def single_domain_user_inc(self):
        r"""Gets the single_domain_user_inc of this CreateDesktopNamePolicyReq.

        是否单用户名递增。 - 1 单用户名递增。 - 0 租户递增。

        :return: The single_domain_user_inc of this CreateDesktopNamePolicyReq.
        :rtype: int
        """
        return self._single_domain_user_inc

    @single_domain_user_inc.setter
    def single_domain_user_inc(self, single_domain_user_inc):
        r"""Sets the single_domain_user_inc of this CreateDesktopNamePolicyReq.

        是否单用户名递增。 - 1 单用户名递增。 - 0 租户递增。

        :param single_domain_user_inc: The single_domain_user_inc of this CreateDesktopNamePolicyReq.
        :type single_domain_user_inc: int
        """
        self._single_domain_user_inc = single_domain_user_inc

    @property
    def is_default_policy(self):
        r"""Gets the is_default_policy of this CreateDesktopNamePolicyReq.

        是否为默认策略，true默认策略。

        :return: The is_default_policy of this CreateDesktopNamePolicyReq.
        :rtype: bool
        """
        return self._is_default_policy

    @is_default_policy.setter
    def is_default_policy(self, is_default_policy):
        r"""Sets the is_default_policy of this CreateDesktopNamePolicyReq.

        是否为默认策略，true默认策略。

        :param is_default_policy: The is_default_policy of this CreateDesktopNamePolicyReq.
        :type is_default_policy: bool
        """
        self._is_default_policy = is_default_policy

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
        if not isinstance(other, CreateDesktopNamePolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
