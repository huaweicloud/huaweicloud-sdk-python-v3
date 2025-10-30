# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PwdCheckTagInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag': 'str',
        'checked': 'str',
        'sub_tags': 'list[PwdCheckSubTagInfo]'
    }

    attribute_map = {
        'tag': 'tag',
        'checked': 'checked',
        'sub_tags': 'sub_tags'
    }

    def __init__(self, tag=None, checked=None, sub_tags=None):
        r"""PwdCheckTagInfo

        The model defined in huaweicloud sdk

        :param tag: **参数解释** 口令检测一级tag **取值范围** - weakpwd_pwdcomplexity
        :type tag: str
        :param checked: **参数解释** 检测范围。 **取值范围** - true: 如果tag有值,则一级标签tag下所有的检测项都会检测。 - false: 如果tag有值，则一级标签tag下所有的检测项都不会检测。 - indeterminate: 部分检测，具体检测项由sub_tags决定。
        :type checked: str
        :param sub_tags: 服务器风险TOP5列表
        :type sub_tags: list[:class:`huaweicloudsdkhss.v5.PwdCheckSubTagInfo`]
        """
        
        

        self._tag = None
        self._checked = None
        self._sub_tags = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if checked is not None:
            self.checked = checked
        if sub_tags is not None:
            self.sub_tags = sub_tags

    @property
    def tag(self):
        r"""Gets the tag of this PwdCheckTagInfo.

        **参数解释** 口令检测一级tag **取值范围** - weakpwd_pwdcomplexity

        :return: The tag of this PwdCheckTagInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this PwdCheckTagInfo.

        **参数解释** 口令检测一级tag **取值范围** - weakpwd_pwdcomplexity

        :param tag: The tag of this PwdCheckTagInfo.
        :type tag: str
        """
        self._tag = tag

    @property
    def checked(self):
        r"""Gets the checked of this PwdCheckTagInfo.

        **参数解释** 检测范围。 **取值范围** - true: 如果tag有值,则一级标签tag下所有的检测项都会检测。 - false: 如果tag有值，则一级标签tag下所有的检测项都不会检测。 - indeterminate: 部分检测，具体检测项由sub_tags决定。

        :return: The checked of this PwdCheckTagInfo.
        :rtype: str
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        r"""Sets the checked of this PwdCheckTagInfo.

        **参数解释** 检测范围。 **取值范围** - true: 如果tag有值,则一级标签tag下所有的检测项都会检测。 - false: 如果tag有值，则一级标签tag下所有的检测项都不会检测。 - indeterminate: 部分检测，具体检测项由sub_tags决定。

        :param checked: The checked of this PwdCheckTagInfo.
        :type checked: str
        """
        self._checked = checked

    @property
    def sub_tags(self):
        r"""Gets the sub_tags of this PwdCheckTagInfo.

        服务器风险TOP5列表

        :return: The sub_tags of this PwdCheckTagInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.PwdCheckSubTagInfo`]
        """
        return self._sub_tags

    @sub_tags.setter
    def sub_tags(self, sub_tags):
        r"""Sets the sub_tags of this PwdCheckTagInfo.

        服务器风险TOP5列表

        :param sub_tags: The sub_tags of this PwdCheckTagInfo.
        :type sub_tags: list[:class:`huaweicloudsdkhss.v5.PwdCheckSubTagInfo`]
        """
        self._sub_tags = sub_tags

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
        if not isinstance(other, PwdCheckTagInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
