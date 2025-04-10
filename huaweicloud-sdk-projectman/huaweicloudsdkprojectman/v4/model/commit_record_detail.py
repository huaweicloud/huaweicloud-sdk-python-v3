# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitRecordDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'str',
        'branch_name': 'str',
        'commit_id': 'str',
        'commit_short_id': 'str',
        'commit_msg': 'str',
        'commit_url': 'str',
        'user': 'SimpleUser',
        'type': 'str',
        'create_date': 'str',
        'update_date': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'branch_name': 'branch_name',
        'commit_id': 'commit_id',
        'commit_short_id': 'commit_short_id',
        'commit_msg': 'commit_msg',
        'commit_url': 'commit_url',
        'user': 'user',
        'type': 'type',
        'create_date': 'create_date',
        'update_date': 'update_date'
    }

    def __init__(self, repository_id=None, branch_name=None, commit_id=None, commit_short_id=None, commit_msg=None, commit_url=None, user=None, type=None, create_date=None, update_date=None):
        r"""CommitRecordDetail

        The model defined in huaweicloud sdk

        :param repository_id: 仓库ID
        :type repository_id: str
        :param branch_name: 分支名称
        :type branch_name: str
        :param commit_id: commit id
        :type commit_id: str
        :param commit_short_id: commit short id
        :type commit_short_id: str
        :param commit_msg: commit 信息
        :type commit_msg: str
        :param commit_url: commit URL
        :type commit_url: str
        :param user: 
        :type user: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        :param type: 查询的类型
        :type type: str
        :param create_date: 创建时间
        :type create_date: str
        :param update_date: 更新时间
        :type update_date: str
        """
        
        

        self._repository_id = None
        self._branch_name = None
        self._commit_id = None
        self._commit_short_id = None
        self._commit_msg = None
        self._commit_url = None
        self._user = None
        self._type = None
        self._create_date = None
        self._update_date = None
        self.discriminator = None

        if repository_id is not None:
            self.repository_id = repository_id
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
        if user is not None:
            self.user = user
        if type is not None:
            self.type = type
        if create_date is not None:
            self.create_date = create_date
        if update_date is not None:
            self.update_date = update_date

    @property
    def repository_id(self):
        r"""Gets the repository_id of this CommitRecordDetail.

        仓库ID

        :return: The repository_id of this CommitRecordDetail.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this CommitRecordDetail.

        仓库ID

        :param repository_id: The repository_id of this CommitRecordDetail.
        :type repository_id: str
        """
        self._repository_id = repository_id

    @property
    def branch_name(self):
        r"""Gets the branch_name of this CommitRecordDetail.

        分支名称

        :return: The branch_name of this CommitRecordDetail.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this CommitRecordDetail.

        分支名称

        :param branch_name: The branch_name of this CommitRecordDetail.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def commit_id(self):
        r"""Gets the commit_id of this CommitRecordDetail.

        commit id

        :return: The commit_id of this CommitRecordDetail.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this CommitRecordDetail.

        commit id

        :param commit_id: The commit_id of this CommitRecordDetail.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def commit_short_id(self):
        r"""Gets the commit_short_id of this CommitRecordDetail.

        commit short id

        :return: The commit_short_id of this CommitRecordDetail.
        :rtype: str
        """
        return self._commit_short_id

    @commit_short_id.setter
    def commit_short_id(self, commit_short_id):
        r"""Sets the commit_short_id of this CommitRecordDetail.

        commit short id

        :param commit_short_id: The commit_short_id of this CommitRecordDetail.
        :type commit_short_id: str
        """
        self._commit_short_id = commit_short_id

    @property
    def commit_msg(self):
        r"""Gets the commit_msg of this CommitRecordDetail.

        commit 信息

        :return: The commit_msg of this CommitRecordDetail.
        :rtype: str
        """
        return self._commit_msg

    @commit_msg.setter
    def commit_msg(self, commit_msg):
        r"""Sets the commit_msg of this CommitRecordDetail.

        commit 信息

        :param commit_msg: The commit_msg of this CommitRecordDetail.
        :type commit_msg: str
        """
        self._commit_msg = commit_msg

    @property
    def commit_url(self):
        r"""Gets the commit_url of this CommitRecordDetail.

        commit URL

        :return: The commit_url of this CommitRecordDetail.
        :rtype: str
        """
        return self._commit_url

    @commit_url.setter
    def commit_url(self, commit_url):
        r"""Sets the commit_url of this CommitRecordDetail.

        commit URL

        :param commit_url: The commit_url of this CommitRecordDetail.
        :type commit_url: str
        """
        self._commit_url = commit_url

    @property
    def user(self):
        r"""Gets the user of this CommitRecordDetail.

        :return: The user of this CommitRecordDetail.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this CommitRecordDetail.

        :param user: The user of this CommitRecordDetail.
        :type user: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        self._user = user

    @property
    def type(self):
        r"""Gets the type of this CommitRecordDetail.

        查询的类型

        :return: The type of this CommitRecordDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CommitRecordDetail.

        查询的类型

        :param type: The type of this CommitRecordDetail.
        :type type: str
        """
        self._type = type

    @property
    def create_date(self):
        r"""Gets the create_date of this CommitRecordDetail.

        创建时间

        :return: The create_date of this CommitRecordDetail.
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        r"""Sets the create_date of this CommitRecordDetail.

        创建时间

        :param create_date: The create_date of this CommitRecordDetail.
        :type create_date: str
        """
        self._create_date = create_date

    @property
    def update_date(self):
        r"""Gets the update_date of this CommitRecordDetail.

        更新时间

        :return: The update_date of this CommitRecordDetail.
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        r"""Sets the update_date of this CommitRecordDetail.

        更新时间

        :param update_date: The update_date of this CommitRecordDetail.
        :type update_date: str
        """
        self._update_date = update_date

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
        if not isinstance(other, CommitRecordDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
