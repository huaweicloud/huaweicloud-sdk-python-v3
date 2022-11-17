# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Urls:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'url': 'str',
        'status': 'str',
        'type': 'str',
        'task_id': 'int',
        'modify_time': 'int',
        'create_time': 'int',
        'file_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'status': 'status',
        'type': 'type',
        'task_id': 'task_id',
        'modify_time': 'modify_time',
        'create_time': 'create_time',
        'file_type': 'file_type'
    }

    def __init__(self, id=None, url=None, status=None, type=None, task_id=None, modify_time=None, create_time=None, file_type=None):
        """Urls

        The model defined in huaweicloud sdk

        :param id: urlid
        :type id: int
        :param url: url具体值
        :type url: str
        :param status: url状态
        :type status: str
        :param type: 任务类型
        :type type: str
        :param task_id: 任务id
        :type task_id: int
        :param modify_time: 修改时间戳（毫秒）
        :type modify_time: int
        :param create_time: 创建时间戳（毫秒）
        :type create_time: int
        :param file_type: 文件类型，目录还是文件
        :type file_type: str
        """
        
        

        self._id = None
        self._url = None
        self._status = None
        self._type = None
        self._task_id = None
        self._modify_time = None
        self._create_time = None
        self._file_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if task_id is not None:
            self.task_id = task_id
        if modify_time is not None:
            self.modify_time = modify_time
        if create_time is not None:
            self.create_time = create_time
        if file_type is not None:
            self.file_type = file_type

    @property
    def id(self):
        """Gets the id of this Urls.

        urlid

        :return: The id of this Urls.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Urls.

        urlid

        :param id: The id of this Urls.
        :type id: int
        """
        self._id = id

    @property
    def url(self):
        """Gets the url of this Urls.

        url具体值

        :return: The url of this Urls.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Urls.

        url具体值

        :param url: The url of this Urls.
        :type url: str
        """
        self._url = url

    @property
    def status(self):
        """Gets the status of this Urls.

        url状态

        :return: The status of this Urls.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Urls.

        url状态

        :param status: The status of this Urls.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this Urls.

        任务类型

        :return: The type of this Urls.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Urls.

        任务类型

        :param type: The type of this Urls.
        :type type: str
        """
        self._type = type

    @property
    def task_id(self):
        """Gets the task_id of this Urls.

        任务id

        :return: The task_id of this Urls.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Urls.

        任务id

        :param task_id: The task_id of this Urls.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def modify_time(self):
        """Gets the modify_time of this Urls.

        修改时间戳（毫秒）

        :return: The modify_time of this Urls.
        :rtype: int
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        """Sets the modify_time of this Urls.

        修改时间戳（毫秒）

        :param modify_time: The modify_time of this Urls.
        :type modify_time: int
        """
        self._modify_time = modify_time

    @property
    def create_time(self):
        """Gets the create_time of this Urls.

        创建时间戳（毫秒）

        :return: The create_time of this Urls.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Urls.

        创建时间戳（毫秒）

        :param create_time: The create_time of this Urls.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def file_type(self):
        """Gets the file_type of this Urls.

        文件类型，目录还是文件

        :return: The file_type of this Urls.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this Urls.

        文件类型，目录还是文件

        :param file_type: The file_type of this Urls.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, Urls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
