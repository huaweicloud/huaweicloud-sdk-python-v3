# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCommitRequestBody:

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
        'start_branch': 'str',
        'actions': 'list[CommitAction]',
        'author_email': 'str',
        'author_name': 'str',
        'stats': 'bool',
        'force': 'bool'
    }

    attribute_map = {
        'branch': 'branch',
        'commit_message': 'commit_message',
        'start_branch': 'start_branch',
        'actions': 'actions',
        'author_email': 'author_email',
        'author_name': 'author_name',
        'stats': 'stats',
        'force': 'force'
    }

    def __init__(self, branch=None, commit_message=None, start_branch=None, actions=None, author_email=None, author_name=None, stats=None, force=None):
        """CreateCommitRequestBody

        The model defined in huaweicloud sdk

        :param branch: 目标分支
        :type branch: str
        :param commit_message: 提交信息
        :type commit_message: str
        :param start_branch: 创建分支时，新的分支名
        :type start_branch: str
        :param actions: 提交处理列表
        :type actions: list[:class:`huaweicloudsdkcodehub.v3.CommitAction`]
        :param author_email: 提交作者的电子邮件地址
        :type author_email: str
        :param author_name: 提交作者的名称
        :type author_name: str
        :param stats: 是否包括提交统计信息。默认值为true
        :type stats: bool
        :param force: 是否覆盖目标分支。当true时，使用基于start_branch的新提交覆盖目标分支
        :type force: bool
        """
        
        

        self._branch = None
        self._commit_message = None
        self._start_branch = None
        self._actions = None
        self._author_email = None
        self._author_name = None
        self._stats = None
        self._force = None
        self.discriminator = None

        self.branch = branch
        self.commit_message = commit_message
        if start_branch is not None:
            self.start_branch = start_branch
        self.actions = actions
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
        """Gets the branch of this CreateCommitRequestBody.

        目标分支

        :return: The branch of this CreateCommitRequestBody.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this CreateCommitRequestBody.

        目标分支

        :param branch: The branch of this CreateCommitRequestBody.
        :type branch: str
        """
        self._branch = branch

    @property
    def commit_message(self):
        """Gets the commit_message of this CreateCommitRequestBody.

        提交信息

        :return: The commit_message of this CreateCommitRequestBody.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this CreateCommitRequestBody.

        提交信息

        :param commit_message: The commit_message of this CreateCommitRequestBody.
        :type commit_message: str
        """
        self._commit_message = commit_message

    @property
    def start_branch(self):
        """Gets the start_branch of this CreateCommitRequestBody.

        创建分支时，新的分支名

        :return: The start_branch of this CreateCommitRequestBody.
        :rtype: str
        """
        return self._start_branch

    @start_branch.setter
    def start_branch(self, start_branch):
        """Sets the start_branch of this CreateCommitRequestBody.

        创建分支时，新的分支名

        :param start_branch: The start_branch of this CreateCommitRequestBody.
        :type start_branch: str
        """
        self._start_branch = start_branch

    @property
    def actions(self):
        """Gets the actions of this CreateCommitRequestBody.

        提交处理列表

        :return: The actions of this CreateCommitRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.CommitAction`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this CreateCommitRequestBody.

        提交处理列表

        :param actions: The actions of this CreateCommitRequestBody.
        :type actions: list[:class:`huaweicloudsdkcodehub.v3.CommitAction`]
        """
        self._actions = actions

    @property
    def author_email(self):
        """Gets the author_email of this CreateCommitRequestBody.

        提交作者的电子邮件地址

        :return: The author_email of this CreateCommitRequestBody.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        """Sets the author_email of this CreateCommitRequestBody.

        提交作者的电子邮件地址

        :param author_email: The author_email of this CreateCommitRequestBody.
        :type author_email: str
        """
        self._author_email = author_email

    @property
    def author_name(self):
        """Gets the author_name of this CreateCommitRequestBody.

        提交作者的名称

        :return: The author_name of this CreateCommitRequestBody.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this CreateCommitRequestBody.

        提交作者的名称

        :param author_name: The author_name of this CreateCommitRequestBody.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def stats(self):
        """Gets the stats of this CreateCommitRequestBody.

        是否包括提交统计信息。默认值为true

        :return: The stats of this CreateCommitRequestBody.
        :rtype: bool
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this CreateCommitRequestBody.

        是否包括提交统计信息。默认值为true

        :param stats: The stats of this CreateCommitRequestBody.
        :type stats: bool
        """
        self._stats = stats

    @property
    def force(self):
        """Gets the force of this CreateCommitRequestBody.

        是否覆盖目标分支。当true时，使用基于start_branch的新提交覆盖目标分支

        :return: The force of this CreateCommitRequestBody.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this CreateCommitRequestBody.

        是否覆盖目标分支。当true时，使用基于start_branch的新提交覆盖目标分支

        :param force: The force of this CreateCommitRequestBody.
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
        if not isinstance(other, CreateCommitRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
