# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FolderRedirectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relative_path': 'str',
        'storage_paths': 'str',
        'include_common_folders': 'int'
    }

    attribute_map = {
        'relative_path': 'relative_path',
        'storage_paths': 'storage_paths',
        'include_common_folders': 'include_common_folders'
    }

    def __init__(self, relative_path=None, storage_paths=None, include_common_folders=None):
        r"""FolderRedirectionOptions

        The model defined in huaweicloud sdk

        :param relative_path: 目标文件夹位置。
        :type relative_path: str
        :param storage_paths: 用户存储路径。
        :type storage_paths: str
        :param include_common_folders: 文件夹选项。
        :type include_common_folders: int
        """
        
        

        self._relative_path = None
        self._storage_paths = None
        self._include_common_folders = None
        self.discriminator = None

        if relative_path is not None:
            self.relative_path = relative_path
        if storage_paths is not None:
            self.storage_paths = storage_paths
        if include_common_folders is not None:
            self.include_common_folders = include_common_folders

    @property
    def relative_path(self):
        r"""Gets the relative_path of this FolderRedirectionOptions.

        目标文件夹位置。

        :return: The relative_path of this FolderRedirectionOptions.
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        r"""Sets the relative_path of this FolderRedirectionOptions.

        目标文件夹位置。

        :param relative_path: The relative_path of this FolderRedirectionOptions.
        :type relative_path: str
        """
        self._relative_path = relative_path

    @property
    def storage_paths(self):
        r"""Gets the storage_paths of this FolderRedirectionOptions.

        用户存储路径。

        :return: The storage_paths of this FolderRedirectionOptions.
        :rtype: str
        """
        return self._storage_paths

    @storage_paths.setter
    def storage_paths(self, storage_paths):
        r"""Sets the storage_paths of this FolderRedirectionOptions.

        用户存储路径。

        :param storage_paths: The storage_paths of this FolderRedirectionOptions.
        :type storage_paths: str
        """
        self._storage_paths = storage_paths

    @property
    def include_common_folders(self):
        r"""Gets the include_common_folders of this FolderRedirectionOptions.

        文件夹选项。

        :return: The include_common_folders of this FolderRedirectionOptions.
        :rtype: int
        """
        return self._include_common_folders

    @include_common_folders.setter
    def include_common_folders(self, include_common_folders):
        r"""Sets the include_common_folders of this FolderRedirectionOptions.

        文件夹选项。

        :param include_common_folders: The include_common_folders of this FolderRedirectionOptions.
        :type include_common_folders: int
        """
        self._include_common_folders = include_common_folders

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
        if not isinstance(other, FolderRedirectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
