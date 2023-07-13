# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTaskRequest:

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
        'name': 'str',
        'data_source_type': 'str',
        'data_connection_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'directory_id': 'str',
        'bucket_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'name': 'name',
        'data_source_type': 'data_source_type',
        'data_connection_id': 'data_connection_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'directory_id': 'directory_id',
        'bucket_name': 'bucket_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, user_name=None, name=None, data_source_type=None, data_connection_id=None, start_time=None, end_time=None, directory_id=None, bucket_name=None, limit=None, offset=None):
        """QueryTaskRequest

        The model defined in huaweicloud sdk

        :param user_name: 创建人
        :type user_name: str
        :param name: 任务名
        :type name: str
        :param data_source_type: 数据源类型
        :type data_source_type: str
        :param data_connection_id: 数据连接id
        :type data_connection_id: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param directory_id: 目录id
        :type directory_id: str
        :param bucket_name: 桶名
        :type bucket_name: str
        :param limit: 分页参数limit，默认值：10
        :type limit: int
        :param offset: 分页参数offset，默认值：0
        :type offset: int
        """
        
        

        self._user_name = None
        self._name = None
        self._data_source_type = None
        self._data_connection_id = None
        self._start_time = None
        self._end_time = None
        self._directory_id = None
        self._bucket_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if name is not None:
            self.name = name
        if data_source_type is not None:
            self.data_source_type = data_source_type
        if data_connection_id is not None:
            self.data_connection_id = data_connection_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if directory_id is not None:
            self.directory_id = directory_id
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def user_name(self):
        """Gets the user_name of this QueryTaskRequest.

        创建人

        :return: The user_name of this QueryTaskRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this QueryTaskRequest.

        创建人

        :param user_name: The user_name of this QueryTaskRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def name(self):
        """Gets the name of this QueryTaskRequest.

        任务名

        :return: The name of this QueryTaskRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryTaskRequest.

        任务名

        :param name: The name of this QueryTaskRequest.
        :type name: str
        """
        self._name = name

    @property
    def data_source_type(self):
        """Gets the data_source_type of this QueryTaskRequest.

        数据源类型

        :return: The data_source_type of this QueryTaskRequest.
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """Sets the data_source_type of this QueryTaskRequest.

        数据源类型

        :param data_source_type: The data_source_type of this QueryTaskRequest.
        :type data_source_type: str
        """
        self._data_source_type = data_source_type

    @property
    def data_connection_id(self):
        """Gets the data_connection_id of this QueryTaskRequest.

        数据连接id

        :return: The data_connection_id of this QueryTaskRequest.
        :rtype: str
        """
        return self._data_connection_id

    @data_connection_id.setter
    def data_connection_id(self, data_connection_id):
        """Sets the data_connection_id of this QueryTaskRequest.

        数据连接id

        :param data_connection_id: The data_connection_id of this QueryTaskRequest.
        :type data_connection_id: str
        """
        self._data_connection_id = data_connection_id

    @property
    def start_time(self):
        """Gets the start_time of this QueryTaskRequest.

        开始时间

        :return: The start_time of this QueryTaskRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this QueryTaskRequest.

        开始时间

        :param start_time: The start_time of this QueryTaskRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this QueryTaskRequest.

        结束时间

        :return: The end_time of this QueryTaskRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryTaskRequest.

        结束时间

        :param end_time: The end_time of this QueryTaskRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def directory_id(self):
        """Gets the directory_id of this QueryTaskRequest.

        目录id

        :return: The directory_id of this QueryTaskRequest.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this QueryTaskRequest.

        目录id

        :param directory_id: The directory_id of this QueryTaskRequest.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def bucket_name(self):
        """Gets the bucket_name of this QueryTaskRequest.

        桶名

        :return: The bucket_name of this QueryTaskRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this QueryTaskRequest.

        桶名

        :param bucket_name: The bucket_name of this QueryTaskRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def limit(self):
        """Gets the limit of this QueryTaskRequest.

        分页参数limit，默认值：10

        :return: The limit of this QueryTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryTaskRequest.

        分页参数limit，默认值：10

        :param limit: The limit of this QueryTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this QueryTaskRequest.

        分页参数offset，默认值：0

        :return: The offset of this QueryTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryTaskRequest.

        分页参数offset，默认值：0

        :param offset: The offset of this QueryTaskRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, QueryTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
