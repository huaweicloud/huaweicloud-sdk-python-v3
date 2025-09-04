# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFoldersAndFilesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'cloud_storage_assignment_id': 'str',
        'folder_url': 'str',
        'marker': 'str',
        'max_keys': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'cloud_storage_assignment_id': 'cloud_storage_assignment_id',
        'folder_url': 'folder_url',
        'marker': 'marker',
        'max_keys': 'max_keys'
    }

    def __init__(self, user_name=None, cloud_storage_assignment_id=None, folder_url=None, marker=None, max_keys=None):
        r"""ListFoldersAndFilesRequest

        The model defined in huaweicloud sdk

        :param user_name: 用户名
        :type user_name: str
        :param cloud_storage_assignment_id: 个人文件夹ID。(用户拥有多个文件夹时，如果不传个人文件夹id则选择最早创建的文件系统进行文件查询)
        :type cloud_storage_assignment_id: str
        :param folder_url: 查询文件夹路径
        :type folder_url: str
        :param marker: 指定一个标识符，从该标识符以后按文件名的字典顺序返回文件列表。
        :type marker: str
        :param max_keys: 列举文件系统的最大数目，返回的文件系统列表将是按照字典顺序的最多前 maxKeys 个，默认取值为1000。
        :type max_keys: int
        """
        
        

        self._user_name = None
        self._cloud_storage_assignment_id = None
        self._folder_url = None
        self._marker = None
        self._max_keys = None
        self.discriminator = None

        self.user_name = user_name
        if cloud_storage_assignment_id is not None:
            self.cloud_storage_assignment_id = cloud_storage_assignment_id
        self.folder_url = folder_url
        if marker is not None:
            self.marker = marker
        if max_keys is not None:
            self.max_keys = max_keys

    @property
    def user_name(self):
        r"""Gets the user_name of this ListFoldersAndFilesRequest.

        用户名

        :return: The user_name of this ListFoldersAndFilesRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListFoldersAndFilesRequest.

        用户名

        :param user_name: The user_name of this ListFoldersAndFilesRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def cloud_storage_assignment_id(self):
        r"""Gets the cloud_storage_assignment_id of this ListFoldersAndFilesRequest.

        个人文件夹ID。(用户拥有多个文件夹时，如果不传个人文件夹id则选择最早创建的文件系统进行文件查询)

        :return: The cloud_storage_assignment_id of this ListFoldersAndFilesRequest.
        :rtype: str
        """
        return self._cloud_storage_assignment_id

    @cloud_storage_assignment_id.setter
    def cloud_storage_assignment_id(self, cloud_storage_assignment_id):
        r"""Sets the cloud_storage_assignment_id of this ListFoldersAndFilesRequest.

        个人文件夹ID。(用户拥有多个文件夹时，如果不传个人文件夹id则选择最早创建的文件系统进行文件查询)

        :param cloud_storage_assignment_id: The cloud_storage_assignment_id of this ListFoldersAndFilesRequest.
        :type cloud_storage_assignment_id: str
        """
        self._cloud_storage_assignment_id = cloud_storage_assignment_id

    @property
    def folder_url(self):
        r"""Gets the folder_url of this ListFoldersAndFilesRequest.

        查询文件夹路径

        :return: The folder_url of this ListFoldersAndFilesRequest.
        :rtype: str
        """
        return self._folder_url

    @folder_url.setter
    def folder_url(self, folder_url):
        r"""Sets the folder_url of this ListFoldersAndFilesRequest.

        查询文件夹路径

        :param folder_url: The folder_url of this ListFoldersAndFilesRequest.
        :type folder_url: str
        """
        self._folder_url = folder_url

    @property
    def marker(self):
        r"""Gets the marker of this ListFoldersAndFilesRequest.

        指定一个标识符，从该标识符以后按文件名的字典顺序返回文件列表。

        :return: The marker of this ListFoldersAndFilesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFoldersAndFilesRequest.

        指定一个标识符，从该标识符以后按文件名的字典顺序返回文件列表。

        :param marker: The marker of this ListFoldersAndFilesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def max_keys(self):
        r"""Gets the max_keys of this ListFoldersAndFilesRequest.

        列举文件系统的最大数目，返回的文件系统列表将是按照字典顺序的最多前 maxKeys 个，默认取值为1000。

        :return: The max_keys of this ListFoldersAndFilesRequest.
        :rtype: int
        """
        return self._max_keys

    @max_keys.setter
    def max_keys(self, max_keys):
        r"""Sets the max_keys of this ListFoldersAndFilesRequest.

        列举文件系统的最大数目，返回的文件系统列表将是按照字典顺序的最多前 maxKeys 个，默认取值为1000。

        :param max_keys: The max_keys of this ListFoldersAndFilesRequest.
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
        if not isinstance(other, ListFoldersAndFilesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
