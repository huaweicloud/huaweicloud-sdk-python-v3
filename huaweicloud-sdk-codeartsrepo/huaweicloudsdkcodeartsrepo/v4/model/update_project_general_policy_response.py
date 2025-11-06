# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProjectGeneralPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disable_fork': 'bool',
        'branch_name_regex': 'str',
        'tag_name_regex': 'str',
        'generate_pre_merge_ref': 'bool'
    }

    attribute_map = {
        'disable_fork': 'disable_fork',
        'branch_name_regex': 'branch_name_regex',
        'tag_name_regex': 'tag_name_regex',
        'generate_pre_merge_ref': 'generate_pre_merge_ref'
    }

    def __init__(self, disable_fork=None, branch_name_regex=None, tag_name_regex=None, generate_pre_merge_ref=None):
        r"""UpdateProjectGeneralPolicyResponse

        The model defined in huaweicloud sdk

        :param disable_fork: **参数解释：** 是否禁用fork。
        :type disable_fork: bool
        :param branch_name_regex: **参数解释：** 分支名称正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type branch_name_regex: str
        :param tag_name_regex: **参数解释：** 标签名正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type tag_name_regex: str
        :param generate_pre_merge_ref: **参数解释：** 生成合并请求预合并。
        :type generate_pre_merge_ref: bool
        """
        
        super().__init__()

        self._disable_fork = None
        self._branch_name_regex = None
        self._tag_name_regex = None
        self._generate_pre_merge_ref = None
        self.discriminator = None

        if disable_fork is not None:
            self.disable_fork = disable_fork
        if branch_name_regex is not None:
            self.branch_name_regex = branch_name_regex
        if tag_name_regex is not None:
            self.tag_name_regex = tag_name_regex
        if generate_pre_merge_ref is not None:
            self.generate_pre_merge_ref = generate_pre_merge_ref

    @property
    def disable_fork(self):
        r"""Gets the disable_fork of this UpdateProjectGeneralPolicyResponse.

        **参数解释：** 是否禁用fork。

        :return: The disable_fork of this UpdateProjectGeneralPolicyResponse.
        :rtype: bool
        """
        return self._disable_fork

    @disable_fork.setter
    def disable_fork(self, disable_fork):
        r"""Sets the disable_fork of this UpdateProjectGeneralPolicyResponse.

        **参数解释：** 是否禁用fork。

        :param disable_fork: The disable_fork of this UpdateProjectGeneralPolicyResponse.
        :type disable_fork: bool
        """
        self._disable_fork = disable_fork

    @property
    def branch_name_regex(self):
        r"""Gets the branch_name_regex of this UpdateProjectGeneralPolicyResponse.

        **参数解释：** 分支名称正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The branch_name_regex of this UpdateProjectGeneralPolicyResponse.
        :rtype: str
        """
        return self._branch_name_regex

    @branch_name_regex.setter
    def branch_name_regex(self, branch_name_regex):
        r"""Sets the branch_name_regex of this UpdateProjectGeneralPolicyResponse.

        **参数解释：** 分支名称正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param branch_name_regex: The branch_name_regex of this UpdateProjectGeneralPolicyResponse.
        :type branch_name_regex: str
        """
        self._branch_name_regex = branch_name_regex

    @property
    def tag_name_regex(self):
        r"""Gets the tag_name_regex of this UpdateProjectGeneralPolicyResponse.

        **参数解释：** 标签名正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The tag_name_regex of this UpdateProjectGeneralPolicyResponse.
        :rtype: str
        """
        return self._tag_name_regex

    @tag_name_regex.setter
    def tag_name_regex(self, tag_name_regex):
        r"""Sets the tag_name_regex of this UpdateProjectGeneralPolicyResponse.

        **参数解释：** 标签名正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param tag_name_regex: The tag_name_regex of this UpdateProjectGeneralPolicyResponse.
        :type tag_name_regex: str
        """
        self._tag_name_regex = tag_name_regex

    @property
    def generate_pre_merge_ref(self):
        r"""Gets the generate_pre_merge_ref of this UpdateProjectGeneralPolicyResponse.

        **参数解释：** 生成合并请求预合并。

        :return: The generate_pre_merge_ref of this UpdateProjectGeneralPolicyResponse.
        :rtype: bool
        """
        return self._generate_pre_merge_ref

    @generate_pre_merge_ref.setter
    def generate_pre_merge_ref(self, generate_pre_merge_ref):
        r"""Sets the generate_pre_merge_ref of this UpdateProjectGeneralPolicyResponse.

        **参数解释：** 生成合并请求预合并。

        :param generate_pre_merge_ref: The generate_pre_merge_ref of this UpdateProjectGeneralPolicyResponse.
        :type generate_pre_merge_ref: bool
        """
        self._generate_pre_merge_ref = generate_pre_merge_ref

    def to_dict(self):
        import warnings
        warnings.warn("UpdateProjectGeneralPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateProjectGeneralPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
