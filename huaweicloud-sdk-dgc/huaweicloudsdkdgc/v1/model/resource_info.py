# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'location': 'str',
        'depend_files': 'list[str]',
        'desc': 'str',
        'directory': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'location': 'location',
        'depend_files': 'dependFiles',
        'desc': 'desc',
        'directory': 'directory'
    }

    def __init__(self, name=None, type=None, location=None, depend_files=None, desc=None, directory=None):
        """ResourceInfo

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param type: 
        :type type: str
        :param location: 资源文件所在OBS路径
        :type location: str
        :param depend_files: 
        :type depend_files: list[str]
        :param desc: 
        :type desc: str
        :param directory: 资源所在目录
        :type directory: str
        """
        
        

        self._name = None
        self._type = None
        self._location = None
        self._depend_files = None
        self._desc = None
        self._directory = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if location is not None:
            self.location = location
        if depend_files is not None:
            self.depend_files = depend_files
        if desc is not None:
            self.desc = desc
        if directory is not None:
            self.directory = directory

    @property
    def name(self):
        """Gets the name of this ResourceInfo.

        :return: The name of this ResourceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceInfo.

        :param name: The name of this ResourceInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ResourceInfo.

        :return: The type of this ResourceInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceInfo.

        :param type: The type of this ResourceInfo.
        :type type: str
        """
        self._type = type

    @property
    def location(self):
        """Gets the location of this ResourceInfo.

        资源文件所在OBS路径

        :return: The location of this ResourceInfo.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ResourceInfo.

        资源文件所在OBS路径

        :param location: The location of this ResourceInfo.
        :type location: str
        """
        self._location = location

    @property
    def depend_files(self):
        """Gets the depend_files of this ResourceInfo.

        :return: The depend_files of this ResourceInfo.
        :rtype: list[str]
        """
        return self._depend_files

    @depend_files.setter
    def depend_files(self, depend_files):
        """Sets the depend_files of this ResourceInfo.

        :param depend_files: The depend_files of this ResourceInfo.
        :type depend_files: list[str]
        """
        self._depend_files = depend_files

    @property
    def desc(self):
        """Gets the desc of this ResourceInfo.

        :return: The desc of this ResourceInfo.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ResourceInfo.

        :param desc: The desc of this ResourceInfo.
        :type desc: str
        """
        self._desc = desc

    @property
    def directory(self):
        """Gets the directory of this ResourceInfo.

        资源所在目录

        :return: The directory of this ResourceInfo.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this ResourceInfo.

        资源所在目录

        :param directory: The directory of this ResourceInfo.
        :type directory: str
        """
        self._directory = directory

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
        if not isinstance(other, ResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
