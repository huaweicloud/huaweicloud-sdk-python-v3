# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJob:

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
        'action': 'str',
        'status': 'str',
        'error_task': 'str',
        'error_code': 'str',
        'error_message': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'action': 'action',
        'status': 'status',
        'error_task': 'error_task',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, action=None, status=None, error_task=None, error_code=None, error_message=None, start_time=None, end_time=None):
        r"""ShowJob

        The model defined in huaweicloud sdk

        :param id: Job的ID
        :type id: str
        :param action: 处理规则
        :type action: str
        :param status: 状态
        :type status: str
        :param error_task: error_task
        :type error_task: str
        :param error_code: error_code
        :type error_code: str
        :param error_message: error_message
        :type error_message: str
        :param start_time: 起始时间
        :type start_time: datetime
        :param end_time: 结束时间
        :type end_time: datetime
        """
        
        

        self._id = None
        self._action = None
        self._status = None
        self._error_task = None
        self._error_code = None
        self._error_message = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if action is not None:
            self.action = action
        if status is not None:
            self.status = status
        if error_task is not None:
            self.error_task = error_task
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        r"""Gets the id of this ShowJob.

        Job的ID

        :return: The id of this ShowJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowJob.

        Job的ID

        :param id: The id of this ShowJob.
        :type id: str
        """
        self._id = id

    @property
    def action(self):
        r"""Gets the action of this ShowJob.

        处理规则

        :return: The action of this ShowJob.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowJob.

        处理规则

        :param action: The action of this ShowJob.
        :type action: str
        """
        self._action = action

    @property
    def status(self):
        r"""Gets the status of this ShowJob.

        状态

        :return: The status of this ShowJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowJob.

        状态

        :param status: The status of this ShowJob.
        :type status: str
        """
        self._status = status

    @property
    def error_task(self):
        r"""Gets the error_task of this ShowJob.

        error_task

        :return: The error_task of this ShowJob.
        :rtype: str
        """
        return self._error_task

    @error_task.setter
    def error_task(self, error_task):
        r"""Sets the error_task of this ShowJob.

        error_task

        :param error_task: The error_task of this ShowJob.
        :type error_task: str
        """
        self._error_task = error_task

    @property
    def error_code(self):
        r"""Gets the error_code of this ShowJob.

        error_code

        :return: The error_code of this ShowJob.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ShowJob.

        error_code

        :param error_code: The error_code of this ShowJob.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this ShowJob.

        error_message

        :return: The error_message of this ShowJob.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ShowJob.

        error_message

        :param error_message: The error_message of this ShowJob.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowJob.

        起始时间

        :return: The start_time of this ShowJob.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowJob.

        起始时间

        :param start_time: The start_time of this ShowJob.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowJob.

        结束时间

        :return: The end_time of this ShowJob.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowJob.

        结束时间

        :param end_time: The end_time of this ShowJob.
        :type end_time: datetime
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
