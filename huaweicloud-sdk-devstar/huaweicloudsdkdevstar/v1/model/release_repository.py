# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReleaseRepository:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'download_path': 'str',
        'size': 'str',
        'category_name': 'str',
        'file_type': 'str',
        'created': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'download_path': 'download_path',
        'size': 'size',
        'category_name': 'category_name',
        'file_type': 'file_type',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, name=None, download_path=None, size=None, category_name=None, file_type=None, created=None, updated=None):
        """ReleaseRepository

        The model defined in huaweicloud sdk

        :param id: 软件包id
        :type id: str
        :param name: 软件包名称
        :type name: str
        :param download_path: 软件包下载地址
        :type download_path: str
        :param size: 软件包大小
        :type size: str
        :param category_name: 软件包类型名称
        :type category_name: str
        :param file_type: 文件类型
        :type file_type: str
        :param created: 创建时间
        :type created: str
        :param updated: 修改时间
        :type updated: str
        """
        
        

        self._id = None
        self._name = None
        self._download_path = None
        self._size = None
        self._category_name = None
        self._file_type = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if download_path is not None:
            self.download_path = download_path
        if size is not None:
            self.size = size
        if category_name is not None:
            self.category_name = category_name
        if file_type is not None:
            self.file_type = file_type
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this ReleaseRepository.

        软件包id

        :return: The id of this ReleaseRepository.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReleaseRepository.

        软件包id

        :param id: The id of this ReleaseRepository.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ReleaseRepository.

        软件包名称

        :return: The name of this ReleaseRepository.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReleaseRepository.

        软件包名称

        :param name: The name of this ReleaseRepository.
        :type name: str
        """
        self._name = name

    @property
    def download_path(self):
        """Gets the download_path of this ReleaseRepository.

        软件包下载地址

        :return: The download_path of this ReleaseRepository.
        :rtype: str
        """
        return self._download_path

    @download_path.setter
    def download_path(self, download_path):
        """Sets the download_path of this ReleaseRepository.

        软件包下载地址

        :param download_path: The download_path of this ReleaseRepository.
        :type download_path: str
        """
        self._download_path = download_path

    @property
    def size(self):
        """Gets the size of this ReleaseRepository.

        软件包大小

        :return: The size of this ReleaseRepository.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ReleaseRepository.

        软件包大小

        :param size: The size of this ReleaseRepository.
        :type size: str
        """
        self._size = size

    @property
    def category_name(self):
        """Gets the category_name of this ReleaseRepository.

        软件包类型名称

        :return: The category_name of this ReleaseRepository.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this ReleaseRepository.

        软件包类型名称

        :param category_name: The category_name of this ReleaseRepository.
        :type category_name: str
        """
        self._category_name = category_name

    @property
    def file_type(self):
        """Gets the file_type of this ReleaseRepository.

        文件类型

        :return: The file_type of this ReleaseRepository.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ReleaseRepository.

        文件类型

        :param file_type: The file_type of this ReleaseRepository.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def created(self):
        """Gets the created of this ReleaseRepository.

        创建时间

        :return: The created of this ReleaseRepository.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ReleaseRepository.

        创建时间

        :param created: The created of this ReleaseRepository.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ReleaseRepository.

        修改时间

        :return: The updated of this ReleaseRepository.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ReleaseRepository.

        修改时间

        :param updated: The updated of this ReleaseRepository.
        :type updated: str
        """
        self._updated = updated

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
        if not isinstance(other, ReleaseRepository):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
