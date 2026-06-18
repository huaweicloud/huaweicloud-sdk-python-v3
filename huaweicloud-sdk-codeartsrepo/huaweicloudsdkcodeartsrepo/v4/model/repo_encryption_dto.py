# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoEncryptionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_id': 'int',
        'repo_name': 'str',
        'full_path': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'owner_id': 'int',
        'owner_iam_id': 'str',
        'owner_tenant_name': 'str',
        'owner_nick_name': 'str',
        'owner_name': 'str'
    }

    attribute_map = {
        'repo_id': 'repo_id',
        'repo_name': 'repo_name',
        'full_path': 'full_path',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'owner_id': 'owner_id',
        'owner_iam_id': 'owner_iam_id',
        'owner_tenant_name': 'owner_tenant_name',
        'owner_nick_name': 'owner_nick_name',
        'owner_name': 'owner_name'
    }

    def __init__(self, repo_id=None, repo_name=None, full_path=None, project_id=None, project_name=None, owner_id=None, owner_iam_id=None, owner_tenant_name=None, owner_nick_name=None, owner_name=None):
        r"""RepoEncryptionDto

        The model defined in huaweicloud sdk

        :param repo_id: **参数解释：** 代码仓id。
        :type repo_id: int
        :param repo_name: **参数解释：** 代码仓名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type repo_name: str
        :param full_path: **参数解释：** 代码仓全路径。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type full_path: str
        :param project_id: **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type project_id: str
        :param project_name: **参数解释：** 项目名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type project_name: str
        :param owner_id: **参数解释：** 代码仓所有者id。
        :type owner_id: int
        :param owner_iam_id: **参数解释：** 代码仓所有者iamId。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type owner_iam_id: str
        :param owner_tenant_name: **参数解释：** 代码仓所有者租户id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type owner_tenant_name: str
        :param owner_nick_name: **参数解释：** 代码仓所有者昵称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type owner_nick_name: str
        :param owner_name: **参数解释：** 代码仓所有者名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type owner_name: str
        """
        
        

        self._repo_id = None
        self._repo_name = None
        self._full_path = None
        self._project_id = None
        self._project_name = None
        self._owner_id = None
        self._owner_iam_id = None
        self._owner_tenant_name = None
        self._owner_nick_name = None
        self._owner_name = None
        self.discriminator = None

        if repo_id is not None:
            self.repo_id = repo_id
        if repo_name is not None:
            self.repo_name = repo_name
        if full_path is not None:
            self.full_path = full_path
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_iam_id is not None:
            self.owner_iam_id = owner_iam_id
        if owner_tenant_name is not None:
            self.owner_tenant_name = owner_tenant_name
        if owner_nick_name is not None:
            self.owner_nick_name = owner_nick_name
        if owner_name is not None:
            self.owner_name = owner_name

    @property
    def repo_id(self):
        r"""Gets the repo_id of this RepoEncryptionDto.

        **参数解释：** 代码仓id。

        :return: The repo_id of this RepoEncryptionDto.
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this RepoEncryptionDto.

        **参数解释：** 代码仓id。

        :param repo_id: The repo_id of this RepoEncryptionDto.
        :type repo_id: int
        """
        self._repo_id = repo_id

    @property
    def repo_name(self):
        r"""Gets the repo_name of this RepoEncryptionDto.

        **参数解释：** 代码仓名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The repo_name of this RepoEncryptionDto.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this RepoEncryptionDto.

        **参数解释：** 代码仓名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param repo_name: The repo_name of this RepoEncryptionDto.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def full_path(self):
        r"""Gets the full_path of this RepoEncryptionDto.

        **参数解释：** 代码仓全路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The full_path of this RepoEncryptionDto.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        r"""Sets the full_path of this RepoEncryptionDto.

        **参数解释：** 代码仓全路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param full_path: The full_path of this RepoEncryptionDto.
        :type full_path: str
        """
        self._full_path = full_path

    @property
    def project_id(self):
        r"""Gets the project_id of this RepoEncryptionDto.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The project_id of this RepoEncryptionDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RepoEncryptionDto.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param project_id: The project_id of this RepoEncryptionDto.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this RepoEncryptionDto.

        **参数解释：** 项目名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The project_name of this RepoEncryptionDto.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this RepoEncryptionDto.

        **参数解释：** 项目名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param project_name: The project_name of this RepoEncryptionDto.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def owner_id(self):
        r"""Gets the owner_id of this RepoEncryptionDto.

        **参数解释：** 代码仓所有者id。

        :return: The owner_id of this RepoEncryptionDto.
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this RepoEncryptionDto.

        **参数解释：** 代码仓所有者id。

        :param owner_id: The owner_id of this RepoEncryptionDto.
        :type owner_id: int
        """
        self._owner_id = owner_id

    @property
    def owner_iam_id(self):
        r"""Gets the owner_iam_id of this RepoEncryptionDto.

        **参数解释：** 代码仓所有者iamId。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The owner_iam_id of this RepoEncryptionDto.
        :rtype: str
        """
        return self._owner_iam_id

    @owner_iam_id.setter
    def owner_iam_id(self, owner_iam_id):
        r"""Sets the owner_iam_id of this RepoEncryptionDto.

        **参数解释：** 代码仓所有者iamId。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param owner_iam_id: The owner_iam_id of this RepoEncryptionDto.
        :type owner_iam_id: str
        """
        self._owner_iam_id = owner_iam_id

    @property
    def owner_tenant_name(self):
        r"""Gets the owner_tenant_name of this RepoEncryptionDto.

        **参数解释：** 代码仓所有者租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The owner_tenant_name of this RepoEncryptionDto.
        :rtype: str
        """
        return self._owner_tenant_name

    @owner_tenant_name.setter
    def owner_tenant_name(self, owner_tenant_name):
        r"""Sets the owner_tenant_name of this RepoEncryptionDto.

        **参数解释：** 代码仓所有者租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param owner_tenant_name: The owner_tenant_name of this RepoEncryptionDto.
        :type owner_tenant_name: str
        """
        self._owner_tenant_name = owner_tenant_name

    @property
    def owner_nick_name(self):
        r"""Gets the owner_nick_name of this RepoEncryptionDto.

        **参数解释：** 代码仓所有者昵称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The owner_nick_name of this RepoEncryptionDto.
        :rtype: str
        """
        return self._owner_nick_name

    @owner_nick_name.setter
    def owner_nick_name(self, owner_nick_name):
        r"""Sets the owner_nick_name of this RepoEncryptionDto.

        **参数解释：** 代码仓所有者昵称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param owner_nick_name: The owner_nick_name of this RepoEncryptionDto.
        :type owner_nick_name: str
        """
        self._owner_nick_name = owner_nick_name

    @property
    def owner_name(self):
        r"""Gets the owner_name of this RepoEncryptionDto.

        **参数解释：** 代码仓所有者名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The owner_name of this RepoEncryptionDto.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this RepoEncryptionDto.

        **参数解释：** 代码仓所有者名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param owner_name: The owner_name of this RepoEncryptionDto.
        :type owner_name: str
        """
        self._owner_name = owner_name

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
        if not isinstance(other, RepoEncryptionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
