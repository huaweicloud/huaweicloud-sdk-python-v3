# coding: utf-8

import pprint
import re

import six





class Material:


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
        'last_updated_by': 'str',
        'update_time': 'int',
        'material_name': 'str',
        'material_resolution': 'str',
        'material_size_str': 'str',
        'file_path': 'str'
    }

    attribute_map = {
        'id': 'id',
        'last_updated_by': 'lastUpdatedBy',
        'update_time': 'updateTime',
        'material_name': 'materialName',
        'material_resolution': 'materialResolution',
        'material_size_str': 'materialSizeStr',
        'file_path': 'filePath'
    }

    def __init__(self, id=None, last_updated_by=None, update_time=None, material_name=None, material_resolution=None, material_size_str=None, file_path=None):
        """Material - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._last_updated_by = None
        self._update_time = None
        self._material_name = None
        self._material_resolution = None
        self._material_size_str = None
        self._file_path = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if update_time is not None:
            self.update_time = update_time
        if material_name is not None:
            self.material_name = material_name
        if material_resolution is not None:
            self.material_resolution = material_resolution
        if material_size_str is not None:
            self.material_size_str = material_size_str
        if file_path is not None:
            self.file_path = file_path

    @property
    def id(self):
        """Gets the id of this Material.

        素材ID

        :return: The id of this Material.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Material.

        素材ID

        :param id: The id of this Material.
        :type: str
        """
        self._id = id

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this Material.

        更新者

        :return: The last_updated_by of this Material.
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this Material.

        更新者

        :param last_updated_by: The last_updated_by of this Material.
        :type: str
        """
        self._last_updated_by = last_updated_by

    @property
    def update_time(self):
        """Gets the update_time of this Material.

        更新时间

        :return: The update_time of this Material.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Material.

        更新时间

        :param update_time: The update_time of this Material.
        :type: int
        """
        self._update_time = update_time

    @property
    def material_name(self):
        """Gets the material_name of this Material.

        素材名称

        :return: The material_name of this Material.
        :rtype: str
        """
        return self._material_name

    @material_name.setter
    def material_name(self, material_name):
        """Sets the material_name of this Material.

        素材名称

        :param material_name: The material_name of this Material.
        :type: str
        """
        self._material_name = material_name

    @property
    def material_resolution(self):
        """Gets the material_resolution of this Material.

        素材分辨率

        :return: The material_resolution of this Material.
        :rtype: str
        """
        return self._material_resolution

    @material_resolution.setter
    def material_resolution(self, material_resolution):
        """Sets the material_resolution of this Material.

        素材分辨率

        :param material_resolution: The material_resolution of this Material.
        :type: str
        """
        self._material_resolution = material_resolution

    @property
    def material_size_str(self):
        """Gets the material_size_str of this Material.

        素材大小（含单位）

        :return: The material_size_str of this Material.
        :rtype: str
        """
        return self._material_size_str

    @material_size_str.setter
    def material_size_str(self, material_size_str):
        """Sets the material_size_str of this Material.

        素材大小（含单位）

        :param material_size_str: The material_size_str of this Material.
        :type: str
        """
        self._material_size_str = material_size_str

    @property
    def file_path(self):
        """Gets the file_path of this Material.

        素材云盘存储文件下载地址

        :return: The file_path of this Material.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this Material.

        素材云盘存储文件下载地址

        :param file_path: The file_path of this Material.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Material):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
