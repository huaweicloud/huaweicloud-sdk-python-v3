# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitDto:

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
        'message': 'str',
        'parent_ids': 'list[str]',
        'authored_date': 'str',
        'author_name': 'str',
        'author_email': 'str',
        'committed_date': 'str',
        'committer_name': 'str',
        'committer_email': 'str',
        'open_gpg_verified': 'bool',
        'verification_status': 'int',
        'gpg_primary_key_id': 'str',
        'name': 'str',
        'gpg_nick_name': 'str',
        'gpg_tenant_name': 'str',
        'gpg_user_name': 'str',
        'short_id': 'str',
        'created_at': 'str',
        'title': 'str',
        'author_avatar_url': 'str',
        'committer_avatar_url': 'str',
        'relate_url': 'list[RelatedCommitSimpleDto]',
        'nick_name': 'str',
        'tenant_name': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'message': 'message',
        'parent_ids': 'parent_ids',
        'authored_date': 'authored_date',
        'author_name': 'author_name',
        'author_email': 'author_email',
        'committed_date': 'committed_date',
        'committer_name': 'committer_name',
        'committer_email': 'committer_email',
        'open_gpg_verified': 'open_gpg_verified',
        'verification_status': 'verification_status',
        'gpg_primary_key_id': 'gpg_primary_key_id',
        'name': 'name',
        'gpg_nick_name': 'gpg_nick_name',
        'gpg_tenant_name': 'gpg_tenant_name',
        'gpg_user_name': 'gpg_user_name',
        'short_id': 'short_id',
        'created_at': 'created_at',
        'title': 'title',
        'author_avatar_url': 'author_avatar_url',
        'committer_avatar_url': 'committer_avatar_url',
        'relate_url': 'relate_url',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name',
        'user_name': 'user_name'
    }

    def __init__(self, id=None, message=None, parent_ids=None, authored_date=None, author_name=None, author_email=None, committed_date=None, committer_name=None, committer_email=None, open_gpg_verified=None, verification_status=None, gpg_primary_key_id=None, name=None, gpg_nick_name=None, gpg_tenant_name=None, gpg_user_name=None, short_id=None, created_at=None, title=None, author_avatar_url=None, committer_avatar_url=None, relate_url=None, nick_name=None, tenant_name=None, user_name=None):
        r"""CommitDto

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param message: 消息
        :type message: str
        :param parent_ids: 父节点提交ID
        :type parent_ids: list[str]
        :param authored_date: 创建该分支的时间
        :type authored_date: str
        :param author_name: 创建者名称
        :type author_name: str
        :param author_email: 创建者邮箱
        :type author_email: str
        :param committed_date: 代码提交的日期和时间
        :type committed_date: str
        :param committer_name: 提交者名称
        :type committer_name: str
        :param committer_email: 提交者邮箱
        :type committer_email: str
        :param open_gpg_verified: 是否打开gpg校验
        :type open_gpg_verified: bool
        :param verification_status: 验证状态
        :type verification_status: int
        :param gpg_primary_key_id: GPG公钥的标识符
        :type gpg_primary_key_id: str
        :param name: 用户名
        :type name: str
        :param gpg_nick_name: 昵称
        :type gpg_nick_name: str
        :param gpg_tenant_name: 租户名
        :type gpg_tenant_name: str
        :param gpg_user_name: 特定GPG用户相关的信息
        :type gpg_user_name: str
        :param short_id: 短id
        :type short_id: str
        :param created_at: 创建时间
        :type created_at: str
        :param title: 标题
        :type title: str
        :param author_avatar_url: author_avatar_url
        :type author_avatar_url: str
        :param committer_avatar_url: committer_avatar_url
        :type committer_avatar_url: str
        :param relate_url: only for DevCloud
        :type relate_url: list[:class:`huaweicloudsdkcodehub.v4.RelatedCommitSimpleDto`]
        :param nick_name: 标题
        :type nick_name: str
        :param tenant_name: tenant_name
        :type tenant_name: str
        :param user_name: 用户名
        :type user_name: str
        """
        
        

        self._id = None
        self._message = None
        self._parent_ids = None
        self._authored_date = None
        self._author_name = None
        self._author_email = None
        self._committed_date = None
        self._committer_name = None
        self._committer_email = None
        self._open_gpg_verified = None
        self._verification_status = None
        self._gpg_primary_key_id = None
        self._name = None
        self._gpg_nick_name = None
        self._gpg_tenant_name = None
        self._gpg_user_name = None
        self._short_id = None
        self._created_at = None
        self._title = None
        self._author_avatar_url = None
        self._committer_avatar_url = None
        self._relate_url = None
        self._nick_name = None
        self._tenant_name = None
        self._user_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if parent_ids is not None:
            self.parent_ids = parent_ids
        if authored_date is not None:
            self.authored_date = authored_date
        if author_name is not None:
            self.author_name = author_name
        if author_email is not None:
            self.author_email = author_email
        if committed_date is not None:
            self.committed_date = committed_date
        if committer_name is not None:
            self.committer_name = committer_name
        if committer_email is not None:
            self.committer_email = committer_email
        if open_gpg_verified is not None:
            self.open_gpg_verified = open_gpg_verified
        if verification_status is not None:
            self.verification_status = verification_status
        if gpg_primary_key_id is not None:
            self.gpg_primary_key_id = gpg_primary_key_id
        if name is not None:
            self.name = name
        if gpg_nick_name is not None:
            self.gpg_nick_name = gpg_nick_name
        if gpg_tenant_name is not None:
            self.gpg_tenant_name = gpg_tenant_name
        if gpg_user_name is not None:
            self.gpg_user_name = gpg_user_name
        if short_id is not None:
            self.short_id = short_id
        if created_at is not None:
            self.created_at = created_at
        if title is not None:
            self.title = title
        if author_avatar_url is not None:
            self.author_avatar_url = author_avatar_url
        if committer_avatar_url is not None:
            self.committer_avatar_url = committer_avatar_url
        if relate_url is not None:
            self.relate_url = relate_url
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if user_name is not None:
            self.user_name = user_name

    @property
    def id(self):
        r"""Gets the id of this CommitDto.

        id

        :return: The id of this CommitDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CommitDto.

        id

        :param id: The id of this CommitDto.
        :type id: str
        """
        self._id = id

    @property
    def message(self):
        r"""Gets the message of this CommitDto.

        消息

        :return: The message of this CommitDto.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CommitDto.

        消息

        :param message: The message of this CommitDto.
        :type message: str
        """
        self._message = message

    @property
    def parent_ids(self):
        r"""Gets the parent_ids of this CommitDto.

        父节点提交ID

        :return: The parent_ids of this CommitDto.
        :rtype: list[str]
        """
        return self._parent_ids

    @parent_ids.setter
    def parent_ids(self, parent_ids):
        r"""Sets the parent_ids of this CommitDto.

        父节点提交ID

        :param parent_ids: The parent_ids of this CommitDto.
        :type parent_ids: list[str]
        """
        self._parent_ids = parent_ids

    @property
    def authored_date(self):
        r"""Gets the authored_date of this CommitDto.

        创建该分支的时间

        :return: The authored_date of this CommitDto.
        :rtype: str
        """
        return self._authored_date

    @authored_date.setter
    def authored_date(self, authored_date):
        r"""Sets the authored_date of this CommitDto.

        创建该分支的时间

        :param authored_date: The authored_date of this CommitDto.
        :type authored_date: str
        """
        self._authored_date = authored_date

    @property
    def author_name(self):
        r"""Gets the author_name of this CommitDto.

        创建者名称

        :return: The author_name of this CommitDto.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this CommitDto.

        创建者名称

        :param author_name: The author_name of this CommitDto.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def author_email(self):
        r"""Gets the author_email of this CommitDto.

        创建者邮箱

        :return: The author_email of this CommitDto.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        r"""Sets the author_email of this CommitDto.

        创建者邮箱

        :param author_email: The author_email of this CommitDto.
        :type author_email: str
        """
        self._author_email = author_email

    @property
    def committed_date(self):
        r"""Gets the committed_date of this CommitDto.

        代码提交的日期和时间

        :return: The committed_date of this CommitDto.
        :rtype: str
        """
        return self._committed_date

    @committed_date.setter
    def committed_date(self, committed_date):
        r"""Sets the committed_date of this CommitDto.

        代码提交的日期和时间

        :param committed_date: The committed_date of this CommitDto.
        :type committed_date: str
        """
        self._committed_date = committed_date

    @property
    def committer_name(self):
        r"""Gets the committer_name of this CommitDto.

        提交者名称

        :return: The committer_name of this CommitDto.
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        r"""Sets the committer_name of this CommitDto.

        提交者名称

        :param committer_name: The committer_name of this CommitDto.
        :type committer_name: str
        """
        self._committer_name = committer_name

    @property
    def committer_email(self):
        r"""Gets the committer_email of this CommitDto.

        提交者邮箱

        :return: The committer_email of this CommitDto.
        :rtype: str
        """
        return self._committer_email

    @committer_email.setter
    def committer_email(self, committer_email):
        r"""Sets the committer_email of this CommitDto.

        提交者邮箱

        :param committer_email: The committer_email of this CommitDto.
        :type committer_email: str
        """
        self._committer_email = committer_email

    @property
    def open_gpg_verified(self):
        r"""Gets the open_gpg_verified of this CommitDto.

        是否打开gpg校验

        :return: The open_gpg_verified of this CommitDto.
        :rtype: bool
        """
        return self._open_gpg_verified

    @open_gpg_verified.setter
    def open_gpg_verified(self, open_gpg_verified):
        r"""Sets the open_gpg_verified of this CommitDto.

        是否打开gpg校验

        :param open_gpg_verified: The open_gpg_verified of this CommitDto.
        :type open_gpg_verified: bool
        """
        self._open_gpg_verified = open_gpg_verified

    @property
    def verification_status(self):
        r"""Gets the verification_status of this CommitDto.

        验证状态

        :return: The verification_status of this CommitDto.
        :rtype: int
        """
        return self._verification_status

    @verification_status.setter
    def verification_status(self, verification_status):
        r"""Sets the verification_status of this CommitDto.

        验证状态

        :param verification_status: The verification_status of this CommitDto.
        :type verification_status: int
        """
        self._verification_status = verification_status

    @property
    def gpg_primary_key_id(self):
        r"""Gets the gpg_primary_key_id of this CommitDto.

        GPG公钥的标识符

        :return: The gpg_primary_key_id of this CommitDto.
        :rtype: str
        """
        return self._gpg_primary_key_id

    @gpg_primary_key_id.setter
    def gpg_primary_key_id(self, gpg_primary_key_id):
        r"""Sets the gpg_primary_key_id of this CommitDto.

        GPG公钥的标识符

        :param gpg_primary_key_id: The gpg_primary_key_id of this CommitDto.
        :type gpg_primary_key_id: str
        """
        self._gpg_primary_key_id = gpg_primary_key_id

    @property
    def name(self):
        r"""Gets the name of this CommitDto.

        用户名

        :return: The name of this CommitDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CommitDto.

        用户名

        :param name: The name of this CommitDto.
        :type name: str
        """
        self._name = name

    @property
    def gpg_nick_name(self):
        r"""Gets the gpg_nick_name of this CommitDto.

        昵称

        :return: The gpg_nick_name of this CommitDto.
        :rtype: str
        """
        return self._gpg_nick_name

    @gpg_nick_name.setter
    def gpg_nick_name(self, gpg_nick_name):
        r"""Sets the gpg_nick_name of this CommitDto.

        昵称

        :param gpg_nick_name: The gpg_nick_name of this CommitDto.
        :type gpg_nick_name: str
        """
        self._gpg_nick_name = gpg_nick_name

    @property
    def gpg_tenant_name(self):
        r"""Gets the gpg_tenant_name of this CommitDto.

        租户名

        :return: The gpg_tenant_name of this CommitDto.
        :rtype: str
        """
        return self._gpg_tenant_name

    @gpg_tenant_name.setter
    def gpg_tenant_name(self, gpg_tenant_name):
        r"""Sets the gpg_tenant_name of this CommitDto.

        租户名

        :param gpg_tenant_name: The gpg_tenant_name of this CommitDto.
        :type gpg_tenant_name: str
        """
        self._gpg_tenant_name = gpg_tenant_name

    @property
    def gpg_user_name(self):
        r"""Gets the gpg_user_name of this CommitDto.

        特定GPG用户相关的信息

        :return: The gpg_user_name of this CommitDto.
        :rtype: str
        """
        return self._gpg_user_name

    @gpg_user_name.setter
    def gpg_user_name(self, gpg_user_name):
        r"""Sets the gpg_user_name of this CommitDto.

        特定GPG用户相关的信息

        :param gpg_user_name: The gpg_user_name of this CommitDto.
        :type gpg_user_name: str
        """
        self._gpg_user_name = gpg_user_name

    @property
    def short_id(self):
        r"""Gets the short_id of this CommitDto.

        短id

        :return: The short_id of this CommitDto.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        r"""Sets the short_id of this CommitDto.

        短id

        :param short_id: The short_id of this CommitDto.
        :type short_id: str
        """
        self._short_id = short_id

    @property
    def created_at(self):
        r"""Gets the created_at of this CommitDto.

        创建时间

        :return: The created_at of this CommitDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CommitDto.

        创建时间

        :param created_at: The created_at of this CommitDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def title(self):
        r"""Gets the title of this CommitDto.

        标题

        :return: The title of this CommitDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CommitDto.

        标题

        :param title: The title of this CommitDto.
        :type title: str
        """
        self._title = title

    @property
    def author_avatar_url(self):
        r"""Gets the author_avatar_url of this CommitDto.

        author_avatar_url

        :return: The author_avatar_url of this CommitDto.
        :rtype: str
        """
        return self._author_avatar_url

    @author_avatar_url.setter
    def author_avatar_url(self, author_avatar_url):
        r"""Sets the author_avatar_url of this CommitDto.

        author_avatar_url

        :param author_avatar_url: The author_avatar_url of this CommitDto.
        :type author_avatar_url: str
        """
        self._author_avatar_url = author_avatar_url

    @property
    def committer_avatar_url(self):
        r"""Gets the committer_avatar_url of this CommitDto.

        committer_avatar_url

        :return: The committer_avatar_url of this CommitDto.
        :rtype: str
        """
        return self._committer_avatar_url

    @committer_avatar_url.setter
    def committer_avatar_url(self, committer_avatar_url):
        r"""Sets the committer_avatar_url of this CommitDto.

        committer_avatar_url

        :param committer_avatar_url: The committer_avatar_url of this CommitDto.
        :type committer_avatar_url: str
        """
        self._committer_avatar_url = committer_avatar_url

    @property
    def relate_url(self):
        r"""Gets the relate_url of this CommitDto.

        only for DevCloud

        :return: The relate_url of this CommitDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.RelatedCommitSimpleDto`]
        """
        return self._relate_url

    @relate_url.setter
    def relate_url(self, relate_url):
        r"""Sets the relate_url of this CommitDto.

        only for DevCloud

        :param relate_url: The relate_url of this CommitDto.
        :type relate_url: list[:class:`huaweicloudsdkcodehub.v4.RelatedCommitSimpleDto`]
        """
        self._relate_url = relate_url

    @property
    def nick_name(self):
        r"""Gets the nick_name of this CommitDto.

        标题

        :return: The nick_name of this CommitDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this CommitDto.

        标题

        :param nick_name: The nick_name of this CommitDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this CommitDto.

        tenant_name

        :return: The tenant_name of this CommitDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this CommitDto.

        tenant_name

        :param tenant_name: The tenant_name of this CommitDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def user_name(self):
        r"""Gets the user_name of this CommitDto.

        用户名

        :return: The user_name of this CommitDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CommitDto.

        用户名

        :param user_name: The user_name of this CommitDto.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, CommitDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
