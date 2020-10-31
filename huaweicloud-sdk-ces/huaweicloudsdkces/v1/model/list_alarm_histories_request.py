# coding: utf-8

import pprint
import re

import six





class ListAlarmHistoriesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'alarm_id': 'str',
        'alarm_name': 'str',
        'alarm_status': 'str',
        'alarm_level': 'str',
        'namespace': 'str',
        '_from': 'str',
        'to': 'str',
        'start': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'alarm_id': 'alarm_id',
        'alarm_name': 'alarm_name',
        'alarm_status': 'alarm_status',
        'alarm_level': 'alarm_level',
        'namespace': 'namespace',
        '_from': 'from',
        'to': 'to',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, group_id=None, alarm_id=None, alarm_name=None, alarm_status=None, alarm_level=None, namespace=None, _from=None, to=None, start=None, limit=None):
        """ListAlarmHistoriesRequest - a model defined in huaweicloud sdk"""
        
        

        self._group_id = None
        self._alarm_id = None
        self._alarm_name = None
        self._alarm_status = None
        self._alarm_level = None
        self._namespace = None
        self.__from = None
        self._to = None
        self._start = None
        self._limit = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if alarm_name is not None:
            self.alarm_name = alarm_name
        if alarm_status is not None:
            self.alarm_status = alarm_status
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if namespace is not None:
            self.namespace = namespace
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def group_id(self):
        """Gets the group_id of this ListAlarmHistoriesRequest.


        :return: The group_id of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListAlarmHistoriesRequest.


        :param group_id: The group_id of this ListAlarmHistoriesRequest.
        :type: str
        """
        self._group_id = group_id

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ListAlarmHistoriesRequest.


        :return: The alarm_id of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ListAlarmHistoriesRequest.


        :param alarm_id: The alarm_id of this ListAlarmHistoriesRequest.
        :type: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_name(self):
        """Gets the alarm_name of this ListAlarmHistoriesRequest.


        :return: The alarm_name of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        """Sets the alarm_name of this ListAlarmHistoriesRequest.


        :param alarm_name: The alarm_name of this ListAlarmHistoriesRequest.
        :type: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_status(self):
        """Gets the alarm_status of this ListAlarmHistoriesRequest.


        :return: The alarm_status of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        """Sets the alarm_status of this ListAlarmHistoriesRequest.


        :param alarm_status: The alarm_status of this ListAlarmHistoriesRequest.
        :type: str
        """
        self._alarm_status = alarm_status

    @property
    def alarm_level(self):
        """Gets the alarm_level of this ListAlarmHistoriesRequest.


        :return: The alarm_level of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this ListAlarmHistoriesRequest.


        :param alarm_level: The alarm_level of this ListAlarmHistoriesRequest.
        :type: str
        """
        self._alarm_level = alarm_level

    @property
    def namespace(self):
        """Gets the namespace of this ListAlarmHistoriesRequest.


        :return: The namespace of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListAlarmHistoriesRequest.


        :param namespace: The namespace of this ListAlarmHistoriesRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def _from(self):
        """Gets the _from of this ListAlarmHistoriesRequest.


        :return: The _from of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListAlarmHistoriesRequest.


        :param _from: The _from of this ListAlarmHistoriesRequest.
        :type: str
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListAlarmHistoriesRequest.


        :return: The to of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListAlarmHistoriesRequest.


        :param to: The to of this ListAlarmHistoriesRequest.
        :type: str
        """
        self._to = to

    @property
    def start(self):
        """Gets the start of this ListAlarmHistoriesRequest.


        :return: The start of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListAlarmHistoriesRequest.


        :param start: The start of this ListAlarmHistoriesRequest.
        :type: str
        """
        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ListAlarmHistoriesRequest.


        :return: The limit of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlarmHistoriesRequest.


        :param limit: The limit of this ListAlarmHistoriesRequest.
        :type: str
        """
        self._limit = limit

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAlarmHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
