# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsFolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'folder_name': 'str',
        'folder_guid': 'str',
        'folder_qualified_name': 'str',
        'object_count': 'int',
        'data_size': 'float'
    }

    attribute_map = {
        'folder_name': 'folder_name',
        'folder_guid': 'folder_guid',
        'folder_qualified_name': 'folder_qualified_name',
        'object_count': 'object_count',
        'data_size': 'data_size'
    }

    def __init__(self, folder_name=None, folder_guid=None, folder_qualified_name=None, object_count=None, data_size=None):
        """ObsFolder

        The model defined in huaweicloud sdk

        :param folder_name: 目录名称
        :type folder_name: str
        :param folder_guid: 目录的guid
        :type folder_guid: str
        :param folder_qualified_name: 目录的唯一标识名称
        :type folder_qualified_name: str
        :param object_count: 对象总数
        :type object_count: int
        :param data_size: 数据量
        :type data_size: float
        """
        
        

        self._folder_name = None
        self._folder_guid = None
        self._folder_qualified_name = None
        self._object_count = None
        self._data_size = None
        self.discriminator = None

        if folder_name is not None:
            self.folder_name = folder_name
        if folder_guid is not None:
            self.folder_guid = folder_guid
        if folder_qualified_name is not None:
            self.folder_qualified_name = folder_qualified_name
        if object_count is not None:
            self.object_count = object_count
        if data_size is not None:
            self.data_size = data_size

    @property
    def folder_name(self):
        """Gets the folder_name of this ObsFolder.

        目录名称

        :return: The folder_name of this ObsFolder.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this ObsFolder.

        目录名称

        :param folder_name: The folder_name of this ObsFolder.
        :type folder_name: str
        """
        self._folder_name = folder_name

    @property
    def folder_guid(self):
        """Gets the folder_guid of this ObsFolder.

        目录的guid

        :return: The folder_guid of this ObsFolder.
        :rtype: str
        """
        return self._folder_guid

    @folder_guid.setter
    def folder_guid(self, folder_guid):
        """Sets the folder_guid of this ObsFolder.

        目录的guid

        :param folder_guid: The folder_guid of this ObsFolder.
        :type folder_guid: str
        """
        self._folder_guid = folder_guid

    @property
    def folder_qualified_name(self):
        """Gets the folder_qualified_name of this ObsFolder.

        目录的唯一标识名称

        :return: The folder_qualified_name of this ObsFolder.
        :rtype: str
        """
        return self._folder_qualified_name

    @folder_qualified_name.setter
    def folder_qualified_name(self, folder_qualified_name):
        """Sets the folder_qualified_name of this ObsFolder.

        目录的唯一标识名称

        :param folder_qualified_name: The folder_qualified_name of this ObsFolder.
        :type folder_qualified_name: str
        """
        self._folder_qualified_name = folder_qualified_name

    @property
    def object_count(self):
        """Gets the object_count of this ObsFolder.

        对象总数

        :return: The object_count of this ObsFolder.
        :rtype: int
        """
        return self._object_count

    @object_count.setter
    def object_count(self, object_count):
        """Sets the object_count of this ObsFolder.

        对象总数

        :param object_count: The object_count of this ObsFolder.
        :type object_count: int
        """
        self._object_count = object_count

    @property
    def data_size(self):
        """Gets the data_size of this ObsFolder.

        数据量

        :return: The data_size of this ObsFolder.
        :rtype: float
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        """Sets the data_size of this ObsFolder.

        数据量

        :param data_size: The data_size of this ObsFolder.
        :type data_size: float
        """
        self._data_size = data_size

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
        if not isinstance(other, ObsFolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
