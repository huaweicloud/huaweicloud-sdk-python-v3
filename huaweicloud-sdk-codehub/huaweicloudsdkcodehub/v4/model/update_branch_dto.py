# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBranchDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_branch': 'str',
        'old_branch': 'str'
    }

    attribute_map = {
        'new_branch': 'new_branch',
        'old_branch': 'old_branch'
    }

    def __init__(self, new_branch=None, old_branch=None):
        r"""UpdateBranchDto

        The model defined in huaweicloud sdk

        :param new_branch: **参数解释：** 新分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ &lt; ~ ^ : ? * ! ( ) &#39; \&quot; | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。
        :type new_branch: str
        :param old_branch: **参数解释：** 基于分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ &lt; ~ ^ : ? * ! ( ) &#39; \&quot; | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。
        :type old_branch: str
        """
        
        

        self._new_branch = None
        self._old_branch = None
        self.discriminator = None

        self.new_branch = new_branch
        self.old_branch = old_branch

    @property
    def new_branch(self):
        r"""Gets the new_branch of this UpdateBranchDto.

        **参数解释：** 新分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :return: The new_branch of this UpdateBranchDto.
        :rtype: str
        """
        return self._new_branch

    @new_branch.setter
    def new_branch(self, new_branch):
        r"""Sets the new_branch of this UpdateBranchDto.

        **参数解释：** 新分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :param new_branch: The new_branch of this UpdateBranchDto.
        :type new_branch: str
        """
        self._new_branch = new_branch

    @property
    def old_branch(self):
        r"""Gets the old_branch of this UpdateBranchDto.

        **参数解释：** 基于分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :return: The old_branch of this UpdateBranchDto.
        :rtype: str
        """
        return self._old_branch

    @old_branch.setter
    def old_branch(self, old_branch):
        r"""Sets the old_branch of this UpdateBranchDto.

        **参数解释：** 基于分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :param old_branch: The old_branch of this UpdateBranchDto.
        :type old_branch: str
        """
        self._old_branch = old_branch

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
        if not isinstance(other, UpdateBranchDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
