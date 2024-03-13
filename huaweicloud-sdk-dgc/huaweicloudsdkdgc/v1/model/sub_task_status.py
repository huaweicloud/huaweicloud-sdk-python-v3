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
        'last_update': 'int',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'last_update': 'lastUpdate',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, id=None, name=None, last_update=None, status=None, message=None):
        """SubTaskStatus

        The model defined in huaweicloud sdk

        :param id: 作业ID
        :type id: str
        :param name: 作业名称
        :type name: str
        :param last_update: 作业最后更新日期
        :type last_update: int
        :param status: 作业运行状态 RUNNING：运行中 SUCCESSFUL：运行成功 FAILED：运行失败
        :type status: str
        :param message: 作业消息
        :type message: str
        """
        
        

        self._id = None
        self._name = None
        self._last_update = None
        self._status = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if last_update is not None:
            self.last_update = last_update
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def id(self):
        """Gets the id of this SubTaskStatus.

        作业ID

        :return: The id of this SubTaskStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubTaskStatus.

        作业ID

        :param id: The id of this SubTaskStatus.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SubTaskStatus.

        作业名称

        :return: The name of this SubTaskStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubTaskStatus.

        作业名称

        :param name: The name of this SubTaskStatus.
        :type name: str
        """
        self._name = name

    @property
    def last_update(self):
        """Gets the last_update of this SubTaskStatus.

        作业最后更新日期

        :return: The last_update of this SubTaskStatus.
        :rtype: int
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this SubTaskStatus.

        作业最后更新日期

        :param last_update: The last_update of this SubTaskStatus.
        :type last_update: int
        """
        self._last_update = last_update

    @property
    def status(self):
        """Gets the status of this SubTaskStatus.

        作业运行状态 RUNNING：运行中 SUCCESSFUL：运行成功 FAILED：运行失败

        :return: The status of this SubTaskStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubTaskStatus.

        作业运行状态 RUNNING：运行中 SUCCESSFUL：运行成功 FAILED：运行失败

        :param status: The status of this SubTaskStatus.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        """Gets the message of this SubTaskStatus.

        作业消息

        :return: The message of this SubTaskStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SubTaskStatus.

        作业消息

        :param message: The message of this SubTaskStatus.
        :type message: str
        """
        self._message = message

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
