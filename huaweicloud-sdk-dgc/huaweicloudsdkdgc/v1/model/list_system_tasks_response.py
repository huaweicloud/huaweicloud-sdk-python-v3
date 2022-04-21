# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSystemTasksResponse(SdkResponse):

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
        'start_time': 'str',
        'end_time': 'str',
        'last_update': 'str',
        'status': 'str',
        'message': 'str',
        'sub_tasks': 'list[SubTaskStatus]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'last_update': 'lastUpdate',
        'status': 'status',
        'message': 'message',
        'sub_tasks': 'subTasks'
    }

    def __init__(self, id=None, name=None, start_time=None, end_time=None, last_update=None, status=None, message=None, sub_tasks=None):
        """ListSystemTasksResponse

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param start_time: 
        :type start_time: str
        :param end_time: 
        :type end_time: str
        :param last_update: 
        :type last_update: str
        :param status: 
        :type status: str
        :param message: 
        :type message: str
        :param sub_tasks: 
        :type sub_tasks: list[:class:`huaweicloudsdkdgc.v1.SubTaskStatus`]
        """
        
        super(ListSystemTasksResponse, self).__init__()

        self._id = None
        self._name = None
        self._start_time = None
        self._end_time = None
        self._last_update = None
        self._status = None
        self._message = None
        self._sub_tasks = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if last_update is not None:
            self.last_update = last_update
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if sub_tasks is not None:
            self.sub_tasks = sub_tasks

    @property
    def id(self):
        """Gets the id of this ListSystemTasksResponse.


        :return: The id of this ListSystemTasksResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListSystemTasksResponse.


        :param id: The id of this ListSystemTasksResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListSystemTasksResponse.


        :return: The name of this ListSystemTasksResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListSystemTasksResponse.


        :param name: The name of this ListSystemTasksResponse.
        :type name: str
        """
        self._name = name

    @property
    def start_time(self):
        """Gets the start_time of this ListSystemTasksResponse.


        :return: The start_time of this ListSystemTasksResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListSystemTasksResponse.


        :param start_time: The start_time of this ListSystemTasksResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListSystemTasksResponse.


        :return: The end_time of this ListSystemTasksResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListSystemTasksResponse.


        :param end_time: The end_time of this ListSystemTasksResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def last_update(self):
        """Gets the last_update of this ListSystemTasksResponse.


        :return: The last_update of this ListSystemTasksResponse.
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this ListSystemTasksResponse.


        :param last_update: The last_update of this ListSystemTasksResponse.
        :type last_update: str
        """
        self._last_update = last_update

    @property
    def status(self):
        """Gets the status of this ListSystemTasksResponse.


        :return: The status of this ListSystemTasksResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSystemTasksResponse.


        :param status: The status of this ListSystemTasksResponse.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        """Gets the message of this ListSystemTasksResponse.


        :return: The message of this ListSystemTasksResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListSystemTasksResponse.


        :param message: The message of this ListSystemTasksResponse.
        :type message: str
        """
        self._message = message

    @property
    def sub_tasks(self):
        """Gets the sub_tasks of this ListSystemTasksResponse.


        :return: The sub_tasks of this ListSystemTasksResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.SubTaskStatus`]
        """
        return self._sub_tasks

    @sub_tasks.setter
    def sub_tasks(self, sub_tasks):
        """Sets the sub_tasks of this ListSystemTasksResponse.


        :param sub_tasks: The sub_tasks of this ListSystemTasksResponse.
        :type sub_tasks: list[:class:`huaweicloudsdkdgc.v1.SubTaskStatus`]
        """
        self._sub_tasks = sub_tasks

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
        if not isinstance(other, ListSystemTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
