# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupDto:

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
        'type': 'str',
        'region': 'str',
        'paths': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'size': 'int',
        'description': 'str',
        'operator_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'region': 'region',
        'paths': 'paths',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'size': 'size',
        'description': 'description',
        'operator_name': 'operator_name'
    }

    def __init__(self, id=None, name=None, type=None, region=None, paths=None, start_time=None, end_time=None, size=None, description=None, operator_name=None):
        """BackupDto

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param name: 归档名称
        :type name: str
        :param type: 类型
        :type type: str
        :param region: 区域
        :type region: str
        :param paths: 归档数据路径集
        :type paths: list[str]
        :param start_time: 归档开始时间
        :type start_time: str
        :param end_time: 归档结束时间
        :type end_time: str
        :param size: 大小
        :type size: int
        :param description: 归档描述
        :type description: str
        :param operator_name: 归档人员姓名
        :type operator_name: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._region = None
        self._paths = None
        self._start_time = None
        self._end_time = None
        self._size = None
        self._description = None
        self._operator_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if region is not None:
            self.region = region
        if paths is not None:
            self.paths = paths
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if size is not None:
            self.size = size
        if description is not None:
            self.description = description
        if operator_name is not None:
            self.operator_name = operator_name

    @property
    def id(self):
        """Gets the id of this BackupDto.

        id

        :return: The id of this BackupDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupDto.

        id

        :param id: The id of this BackupDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BackupDto.

        归档名称

        :return: The name of this BackupDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackupDto.

        归档名称

        :param name: The name of this BackupDto.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this BackupDto.

        类型

        :return: The type of this BackupDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackupDto.

        类型

        :param type: The type of this BackupDto.
        :type type: str
        """
        self._type = type

    @property
    def region(self):
        """Gets the region of this BackupDto.

        区域

        :return: The region of this BackupDto.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this BackupDto.

        区域

        :param region: The region of this BackupDto.
        :type region: str
        """
        self._region = region

    @property
    def paths(self):
        """Gets the paths of this BackupDto.

        归档数据路径集

        :return: The paths of this BackupDto.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this BackupDto.

        归档数据路径集

        :param paths: The paths of this BackupDto.
        :type paths: list[str]
        """
        self._paths = paths

    @property
    def start_time(self):
        """Gets the start_time of this BackupDto.

        归档开始时间

        :return: The start_time of this BackupDto.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BackupDto.

        归档开始时间

        :param start_time: The start_time of this BackupDto.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this BackupDto.

        归档结束时间

        :return: The end_time of this BackupDto.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BackupDto.

        归档结束时间

        :param end_time: The end_time of this BackupDto.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def size(self):
        """Gets the size of this BackupDto.

        大小

        :return: The size of this BackupDto.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BackupDto.

        大小

        :param size: The size of this BackupDto.
        :type size: int
        """
        self._size = size

    @property
    def description(self):
        """Gets the description of this BackupDto.

        归档描述

        :return: The description of this BackupDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BackupDto.

        归档描述

        :param description: The description of this BackupDto.
        :type description: str
        """
        self._description = description

    @property
    def operator_name(self):
        """Gets the operator_name of this BackupDto.

        归档人员姓名

        :return: The operator_name of this BackupDto.
        :rtype: str
        """
        return self._operator_name

    @operator_name.setter
    def operator_name(self, operator_name):
        """Sets the operator_name of this BackupDto.

        归档人员姓名

        :param operator_name: The operator_name of this BackupDto.
        :type operator_name: str
        """
        self._operator_name = operator_name

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
        if not isinstance(other, BackupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
