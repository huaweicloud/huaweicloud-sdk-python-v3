# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogTreeDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'path': 'str',
        'type': 'str',
        'commit': 'RepositoryCommitDto',
        'blob_id': 'str',
        'submodule_url': 'str',
        'is_limited': 'bool',
        'submodule_link': 'str',
        'md5': 'str',
        'nick_name': 'str',
        'tenant_name': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'type': 'type',
        'commit': 'commit',
        'blob_id': 'blob_id',
        'submodule_url': 'submodule_url',
        'is_limited': 'is_limited',
        'submodule_link': 'submodule_link',
        'md5': 'md5',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name',
        'user_name': 'user_name'
    }

    def __init__(self, name=None, path=None, type=None, commit=None, blob_id=None, submodule_url=None, is_limited=None, submodule_link=None, md5=None, nick_name=None, tenant_name=None, user_name=None):
        r"""LogTreeDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 文件名
        :type name: str
        :param path: **参数解释：** 路径
        :type path: str
        :param type: **参数解释：** 文件类型
        :type type: str
        :param commit: **参数解释：** 最近提交信息
        :type commit: :class:`huaweicloudsdkcodeartsrepo.v4.RepositoryCommitDto`
        :param blob_id: **参数解释：** 文件id
        :type blob_id: str
        :param submodule_url: **参数解释：** 子模块url地址
        :type submodule_url: str
        :param is_limited: **参数解释：** 文件是否受限
        :type is_limited: bool
        :param submodule_link: **参数解释：** 子模块链接
        :type submodule_link: str
        :param md5: **参数解释：** 文件md5
        :type md5: str
        :param nick_name: **参数解释：** 最近提交作者昵称
        :type nick_name: str
        :param tenant_name: **参数解释：** 租户名称
        :type tenant_name: str
        :param user_name: **参数解释：** 用户名
        :type user_name: str
        """
        
        

        self._name = None
        self._path = None
        self._type = None
        self._commit = None
        self._blob_id = None
        self._submodule_url = None
        self._is_limited = None
        self._submodule_link = None
        self._md5 = None
        self._nick_name = None
        self._tenant_name = None
        self._user_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if type is not None:
            self.type = type
        if commit is not None:
            self.commit = commit
        if blob_id is not None:
            self.blob_id = blob_id
        if submodule_url is not None:
            self.submodule_url = submodule_url
        if is_limited is not None:
            self.is_limited = is_limited
        if submodule_link is not None:
            self.submodule_link = submodule_link
        if md5 is not None:
            self.md5 = md5
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if user_name is not None:
            self.user_name = user_name

    @property
    def name(self):
        r"""Gets the name of this LogTreeDto.

        **参数解释：** 文件名

        :return: The name of this LogTreeDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LogTreeDto.

        **参数解释：** 文件名

        :param name: The name of this LogTreeDto.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        r"""Gets the path of this LogTreeDto.

        **参数解释：** 路径

        :return: The path of this LogTreeDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this LogTreeDto.

        **参数解释：** 路径

        :param path: The path of this LogTreeDto.
        :type path: str
        """
        self._path = path

    @property
    def type(self):
        r"""Gets the type of this LogTreeDto.

        **参数解释：** 文件类型

        :return: The type of this LogTreeDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LogTreeDto.

        **参数解释：** 文件类型

        :param type: The type of this LogTreeDto.
        :type type: str
        """
        self._type = type

    @property
    def commit(self):
        r"""Gets the commit of this LogTreeDto.

        **参数解释：** 最近提交信息

        :return: The commit of this LogTreeDto.
        :rtype: :class:`huaweicloudsdkcodeartsrepo.v4.RepositoryCommitDto`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        r"""Sets the commit of this LogTreeDto.

        **参数解释：** 最近提交信息

        :param commit: The commit of this LogTreeDto.
        :type commit: :class:`huaweicloudsdkcodeartsrepo.v4.RepositoryCommitDto`
        """
        self._commit = commit

    @property
    def blob_id(self):
        r"""Gets the blob_id of this LogTreeDto.

        **参数解释：** 文件id

        :return: The blob_id of this LogTreeDto.
        :rtype: str
        """
        return self._blob_id

    @blob_id.setter
    def blob_id(self, blob_id):
        r"""Sets the blob_id of this LogTreeDto.

        **参数解释：** 文件id

        :param blob_id: The blob_id of this LogTreeDto.
        :type blob_id: str
        """
        self._blob_id = blob_id

    @property
    def submodule_url(self):
        r"""Gets the submodule_url of this LogTreeDto.

        **参数解释：** 子模块url地址

        :return: The submodule_url of this LogTreeDto.
        :rtype: str
        """
        return self._submodule_url

    @submodule_url.setter
    def submodule_url(self, submodule_url):
        r"""Sets the submodule_url of this LogTreeDto.

        **参数解释：** 子模块url地址

        :param submodule_url: The submodule_url of this LogTreeDto.
        :type submodule_url: str
        """
        self._submodule_url = submodule_url

    @property
    def is_limited(self):
        r"""Gets the is_limited of this LogTreeDto.

        **参数解释：** 文件是否受限

        :return: The is_limited of this LogTreeDto.
        :rtype: bool
        """
        return self._is_limited

    @is_limited.setter
    def is_limited(self, is_limited):
        r"""Sets the is_limited of this LogTreeDto.

        **参数解释：** 文件是否受限

        :param is_limited: The is_limited of this LogTreeDto.
        :type is_limited: bool
        """
        self._is_limited = is_limited

    @property
    def submodule_link(self):
        r"""Gets the submodule_link of this LogTreeDto.

        **参数解释：** 子模块链接

        :return: The submodule_link of this LogTreeDto.
        :rtype: str
        """
        return self._submodule_link

    @submodule_link.setter
    def submodule_link(self, submodule_link):
        r"""Sets the submodule_link of this LogTreeDto.

        **参数解释：** 子模块链接

        :param submodule_link: The submodule_link of this LogTreeDto.
        :type submodule_link: str
        """
        self._submodule_link = submodule_link

    @property
    def md5(self):
        r"""Gets the md5 of this LogTreeDto.

        **参数解释：** 文件md5

        :return: The md5 of this LogTreeDto.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        r"""Sets the md5 of this LogTreeDto.

        **参数解释：** 文件md5

        :param md5: The md5 of this LogTreeDto.
        :type md5: str
        """
        self._md5 = md5

    @property
    def nick_name(self):
        r"""Gets the nick_name of this LogTreeDto.

        **参数解释：** 最近提交作者昵称

        :return: The nick_name of this LogTreeDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this LogTreeDto.

        **参数解释：** 最近提交作者昵称

        :param nick_name: The nick_name of this LogTreeDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this LogTreeDto.

        **参数解释：** 租户名称

        :return: The tenant_name of this LogTreeDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this LogTreeDto.

        **参数解释：** 租户名称

        :param tenant_name: The tenant_name of this LogTreeDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def user_name(self):
        r"""Gets the user_name of this LogTreeDto.

        **参数解释：** 用户名

        :return: The user_name of this LogTreeDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this LogTreeDto.

        **参数解释：** 用户名

        :param user_name: The user_name of this LogTreeDto.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, LogTreeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
