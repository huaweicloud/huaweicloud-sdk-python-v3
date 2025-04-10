# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportCustomEventRequestBody:

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
        'time': 'int',
        'name_space': 'str',
        'region_id': 'str',
        'application_id': 'str',
        'resource_name': 'str',
        'resource_id': 'str',
        'alarm_desc': 'str',
        'url': 'str',
        'alarm_status': 'str',
        'alarm_source': 'str',
        'additional': 'object'
    }

    attribute_map = {
        'alarm_id': 'alarmId',
        'alarm_name': 'alarmName',
        'alarm_level': 'alarmLevel',
        'time': 'time',
        'name_space': 'nameSpace',
        'region_id': 'regionId',
        'application_id': 'applicationId',
        'resource_name': 'resourceName',
        'resource_id': 'resourceId',
        'alarm_desc': 'alarmDesc',
        'url': 'URL',
        'alarm_status': 'alarmStatus',
        'alarm_source': 'alarmSource',
        'additional': 'additional'
    }

    def __init__(self, alarm_id=None, alarm_name=None, alarm_level=None, time=None, name_space=None, region_id=None, application_id=None, resource_name=None, resource_id=None, alarm_desc=None, url=None, alarm_status=None, alarm_source=None, additional=None):
        r"""ReportCustomEventRequestBody

        The model defined in huaweicloud sdk

        :param alarm_id: 告警id
        :type alarm_id: str
        :param alarm_name: 告警名称
        :type alarm_name: str
        :param alarm_level: 告警级别。取值为Critical（紧急）, Major（重要）, Minor（次要）, Info（提示）
        :type alarm_level: str
        :param time: 告警发生时间
        :type time: int
        :param name_space: 告警发生时间
        :type name_space: str
        :param region_id: 告警发生区域
        :type region_id: str
        :param application_id: 应用id
        :type application_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param alarm_desc: 告警描述
        :type alarm_desc: str
        :param url: 原始告警URL
        :type url: str
        :param alarm_status: 告警状态。一般取值为alarm（告警中）和ok（已恢复）
        :type alarm_status: str
        :param alarm_source: 告警源
        :type alarm_source: str
        :param additional: 告警附加信息
        :type additional: object
        """
        
        

        self._alarm_id = None
        self._alarm_name = None
        self._alarm_level = None
        self._time = None
        self._name_space = None
        self._region_id = None
        self._application_id = None
        self._resource_name = None
        self._resource_id = None
        self._alarm_desc = None
        self._url = None
        self._alarm_status = None
        self._alarm_source = None
        self._additional = None
        self.discriminator = None

        self.alarm_id = alarm_id
        self.alarm_name = alarm_name
        self.alarm_level = alarm_level
        self.time = time
        self.name_space = name_space
        if region_id is not None:
            self.region_id = region_id
        if application_id is not None:
            self.application_id = application_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_id is not None:
            self.resource_id = resource_id
        self.alarm_desc = alarm_desc
        if url is not None:
            self.url = url
        if alarm_status is not None:
            self.alarm_status = alarm_status
        self.alarm_source = alarm_source
        if additional is not None:
            self.additional = additional

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this ReportCustomEventRequestBody.

        告警id

        :return: The alarm_id of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this ReportCustomEventRequestBody.

        告警id

        :param alarm_id: The alarm_id of this ReportCustomEventRequestBody.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_name(self):
        r"""Gets the alarm_name of this ReportCustomEventRequestBody.

        告警名称

        :return: The alarm_name of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        r"""Sets the alarm_name of this ReportCustomEventRequestBody.

        告警名称

        :param alarm_name: The alarm_name of this ReportCustomEventRequestBody.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this ReportCustomEventRequestBody.

        告警级别。取值为Critical（紧急）, Major（重要）, Minor（次要）, Info（提示）

        :return: The alarm_level of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this ReportCustomEventRequestBody.

        告警级别。取值为Critical（紧急）, Major（重要）, Minor（次要）, Info（提示）

        :param alarm_level: The alarm_level of this ReportCustomEventRequestBody.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def time(self):
        r"""Gets the time of this ReportCustomEventRequestBody.

        告警发生时间

        :return: The time of this ReportCustomEventRequestBody.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ReportCustomEventRequestBody.

        告警发生时间

        :param time: The time of this ReportCustomEventRequestBody.
        :type time: int
        """
        self._time = time

    @property
    def name_space(self):
        r"""Gets the name_space of this ReportCustomEventRequestBody.

        告警发生时间

        :return: The name_space of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        r"""Sets the name_space of this ReportCustomEventRequestBody.

        告警发生时间

        :param name_space: The name_space of this ReportCustomEventRequestBody.
        :type name_space: str
        """
        self._name_space = name_space

    @property
    def region_id(self):
        r"""Gets the region_id of this ReportCustomEventRequestBody.

        告警发生区域

        :return: The region_id of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ReportCustomEventRequestBody.

        告警发生区域

        :param region_id: The region_id of this ReportCustomEventRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def application_id(self):
        r"""Gets the application_id of this ReportCustomEventRequestBody.

        应用id

        :return: The application_id of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ReportCustomEventRequestBody.

        应用id

        :param application_id: The application_id of this ReportCustomEventRequestBody.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ReportCustomEventRequestBody.

        资源名称

        :return: The resource_name of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ReportCustomEventRequestBody.

        资源名称

        :param resource_name: The resource_name of this ReportCustomEventRequestBody.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ReportCustomEventRequestBody.

        资源ID

        :return: The resource_id of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ReportCustomEventRequestBody.

        资源ID

        :param resource_id: The resource_id of this ReportCustomEventRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def alarm_desc(self):
        r"""Gets the alarm_desc of this ReportCustomEventRequestBody.

        告警描述

        :return: The alarm_desc of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._alarm_desc

    @alarm_desc.setter
    def alarm_desc(self, alarm_desc):
        r"""Sets the alarm_desc of this ReportCustomEventRequestBody.

        告警描述

        :param alarm_desc: The alarm_desc of this ReportCustomEventRequestBody.
        :type alarm_desc: str
        """
        self._alarm_desc = alarm_desc

    @property
    def url(self):
        r"""Gets the url of this ReportCustomEventRequestBody.

        原始告警URL

        :return: The url of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ReportCustomEventRequestBody.

        原始告警URL

        :param url: The url of this ReportCustomEventRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def alarm_status(self):
        r"""Gets the alarm_status of this ReportCustomEventRequestBody.

        告警状态。一般取值为alarm（告警中）和ok（已恢复）

        :return: The alarm_status of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        r"""Sets the alarm_status of this ReportCustomEventRequestBody.

        告警状态。一般取值为alarm（告警中）和ok（已恢复）

        :param alarm_status: The alarm_status of this ReportCustomEventRequestBody.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

    @property
    def alarm_source(self):
        r"""Gets the alarm_source of this ReportCustomEventRequestBody.

        告警源

        :return: The alarm_source of this ReportCustomEventRequestBody.
        :rtype: str
        """
        return self._alarm_source

    @alarm_source.setter
    def alarm_source(self, alarm_source):
        r"""Sets the alarm_source of this ReportCustomEventRequestBody.

        告警源

        :param alarm_source: The alarm_source of this ReportCustomEventRequestBody.
        :type alarm_source: str
        """
        self._alarm_source = alarm_source

    @property
    def additional(self):
        r"""Gets the additional of this ReportCustomEventRequestBody.

        告警附加信息

        :return: The additional of this ReportCustomEventRequestBody.
        :rtype: object
        """
        return self._additional

    @additional.setter
    def additional(self, additional):
        r"""Sets the additional of this ReportCustomEventRequestBody.

        告警附加信息

        :param additional: The additional of this ReportCustomEventRequestBody.
        :type additional: object
        """
        self._additional = additional

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
        if not isinstance(other, ReportCustomEventRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
