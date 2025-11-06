# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PwdCheckSubTagInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_tag': 'str',
        'checked': 'str',
        'check_rule_ids': 'list[str]'
    }

    attribute_map = {
        'sub_tag': 'sub_tag',
        'checked': 'checked',
        'check_rule_ids': 'check_rule_ids'
    }

    def __init__(self, sub_tag=None, checked=None, check_rule_ids=None):
        r"""PwdCheckSubTagInfo

        The model defined in huaweicloud sdk

        :param sub_tag: **参数解释** 口令检测二级tag **取值范围** - weakpwd - pwdcomplexity
        :type sub_tag: str
        :param checked: **参数解释** 检测范围。 **取值范围** - true: 如果sub_tag有值,则二级标签sub_tag下所有的检测项都会检测 - false: 如果sub_tag有值，则二级标签sub_tag下所有的检测项都不会检测。 - indeterminate: 部分检测，由check_rule_ids决定具体检测项。
        :type checked: str
        :param check_rule_ids: 检测项列表
        :type check_rule_ids: list[str]
        """
        
        

        self._sub_tag = None
        self._checked = None
        self._check_rule_ids = None
        self.discriminator = None

        if sub_tag is not None:
            self.sub_tag = sub_tag
        if checked is not None:
            self.checked = checked
        if check_rule_ids is not None:
            self.check_rule_ids = check_rule_ids

    @property
    def sub_tag(self):
        r"""Gets the sub_tag of this PwdCheckSubTagInfo.

        **参数解释** 口令检测二级tag **取值范围** - weakpwd - pwdcomplexity

        :return: The sub_tag of this PwdCheckSubTagInfo.
        :rtype: str
        """
        return self._sub_tag

    @sub_tag.setter
    def sub_tag(self, sub_tag):
        r"""Sets the sub_tag of this PwdCheckSubTagInfo.

        **参数解释** 口令检测二级tag **取值范围** - weakpwd - pwdcomplexity

        :param sub_tag: The sub_tag of this PwdCheckSubTagInfo.
        :type sub_tag: str
        """
        self._sub_tag = sub_tag

    @property
    def checked(self):
        r"""Gets the checked of this PwdCheckSubTagInfo.

        **参数解释** 检测范围。 **取值范围** - true: 如果sub_tag有值,则二级标签sub_tag下所有的检测项都会检测 - false: 如果sub_tag有值，则二级标签sub_tag下所有的检测项都不会检测。 - indeterminate: 部分检测，由check_rule_ids决定具体检测项。

        :return: The checked of this PwdCheckSubTagInfo.
        :rtype: str
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        r"""Sets the checked of this PwdCheckSubTagInfo.

        **参数解释** 检测范围。 **取值范围** - true: 如果sub_tag有值,则二级标签sub_tag下所有的检测项都会检测 - false: 如果sub_tag有值，则二级标签sub_tag下所有的检测项都不会检测。 - indeterminate: 部分检测，由check_rule_ids决定具体检测项。

        :param checked: The checked of this PwdCheckSubTagInfo.
        :type checked: str
        """
        self._checked = checked

    @property
    def check_rule_ids(self):
        r"""Gets the check_rule_ids of this PwdCheckSubTagInfo.

        检测项列表

        :return: The check_rule_ids of this PwdCheckSubTagInfo.
        :rtype: list[str]
        """
        return self._check_rule_ids

    @check_rule_ids.setter
    def check_rule_ids(self, check_rule_ids):
        r"""Sets the check_rule_ids of this PwdCheckSubTagInfo.

        检测项列表

        :param check_rule_ids: The check_rule_ids of this PwdCheckSubTagInfo.
        :type check_rule_ids: list[str]
        """
        self._check_rule_ids = check_rule_ids

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
        if not isinstance(other, PwdCheckSubTagInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
