# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryNavigationOutlineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'revision': 'str',
        'ref': 'str',
        'language': 'str',
        'blob': 'str',
        'file_path': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'revision': 'revision',
        'ref': 'ref',
        'language': 'language',
        'blob': 'blob',
        'file_path': 'file_path'
    }

    def __init__(self, repository_id=None, revision=None, ref=None, language=None, blob=None, file_path=None):
        r"""ShowRepositoryNavigationOutlineRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[[查询用户所有仓库](https://support.huaweicloud.com/intl/zh-cn/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk_ch)[[查询用户所有仓库](https://support.huaweicloud.com/eu/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type repository_id: int
        :param revision: **参数解释：** 版本提交id **取值范围：** 不涉及
        :type revision: str
        :param ref: **参数解释：** 引用，可以是分支名称、标签名称或者commitid，如果不传则为默认分支。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type ref: str
        :param language: **参数解释：** 代码语言 **取值范围：** - C - C++ - Go - Java - JavaScript - PHP - Python - Ruby - Rust
        :type language: str
        :param blob: **参数解释：** blob文件ID。通过[[查询某个仓库的文件信息](https://support.huaweicloud.com/api-codeartsrepo/ListFilesByQuery.html)](tag:hws)[[查询某个仓库的文件信息](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListFilesByQuery.html)](tag:hws_hk)[查询某个仓库的文件信息](tag:hcs,hcs_sm)接口查询某个仓库的文件信息获取。 **取值范围：** 不涉及。
        :type blob: str
        :param file_path: **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。
        :type file_path: str
        """
        
        

        self._repository_id = None
        self._revision = None
        self._ref = None
        self._language = None
        self._blob = None
        self._file_path = None
        self.discriminator = None

        self.repository_id = repository_id
        if revision is not None:
            self.revision = revision
        if ref is not None:
            self.ref = ref
        self.language = language
        self.blob = blob
        self.file_path = file_path

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[[查询用户所有仓库](https://support.huaweicloud.com/intl/zh-cn/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk_ch)[[查询用户所有仓库](https://support.huaweicloud.com/eu/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The repository_id of this ShowRepositoryNavigationOutlineRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[[查询用户所有仓库](https://support.huaweicloud.com/intl/zh-cn/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk_ch)[[查询用户所有仓库](https://support.huaweicloud.com/eu/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param repository_id: The repository_id of this ShowRepositoryNavigationOutlineRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def revision(self):
        r"""Gets the revision of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** 版本提交id **取值范围：** 不涉及

        :return: The revision of this ShowRepositoryNavigationOutlineRequest.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        r"""Sets the revision of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** 版本提交id **取值范围：** 不涉及

        :param revision: The revision of this ShowRepositoryNavigationOutlineRequest.
        :type revision: str
        """
        self._revision = revision

    @property
    def ref(self):
        r"""Gets the ref of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** 引用，可以是分支名称、标签名称或者commitid，如果不传则为默认分支。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The ref of this ShowRepositoryNavigationOutlineRequest.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** 引用，可以是分支名称、标签名称或者commitid，如果不传则为默认分支。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param ref: The ref of this ShowRepositoryNavigationOutlineRequest.
        :type ref: str
        """
        self._ref = ref

    @property
    def language(self):
        r"""Gets the language of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** 代码语言 **取值范围：** - C - C++ - Go - Java - JavaScript - PHP - Python - Ruby - Rust

        :return: The language of this ShowRepositoryNavigationOutlineRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** 代码语言 **取值范围：** - C - C++ - Go - Java - JavaScript - PHP - Python - Ruby - Rust

        :param language: The language of this ShowRepositoryNavigationOutlineRequest.
        :type language: str
        """
        self._language = language

    @property
    def blob(self):
        r"""Gets the blob of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** blob文件ID。通过[[查询某个仓库的文件信息](https://support.huaweicloud.com/api-codeartsrepo/ListFilesByQuery.html)](tag:hws)[[查询某个仓库的文件信息](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListFilesByQuery.html)](tag:hws_hk)[查询某个仓库的文件信息](tag:hcs,hcs_sm)接口查询某个仓库的文件信息获取。 **取值范围：** 不涉及。

        :return: The blob of this ShowRepositoryNavigationOutlineRequest.
        :rtype: str
        """
        return self._blob

    @blob.setter
    def blob(self, blob):
        r"""Sets the blob of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** blob文件ID。通过[[查询某个仓库的文件信息](https://support.huaweicloud.com/api-codeartsrepo/ListFilesByQuery.html)](tag:hws)[[查询某个仓库的文件信息](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListFilesByQuery.html)](tag:hws_hk)[查询某个仓库的文件信息](tag:hcs,hcs_sm)接口查询某个仓库的文件信息获取。 **取值范围：** 不涉及。

        :param blob: The blob of this ShowRepositoryNavigationOutlineRequest.
        :type blob: str
        """
        self._blob = blob

    @property
    def file_path(self):
        r"""Gets the file_path of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。

        :return: The file_path of this ShowRepositoryNavigationOutlineRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ShowRepositoryNavigationOutlineRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。

        :param file_path: The file_path of this ShowRepositoryNavigationOutlineRequest.
        :type file_path: str
        """
        self._file_path = file_path

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
        if not isinstance(other, ShowRepositoryNavigationOutlineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
