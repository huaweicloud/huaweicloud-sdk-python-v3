# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchErrorInfoSource4ApiRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'task_id': 'int',
        'file_name': 'str',
        'db_name': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'task_id': 'task_id',
        'file_name': 'file_name',
        'db_name': 'db_name'
    }

    def __init__(self, connection_id=None, task_id=None, file_name=None, db_name=None):
        r"""SearchErrorInfoSource4ApiRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param task_id: 解析任务ID
        :type task_id: int
        :param file_name: 文件名称
        :type file_name: str
        :param db_name: 数据库名称
        :type db_name: str
        """
        
        

        self._connection_id = None
        self._task_id = None
        self._file_name = None
        self._db_name = None
        self.discriminator = None

        self.connection_id = connection_id
        self.task_id = task_id
        if file_name is not None:
            self.file_name = file_name
        if db_name is not None:
            self.db_name = db_name

    @property
    def connection_id(self):
        r"""Gets the connection_id of this SearchErrorInfoSource4ApiRequest.

        连接ID

        :return: The connection_id of this SearchErrorInfoSource4ApiRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this SearchErrorInfoSource4ApiRequest.

        连接ID

        :param connection_id: The connection_id of this SearchErrorInfoSource4ApiRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def task_id(self):
        r"""Gets the task_id of this SearchErrorInfoSource4ApiRequest.

        解析任务ID

        :return: The task_id of this SearchErrorInfoSource4ApiRequest.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SearchErrorInfoSource4ApiRequest.

        解析任务ID

        :param task_id: The task_id of this SearchErrorInfoSource4ApiRequest.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def file_name(self):
        r"""Gets the file_name of this SearchErrorInfoSource4ApiRequest.

        文件名称

        :return: The file_name of this SearchErrorInfoSource4ApiRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this SearchErrorInfoSource4ApiRequest.

        文件名称

        :param file_name: The file_name of this SearchErrorInfoSource4ApiRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def db_name(self):
        r"""Gets the db_name of this SearchErrorInfoSource4ApiRequest.

        数据库名称

        :return: The db_name of this SearchErrorInfoSource4ApiRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this SearchErrorInfoSource4ApiRequest.

        数据库名称

        :param db_name: The db_name of this SearchErrorInfoSource4ApiRequest.
        :type db_name: str
        """
        self._db_name = db_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchErrorInfoSource4ApiRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
