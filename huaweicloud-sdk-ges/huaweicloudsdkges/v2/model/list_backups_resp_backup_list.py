# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupsRespBackupList:

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
        'backup_method': 'str',
        'graph_id': 'str',
        'graph_name': 'str',
        'graph_status': 'str',
        'graph_size_type_index': 'str',
        'data_store_version': 'str',
        'arch': 'str',
        'status': 'str',
        'start_timestamp': 'int',
        'start_time': 'str',
        'end_timestamp': 'int',
        'end_time': 'str',
        'size': 'int',
        'duration': 'int',
        'encrypted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'backup_method': 'backup_method',
        'graph_id': 'graph_id',
        'graph_name': 'graph_name',
        'graph_status': 'graph_status',
        'graph_size_type_index': 'graph_size_type_index',
        'data_store_version': 'data_store_version',
        'arch': 'arch',
        'status': 'status',
        'start_timestamp': 'start_timestamp',
        'start_time': 'start_time',
        'end_timestamp': 'end_timestamp',
        'end_time': 'end_time',
        'size': 'size',
        'duration': 'duration',
        'encrypted': 'encrypted'
    }

    def __init__(self, id=None, name=None, backup_method=None, graph_id=None, graph_name=None, graph_status=None, graph_size_type_index=None, data_store_version=None, arch=None, status=None, start_timestamp=None, start_time=None, end_timestamp=None, end_time=None, size=None, duration=None, encrypted=None):
        """ListBackupsRespBackupList

        The model defined in huaweicloud sdk

        :param id: 备份ID。
        :type id: str
        :param name: 备份名称。
        :type name: str
        :param backup_method: 备份方法，取值为auto或manual。
        :type backup_method: str
        :param graph_id: 备份关联的图ID。
        :type graph_id: str
        :param graph_name: 备份关联的图Name。
        :type graph_name: str
        :param graph_status: 备份关联的图状态。
        :type graph_status: str
        :param graph_size_type_index: 备份关联的图规格。
        :type graph_size_type_index: str
        :param data_store_version: 备份关联的图版本。
        :type data_store_version: str
        :param arch: 备份关联的图CPU架构。
        :type arch: str
        :param status: 备份状态。  - backing_up：备份中 - success：备份成功 - failed：备份失败
        :type status: str
        :param start_timestamp: 备份开始时间戳。
        :type start_timestamp: int
        :param start_time: 备份开始时间。
        :type start_time: str
        :param end_timestamp: 备份结束时间戳。
        :type end_timestamp: int
        :param end_time: 备份结束时间。
        :type end_time: str
        :param size: 备份文件大小，单位为MB。
        :type size: int
        :param duration: 备份时间，单位为秒。
        :type duration: int
        :param encrypted: 是否加密。true表示加密，默认值为\&quot;false\&quot;，不加密。
        :type encrypted: bool
        """
        
        

        self._id = None
        self._name = None
        self._backup_method = None
        self._graph_id = None
        self._graph_name = None
        self._graph_status = None
        self._graph_size_type_index = None
        self._data_store_version = None
        self._arch = None
        self._status = None
        self._start_timestamp = None
        self._start_time = None
        self._end_timestamp = None
        self._end_time = None
        self._size = None
        self._duration = None
        self._encrypted = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if backup_method is not None:
            self.backup_method = backup_method
        if graph_id is not None:
            self.graph_id = graph_id
        if graph_name is not None:
            self.graph_name = graph_name
        if graph_status is not None:
            self.graph_status = graph_status
        if graph_size_type_index is not None:
            self.graph_size_type_index = graph_size_type_index
        if data_store_version is not None:
            self.data_store_version = data_store_version
        if arch is not None:
            self.arch = arch
        if status is not None:
            self.status = status
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if start_time is not None:
            self.start_time = start_time
        if end_timestamp is not None:
            self.end_timestamp = end_timestamp
        if end_time is not None:
            self.end_time = end_time
        if size is not None:
            self.size = size
        if duration is not None:
            self.duration = duration
        if encrypted is not None:
            self.encrypted = encrypted

    @property
    def id(self):
        """Gets the id of this ListBackupsRespBackupList.

        备份ID。

        :return: The id of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListBackupsRespBackupList.

        备份ID。

        :param id: The id of this ListBackupsRespBackupList.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListBackupsRespBackupList.

        备份名称。

        :return: The name of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListBackupsRespBackupList.

        备份名称。

        :param name: The name of this ListBackupsRespBackupList.
        :type name: str
        """
        self._name = name

    @property
    def backup_method(self):
        """Gets the backup_method of this ListBackupsRespBackupList.

        备份方法，取值为auto或manual。

        :return: The backup_method of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._backup_method

    @backup_method.setter
    def backup_method(self, backup_method):
        """Sets the backup_method of this ListBackupsRespBackupList.

        备份方法，取值为auto或manual。

        :param backup_method: The backup_method of this ListBackupsRespBackupList.
        :type backup_method: str
        """
        self._backup_method = backup_method

    @property
    def graph_id(self):
        """Gets the graph_id of this ListBackupsRespBackupList.

        备份关联的图ID。

        :return: The graph_id of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._graph_id

    @graph_id.setter
    def graph_id(self, graph_id):
        """Sets the graph_id of this ListBackupsRespBackupList.

        备份关联的图ID。

        :param graph_id: The graph_id of this ListBackupsRespBackupList.
        :type graph_id: str
        """
        self._graph_id = graph_id

    @property
    def graph_name(self):
        """Gets the graph_name of this ListBackupsRespBackupList.

        备份关联的图Name。

        :return: The graph_name of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._graph_name

    @graph_name.setter
    def graph_name(self, graph_name):
        """Sets the graph_name of this ListBackupsRespBackupList.

        备份关联的图Name。

        :param graph_name: The graph_name of this ListBackupsRespBackupList.
        :type graph_name: str
        """
        self._graph_name = graph_name

    @property
    def graph_status(self):
        """Gets the graph_status of this ListBackupsRespBackupList.

        备份关联的图状态。

        :return: The graph_status of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._graph_status

    @graph_status.setter
    def graph_status(self, graph_status):
        """Sets the graph_status of this ListBackupsRespBackupList.

        备份关联的图状态。

        :param graph_status: The graph_status of this ListBackupsRespBackupList.
        :type graph_status: str
        """
        self._graph_status = graph_status

    @property
    def graph_size_type_index(self):
        """Gets the graph_size_type_index of this ListBackupsRespBackupList.

        备份关联的图规格。

        :return: The graph_size_type_index of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._graph_size_type_index

    @graph_size_type_index.setter
    def graph_size_type_index(self, graph_size_type_index):
        """Sets the graph_size_type_index of this ListBackupsRespBackupList.

        备份关联的图规格。

        :param graph_size_type_index: The graph_size_type_index of this ListBackupsRespBackupList.
        :type graph_size_type_index: str
        """
        self._graph_size_type_index = graph_size_type_index

    @property
    def data_store_version(self):
        """Gets the data_store_version of this ListBackupsRespBackupList.

        备份关联的图版本。

        :return: The data_store_version of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._data_store_version

    @data_store_version.setter
    def data_store_version(self, data_store_version):
        """Sets the data_store_version of this ListBackupsRespBackupList.

        备份关联的图版本。

        :param data_store_version: The data_store_version of this ListBackupsRespBackupList.
        :type data_store_version: str
        """
        self._data_store_version = data_store_version

    @property
    def arch(self):
        """Gets the arch of this ListBackupsRespBackupList.

        备份关联的图CPU架构。

        :return: The arch of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ListBackupsRespBackupList.

        备份关联的图CPU架构。

        :param arch: The arch of this ListBackupsRespBackupList.
        :type arch: str
        """
        self._arch = arch

    @property
    def status(self):
        """Gets the status of this ListBackupsRespBackupList.

        备份状态。  - backing_up：备份中 - success：备份成功 - failed：备份失败

        :return: The status of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListBackupsRespBackupList.

        备份状态。  - backing_up：备份中 - success：备份成功 - failed：备份失败

        :param status: The status of this ListBackupsRespBackupList.
        :type status: str
        """
        self._status = status

    @property
    def start_timestamp(self):
        """Gets the start_timestamp of this ListBackupsRespBackupList.

        备份开始时间戳。

        :return: The start_timestamp of this ListBackupsRespBackupList.
        :rtype: int
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """Sets the start_timestamp of this ListBackupsRespBackupList.

        备份开始时间戳。

        :param start_timestamp: The start_timestamp of this ListBackupsRespBackupList.
        :type start_timestamp: int
        """
        self._start_timestamp = start_timestamp

    @property
    def start_time(self):
        """Gets the start_time of this ListBackupsRespBackupList.

        备份开始时间。

        :return: The start_time of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListBackupsRespBackupList.

        备份开始时间。

        :param start_time: The start_time of this ListBackupsRespBackupList.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_timestamp(self):
        """Gets the end_timestamp of this ListBackupsRespBackupList.

        备份结束时间戳。

        :return: The end_timestamp of this ListBackupsRespBackupList.
        :rtype: int
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """Sets the end_timestamp of this ListBackupsRespBackupList.

        备份结束时间戳。

        :param end_timestamp: The end_timestamp of this ListBackupsRespBackupList.
        :type end_timestamp: int
        """
        self._end_timestamp = end_timestamp

    @property
    def end_time(self):
        """Gets the end_time of this ListBackupsRespBackupList.

        备份结束时间。

        :return: The end_time of this ListBackupsRespBackupList.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListBackupsRespBackupList.

        备份结束时间。

        :param end_time: The end_time of this ListBackupsRespBackupList.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def size(self):
        """Gets the size of this ListBackupsRespBackupList.

        备份文件大小，单位为MB。

        :return: The size of this ListBackupsRespBackupList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListBackupsRespBackupList.

        备份文件大小，单位为MB。

        :param size: The size of this ListBackupsRespBackupList.
        :type size: int
        """
        self._size = size

    @property
    def duration(self):
        """Gets the duration of this ListBackupsRespBackupList.

        备份时间，单位为秒。

        :return: The duration of this ListBackupsRespBackupList.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ListBackupsRespBackupList.

        备份时间，单位为秒。

        :param duration: The duration of this ListBackupsRespBackupList.
        :type duration: int
        """
        self._duration = duration

    @property
    def encrypted(self):
        """Gets the encrypted of this ListBackupsRespBackupList.

        是否加密。true表示加密，默认值为\"false\"，不加密。

        :return: The encrypted of this ListBackupsRespBackupList.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this ListBackupsRespBackupList.

        是否加密。true表示加密，默认值为\"false\"，不加密。

        :param encrypted: The encrypted of this ListBackupsRespBackupList.
        :type encrypted: bool
        """
        self._encrypted = encrypted

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
        if not isinstance(other, ListBackupsRespBackupList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
