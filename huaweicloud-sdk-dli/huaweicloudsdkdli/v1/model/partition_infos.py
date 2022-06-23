# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionInfos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'partition_name': 'str',
        'create_time': 'int',
        'last_access_time': 'int',
        'locations': 'list[str]',
        'last_ddl_time': 'int',
        'num_rows': 'int',
        'num_files': 'int',
        'total_size': 'int'
    }

    attribute_map = {
        'partition_name': 'partition_name',
        'create_time': 'create_time',
        'last_access_time': 'last_access_time',
        'locations': 'locations',
        'last_ddl_time': 'last_ddl_time',
        'num_rows': 'num_rows',
        'num_files': 'num_files',
        'total_size': 'total_size'
    }

    def __init__(self, partition_name=None, create_time=None, last_access_time=None, locations=None, last_ddl_time=None, num_rows=None, num_files=None, total_size=None):
        """PartitionInfos

        The model defined in huaweicloud sdk

        :param partition_name: 分区名
        :type partition_name: str
        :param create_time: 创建时间
        :type create_time: int
        :param last_access_time: 最后改动时间
        :type last_access_time: int
        :param locations: 路径，外表显示，内表不显示
        :type locations: list[str]
        :param last_ddl_time: 最后一个ddl语句执行时间，时间戳单位：秒
        :type last_ddl_time: int
        :param num_rows: 该分区数据总行数
        :type num_rows: int
        :param num_files: 分区文件数
        :type num_files: int
        :param total_size: 该分区总的数据大小（单位：字节）
        :type total_size: int
        """
        
        

        self._partition_name = None
        self._create_time = None
        self._last_access_time = None
        self._locations = None
        self._last_ddl_time = None
        self._num_rows = None
        self._num_files = None
        self._total_size = None
        self.discriminator = None

        self.partition_name = partition_name
        self.create_time = create_time
        self.last_access_time = last_access_time
        if locations is not None:
            self.locations = locations
        if last_ddl_time is not None:
            self.last_ddl_time = last_ddl_time
        if num_rows is not None:
            self.num_rows = num_rows
        if num_files is not None:
            self.num_files = num_files
        if total_size is not None:
            self.total_size = total_size

    @property
    def partition_name(self):
        """Gets the partition_name of this PartitionInfos.

        分区名

        :return: The partition_name of this PartitionInfos.
        :rtype: str
        """
        return self._partition_name

    @partition_name.setter
    def partition_name(self, partition_name):
        """Sets the partition_name of this PartitionInfos.

        分区名

        :param partition_name: The partition_name of this PartitionInfos.
        :type partition_name: str
        """
        self._partition_name = partition_name

    @property
    def create_time(self):
        """Gets the create_time of this PartitionInfos.

        创建时间

        :return: The create_time of this PartitionInfos.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PartitionInfos.

        创建时间

        :param create_time: The create_time of this PartitionInfos.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_access_time(self):
        """Gets the last_access_time of this PartitionInfos.

        最后改动时间

        :return: The last_access_time of this PartitionInfos.
        :rtype: int
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        """Sets the last_access_time of this PartitionInfos.

        最后改动时间

        :param last_access_time: The last_access_time of this PartitionInfos.
        :type last_access_time: int
        """
        self._last_access_time = last_access_time

    @property
    def locations(self):
        """Gets the locations of this PartitionInfos.

        路径，外表显示，内表不显示

        :return: The locations of this PartitionInfos.
        :rtype: list[str]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this PartitionInfos.

        路径，外表显示，内表不显示

        :param locations: The locations of this PartitionInfos.
        :type locations: list[str]
        """
        self._locations = locations

    @property
    def last_ddl_time(self):
        """Gets the last_ddl_time of this PartitionInfos.

        最后一个ddl语句执行时间，时间戳单位：秒

        :return: The last_ddl_time of this PartitionInfos.
        :rtype: int
        """
        return self._last_ddl_time

    @last_ddl_time.setter
    def last_ddl_time(self, last_ddl_time):
        """Sets the last_ddl_time of this PartitionInfos.

        最后一个ddl语句执行时间，时间戳单位：秒

        :param last_ddl_time: The last_ddl_time of this PartitionInfos.
        :type last_ddl_time: int
        """
        self._last_ddl_time = last_ddl_time

    @property
    def num_rows(self):
        """Gets the num_rows of this PartitionInfos.

        该分区数据总行数

        :return: The num_rows of this PartitionInfos.
        :rtype: int
        """
        return self._num_rows

    @num_rows.setter
    def num_rows(self, num_rows):
        """Sets the num_rows of this PartitionInfos.

        该分区数据总行数

        :param num_rows: The num_rows of this PartitionInfos.
        :type num_rows: int
        """
        self._num_rows = num_rows

    @property
    def num_files(self):
        """Gets the num_files of this PartitionInfos.

        分区文件数

        :return: The num_files of this PartitionInfos.
        :rtype: int
        """
        return self._num_files

    @num_files.setter
    def num_files(self, num_files):
        """Sets the num_files of this PartitionInfos.

        分区文件数

        :param num_files: The num_files of this PartitionInfos.
        :type num_files: int
        """
        self._num_files = num_files

    @property
    def total_size(self):
        """Gets the total_size of this PartitionInfos.

        该分区总的数据大小（单位：字节）

        :return: The total_size of this PartitionInfos.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this PartitionInfos.

        该分区总的数据大小（单位：字节）

        :param total_size: The total_size of this PartitionInfos.
        :type total_size: int
        """
        self._total_size = total_size

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
        if not isinstance(other, PartitionInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
