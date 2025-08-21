# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestCommitDto:

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
        'short_id': 'str',
        'title': 'str',
        'message': 'str',
        'author_name': 'str',
        'name': 'str',
        'user_name': 'str',
        'tenant_name': 'str',
        'nick_name': 'str',
        'authored_date': 'str',
        'committed_date': 'str',
        'committer_name': 'str',
        'gpg_primary_key_id': 'str',
        'open_gpg_verified': 'bool',
        'verification_status': 'bool',
        'parent_ids': 'list[str]',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'short_id': 'short_id',
        'title': 'title',
        'message': 'message',
        'author_name': 'author_name',
        'name': 'name',
        'user_name': 'user_name',
        'tenant_name': 'tenant_name',
        'nick_name': 'nick_name',
        'authored_date': 'authored_date',
        'committed_date': 'committed_date',
        'committer_name': 'committer_name',
        'gpg_primary_key_id': 'gpg_primary_key_id',
        'open_gpg_verified': 'open_gpg_verified',
        'verification_status': 'verification_status',
        'parent_ids': 'parent_ids',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, short_id=None, title=None, message=None, author_name=None, name=None, user_name=None, tenant_name=None, nick_name=None, authored_date=None, committed_date=None, committer_name=None, gpg_primary_key_id=None, open_gpg_verified=None, verification_status=None, parent_ids=None, created_at=None):
        r"""MergeRequestCommitDto

        The model defined in huaweicloud sdk

        :param id: commit id
        :type id: str
        :param short_id: commit 短id
        :type short_id: str
        :param title: 提交标题
        :type title: str
        :param message: 提交信息
        :type message: str
        :param author_name: commit 作者名称
        :type author_name: str
        :param name: 用户名
        :type name: str
        :param user_name: 用户名
        :type user_name: str
        :param tenant_name: 租户名
        :type tenant_name: str
        :param nick_name: 昵称
        :type nick_name: str
        :param authored_date: 最初commit 提交日期（本地提交日期）
        :type authored_date: str
        :param committed_date: commit提交日期（推送至仓库日期）
        :type committed_date: str
        :param committer_name: commit 提交者名称
        :type committer_name: str
        :param gpg_primary_key_id: pgp key id
        :type gpg_primary_key_id: str
        :param open_gpg_verified: gpg公钥验证是否开启
        :type open_gpg_verified: bool
        :param verification_status: gpg公钥验证是否通过
        :type verification_status: bool
        :param parent_ids: 提交父commit节点
        :type parent_ids: list[str]
        :param created_at: commit 数据库记录创建时间
        :type created_at: str
        """
        
        

        self._id = None
        self._short_id = None
        self._title = None
        self._message = None
        self._author_name = None
        self._name = None
        self._user_name = None
        self._tenant_name = None
        self._nick_name = None
        self._authored_date = None
        self._committed_date = None
        self._committer_name = None
        self._gpg_primary_key_id = None
        self._open_gpg_verified = None
        self._verification_status = None
        self._parent_ids = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if short_id is not None:
            self.short_id = short_id
        if title is not None:
            self.title = title
        if message is not None:
            self.message = message
        if author_name is not None:
            self.author_name = author_name
        if name is not None:
            self.name = name
        if user_name is not None:
            self.user_name = user_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if nick_name is not None:
            self.nick_name = nick_name
        if authored_date is not None:
            self.authored_date = authored_date
        if committed_date is not None:
            self.committed_date = committed_date
        if committer_name is not None:
            self.committer_name = committer_name
        if gpg_primary_key_id is not None:
            self.gpg_primary_key_id = gpg_primary_key_id
        if open_gpg_verified is not None:
            self.open_gpg_verified = open_gpg_verified
        if verification_status is not None:
            self.verification_status = verification_status
        if parent_ids is not None:
            self.parent_ids = parent_ids
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this MergeRequestCommitDto.

        commit id

        :return: The id of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MergeRequestCommitDto.

        commit id

        :param id: The id of this MergeRequestCommitDto.
        :type id: str
        """
        self._id = id

    @property
    def short_id(self):
        r"""Gets the short_id of this MergeRequestCommitDto.

        commit 短id

        :return: The short_id of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        r"""Sets the short_id of this MergeRequestCommitDto.

        commit 短id

        :param short_id: The short_id of this MergeRequestCommitDto.
        :type short_id: str
        """
        self._short_id = short_id

    @property
    def title(self):
        r"""Gets the title of this MergeRequestCommitDto.

        提交标题

        :return: The title of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this MergeRequestCommitDto.

        提交标题

        :param title: The title of this MergeRequestCommitDto.
        :type title: str
        """
        self._title = title

    @property
    def message(self):
        r"""Gets the message of this MergeRequestCommitDto.

        提交信息

        :return: The message of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this MergeRequestCommitDto.

        提交信息

        :param message: The message of this MergeRequestCommitDto.
        :type message: str
        """
        self._message = message

    @property
    def author_name(self):
        r"""Gets the author_name of this MergeRequestCommitDto.

        commit 作者名称

        :return: The author_name of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this MergeRequestCommitDto.

        commit 作者名称

        :param author_name: The author_name of this MergeRequestCommitDto.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def name(self):
        r"""Gets the name of this MergeRequestCommitDto.

        用户名

        :return: The name of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MergeRequestCommitDto.

        用户名

        :param name: The name of this MergeRequestCommitDto.
        :type name: str
        """
        self._name = name

    @property
    def user_name(self):
        r"""Gets the user_name of this MergeRequestCommitDto.

        用户名

        :return: The user_name of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this MergeRequestCommitDto.

        用户名

        :param user_name: The user_name of this MergeRequestCommitDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this MergeRequestCommitDto.

        租户名

        :return: The tenant_name of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this MergeRequestCommitDto.

        租户名

        :param tenant_name: The tenant_name of this MergeRequestCommitDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this MergeRequestCommitDto.

        昵称

        :return: The nick_name of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this MergeRequestCommitDto.

        昵称

        :param nick_name: The nick_name of this MergeRequestCommitDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def authored_date(self):
        r"""Gets the authored_date of this MergeRequestCommitDto.

        最初commit 提交日期（本地提交日期）

        :return: The authored_date of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._authored_date

    @authored_date.setter
    def authored_date(self, authored_date):
        r"""Sets the authored_date of this MergeRequestCommitDto.

        最初commit 提交日期（本地提交日期）

        :param authored_date: The authored_date of this MergeRequestCommitDto.
        :type authored_date: str
        """
        self._authored_date = authored_date

    @property
    def committed_date(self):
        r"""Gets the committed_date of this MergeRequestCommitDto.

        commit提交日期（推送至仓库日期）

        :return: The committed_date of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._committed_date

    @committed_date.setter
    def committed_date(self, committed_date):
        r"""Sets the committed_date of this MergeRequestCommitDto.

        commit提交日期（推送至仓库日期）

        :param committed_date: The committed_date of this MergeRequestCommitDto.
        :type committed_date: str
        """
        self._committed_date = committed_date

    @property
    def committer_name(self):
        r"""Gets the committer_name of this MergeRequestCommitDto.

        commit 提交者名称

        :return: The committer_name of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        r"""Sets the committer_name of this MergeRequestCommitDto.

        commit 提交者名称

        :param committer_name: The committer_name of this MergeRequestCommitDto.
        :type committer_name: str
        """
        self._committer_name = committer_name

    @property
    def gpg_primary_key_id(self):
        r"""Gets the gpg_primary_key_id of this MergeRequestCommitDto.

        pgp key id

        :return: The gpg_primary_key_id of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._gpg_primary_key_id

    @gpg_primary_key_id.setter
    def gpg_primary_key_id(self, gpg_primary_key_id):
        r"""Sets the gpg_primary_key_id of this MergeRequestCommitDto.

        pgp key id

        :param gpg_primary_key_id: The gpg_primary_key_id of this MergeRequestCommitDto.
        :type gpg_primary_key_id: str
        """
        self._gpg_primary_key_id = gpg_primary_key_id

    @property
    def open_gpg_verified(self):
        r"""Gets the open_gpg_verified of this MergeRequestCommitDto.

        gpg公钥验证是否开启

        :return: The open_gpg_verified of this MergeRequestCommitDto.
        :rtype: bool
        """
        return self._open_gpg_verified

    @open_gpg_verified.setter
    def open_gpg_verified(self, open_gpg_verified):
        r"""Sets the open_gpg_verified of this MergeRequestCommitDto.

        gpg公钥验证是否开启

        :param open_gpg_verified: The open_gpg_verified of this MergeRequestCommitDto.
        :type open_gpg_verified: bool
        """
        self._open_gpg_verified = open_gpg_verified

    @property
    def verification_status(self):
        r"""Gets the verification_status of this MergeRequestCommitDto.

        gpg公钥验证是否通过

        :return: The verification_status of this MergeRequestCommitDto.
        :rtype: bool
        """
        return self._verification_status

    @verification_status.setter
    def verification_status(self, verification_status):
        r"""Sets the verification_status of this MergeRequestCommitDto.

        gpg公钥验证是否通过

        :param verification_status: The verification_status of this MergeRequestCommitDto.
        :type verification_status: bool
        """
        self._verification_status = verification_status

    @property
    def parent_ids(self):
        r"""Gets the parent_ids of this MergeRequestCommitDto.

        提交父commit节点

        :return: The parent_ids of this MergeRequestCommitDto.
        :rtype: list[str]
        """
        return self._parent_ids

    @parent_ids.setter
    def parent_ids(self, parent_ids):
        r"""Sets the parent_ids of this MergeRequestCommitDto.

        提交父commit节点

        :param parent_ids: The parent_ids of this MergeRequestCommitDto.
        :type parent_ids: list[str]
        """
        self._parent_ids = parent_ids

    @property
    def created_at(self):
        r"""Gets the created_at of this MergeRequestCommitDto.

        commit 数据库记录创建时间

        :return: The created_at of this MergeRequestCommitDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MergeRequestCommitDto.

        commit 数据库记录创建时间

        :param created_at: The created_at of this MergeRequestCommitDto.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, MergeRequestCommitDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
