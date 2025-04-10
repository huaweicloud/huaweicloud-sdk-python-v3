# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelatedCommitVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'iam_id': 'str',
        'user_name': 'str',
        'repository_id': 'str',
        'type': 'str',
        'user_id': 'str',
        'branch_name': 'str',
        'commit_id': 'str',
        'commit_short_id': 'str',
        'commit_msg': 'str',
        'commit_url': 'str',
        'commit_type': 'str',
        'related_id': 'str',
        'create_at': 'str',
        'update_at': 'str',
        'related_url': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'iam_id': 'iamId',
        'user_name': 'userName',
        'repository_id': 'repositoryId',
        'type': 'type',
        'user_id': 'userId',
        'branch_name': 'branchName',
        'commit_id': 'commitId',
        'commit_short_id': 'commitShortId',
        'commit_msg': 'commitMsg',
        'commit_url': 'commitUrl',
        'commit_type': 'commitType',
        'related_id': 'relatedId',
        'create_at': 'createAt',
        'update_at': 'updateAt',
        'related_url': 'relatedUrl',
        'message': 'message'
    }

    def __init__(self, id=None, iam_id=None, user_name=None, repository_id=None, type=None, user_id=None, branch_name=None, commit_id=None, commit_short_id=None, commit_msg=None, commit_url=None, commit_type=None, related_id=None, create_at=None, update_at=None, related_url=None, message=None):
        r"""RelatedCommitVo

        The model defined in huaweicloud sdk

        :param id: 主键ID
        :type id: str
        :param iam_id: 用户ID
        :type iam_id: str
        :param user_name: 用户名称
        :type user_name: str
        :param repository_id: 仓库ID
        :type repository_id: str
        :param type: 类型
        :type type: str
        :param user_id: 用户ID
        :type user_id: str
        :param branch_name: 分支名称
        :type branch_name: str
        :param commit_id: Commit ID
        :type commit_id: str
        :param commit_short_id: Commit 短ID
        :type commit_short_id: str
        :param commit_msg: 提交信息
        :type commit_msg: str
        :param commit_url: 提交URL
        :type commit_url: str
        :param commit_type: 提交类型
        :type commit_type: str
        :param related_id: 
        :type related_id: str
        :param create_at: 创建时间
        :type create_at: str
        :param update_at: 更新时间
        :type update_at: str
        :param related_url: 
        :type related_url: str
        :param message: 描述
        :type message: str
        """
        
        

        self._id = None
        self._iam_id = None
        self._user_name = None
        self._repository_id = None
        self._type = None
        self._user_id = None
        self._branch_name = None
        self._commit_id = None
        self._commit_short_id = None
        self._commit_msg = None
        self._commit_url = None
        self._commit_type = None
        self._related_id = None
        self._create_at = None
        self._update_at = None
        self._related_url = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if iam_id is not None:
            self.iam_id = iam_id
        if user_name is not None:
            self.user_name = user_name
        if repository_id is not None:
            self.repository_id = repository_id
        if type is not None:
            self.type = type
        if user_id is not None:
            self.user_id = user_id
        if branch_name is not None:
            self.branch_name = branch_name
        if commit_id is not None:
            self.commit_id = commit_id
        if commit_short_id is not None:
            self.commit_short_id = commit_short_id
        if commit_msg is not None:
            self.commit_msg = commit_msg
        if commit_url is not None:
            self.commit_url = commit_url
        if commit_type is not None:
            self.commit_type = commit_type
        if related_id is not None:
            self.related_id = related_id
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if related_url is not None:
            self.related_url = related_url
        if message is not None:
            self.message = message

    @property
    def id(self):
        r"""Gets the id of this RelatedCommitVo.

        主键ID

        :return: The id of this RelatedCommitVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RelatedCommitVo.

        主键ID

        :param id: The id of this RelatedCommitVo.
        :type id: str
        """
        self._id = id

    @property
    def iam_id(self):
        r"""Gets the iam_id of this RelatedCommitVo.

        用户ID

        :return: The iam_id of this RelatedCommitVo.
        :rtype: str
        """
        return self._iam_id

    @iam_id.setter
    def iam_id(self, iam_id):
        r"""Sets the iam_id of this RelatedCommitVo.

        用户ID

        :param iam_id: The iam_id of this RelatedCommitVo.
        :type iam_id: str
        """
        self._iam_id = iam_id

    @property
    def user_name(self):
        r"""Gets the user_name of this RelatedCommitVo.

        用户名称

        :return: The user_name of this RelatedCommitVo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this RelatedCommitVo.

        用户名称

        :param user_name: The user_name of this RelatedCommitVo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def repository_id(self):
        r"""Gets the repository_id of this RelatedCommitVo.

        仓库ID

        :return: The repository_id of this RelatedCommitVo.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this RelatedCommitVo.

        仓库ID

        :param repository_id: The repository_id of this RelatedCommitVo.
        :type repository_id: str
        """
        self._repository_id = repository_id

    @property
    def type(self):
        r"""Gets the type of this RelatedCommitVo.

        类型

        :return: The type of this RelatedCommitVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RelatedCommitVo.

        类型

        :param type: The type of this RelatedCommitVo.
        :type type: str
        """
        self._type = type

    @property
    def user_id(self):
        r"""Gets the user_id of this RelatedCommitVo.

        用户ID

        :return: The user_id of this RelatedCommitVo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this RelatedCommitVo.

        用户ID

        :param user_id: The user_id of this RelatedCommitVo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def branch_name(self):
        r"""Gets the branch_name of this RelatedCommitVo.

        分支名称

        :return: The branch_name of this RelatedCommitVo.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this RelatedCommitVo.

        分支名称

        :param branch_name: The branch_name of this RelatedCommitVo.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def commit_id(self):
        r"""Gets the commit_id of this RelatedCommitVo.

        Commit ID

        :return: The commit_id of this RelatedCommitVo.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this RelatedCommitVo.

        Commit ID

        :param commit_id: The commit_id of this RelatedCommitVo.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def commit_short_id(self):
        r"""Gets the commit_short_id of this RelatedCommitVo.

        Commit 短ID

        :return: The commit_short_id of this RelatedCommitVo.
        :rtype: str
        """
        return self._commit_short_id

    @commit_short_id.setter
    def commit_short_id(self, commit_short_id):
        r"""Sets the commit_short_id of this RelatedCommitVo.

        Commit 短ID

        :param commit_short_id: The commit_short_id of this RelatedCommitVo.
        :type commit_short_id: str
        """
        self._commit_short_id = commit_short_id

    @property
    def commit_msg(self):
        r"""Gets the commit_msg of this RelatedCommitVo.

        提交信息

        :return: The commit_msg of this RelatedCommitVo.
        :rtype: str
        """
        return self._commit_msg

    @commit_msg.setter
    def commit_msg(self, commit_msg):
        r"""Sets the commit_msg of this RelatedCommitVo.

        提交信息

        :param commit_msg: The commit_msg of this RelatedCommitVo.
        :type commit_msg: str
        """
        self._commit_msg = commit_msg

    @property
    def commit_url(self):
        r"""Gets the commit_url of this RelatedCommitVo.

        提交URL

        :return: The commit_url of this RelatedCommitVo.
        :rtype: str
        """
        return self._commit_url

    @commit_url.setter
    def commit_url(self, commit_url):
        r"""Sets the commit_url of this RelatedCommitVo.

        提交URL

        :param commit_url: The commit_url of this RelatedCommitVo.
        :type commit_url: str
        """
        self._commit_url = commit_url

    @property
    def commit_type(self):
        r"""Gets the commit_type of this RelatedCommitVo.

        提交类型

        :return: The commit_type of this RelatedCommitVo.
        :rtype: str
        """
        return self._commit_type

    @commit_type.setter
    def commit_type(self, commit_type):
        r"""Sets the commit_type of this RelatedCommitVo.

        提交类型

        :param commit_type: The commit_type of this RelatedCommitVo.
        :type commit_type: str
        """
        self._commit_type = commit_type

    @property
    def related_id(self):
        r"""Gets the related_id of this RelatedCommitVo.

        :return: The related_id of this RelatedCommitVo.
        :rtype: str
        """
        return self._related_id

    @related_id.setter
    def related_id(self, related_id):
        r"""Sets the related_id of this RelatedCommitVo.

        :param related_id: The related_id of this RelatedCommitVo.
        :type related_id: str
        """
        self._related_id = related_id

    @property
    def create_at(self):
        r"""Gets the create_at of this RelatedCommitVo.

        创建时间

        :return: The create_at of this RelatedCommitVo.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this RelatedCommitVo.

        创建时间

        :param create_at: The create_at of this RelatedCommitVo.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this RelatedCommitVo.

        更新时间

        :return: The update_at of this RelatedCommitVo.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this RelatedCommitVo.

        更新时间

        :param update_at: The update_at of this RelatedCommitVo.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def related_url(self):
        r"""Gets the related_url of this RelatedCommitVo.

        :return: The related_url of this RelatedCommitVo.
        :rtype: str
        """
        return self._related_url

    @related_url.setter
    def related_url(self, related_url):
        r"""Sets the related_url of this RelatedCommitVo.

        :param related_url: The related_url of this RelatedCommitVo.
        :type related_url: str
        """
        self._related_url = related_url

    @property
    def message(self):
        r"""Gets the message of this RelatedCommitVo.

        描述

        :return: The message of this RelatedCommitVo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this RelatedCommitVo.

        描述

        :param message: The message of this RelatedCommitVo.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, RelatedCommitVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
