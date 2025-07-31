# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPwdDirectoryInfo:

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
        'sub_tag': 'str',
        'checked': 'bool',
        'key': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'sub_tag': 'sub_tag',
        'checked': 'checked',
        'key': 'key'
    }

    def __init__(self, tag=None, sub_tag=None, checked=None, key=None):
        r"""ShowPwdDirectoryInfo

        The model defined in huaweicloud sdk

        :param tag: 弱口令及口令复杂度一级标签，包含如下:   - weakpwd_pwdcomplexity : 弱口令及口令复杂度检测   - weakpwd               : 弱口令检测
        :type tag: str
        :param sub_tag: 口令检查包含子标签，包含如下:   - weak_pwd : 经典弱口令检测   - pwd_complexity : 口令复杂度策略检
        :type sub_tag: str
        :param checked: **参数解释** 该项是否被选中 **取值范围**  - true : 被选中 - false: 未被选中
        :type checked: bool
        :param key: 表示目录中的唯一值:   - weak_pwd : 经典弱口令检测   - pwd_complexity : 口令复杂度策略检测
        :type key: str
        """
        
        

        self._tag = None
        self._sub_tag = None
        self._checked = None
        self._key = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if sub_tag is not None:
            self.sub_tag = sub_tag
        if checked is not None:
            self.checked = checked
        if key is not None:
            self.key = key

    @property
    def tag(self):
        r"""Gets the tag of this ShowPwdDirectoryInfo.

        弱口令及口令复杂度一级标签，包含如下:   - weakpwd_pwdcomplexity : 弱口令及口令复杂度检测   - weakpwd               : 弱口令检测

        :return: The tag of this ShowPwdDirectoryInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ShowPwdDirectoryInfo.

        弱口令及口令复杂度一级标签，包含如下:   - weakpwd_pwdcomplexity : 弱口令及口令复杂度检测   - weakpwd               : 弱口令检测

        :param tag: The tag of this ShowPwdDirectoryInfo.
        :type tag: str
        """
        self._tag = tag

    @property
    def sub_tag(self):
        r"""Gets the sub_tag of this ShowPwdDirectoryInfo.

        口令检查包含子标签，包含如下:   - weak_pwd : 经典弱口令检测   - pwd_complexity : 口令复杂度策略检

        :return: The sub_tag of this ShowPwdDirectoryInfo.
        :rtype: str
        """
        return self._sub_tag

    @sub_tag.setter
    def sub_tag(self, sub_tag):
        r"""Sets the sub_tag of this ShowPwdDirectoryInfo.

        口令检查包含子标签，包含如下:   - weak_pwd : 经典弱口令检测   - pwd_complexity : 口令复杂度策略检

        :param sub_tag: The sub_tag of this ShowPwdDirectoryInfo.
        :type sub_tag: str
        """
        self._sub_tag = sub_tag

    @property
    def checked(self):
        r"""Gets the checked of this ShowPwdDirectoryInfo.

        **参数解释** 该项是否被选中 **取值范围**  - true : 被选中 - false: 未被选中

        :return: The checked of this ShowPwdDirectoryInfo.
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        r"""Sets the checked of this ShowPwdDirectoryInfo.

        **参数解释** 该项是否被选中 **取值范围**  - true : 被选中 - false: 未被选中

        :param checked: The checked of this ShowPwdDirectoryInfo.
        :type checked: bool
        """
        self._checked = checked

    @property
    def key(self):
        r"""Gets the key of this ShowPwdDirectoryInfo.

        表示目录中的唯一值:   - weak_pwd : 经典弱口令检测   - pwd_complexity : 口令复杂度策略检测

        :return: The key of this ShowPwdDirectoryInfo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ShowPwdDirectoryInfo.

        表示目录中的唯一值:   - weak_pwd : 经典弱口令检测   - pwd_complexity : 口令复杂度策略检测

        :param key: The key of this ShowPwdDirectoryInfo.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, ShowPwdDirectoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
