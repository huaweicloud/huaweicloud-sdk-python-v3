# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadArchiveRequest:

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
        'sha': 'str',
        'path': 'str',
        'archive_format': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'sha': 'sha',
        'path': 'path',
        'archive_format': 'archive_format'
    }

    def __init__(self, repository_id=None, sha=None, path=None, archive_format=None):
        r"""DownloadArchiveRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param sha: **参数解释：** 分支名、tag名、提交ID。
        :type sha: str
        :param path: **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。
        :type path: str
        :param archive_format: **参数解释：** 下载格式。 **取值范围：** - zip。 - tar.gz。   - tar.bz2。 - tar。
        :type archive_format: str
        """
        
        

        self._repository_id = None
        self._sha = None
        self._path = None
        self._archive_format = None
        self.discriminator = None

        self.repository_id = repository_id
        if sha is not None:
            self.sha = sha
        if path is not None:
            self.path = path
        if archive_format is not None:
            self.archive_format = archive_format

    @property
    def repository_id(self):
        r"""Gets the repository_id of this DownloadArchiveRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this DownloadArchiveRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this DownloadArchiveRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this DownloadArchiveRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def sha(self):
        r"""Gets the sha of this DownloadArchiveRequest.

        **参数解释：** 分支名、tag名、提交ID。

        :return: The sha of this DownloadArchiveRequest.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        r"""Sets the sha of this DownloadArchiveRequest.

        **参数解释：** 分支名、tag名、提交ID。

        :param sha: The sha of this DownloadArchiveRequest.
        :type sha: str
        """
        self._sha = sha

    @property
    def path(self):
        r"""Gets the path of this DownloadArchiveRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。

        :return: The path of this DownloadArchiveRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this DownloadArchiveRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。

        :param path: The path of this DownloadArchiveRequest.
        :type path: str
        """
        self._path = path

    @property
    def archive_format(self):
        r"""Gets the archive_format of this DownloadArchiveRequest.

        **参数解释：** 下载格式。 **取值范围：** - zip。 - tar.gz。   - tar.bz2。 - tar。

        :return: The archive_format of this DownloadArchiveRequest.
        :rtype: str
        """
        return self._archive_format

    @archive_format.setter
    def archive_format(self, archive_format):
        r"""Sets the archive_format of this DownloadArchiveRequest.

        **参数解释：** 下载格式。 **取值范围：** - zip。 - tar.gz。   - tar.bz2。 - tar。

        :param archive_format: The archive_format of this DownloadArchiveRequest.
        :type archive_format: str
        """
        self._archive_format = archive_format

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
        if not isinstance(other, DownloadArchiveRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
