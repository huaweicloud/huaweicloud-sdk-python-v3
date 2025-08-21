# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBranchDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch': 'str',
        'ref': 'str',
        'description': 'str',
        'related_ids': 'list[str]'
    }

    attribute_map = {
        'branch': 'branch',
        'ref': 'ref',
        'description': 'description',
        'related_ids': 'related_ids'
    }

    def __init__(self, branch=None, ref=None, description=None, related_ids=None):
        r"""CreateBranchDto

        The model defined in huaweicloud sdk

        :param branch: **参数解释：** 分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ &lt; ~ ^ : ? * ! ( ) &#39; \&quot; | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。
        :type branch: str
        :param ref: **参数解释：** 基于分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ &lt; ~ ^ : ? * ! ( ) &#39; \&quot; | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。
        :type ref: str
        :param description: **参数解释：** 分支描述。  **约束限制：** 无。  **取值范围：** 字符串长度不少于1，不超过2000。 **默认取值：** 不涉及。
        :type description: str
        :param related_ids: **参数解释：** 关联工作项列表。  **约束限制：** 无。  **取值范围：** 无。 **默认取值：** 不涉及。
        :type related_ids: list[str]
        """
        
        

        self._branch = None
        self._ref = None
        self._description = None
        self._related_ids = None
        self.discriminator = None

        self.branch = branch
        self.ref = ref
        if description is not None:
            self.description = description
        if related_ids is not None:
            self.related_ids = related_ids

    @property
    def branch(self):
        r"""Gets the branch of this CreateBranchDto.

        **参数解释：** 分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :return: The branch of this CreateBranchDto.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this CreateBranchDto.

        **参数解释：** 分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :param branch: The branch of this CreateBranchDto.
        :type branch: str
        """
        self._branch = branch

    @property
    def ref(self):
        r"""Gets the ref of this CreateBranchDto.

        **参数解释：** 基于分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :return: The ref of this CreateBranchDto.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this CreateBranchDto.

        **参数解释：** 基于分支名称。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :param ref: The ref of this CreateBranchDto.
        :type ref: str
        """
        self._ref = ref

    @property
    def description(self):
        r"""Gets the description of this CreateBranchDto.

        **参数解释：** 分支描述。  **约束限制：** 无。  **取值范围：** 字符串长度不少于1，不超过2000。 **默认取值：** 不涉及。

        :return: The description of this CreateBranchDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateBranchDto.

        **参数解释：** 分支描述。  **约束限制：** 无。  **取值范围：** 字符串长度不少于1，不超过2000。 **默认取值：** 不涉及。

        :param description: The description of this CreateBranchDto.
        :type description: str
        """
        self._description = description

    @property
    def related_ids(self):
        r"""Gets the related_ids of this CreateBranchDto.

        **参数解释：** 关联工作项列表。  **约束限制：** 无。  **取值范围：** 无。 **默认取值：** 不涉及。

        :return: The related_ids of this CreateBranchDto.
        :rtype: list[str]
        """
        return self._related_ids

    @related_ids.setter
    def related_ids(self, related_ids):
        r"""Sets the related_ids of this CreateBranchDto.

        **参数解释：** 关联工作项列表。  **约束限制：** 无。  **取值范围：** 无。 **默认取值：** 不涉及。

        :param related_ids: The related_ids of this CreateBranchDto.
        :type related_ids: list[str]
        """
        self._related_ids = related_ids

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
        if not isinstance(other, CreateBranchDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
