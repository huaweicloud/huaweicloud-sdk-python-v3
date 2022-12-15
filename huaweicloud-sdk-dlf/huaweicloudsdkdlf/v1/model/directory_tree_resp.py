# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirectoryTreeResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_directory_id': 'str',
        'directory_name': 'str',
        'category_type': 'str',
        'directory_id': 'str',
        'paging': 'bool',
        'offset': 'int',
        'limit': 'int',
        'count': 'int',
        'elements': 'list[TreeNodeElement]',
        'sub_directories': 'list[DirectoryTreeResp]'
    }

    attribute_map = {
        'parent_directory_id': 'parent_directory_id',
        'directory_name': 'directory_name',
        'category_type': 'category_type',
        'directory_id': 'directory_id',
        'paging': 'paging',
        'offset': 'offset',
        'limit': 'limit',
        'count': 'count',
        'elements': 'elements',
        'sub_directories': 'sub_directories'
    }

    def __init__(self, parent_directory_id=None, directory_name=None, category_type=None, directory_id=None, paging=None, offset=None, limit=None, count=None, elements=None, sub_directories=None):
        """DirectoryTreeResp

        The model defined in huaweicloud sdk

        :param parent_directory_id: 
        :type parent_directory_id: str
        :param directory_name: 
        :type directory_name: str
        :param category_type: 
        :type category_type: str
        :param directory_id: 
        :type directory_id: str
        :param paging: 
        :type paging: bool
        :param offset: 
        :type offset: int
        :param limit: 
        :type limit: int
        :param count: 
        :type count: int
        :param elements: 
        :type elements: list[:class:`huaweicloudsdkdlf.v1.TreeNodeElement`]
        :param sub_directories: 
        :type sub_directories: list[:class:`huaweicloudsdkdlf.v1.DirectoryTreeResp`]
        """
        
        

        self._parent_directory_id = None
        self._directory_name = None
        self._category_type = None
        self._directory_id = None
        self._paging = None
        self._offset = None
        self._limit = None
        self._count = None
        self._elements = None
        self._sub_directories = None
        self.discriminator = None

        if parent_directory_id is not None:
            self.parent_directory_id = parent_directory_id
        if directory_name is not None:
            self.directory_name = directory_name
        if category_type is not None:
            self.category_type = category_type
        if directory_id is not None:
            self.directory_id = directory_id
        if paging is not None:
            self.paging = paging
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if count is not None:
            self.count = count
        if elements is not None:
            self.elements = elements
        if sub_directories is not None:
            self.sub_directories = sub_directories

    @property
    def parent_directory_id(self):
        """Gets the parent_directory_id of this DirectoryTreeResp.

        :return: The parent_directory_id of this DirectoryTreeResp.
        :rtype: str
        """
        return self._parent_directory_id

    @parent_directory_id.setter
    def parent_directory_id(self, parent_directory_id):
        """Sets the parent_directory_id of this DirectoryTreeResp.

        :param parent_directory_id: The parent_directory_id of this DirectoryTreeResp.
        :type parent_directory_id: str
        """
        self._parent_directory_id = parent_directory_id

    @property
    def directory_name(self):
        """Gets the directory_name of this DirectoryTreeResp.

        :return: The directory_name of this DirectoryTreeResp.
        :rtype: str
        """
        return self._directory_name

    @directory_name.setter
    def directory_name(self, directory_name):
        """Sets the directory_name of this DirectoryTreeResp.

        :param directory_name: The directory_name of this DirectoryTreeResp.
        :type directory_name: str
        """
        self._directory_name = directory_name

    @property
    def category_type(self):
        """Gets the category_type of this DirectoryTreeResp.

        :return: The category_type of this DirectoryTreeResp.
        :rtype: str
        """
        return self._category_type

    @category_type.setter
    def category_type(self, category_type):
        """Sets the category_type of this DirectoryTreeResp.

        :param category_type: The category_type of this DirectoryTreeResp.
        :type category_type: str
        """
        self._category_type = category_type

    @property
    def directory_id(self):
        """Gets the directory_id of this DirectoryTreeResp.

        :return: The directory_id of this DirectoryTreeResp.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this DirectoryTreeResp.

        :param directory_id: The directory_id of this DirectoryTreeResp.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def paging(self):
        """Gets the paging of this DirectoryTreeResp.

        :return: The paging of this DirectoryTreeResp.
        :rtype: bool
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this DirectoryTreeResp.

        :param paging: The paging of this DirectoryTreeResp.
        :type paging: bool
        """
        self._paging = paging

    @property
    def offset(self):
        """Gets the offset of this DirectoryTreeResp.

        :return: The offset of this DirectoryTreeResp.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this DirectoryTreeResp.

        :param offset: The offset of this DirectoryTreeResp.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this DirectoryTreeResp.

        :return: The limit of this DirectoryTreeResp.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this DirectoryTreeResp.

        :param limit: The limit of this DirectoryTreeResp.
        :type limit: int
        """
        self._limit = limit

    @property
    def count(self):
        """Gets the count of this DirectoryTreeResp.

        :return: The count of this DirectoryTreeResp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DirectoryTreeResp.

        :param count: The count of this DirectoryTreeResp.
        :type count: int
        """
        self._count = count

    @property
    def elements(self):
        """Gets the elements of this DirectoryTreeResp.

        :return: The elements of this DirectoryTreeResp.
        :rtype: list[:class:`huaweicloudsdkdlf.v1.TreeNodeElement`]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this DirectoryTreeResp.

        :param elements: The elements of this DirectoryTreeResp.
        :type elements: list[:class:`huaweicloudsdkdlf.v1.TreeNodeElement`]
        """
        self._elements = elements

    @property
    def sub_directories(self):
        """Gets the sub_directories of this DirectoryTreeResp.

        :return: The sub_directories of this DirectoryTreeResp.
        :rtype: list[:class:`huaweicloudsdkdlf.v1.DirectoryTreeResp`]
        """
        return self._sub_directories

    @sub_directories.setter
    def sub_directories(self, sub_directories):
        """Sets the sub_directories of this DirectoryTreeResp.

        :param sub_directories: The sub_directories of this DirectoryTreeResp.
        :type sub_directories: list[:class:`huaweicloudsdkdlf.v1.DirectoryTreeResp`]
        """
        self._sub_directories = sub_directories

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
        if not isinstance(other, DirectoryTreeResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
