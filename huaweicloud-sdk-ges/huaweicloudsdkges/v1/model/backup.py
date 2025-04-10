# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Backup:

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
        'backup_method': 'backupMethod',
        'graph_id': 'graphId',
        'graph_name': 'graphName',
        'graph_status': 'graphStatus',
        'graph_size_type_index': 'graphSizeTypeIndex',
        'data_store_version': 'dataStoreVersion',
        'arch': 'arch',
        'status': 'status',
        'start_timestamp': 'startTimestamp',
        'start_time': 'startTime',
        'end_timestamp': 'endTimestamp',
        'end_time': 'endTime',
        'size': 'size',
        'duration': 'duration',
        'encrypted': 'encrypted'
    }

    def __init__(self, id=None, name=None, backup_method=None, graph_id=None, graph_name=None, graph_status=None, graph_size_type_index=None, data_store_version=None, arch=None, status=None, start_timestamp=None, start_time=None, end_timestamp=None, end_time=None, size=None, duration=None, encrypted=None):
        r"""Backup

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
        :param start_time: 备份时间。
        :type start_time: str
        :param end_timestamp: 备份结束时间戳。
        :type end_timestamp: int
        :param end_time: 备份时间。
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

        self.id = id
        self.name = name
        self.backup_method = backup_method
        self.graph_id = graph_id
        self.graph_name = graph_name
        self.graph_status = graph_status
        self.graph_size_type_index = graph_size_type_index
        self.data_store_version = data_store_version
        self.arch = arch
        self.status = status
        self.start_timestamp = start_timestamp
        self.start_time = start_time
        self.end_timestamp = end_timestamp
        self.end_time = end_time
        self.size = size
        self.duration = duration
        if encrypted is not None:
            self.encrypted = encrypted

    @property
    def id(self):
        r"""Gets the id of this Backup.

        备份ID。

        :return: The id of this Backup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Backup.

        备份ID。

        :param id: The id of this Backup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Backup.

        备份名称。

        :return: The name of this Backup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Backup.

        备份名称。

        :param name: The name of this Backup.
        :type name: str
        """
        self._name = name

    @property
    def backup_method(self):
        r"""Gets the backup_method of this Backup.

        备份方法，取值为auto或manual。

        :return: The backup_method of this Backup.
        :rtype: str
        """
        return self._backup_method

    @backup_method.setter
    def backup_method(self, backup_method):
        r"""Sets the backup_method of this Backup.

        备份方法，取值为auto或manual。

        :param backup_method: The backup_method of this Backup.
        :type backup_method: str
        """
        self._backup_method = backup_method

    @property
    def graph_id(self):
        r"""Gets the graph_id of this Backup.

        备份关联的图ID。

        :return: The graph_id of this Backup.
        :rtype: str
        """
        return self._graph_id

    @graph_id.setter
    def graph_id(self, graph_id):
        r"""Sets the graph_id of this Backup.

        备份关联的图ID。

        :param graph_id: The graph_id of this Backup.
        :type graph_id: str
        """
        self._graph_id = graph_id

    @property
    def graph_name(self):
        r"""Gets the graph_name of this Backup.

        备份关联的图Name。

        :return: The graph_name of this Backup.
        :rtype: str
        """
        return self._graph_name

    @graph_name.setter
    def graph_name(self, graph_name):
        r"""Sets the graph_name of this Backup.

        备份关联的图Name。

        :param graph_name: The graph_name of this Backup.
        :type graph_name: str
        """
        self._graph_name = graph_name

    @property
    def graph_status(self):
        r"""Gets the graph_status of this Backup.

        备份关联的图状态。

        :return: The graph_status of this Backup.
        :rtype: str
        """
        return self._graph_status

    @graph_status.setter
    def graph_status(self, graph_status):
        r"""Sets the graph_status of this Backup.

        备份关联的图状态。

        :param graph_status: The graph_status of this Backup.
        :type graph_status: str
        """
        self._graph_status = graph_status

    @property
    def graph_size_type_index(self):
        r"""Gets the graph_size_type_index of this Backup.

        备份关联的图规格。

        :return: The graph_size_type_index of this Backup.
        :rtype: str
        """
        return self._graph_size_type_index

    @graph_size_type_index.setter
    def graph_size_type_index(self, graph_size_type_index):
        r"""Sets the graph_size_type_index of this Backup.

        备份关联的图规格。

        :param graph_size_type_index: The graph_size_type_index of this Backup.
        :type graph_size_type_index: str
        """
        self._graph_size_type_index = graph_size_type_index

    @property
    def data_store_version(self):
        r"""Gets the data_store_version of this Backup.

        备份关联的图版本。

        :return: The data_store_version of this Backup.
        :rtype: str
        """
        return self._data_store_version

    @data_store_version.setter
    def data_store_version(self, data_store_version):
        r"""Sets the data_store_version of this Backup.

        备份关联的图版本。

        :param data_store_version: The data_store_version of this Backup.
        :type data_store_version: str
        """
        self._data_store_version = data_store_version

    @property
    def arch(self):
        r"""Gets the arch of this Backup.

        备份关联的图CPU架构。

        :return: The arch of this Backup.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this Backup.

        备份关联的图CPU架构。

        :param arch: The arch of this Backup.
        :type arch: str
        """
        self._arch = arch

    @property
    def status(self):
        r"""Gets the status of this Backup.

        备份状态。  - backing_up：备份中 - success：备份成功 - failed：备份失败

        :return: The status of this Backup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Backup.

        备份状态。  - backing_up：备份中 - success：备份成功 - failed：备份失败

        :param status: The status of this Backup.
        :type status: str
        """
        self._status = status

    @property
    def start_timestamp(self):
        r"""Gets the start_timestamp of this Backup.

        备份开始时间戳。

        :return: The start_timestamp of this Backup.
        :rtype: int
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        r"""Sets the start_timestamp of this Backup.

        备份开始时间戳。

        :param start_timestamp: The start_timestamp of this Backup.
        :type start_timestamp: int
        """
        self._start_timestamp = start_timestamp

    @property
    def start_time(self):
        r"""Gets the start_time of this Backup.

        备份时间。

        :return: The start_time of this Backup.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this Backup.

        备份时间。

        :param start_time: The start_time of this Backup.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_timestamp(self):
        r"""Gets the end_timestamp of this Backup.

        备份结束时间戳。

        :return: The end_timestamp of this Backup.
        :rtype: int
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        r"""Sets the end_timestamp of this Backup.

        备份结束时间戳。

        :param end_timestamp: The end_timestamp of this Backup.
        :type end_timestamp: int
        """
        self._end_timestamp = end_timestamp

    @property
    def end_time(self):
        r"""Gets the end_time of this Backup.

        备份时间。

        :return: The end_time of this Backup.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this Backup.

        备份时间。

        :param end_time: The end_time of this Backup.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def size(self):
        r"""Gets the size of this Backup.

        备份文件大小，单位为MB。

        :return: The size of this Backup.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Backup.

        备份文件大小，单位为MB。

        :param size: The size of this Backup.
        :type size: int
        """
        self._size = size

    @property
    def duration(self):
        r"""Gets the duration of this Backup.

        备份时间，单位为秒。

        :return: The duration of this Backup.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this Backup.

        备份时间，单位为秒。

        :param duration: The duration of this Backup.
        :type duration: int
        """
        self._duration = duration

    @property
    def encrypted(self):
        r"""Gets the encrypted of this Backup.

        是否加密。true表示加密，默认值为\"false\"，不加密。

        :return: The encrypted of this Backup.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        r"""Sets the encrypted of this Backup.

        是否加密。true表示加密，默认值为\"false\"，不加密。

        :param encrypted: The encrypted of this Backup.
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
        if not isinstance(other, Backup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
