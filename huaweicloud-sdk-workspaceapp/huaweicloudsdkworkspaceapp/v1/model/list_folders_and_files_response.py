# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFoldersAndFilesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'location': 'str',
        'prefix': 'str',
        'files': 'list[FileInfo]',
        'folders': 'list[FolderInfo]',
        'marker': 'str',
        'next_marker': 'str',
        'max_keys': 'int'
    }

    attribute_map = {
        'location': 'location',
        'prefix': 'prefix',
        'files': 'files',
        'folders': 'folders',
        'marker': 'marker',
        'next_marker': 'next_marker',
        'max_keys': 'max_keys'
    }

    def __init__(self, location=None, prefix=None, files=None, folders=None, marker=None, next_marker=None, max_keys=None):
        r"""ListFoldersAndFilesResponse

        The model defined in huaweicloud sdk

        :param location: 文件系统所在区域代号。
        :type location: str
        :param prefix: 文件名的绝对路径的前缀。
        :type prefix: str
        :param files: 文件信息列表。
        :type files: list[:class:`huaweicloudsdkworkspaceapp.v1.FileInfo`]
        :param folders: 文件夹信息列表。
        :type folders: list[:class:`huaweicloudsdkworkspaceapp.v1.FolderInfo`]
        :param marker: 本次列举的文件的起始位置，默认为空。
        :type marker: str
        :param next_marker: 下次列举请求的的起始位置，默认为空。
        :type next_marker: str
        :param max_keys: 本次列举可以返回的最大文件数量，非本次列举返回的数量，取入参与系统默认值的小值为准。
        :type max_keys: int
        """
        
        super(ListFoldersAndFilesResponse, self).__init__()

        self._location = None
        self._prefix = None
        self._files = None
        self._folders = None
        self._marker = None
        self._next_marker = None
        self._max_keys = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if prefix is not None:
            self.prefix = prefix
        if files is not None:
            self.files = files
        if folders is not None:
            self.folders = folders
        if marker is not None:
            self.marker = marker
        if next_marker is not None:
            self.next_marker = next_marker
        if max_keys is not None:
            self.max_keys = max_keys

    @property
    def location(self):
        r"""Gets the location of this ListFoldersAndFilesResponse.

        文件系统所在区域代号。

        :return: The location of this ListFoldersAndFilesResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ListFoldersAndFilesResponse.

        文件系统所在区域代号。

        :param location: The location of this ListFoldersAndFilesResponse.
        :type location: str
        """
        self._location = location

    @property
    def prefix(self):
        r"""Gets the prefix of this ListFoldersAndFilesResponse.

        文件名的绝对路径的前缀。

        :return: The prefix of this ListFoldersAndFilesResponse.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this ListFoldersAndFilesResponse.

        文件名的绝对路径的前缀。

        :param prefix: The prefix of this ListFoldersAndFilesResponse.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def files(self):
        r"""Gets the files of this ListFoldersAndFilesResponse.

        文件信息列表。

        :return: The files of this ListFoldersAndFilesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.FileInfo`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this ListFoldersAndFilesResponse.

        文件信息列表。

        :param files: The files of this ListFoldersAndFilesResponse.
        :type files: list[:class:`huaweicloudsdkworkspaceapp.v1.FileInfo`]
        """
        self._files = files

    @property
    def folders(self):
        r"""Gets the folders of this ListFoldersAndFilesResponse.

        文件夹信息列表。

        :return: The folders of this ListFoldersAndFilesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.FolderInfo`]
        """
        return self._folders

    @folders.setter
    def folders(self, folders):
        r"""Sets the folders of this ListFoldersAndFilesResponse.

        文件夹信息列表。

        :param folders: The folders of this ListFoldersAndFilesResponse.
        :type folders: list[:class:`huaweicloudsdkworkspaceapp.v1.FolderInfo`]
        """
        self._folders = folders

    @property
    def marker(self):
        r"""Gets the marker of this ListFoldersAndFilesResponse.

        本次列举的文件的起始位置，默认为空。

        :return: The marker of this ListFoldersAndFilesResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFoldersAndFilesResponse.

        本次列举的文件的起始位置，默认为空。

        :param marker: The marker of this ListFoldersAndFilesResponse.
        :type marker: str
        """
        self._marker = marker

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListFoldersAndFilesResponse.

        下次列举请求的的起始位置，默认为空。

        :return: The next_marker of this ListFoldersAndFilesResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListFoldersAndFilesResponse.

        下次列举请求的的起始位置，默认为空。

        :param next_marker: The next_marker of this ListFoldersAndFilesResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def max_keys(self):
        r"""Gets the max_keys of this ListFoldersAndFilesResponse.

        本次列举可以返回的最大文件数量，非本次列举返回的数量，取入参与系统默认值的小值为准。

        :return: The max_keys of this ListFoldersAndFilesResponse.
        :rtype: int
        """
        return self._max_keys

    @max_keys.setter
    def max_keys(self, max_keys):
        r"""Sets the max_keys of this ListFoldersAndFilesResponse.

        本次列举可以返回的最大文件数量，非本次列举返回的数量，取入参与系统默认值的小值为准。

        :param max_keys: The max_keys of this ListFoldersAndFilesResponse.
        :type max_keys: int
        """
        self._max_keys = max_keys

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
        if not isinstance(other, ListFoldersAndFilesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
