# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBranchNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_branch_name': 'str',
        'old_branch_commit_id': 'str',
        'new_branch_name': 'str',
        'new_branch_commit_id': 'str'
    }

    attribute_map = {
        'old_branch_name': 'old_branch_name',
        'old_branch_commit_id': 'old_branch_commit_id',
        'new_branch_name': 'new_branch_name',
        'new_branch_commit_id': 'new_branch_commit_id'
    }

    def __init__(self, old_branch_name=None, old_branch_commit_id=None, new_branch_name=None, new_branch_commit_id=None):
        r"""UpdateBranchNameResponse

        The model defined in huaweicloud sdk

        :param old_branch_name: **参数解释：** 旧分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ &lt; ~ ^ : ? * ! ( ) &#39; \&quot; | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。
        :type old_branch_name: str
        :param old_branch_commit_id: **参数解释：** 旧分支最新提交ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type old_branch_commit_id: str
        :param new_branch_name: **参数解释：** 新分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ &lt; ~ ^ : ? * ! ( ) &#39; \&quot; | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。
        :type new_branch_name: str
        :param new_branch_commit_id: **参数解释：** 新分支最新提交ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type new_branch_commit_id: str
        """
        
        super(UpdateBranchNameResponse, self).__init__()

        self._old_branch_name = None
        self._old_branch_commit_id = None
        self._new_branch_name = None
        self._new_branch_commit_id = None
        self.discriminator = None

        if old_branch_name is not None:
            self.old_branch_name = old_branch_name
        if old_branch_commit_id is not None:
            self.old_branch_commit_id = old_branch_commit_id
        if new_branch_name is not None:
            self.new_branch_name = new_branch_name
        if new_branch_commit_id is not None:
            self.new_branch_commit_id = new_branch_commit_id

    @property
    def old_branch_name(self):
        r"""Gets the old_branch_name of this UpdateBranchNameResponse.

        **参数解释：** 旧分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :return: The old_branch_name of this UpdateBranchNameResponse.
        :rtype: str
        """
        return self._old_branch_name

    @old_branch_name.setter
    def old_branch_name(self, old_branch_name):
        r"""Sets the old_branch_name of this UpdateBranchNameResponse.

        **参数解释：** 旧分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :param old_branch_name: The old_branch_name of this UpdateBranchNameResponse.
        :type old_branch_name: str
        """
        self._old_branch_name = old_branch_name

    @property
    def old_branch_commit_id(self):
        r"""Gets the old_branch_commit_id of this UpdateBranchNameResponse.

        **参数解释：** 旧分支最新提交ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The old_branch_commit_id of this UpdateBranchNameResponse.
        :rtype: str
        """
        return self._old_branch_commit_id

    @old_branch_commit_id.setter
    def old_branch_commit_id(self, old_branch_commit_id):
        r"""Sets the old_branch_commit_id of this UpdateBranchNameResponse.

        **参数解释：** 旧分支最新提交ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param old_branch_commit_id: The old_branch_commit_id of this UpdateBranchNameResponse.
        :type old_branch_commit_id: str
        """
        self._old_branch_commit_id = old_branch_commit_id

    @property
    def new_branch_name(self):
        r"""Gets the new_branch_name of this UpdateBranchNameResponse.

        **参数解释：** 新分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :return: The new_branch_name of this UpdateBranchNameResponse.
        :rtype: str
        """
        return self._new_branch_name

    @new_branch_name.setter
    def new_branch_name(self, new_branch_name):
        r"""Sets the new_branch_name of this UpdateBranchNameResponse.

        **参数解释：** 新分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :param new_branch_name: The new_branch_name of this UpdateBranchNameResponse.
        :type new_branch_name: str
        """
        self._new_branch_name = new_branch_name

    @property
    def new_branch_commit_id(self):
        r"""Gets the new_branch_commit_id of this UpdateBranchNameResponse.

        **参数解释：** 新分支最新提交ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The new_branch_commit_id of this UpdateBranchNameResponse.
        :rtype: str
        """
        return self._new_branch_commit_id

    @new_branch_commit_id.setter
    def new_branch_commit_id(self, new_branch_commit_id):
        r"""Sets the new_branch_commit_id of this UpdateBranchNameResponse.

        **参数解释：** 新分支最新提交ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param new_branch_commit_id: The new_branch_commit_id of this UpdateBranchNameResponse.
        :type new_branch_commit_id: str
        """
        self._new_branch_commit_id = new_branch_commit_id

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
        if not isinstance(other, UpdateBranchNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
