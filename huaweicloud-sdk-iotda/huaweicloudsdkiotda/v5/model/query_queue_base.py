# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryQueueBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_id': 'str',
        'queue_name': 'str',
        'create_time': 'str',
        'last_modify_time': 'str'
    }

    attribute_map = {
        'queue_id': 'queue_id',
        'queue_name': 'queue_name',
        'create_time': 'create_time',
        'last_modify_time': 'last_modify_time'
    }

    def __init__(self, queue_id=None, queue_name=None, create_time=None, last_modify_time=None):
        """QueryQueueBase

        The model defined in huaweicloud sdk

        :param queue_id: 队列ID，用于唯一标识一个队列。
        :type queue_id: str
        :param queue_name: 队列名称，同一租户不允许重复。
        :type queue_name: str
        :param create_time: 在物联网平台创建队列的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type create_time: str
        :param last_modify_time: 在物联网平台最后修改队列的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type last_modify_time: str
        """
        
        

        self._queue_id = None
        self._queue_name = None
        self._create_time = None
        self._last_modify_time = None
        self.discriminator = None

        if queue_id is not None:
            self.queue_id = queue_id
        if queue_name is not None:
            self.queue_name = queue_name
        if create_time is not None:
            self.create_time = create_time
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time

    @property
    def queue_id(self):
        """Gets the queue_id of this QueryQueueBase.

        队列ID，用于唯一标识一个队列。

        :return: The queue_id of this QueryQueueBase.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this QueryQueueBase.

        队列ID，用于唯一标识一个队列。

        :param queue_id: The queue_id of this QueryQueueBase.
        :type queue_id: str
        """
        self._queue_id = queue_id

    @property
    def queue_name(self):
        """Gets the queue_name of this QueryQueueBase.

        队列名称，同一租户不允许重复。

        :return: The queue_name of this QueryQueueBase.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this QueryQueueBase.

        队列名称，同一租户不允许重复。

        :param queue_name: The queue_name of this QueryQueueBase.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def create_time(self):
        """Gets the create_time of this QueryQueueBase.

        在物联网平台创建队列的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_time of this QueryQueueBase.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryQueueBase.

        在物联网平台创建队列的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_time: The create_time of this QueryQueueBase.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modify_time(self):
        """Gets the last_modify_time of this QueryQueueBase.

        在物联网平台最后修改队列的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The last_modify_time of this QueryQueueBase.
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        """Sets the last_modify_time of this QueryQueueBase.

        在物联网平台最后修改队列的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param last_modify_time: The last_modify_time of this QueryQueueBase.
        :type last_modify_time: str
        """
        self._last_modify_time = last_modify_time

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
        if not isinstance(other, QueryQueueBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
