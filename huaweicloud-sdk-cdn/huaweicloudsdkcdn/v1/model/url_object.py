# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlObject:

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
        'url': 'str',
        'status': 'str',
        'create_time': 'int',
        'task_id': 'str',
        'task_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'status': 'status',
        'create_time': 'create_time',
        'task_id': 'task_id',
        'task_type': 'task_type'
    }

    def __init__(self, id=None, url=None, status=None, create_time=None, task_id=None, task_type=None):
        r"""UrlObject

        The model defined in huaweicloud sdk

        :param id: url的id
        :type id: str
        :param url: url的地址。
        :type url: str
        :param status: url的状态 processing 处理中，succeed 完成，failed 失败，waiting 等待，refreshing 刷新中，preheating 预热中。
        :type status: str
        :param create_time: url创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type create_time: int
        :param task_id: 任务id。
        :type task_id: str
        :param task_type: 任务的类型， 其值可以为REFRESH、PREHEATING、REFRESH_AFTER_PREHEATING
        :type task_type: str
        """
        
        

        self._id = None
        self._url = None
        self._status = None
        self._create_time = None
        self._task_id = None
        self._task_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if task_id is not None:
            self.task_id = task_id
        if task_type is not None:
            self.task_type = task_type

    @property
    def id(self):
        r"""Gets the id of this UrlObject.

        url的id

        :return: The id of this UrlObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UrlObject.

        url的id

        :param id: The id of this UrlObject.
        :type id: str
        """
        self._id = id

    @property
    def url(self):
        r"""Gets the url of this UrlObject.

        url的地址。

        :return: The url of this UrlObject.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this UrlObject.

        url的地址。

        :param url: The url of this UrlObject.
        :type url: str
        """
        self._url = url

    @property
    def status(self):
        r"""Gets the status of this UrlObject.

        url的状态 processing 处理中，succeed 完成，failed 失败，waiting 等待，refreshing 刷新中，preheating 预热中。

        :return: The status of this UrlObject.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UrlObject.

        url的状态 processing 处理中，succeed 完成，failed 失败，waiting 等待，refreshing 刷新中，preheating 预热中。

        :param status: The status of this UrlObject.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this UrlObject.

        url创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The create_time of this UrlObject.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UrlObject.

        url创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param create_time: The create_time of this UrlObject.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def task_id(self):
        r"""Gets the task_id of this UrlObject.

        任务id。

        :return: The task_id of this UrlObject.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this UrlObject.

        任务id。

        :param task_id: The task_id of this UrlObject.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_type(self):
        r"""Gets the task_type of this UrlObject.

        任务的类型， 其值可以为REFRESH、PREHEATING、REFRESH_AFTER_PREHEATING

        :return: The task_type of this UrlObject.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this UrlObject.

        任务的类型， 其值可以为REFRESH、PREHEATING、REFRESH_AFTER_PREHEATING

        :param task_type: The task_type of this UrlObject.
        :type task_type: str
        """
        self._task_type = task_type

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
        if not isinstance(other, UrlObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
