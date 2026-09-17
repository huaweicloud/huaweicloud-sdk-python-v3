# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlLimitingInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_use': 'bool',
        'case_sensitive': 'bool',
        'expire': 'bool',
        'error_msg': 'str',
        'instance_type': 'str',
        'instance_detail_version': 'str',
        'can_readonly_set_rule': 'bool',
        'readonly_set_rule_msg': 'str',
        'max_rule_limit': 'int',
        'can_add_insert_type': 'bool',
        'support_key_str': 'bool'
    }

    attribute_map = {
        'can_use': 'can_use',
        'case_sensitive': 'case_sensitive',
        'expire': 'expire',
        'error_msg': 'error_msg',
        'instance_type': 'instance_type',
        'instance_detail_version': 'instance_detail_version',
        'can_readonly_set_rule': 'can_readonly_set_rule',
        'readonly_set_rule_msg': 'readonly_set_rule_msg',
        'max_rule_limit': 'max_rule_limit',
        'can_add_insert_type': 'can_add_insert_type',
        'support_key_str': 'support_key_str'
    }

    def __init__(self, can_use=None, case_sensitive=None, expire=None, error_msg=None, instance_type=None, instance_detail_version=None, can_readonly_set_rule=None, readonly_set_rule_msg=None, max_rule_limit=None, can_add_insert_type=None, support_key_str=None):
        r"""ShowSqlLimitingInfoResponse

        The model defined in huaweicloud sdk

        :param can_use: 实例能否使用SQL限流功能
        :type can_use: bool
        :param case_sensitive: 是否大小写敏感
        :type case_sensitive: bool
        :param expire: 是否支持展示过期
        :type expire: bool
        :param error_msg: 当canUse为False时展示错误信息
        :type error_msg: str
        :param instance_type: 实例类型
        :type instance_type: str
        :param instance_detail_version: 实例详细版本号
        :type instance_detail_version: str
        :param can_readonly_set_rule: 只读实例是否可以添加、删除限流规则
        :type can_readonly_set_rule: bool
        :param readonly_set_rule_msg: 当canReadonlySetRule为False时展示的提示
        :type readonly_set_rule_msg: str
        :param max_rule_limit: 最大可用SQL限流规则数
        :type max_rule_limit: int
        :param can_add_insert_type: 是否支持添加insert类型sql
        :type can_add_insert_type: bool
        :param support_key_str: 实例能否使用关键字自治限流功能
        :type support_key_str: bool
        """
        
        super().__init__()

        self._can_use = None
        self._case_sensitive = None
        self._expire = None
        self._error_msg = None
        self._instance_type = None
        self._instance_detail_version = None
        self._can_readonly_set_rule = None
        self._readonly_set_rule_msg = None
        self._max_rule_limit = None
        self._can_add_insert_type = None
        self._support_key_str = None
        self.discriminator = None

        if can_use is not None:
            self.can_use = can_use
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if expire is not None:
            self.expire = expire
        if error_msg is not None:
            self.error_msg = error_msg
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_detail_version is not None:
            self.instance_detail_version = instance_detail_version
        if can_readonly_set_rule is not None:
            self.can_readonly_set_rule = can_readonly_set_rule
        if readonly_set_rule_msg is not None:
            self.readonly_set_rule_msg = readonly_set_rule_msg
        if max_rule_limit is not None:
            self.max_rule_limit = max_rule_limit
        if can_add_insert_type is not None:
            self.can_add_insert_type = can_add_insert_type
        if support_key_str is not None:
            self.support_key_str = support_key_str

    @property
    def can_use(self):
        r"""Gets the can_use of this ShowSqlLimitingInfoResponse.

        实例能否使用SQL限流功能

        :return: The can_use of this ShowSqlLimitingInfoResponse.
        :rtype: bool
        """
        return self._can_use

    @can_use.setter
    def can_use(self, can_use):
        r"""Sets the can_use of this ShowSqlLimitingInfoResponse.

        实例能否使用SQL限流功能

        :param can_use: The can_use of this ShowSqlLimitingInfoResponse.
        :type can_use: bool
        """
        self._can_use = can_use

    @property
    def case_sensitive(self):
        r"""Gets the case_sensitive of this ShowSqlLimitingInfoResponse.

        是否大小写敏感

        :return: The case_sensitive of this ShowSqlLimitingInfoResponse.
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        r"""Sets the case_sensitive of this ShowSqlLimitingInfoResponse.

        是否大小写敏感

        :param case_sensitive: The case_sensitive of this ShowSqlLimitingInfoResponse.
        :type case_sensitive: bool
        """
        self._case_sensitive = case_sensitive

    @property
    def expire(self):
        r"""Gets the expire of this ShowSqlLimitingInfoResponse.

        是否支持展示过期

        :return: The expire of this ShowSqlLimitingInfoResponse.
        :rtype: bool
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        r"""Sets the expire of this ShowSqlLimitingInfoResponse.

        是否支持展示过期

        :param expire: The expire of this ShowSqlLimitingInfoResponse.
        :type expire: bool
        """
        self._expire = expire

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ShowSqlLimitingInfoResponse.

        当canUse为False时展示错误信息

        :return: The error_msg of this ShowSqlLimitingInfoResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ShowSqlLimitingInfoResponse.

        当canUse为False时展示错误信息

        :param error_msg: The error_msg of this ShowSqlLimitingInfoResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ShowSqlLimitingInfoResponse.

        实例类型

        :return: The instance_type of this ShowSqlLimitingInfoResponse.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ShowSqlLimitingInfoResponse.

        实例类型

        :param instance_type: The instance_type of this ShowSqlLimitingInfoResponse.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_detail_version(self):
        r"""Gets the instance_detail_version of this ShowSqlLimitingInfoResponse.

        实例详细版本号

        :return: The instance_detail_version of this ShowSqlLimitingInfoResponse.
        :rtype: str
        """
        return self._instance_detail_version

    @instance_detail_version.setter
    def instance_detail_version(self, instance_detail_version):
        r"""Sets the instance_detail_version of this ShowSqlLimitingInfoResponse.

        实例详细版本号

        :param instance_detail_version: The instance_detail_version of this ShowSqlLimitingInfoResponse.
        :type instance_detail_version: str
        """
        self._instance_detail_version = instance_detail_version

    @property
    def can_readonly_set_rule(self):
        r"""Gets the can_readonly_set_rule of this ShowSqlLimitingInfoResponse.

        只读实例是否可以添加、删除限流规则

        :return: The can_readonly_set_rule of this ShowSqlLimitingInfoResponse.
        :rtype: bool
        """
        return self._can_readonly_set_rule

    @can_readonly_set_rule.setter
    def can_readonly_set_rule(self, can_readonly_set_rule):
        r"""Sets the can_readonly_set_rule of this ShowSqlLimitingInfoResponse.

        只读实例是否可以添加、删除限流规则

        :param can_readonly_set_rule: The can_readonly_set_rule of this ShowSqlLimitingInfoResponse.
        :type can_readonly_set_rule: bool
        """
        self._can_readonly_set_rule = can_readonly_set_rule

    @property
    def readonly_set_rule_msg(self):
        r"""Gets the readonly_set_rule_msg of this ShowSqlLimitingInfoResponse.

        当canReadonlySetRule为False时展示的提示

        :return: The readonly_set_rule_msg of this ShowSqlLimitingInfoResponse.
        :rtype: str
        """
        return self._readonly_set_rule_msg

    @readonly_set_rule_msg.setter
    def readonly_set_rule_msg(self, readonly_set_rule_msg):
        r"""Sets the readonly_set_rule_msg of this ShowSqlLimitingInfoResponse.

        当canReadonlySetRule为False时展示的提示

        :param readonly_set_rule_msg: The readonly_set_rule_msg of this ShowSqlLimitingInfoResponse.
        :type readonly_set_rule_msg: str
        """
        self._readonly_set_rule_msg = readonly_set_rule_msg

    @property
    def max_rule_limit(self):
        r"""Gets the max_rule_limit of this ShowSqlLimitingInfoResponse.

        最大可用SQL限流规则数

        :return: The max_rule_limit of this ShowSqlLimitingInfoResponse.
        :rtype: int
        """
        return self._max_rule_limit

    @max_rule_limit.setter
    def max_rule_limit(self, max_rule_limit):
        r"""Sets the max_rule_limit of this ShowSqlLimitingInfoResponse.

        最大可用SQL限流规则数

        :param max_rule_limit: The max_rule_limit of this ShowSqlLimitingInfoResponse.
        :type max_rule_limit: int
        """
        self._max_rule_limit = max_rule_limit

    @property
    def can_add_insert_type(self):
        r"""Gets the can_add_insert_type of this ShowSqlLimitingInfoResponse.

        是否支持添加insert类型sql

        :return: The can_add_insert_type of this ShowSqlLimitingInfoResponse.
        :rtype: bool
        """
        return self._can_add_insert_type

    @can_add_insert_type.setter
    def can_add_insert_type(self, can_add_insert_type):
        r"""Sets the can_add_insert_type of this ShowSqlLimitingInfoResponse.

        是否支持添加insert类型sql

        :param can_add_insert_type: The can_add_insert_type of this ShowSqlLimitingInfoResponse.
        :type can_add_insert_type: bool
        """
        self._can_add_insert_type = can_add_insert_type

    @property
    def support_key_str(self):
        r"""Gets the support_key_str of this ShowSqlLimitingInfoResponse.

        实例能否使用关键字自治限流功能

        :return: The support_key_str of this ShowSqlLimitingInfoResponse.
        :rtype: bool
        """
        return self._support_key_str

    @support_key_str.setter
    def support_key_str(self, support_key_str):
        r"""Sets the support_key_str of this ShowSqlLimitingInfoResponse.

        实例能否使用关键字自治限流功能

        :param support_key_str: The support_key_str of this ShowSqlLimitingInfoResponse.
        :type support_key_str: bool
        """
        self._support_key_str = support_key_str

    def to_dict(self):
        import warnings
        warnings.warn("ShowSqlLimitingInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSqlLimitingInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
