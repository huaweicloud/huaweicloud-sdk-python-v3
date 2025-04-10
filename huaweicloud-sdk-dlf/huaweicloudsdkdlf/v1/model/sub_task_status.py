# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTaskStatus:

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
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'last_update': 'lastUpdate',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, start_time=None, end_time=None, last_update=None, status=None):
        r"""SubTaskStatus

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
        """
        
        

        self._id = None
        self._name = None
        self._start_time = None
        self._end_time = None
        self._last_update = None
        self._status = None
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

    @property
    def id(self):
        r"""Gets the id of this SubTaskStatus.

        :return: The id of this SubTaskStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubTaskStatus.

        :param id: The id of this SubTaskStatus.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SubTaskStatus.

        :return: The name of this SubTaskStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubTaskStatus.

        :param name: The name of this SubTaskStatus.
        :type name: str
        """
        self._name = name

    @property
    def start_time(self):
        r"""Gets the start_time of this SubTaskStatus.

        :return: The start_time of this SubTaskStatus.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SubTaskStatus.

        :param start_time: The start_time of this SubTaskStatus.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SubTaskStatus.

        :return: The end_time of this SubTaskStatus.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SubTaskStatus.

        :param end_time: The end_time of this SubTaskStatus.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def last_update(self):
        r"""Gets the last_update of this SubTaskStatus.

        :return: The last_update of this SubTaskStatus.
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        r"""Sets the last_update of this SubTaskStatus.

        :param last_update: The last_update of this SubTaskStatus.
        :type last_update: str
        """
        self._last_update = last_update

    @property
    def status(self):
        r"""Gets the status of this SubTaskStatus.

        :return: The status of this SubTaskStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SubTaskStatus.

        :param status: The status of this SubTaskStatus.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, SubTaskStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
