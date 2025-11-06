# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItemCommitDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'title': 'str',
        'result': 'int',
        'type': 'str',
        'message': 'str',
        'item_id': 'str',
        'repository_id': 'str',
        'branch_name': 'str',
        'user_name': 'str',
        'commit_id': 'str',
        'commit_short_id': 'str',
        'commit_msg': 'str',
        'commit_url': 'str',
        'iam_id': 'str',
        'create_at': 'str',
        'update_at': 'str',
        'item_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'result': 'result',
        'type': 'type',
        'message': 'message',
        'item_id': 'item_id',
        'repository_id': 'repository_id',
        'branch_name': 'branch_name',
        'user_name': 'user_name',
        'commit_id': 'commit_id',
        'commit_short_id': 'commit_short_id',
        'commit_msg': 'commit_msg',
        'commit_url': 'commit_url',
        'iam_id': 'iam_id',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'item_url': 'item_url'
    }

    def __init__(self, id=None, title=None, result=None, type=None, message=None, item_id=None, repository_id=None, branch_name=None, user_name=None, commit_id=None, commit_short_id=None, commit_msg=None, commit_url=None, iam_id=None, create_at=None, update_at=None, item_url=None):
        r"""ItemCommitDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 关联Id。 **取值范围：** 不涉及
        :type id: int
        :param title: **参数解释：** 合并请求标题。 **取值范围：** 不涉及。
        :type title: str
        :param result: **参数解释：** 仓库状态。 **取值范围：** - 1，关联成功。 - 2，关联失败。 - 3，流转成功。
        :type result: int
        :param type: **参数解释：** 关联提交类型。 **取值范围：** - commit，提交。 - branch，分支。 - mergerequest，合并请求。
        :type type: str
        :param message: **参数解释：** 关联失败的失败原因。 **取值范围：** 不涉及。
        :type message: str
        :param item_id: **参数解释：** 工作项Id。 **取值范围：** 不涉及。
        :type item_id: str
        :param repository_id: **参数解释：** 仓库Id。 **取值范围：** 不涉及。
        :type repository_id: str
        :param branch_name: **参数解释：** 分支名。 **取值范围：** 不涉及。
        :type branch_name: str
        :param user_name: **参数解释：** 用户名。 **取值范围：** 不涉及。
        :type user_name: str
        :param commit_id: **参数解释：** 提交Id。 **取值范围：** 不涉及。
        :type commit_id: str
        :param commit_short_id: **参数解释：** 提交短Id。 **取值范围：** 不涉及。
        :type commit_short_id: str
        :param commit_msg: **参数解释：** 提交信息。 **取值范围：** 不涉及。            
        :type commit_msg: str
        :param commit_url: **参数解释：** 提交访问地址。 **取值范围：** 不涉及。
        :type commit_url: str
        :param iam_id: **参数解释：** iamId。 **取值范围：** 不涉及。
        :type iam_id: str
        :param create_at: **参数解释：** 创建时间。 **取值范围：** 不涉及。
        :type create_at: str
        :param update_at: **参数解释：** 更新时间。 **取值范围：** 不涉及。  
        :type update_at: str
        :param item_url: **参数解释：** 工作项访问地址。 **取值范围：** 不涉及。
        :type item_url: str
        """
        
        

        self._id = None
        self._title = None
        self._result = None
        self._type = None
        self._message = None
        self._item_id = None
        self._repository_id = None
        self._branch_name = None
        self._user_name = None
        self._commit_id = None
        self._commit_short_id = None
        self._commit_msg = None
        self._commit_url = None
        self._iam_id = None
        self._create_at = None
        self._update_at = None
        self._item_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if result is not None:
            self.result = result
        if type is not None:
            self.type = type
        if message is not None:
            self.message = message
        if item_id is not None:
            self.item_id = item_id
        if repository_id is not None:
            self.repository_id = repository_id
        if branch_name is not None:
            self.branch_name = branch_name
        if user_name is not None:
            self.user_name = user_name
        if commit_id is not None:
            self.commit_id = commit_id
        if commit_short_id is not None:
            self.commit_short_id = commit_short_id
        if commit_msg is not None:
            self.commit_msg = commit_msg
        if commit_url is not None:
            self.commit_url = commit_url
        if iam_id is not None:
            self.iam_id = iam_id
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if item_url is not None:
            self.item_url = item_url

    @property
    def id(self):
        r"""Gets the id of this ItemCommitDto.

        **参数解释：** 关联Id。 **取值范围：** 不涉及

        :return: The id of this ItemCommitDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ItemCommitDto.

        **参数解释：** 关联Id。 **取值范围：** 不涉及

        :param id: The id of this ItemCommitDto.
        :type id: int
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this ItemCommitDto.

        **参数解释：** 合并请求标题。 **取值范围：** 不涉及。

        :return: The title of this ItemCommitDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ItemCommitDto.

        **参数解释：** 合并请求标题。 **取值范围：** 不涉及。

        :param title: The title of this ItemCommitDto.
        :type title: str
        """
        self._title = title

    @property
    def result(self):
        r"""Gets the result of this ItemCommitDto.

        **参数解释：** 仓库状态。 **取值范围：** - 1，关联成功。 - 2，关联失败。 - 3，流转成功。

        :return: The result of this ItemCommitDto.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ItemCommitDto.

        **参数解释：** 仓库状态。 **取值范围：** - 1，关联成功。 - 2，关联失败。 - 3，流转成功。

        :param result: The result of this ItemCommitDto.
        :type result: int
        """
        self._result = result

    @property
    def type(self):
        r"""Gets the type of this ItemCommitDto.

        **参数解释：** 关联提交类型。 **取值范围：** - commit，提交。 - branch，分支。 - mergerequest，合并请求。

        :return: The type of this ItemCommitDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ItemCommitDto.

        **参数解释：** 关联提交类型。 **取值范围：** - commit，提交。 - branch，分支。 - mergerequest，合并请求。

        :param type: The type of this ItemCommitDto.
        :type type: str
        """
        self._type = type

    @property
    def message(self):
        r"""Gets the message of this ItemCommitDto.

        **参数解释：** 关联失败的失败原因。 **取值范围：** 不涉及。

        :return: The message of this ItemCommitDto.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ItemCommitDto.

        **参数解释：** 关联失败的失败原因。 **取值范围：** 不涉及。

        :param message: The message of this ItemCommitDto.
        :type message: str
        """
        self._message = message

    @property
    def item_id(self):
        r"""Gets the item_id of this ItemCommitDto.

        **参数解释：** 工作项Id。 **取值范围：** 不涉及。

        :return: The item_id of this ItemCommitDto.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this ItemCommitDto.

        **参数解释：** 工作项Id。 **取值范围：** 不涉及。

        :param item_id: The item_id of this ItemCommitDto.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ItemCommitDto.

        **参数解释：** 仓库Id。 **取值范围：** 不涉及。

        :return: The repository_id of this ItemCommitDto.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ItemCommitDto.

        **参数解释：** 仓库Id。 **取值范围：** 不涉及。

        :param repository_id: The repository_id of this ItemCommitDto.
        :type repository_id: str
        """
        self._repository_id = repository_id

    @property
    def branch_name(self):
        r"""Gets the branch_name of this ItemCommitDto.

        **参数解释：** 分支名。 **取值范围：** 不涉及。

        :return: The branch_name of this ItemCommitDto.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this ItemCommitDto.

        **参数解释：** 分支名。 **取值范围：** 不涉及。

        :param branch_name: The branch_name of this ItemCommitDto.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ItemCommitDto.

        **参数解释：** 用户名。 **取值范围：** 不涉及。

        :return: The user_name of this ItemCommitDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ItemCommitDto.

        **参数解释：** 用户名。 **取值范围：** 不涉及。

        :param user_name: The user_name of this ItemCommitDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def commit_id(self):
        r"""Gets the commit_id of this ItemCommitDto.

        **参数解释：** 提交Id。 **取值范围：** 不涉及。

        :return: The commit_id of this ItemCommitDto.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this ItemCommitDto.

        **参数解释：** 提交Id。 **取值范围：** 不涉及。

        :param commit_id: The commit_id of this ItemCommitDto.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def commit_short_id(self):
        r"""Gets the commit_short_id of this ItemCommitDto.

        **参数解释：** 提交短Id。 **取值范围：** 不涉及。

        :return: The commit_short_id of this ItemCommitDto.
        :rtype: str
        """
        return self._commit_short_id

    @commit_short_id.setter
    def commit_short_id(self, commit_short_id):
        r"""Sets the commit_short_id of this ItemCommitDto.

        **参数解释：** 提交短Id。 **取值范围：** 不涉及。

        :param commit_short_id: The commit_short_id of this ItemCommitDto.
        :type commit_short_id: str
        """
        self._commit_short_id = commit_short_id

    @property
    def commit_msg(self):
        r"""Gets the commit_msg of this ItemCommitDto.

        **参数解释：** 提交信息。 **取值范围：** 不涉及。            

        :return: The commit_msg of this ItemCommitDto.
        :rtype: str
        """
        return self._commit_msg

    @commit_msg.setter
    def commit_msg(self, commit_msg):
        r"""Sets the commit_msg of this ItemCommitDto.

        **参数解释：** 提交信息。 **取值范围：** 不涉及。            

        :param commit_msg: The commit_msg of this ItemCommitDto.
        :type commit_msg: str
        """
        self._commit_msg = commit_msg

    @property
    def commit_url(self):
        r"""Gets the commit_url of this ItemCommitDto.

        **参数解释：** 提交访问地址。 **取值范围：** 不涉及。

        :return: The commit_url of this ItemCommitDto.
        :rtype: str
        """
        return self._commit_url

    @commit_url.setter
    def commit_url(self, commit_url):
        r"""Sets the commit_url of this ItemCommitDto.

        **参数解释：** 提交访问地址。 **取值范围：** 不涉及。

        :param commit_url: The commit_url of this ItemCommitDto.
        :type commit_url: str
        """
        self._commit_url = commit_url

    @property
    def iam_id(self):
        r"""Gets the iam_id of this ItemCommitDto.

        **参数解释：** iamId。 **取值范围：** 不涉及。

        :return: The iam_id of this ItemCommitDto.
        :rtype: str
        """
        return self._iam_id

    @iam_id.setter
    def iam_id(self, iam_id):
        r"""Sets the iam_id of this ItemCommitDto.

        **参数解释：** iamId。 **取值范围：** 不涉及。

        :param iam_id: The iam_id of this ItemCommitDto.
        :type iam_id: str
        """
        self._iam_id = iam_id

    @property
    def create_at(self):
        r"""Gets the create_at of this ItemCommitDto.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :return: The create_at of this ItemCommitDto.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ItemCommitDto.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :param create_at: The create_at of this ItemCommitDto.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ItemCommitDto.

        **参数解释：** 更新时间。 **取值范围：** 不涉及。  

        :return: The update_at of this ItemCommitDto.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ItemCommitDto.

        **参数解释：** 更新时间。 **取值范围：** 不涉及。  

        :param update_at: The update_at of this ItemCommitDto.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def item_url(self):
        r"""Gets the item_url of this ItemCommitDto.

        **参数解释：** 工作项访问地址。 **取值范围：** 不涉及。

        :return: The item_url of this ItemCommitDto.
        :rtype: str
        """
        return self._item_url

    @item_url.setter
    def item_url(self, item_url):
        r"""Sets the item_url of this ItemCommitDto.

        **参数解释：** 工作项访问地址。 **取值范围：** 不涉及。

        :param item_url: The item_url of this ItemCommitDto.
        :type item_url: str
        """
        self._item_url = item_url

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ItemCommitDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
