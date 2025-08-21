# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadBlobsRawRequest:

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
        'blob_id': 'str',
        'file_name': 'str',
        'file_path': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'blob_id': 'blob_id',
        'file_name': 'file_name',
        'file_path': 'file_path'
    }

    def __init__(self, repository_id=None, blob_id=None, file_name=None, file_path=None):
        r"""DownloadBlobsRawRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param blob_id: **参数解释：** bolb文件ID。通过[[查询某个仓库的文件信息](https://support.huaweicloud.com/api-codeartsrepo/ListFilesByQuery.html)](tag:hws)[[查询某个仓库的文件信息](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListFilesByQuery.html)](tag:hws_hk)[查询某个仓库的文件信息](tag:hcs,hcs_sm)接口查询某个仓库的文件信息获取。 **取值范围：** 不涉及。
        :type blob_id: str
        :param file_name: **参数解释：** 下载文件名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type file_name: str
        :param file_path: **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。
        :type file_path: str
        """
        
        

        self._repository_id = None
        self._blob_id = None
        self._file_name = None
        self._file_path = None
        self.discriminator = None

        self.repository_id = repository_id
        self.blob_id = blob_id
        if file_name is not None:
            self.file_name = file_name
        self.file_path = file_path

    @property
    def repository_id(self):
        r"""Gets the repository_id of this DownloadBlobsRawRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this DownloadBlobsRawRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this DownloadBlobsRawRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this DownloadBlobsRawRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def blob_id(self):
        r"""Gets the blob_id of this DownloadBlobsRawRequest.

        **参数解释：** bolb文件ID。通过[[查询某个仓库的文件信息](https://support.huaweicloud.com/api-codeartsrepo/ListFilesByQuery.html)](tag:hws)[[查询某个仓库的文件信息](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListFilesByQuery.html)](tag:hws_hk)[查询某个仓库的文件信息](tag:hcs,hcs_sm)接口查询某个仓库的文件信息获取。 **取值范围：** 不涉及。

        :return: The blob_id of this DownloadBlobsRawRequest.
        :rtype: str
        """
        return self._blob_id

    @blob_id.setter
    def blob_id(self, blob_id):
        r"""Sets the blob_id of this DownloadBlobsRawRequest.

        **参数解释：** bolb文件ID。通过[[查询某个仓库的文件信息](https://support.huaweicloud.com/api-codeartsrepo/ListFilesByQuery.html)](tag:hws)[[查询某个仓库的文件信息](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListFilesByQuery.html)](tag:hws_hk)[查询某个仓库的文件信息](tag:hcs,hcs_sm)接口查询某个仓库的文件信息获取。 **取值范围：** 不涉及。

        :param blob_id: The blob_id of this DownloadBlobsRawRequest.
        :type blob_id: str
        """
        self._blob_id = blob_id

    @property
    def file_name(self):
        r"""Gets the file_name of this DownloadBlobsRawRequest.

        **参数解释：** 下载文件名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The file_name of this DownloadBlobsRawRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this DownloadBlobsRawRequest.

        **参数解释：** 下载文件名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param file_name: The file_name of this DownloadBlobsRawRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this DownloadBlobsRawRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。

        :return: The file_path of this DownloadBlobsRawRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this DownloadBlobsRawRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。

        :param file_path: The file_path of this DownloadBlobsRawRequest.
        :type file_path: str
        """
        self._file_path = file_path

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
        if not isinstance(other, DownloadBlobsRawRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
