# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitParams:

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
        'commit_message': 'str',
        'actions': 'list[ActionDto]',
        'start_branch': 'str',
        'author_email': 'str',
        'author_name': 'str',
        'stats': 'bool',
        'force': 'bool'
    }

    attribute_map = {
        'branch': 'branch',
        'commit_message': 'commit_message',
        'actions': 'actions',
        'start_branch': 'start_branch',
        'author_email': 'author_email',
        'author_name': 'author_name',
        'stats': 'stats',
        'force': 'force'
    }

    def __init__(self, branch=None, commit_message=None, actions=None, start_branch=None, author_email=None, author_name=None, stats=None, force=None):
        r"""CommitParams

        The model defined in huaweicloud sdk

        :param branch: **参数解释：** 分支名称。 **取值范围：** 不涉及。
        :type branch: str
        :param commit_message: **参数解释：** 提交信息。 **取值范围：** 不涉及。
        :type commit_message: str
        :param actions: **参数解释：** 在提交时执行的操作。 **取值范围：** 不涉及。
        :type actions: list[:class:`huaweicloudsdkcodehub.v4.ActionDto`]
        :param start_branch: **参数解释：** 从该分支开始新的提交。  **取值范围：** 不涉及。
        :type start_branch: str
        :param author_email: **参数解释：** 作者邮箱。  **取值范围：** 不涉及。
        :type author_email: str
        :param author_name: **参数解释：** 作者名称。  **取值范围：** 不涉及。
        :type author_name: str
        :param stats: **参数解释：** 是否包括提交统计信息。 **取值范围：** - true，包括提交统计信息。 - false，不包括提交统计信息
        :type stats: bool
        :param force: **参数解释：** 是否强制提交。 **取值范围：** - true，强制提交。 - false，非强制提交
        :type force: bool
        """
        
        

        self._branch = None
        self._commit_message = None
        self._actions = None
        self._start_branch = None
        self._author_email = None
        self._author_name = None
        self._stats = None
        self._force = None
        self.discriminator = None

        self.branch = branch
        self.commit_message = commit_message
        self.actions = actions
        if start_branch is not None:
            self.start_branch = start_branch
        if author_email is not None:
            self.author_email = author_email
        if author_name is not None:
            self.author_name = author_name
        if stats is not None:
            self.stats = stats
        if force is not None:
            self.force = force

    @property
    def branch(self):
        r"""Gets the branch of this CommitParams.

        **参数解释：** 分支名称。 **取值范围：** 不涉及。

        :return: The branch of this CommitParams.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this CommitParams.

        **参数解释：** 分支名称。 **取值范围：** 不涉及。

        :param branch: The branch of this CommitParams.
        :type branch: str
        """
        self._branch = branch

    @property
    def commit_message(self):
        r"""Gets the commit_message of this CommitParams.

        **参数解释：** 提交信息。 **取值范围：** 不涉及。

        :return: The commit_message of this CommitParams.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        r"""Sets the commit_message of this CommitParams.

        **参数解释：** 提交信息。 **取值范围：** 不涉及。

        :param commit_message: The commit_message of this CommitParams.
        :type commit_message: str
        """
        self._commit_message = commit_message

    @property
    def actions(self):
        r"""Gets the actions of this CommitParams.

        **参数解释：** 在提交时执行的操作。 **取值范围：** 不涉及。

        :return: The actions of this CommitParams.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ActionDto`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this CommitParams.

        **参数解释：** 在提交时执行的操作。 **取值范围：** 不涉及。

        :param actions: The actions of this CommitParams.
        :type actions: list[:class:`huaweicloudsdkcodehub.v4.ActionDto`]
        """
        self._actions = actions

    @property
    def start_branch(self):
        r"""Gets the start_branch of this CommitParams.

        **参数解释：** 从该分支开始新的提交。  **取值范围：** 不涉及。

        :return: The start_branch of this CommitParams.
        :rtype: str
        """
        return self._start_branch

    @start_branch.setter
    def start_branch(self, start_branch):
        r"""Sets the start_branch of this CommitParams.

        **参数解释：** 从该分支开始新的提交。  **取值范围：** 不涉及。

        :param start_branch: The start_branch of this CommitParams.
        :type start_branch: str
        """
        self._start_branch = start_branch

    @property
    def author_email(self):
        r"""Gets the author_email of this CommitParams.

        **参数解释：** 作者邮箱。  **取值范围：** 不涉及。

        :return: The author_email of this CommitParams.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        r"""Sets the author_email of this CommitParams.

        **参数解释：** 作者邮箱。  **取值范围：** 不涉及。

        :param author_email: The author_email of this CommitParams.
        :type author_email: str
        """
        self._author_email = author_email

    @property
    def author_name(self):
        r"""Gets the author_name of this CommitParams.

        **参数解释：** 作者名称。  **取值范围：** 不涉及。

        :return: The author_name of this CommitParams.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this CommitParams.

        **参数解释：** 作者名称。  **取值范围：** 不涉及。

        :param author_name: The author_name of this CommitParams.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def stats(self):
        r"""Gets the stats of this CommitParams.

        **参数解释：** 是否包括提交统计信息。 **取值范围：** - true，包括提交统计信息。 - false，不包括提交统计信息

        :return: The stats of this CommitParams.
        :rtype: bool
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        r"""Sets the stats of this CommitParams.

        **参数解释：** 是否包括提交统计信息。 **取值范围：** - true，包括提交统计信息。 - false，不包括提交统计信息

        :param stats: The stats of this CommitParams.
        :type stats: bool
        """
        self._stats = stats

    @property
    def force(self):
        r"""Gets the force of this CommitParams.

        **参数解释：** 是否强制提交。 **取值范围：** - true，强制提交。 - false，非强制提交

        :return: The force of this CommitParams.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        r"""Sets the force of this CommitParams.

        **参数解释：** 是否强制提交。 **取值范围：** - true，强制提交。 - false，非强制提交

        :param force: The force of this CommitParams.
        :type force: bool
        """
        self._force = force

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
        if not isinstance(other, CommitParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
