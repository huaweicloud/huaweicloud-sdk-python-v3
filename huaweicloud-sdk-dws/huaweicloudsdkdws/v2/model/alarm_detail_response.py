# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmDetailResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'alarm_name': 'str',
        'alarm_level': 'str',
        'alarm_source': 'str',
        'alarm_message': 'str',
        'alarm_location': 'str',
        'resource_id': 'str',
        'resource_id_name': 'str',
        'alarm_generate_date': 'str',
        'alarm_status': 'str'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'alarm_name': 'alarm_name',
        'alarm_level': 'alarm_level',
        'alarm_source': 'alarm_source',
        'alarm_message': 'alarm_message',
        'alarm_location': 'alarm_location',
        'resource_id': 'resource_id',
        'resource_id_name': 'resource_id_name',
        'alarm_generate_date': 'alarm_generate_date',
        'alarm_status': 'alarm_status'
    }

    def __init__(self, alarm_id=None, alarm_name=None, alarm_level=None, alarm_source=None, alarm_message=None, alarm_location=None, resource_id=None, resource_id_name=None, alarm_generate_date=None, alarm_status=None):
        """AlarmDetailResponse

        The model defined in huaweicloud sdk

        :param alarm_id: 告警定义ID
        :type alarm_id: str
        :param alarm_name: 告警名称
        :type alarm_name: str
        :param alarm_level: 告警级别
        :type alarm_level: str
        :param alarm_source: 告警服务
        :type alarm_source: str
        :param alarm_message: 告警消息
        :type alarm_message: str
        :param alarm_location: 告警定位信息
        :type alarm_location: str
        :param resource_id: 告警源ID
        :type resource_id: str
        :param resource_id_name: 告警源名称
        :type resource_id_name: str
        :param alarm_generate_date: 告警日期
        :type alarm_generate_date: str
        :param alarm_status: 告警状态
        :type alarm_status: str
        """
        
        

        self._alarm_id = None
        self._alarm_name = None
        self._alarm_level = None
        self._alarm_source = None
        self._alarm_message = None
        self._alarm_location = None
        self._resource_id = None
        self._resource_id_name = None
        self._alarm_generate_date = None
        self._alarm_status = None
        self.discriminator = None

        if alarm_id is not None:
            self.alarm_id = alarm_id
        if alarm_name is not None:
            self.alarm_name = alarm_name
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if alarm_source is not None:
            self.alarm_source = alarm_source
        if alarm_message is not None:
            self.alarm_message = alarm_message
        if alarm_location is not None:
            self.alarm_location = alarm_location
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_id_name is not None:
            self.resource_id_name = resource_id_name
        if alarm_generate_date is not None:
            self.alarm_generate_date = alarm_generate_date
        if alarm_status is not None:
            self.alarm_status = alarm_status

    @property
    def alarm_id(self):
        """Gets the alarm_id of this AlarmDetailResponse.

        告警定义ID

        :return: The alarm_id of this AlarmDetailResponse.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this AlarmDetailResponse.

        告警定义ID

        :param alarm_id: The alarm_id of this AlarmDetailResponse.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_name(self):
        """Gets the alarm_name of this AlarmDetailResponse.

        告警名称

        :return: The alarm_name of this AlarmDetailResponse.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        """Sets the alarm_name of this AlarmDetailResponse.

        告警名称

        :param alarm_name: The alarm_name of this AlarmDetailResponse.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_level(self):
        """Gets the alarm_level of this AlarmDetailResponse.

        告警级别

        :return: The alarm_level of this AlarmDetailResponse.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this AlarmDetailResponse.

        告警级别

        :param alarm_level: The alarm_level of this AlarmDetailResponse.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def alarm_source(self):
        """Gets the alarm_source of this AlarmDetailResponse.

        告警服务

        :return: The alarm_source of this AlarmDetailResponse.
        :rtype: str
        """
        return self._alarm_source

    @alarm_source.setter
    def alarm_source(self, alarm_source):
        """Sets the alarm_source of this AlarmDetailResponse.

        告警服务

        :param alarm_source: The alarm_source of this AlarmDetailResponse.
        :type alarm_source: str
        """
        self._alarm_source = alarm_source

    @property
    def alarm_message(self):
        """Gets the alarm_message of this AlarmDetailResponse.

        告警消息

        :return: The alarm_message of this AlarmDetailResponse.
        :rtype: str
        """
        return self._alarm_message

    @alarm_message.setter
    def alarm_message(self, alarm_message):
        """Sets the alarm_message of this AlarmDetailResponse.

        告警消息

        :param alarm_message: The alarm_message of this AlarmDetailResponse.
        :type alarm_message: str
        """
        self._alarm_message = alarm_message

    @property
    def alarm_location(self):
        """Gets the alarm_location of this AlarmDetailResponse.

        告警定位信息

        :return: The alarm_location of this AlarmDetailResponse.
        :rtype: str
        """
        return self._alarm_location

    @alarm_location.setter
    def alarm_location(self, alarm_location):
        """Sets the alarm_location of this AlarmDetailResponse.

        告警定位信息

        :param alarm_location: The alarm_location of this AlarmDetailResponse.
        :type alarm_location: str
        """
        self._alarm_location = alarm_location

    @property
    def resource_id(self):
        """Gets the resource_id of this AlarmDetailResponse.

        告警源ID

        :return: The resource_id of this AlarmDetailResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this AlarmDetailResponse.

        告警源ID

        :param resource_id: The resource_id of this AlarmDetailResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_id_name(self):
        """Gets the resource_id_name of this AlarmDetailResponse.

        告警源名称

        :return: The resource_id_name of this AlarmDetailResponse.
        :rtype: str
        """
        return self._resource_id_name

    @resource_id_name.setter
    def resource_id_name(self, resource_id_name):
        """Sets the resource_id_name of this AlarmDetailResponse.

        告警源名称

        :param resource_id_name: The resource_id_name of this AlarmDetailResponse.
        :type resource_id_name: str
        """
        self._resource_id_name = resource_id_name

    @property
    def alarm_generate_date(self):
        """Gets the alarm_generate_date of this AlarmDetailResponse.

        告警日期

        :return: The alarm_generate_date of this AlarmDetailResponse.
        :rtype: str
        """
        return self._alarm_generate_date

    @alarm_generate_date.setter
    def alarm_generate_date(self, alarm_generate_date):
        """Sets the alarm_generate_date of this AlarmDetailResponse.

        告警日期

        :param alarm_generate_date: The alarm_generate_date of this AlarmDetailResponse.
        :type alarm_generate_date: str
        """
        self._alarm_generate_date = alarm_generate_date

    @property
    def alarm_status(self):
        """Gets the alarm_status of this AlarmDetailResponse.

        告警状态

        :return: The alarm_status of this AlarmDetailResponse.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        """Sets the alarm_status of this AlarmDetailResponse.

        告警状态

        :param alarm_status: The alarm_status of this AlarmDetailResponse.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

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
        if not isinstance(other, AlarmDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
