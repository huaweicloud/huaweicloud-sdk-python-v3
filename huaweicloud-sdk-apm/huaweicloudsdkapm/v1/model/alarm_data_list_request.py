# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmDataListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'page_size': 'int',
        'region': 'str',
        'app_name': 'str',
        'business_id': 'int',
        'monitor_item_id': 'int',
        'status': 'str',
        'alarm_level': 'str',
        'keyword': 'str',
        'alarm_start_time': 'str',
        'alarm_end_time': 'str',
        'collector_id': 'int',
        'ip_address': 'str',
        'env_list': 'list[int]'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'region': 'region',
        'app_name': 'app_name',
        'business_id': 'business_id',
        'monitor_item_id': 'monitor_item_id',
        'status': 'status',
        'alarm_level': 'alarm_level',
        'keyword': 'keyword',
        'alarm_start_time': 'alarm_start_time',
        'alarm_end_time': 'alarm_end_time',
        'collector_id': 'collector_id',
        'ip_address': 'ip_address',
        'env_list': 'env_list'
    }

    def __init__(self, page=None, page_size=None, region=None, app_name=None, business_id=None, monitor_item_id=None, status=None, alarm_level=None, keyword=None, alarm_start_time=None, alarm_end_time=None, collector_id=None, ip_address=None, env_list=None):
        """AlarmDataListRequest

        The model defined in huaweicloud sdk

        :param page: 页码。
        :type page: int
        :param page_size: 每页数量。
        :type page_size: int
        :param region: region英文名称。
        :type region: str
        :param app_name: 组件环境名称。
        :type app_name: str
        :param business_id: 应用id。
        :type business_id: int
        :param monitor_item_id: 监控项id。
        :type monitor_item_id: int
        :param status: 告警状态  RECOVER：已恢复 ABNORMAL：异常 ALERT：告警中。
        :type status: str
        :param alarm_level: 告警级别  COMMON：轻微  CRITICAL：严重。
        :type alarm_level: str
        :param keyword: 关键字。
        :type keyword: str
        :param alarm_start_time: 告警开始时间。
        :type alarm_start_time: str
        :param alarm_end_time: 告警结束时间。
        :type alarm_end_time: str
        :param collector_id: 采集器id。
        :type collector_id: int
        :param ip_address: 实例ip地址。
        :type ip_address: str
        :param env_list: 环境集合。
        :type env_list: list[int]
        """
        
        

        self._page = None
        self._page_size = None
        self._region = None
        self._app_name = None
        self._business_id = None
        self._monitor_item_id = None
        self._status = None
        self._alarm_level = None
        self._keyword = None
        self._alarm_start_time = None
        self._alarm_end_time = None
        self._collector_id = None
        self._ip_address = None
        self._env_list = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if region is not None:
            self.region = region
        if app_name is not None:
            self.app_name = app_name
        self.business_id = business_id
        if monitor_item_id is not None:
            self.monitor_item_id = monitor_item_id
        if status is not None:
            self.status = status
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if keyword is not None:
            self.keyword = keyword
        if alarm_start_time is not None:
            self.alarm_start_time = alarm_start_time
        if alarm_end_time is not None:
            self.alarm_end_time = alarm_end_time
        if collector_id is not None:
            self.collector_id = collector_id
        if ip_address is not None:
            self.ip_address = ip_address
        if env_list is not None:
            self.env_list = env_list

    @property
    def page(self):
        """Gets the page of this AlarmDataListRequest.

        页码。

        :return: The page of this AlarmDataListRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this AlarmDataListRequest.

        页码。

        :param page: The page of this AlarmDataListRequest.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this AlarmDataListRequest.

        每页数量。

        :return: The page_size of this AlarmDataListRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this AlarmDataListRequest.

        每页数量。

        :param page_size: The page_size of this AlarmDataListRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def region(self):
        """Gets the region of this AlarmDataListRequest.

        region英文名称。

        :return: The region of this AlarmDataListRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AlarmDataListRequest.

        region英文名称。

        :param region: The region of this AlarmDataListRequest.
        :type region: str
        """
        self._region = region

    @property
    def app_name(self):
        """Gets the app_name of this AlarmDataListRequest.

        组件环境名称。

        :return: The app_name of this AlarmDataListRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AlarmDataListRequest.

        组件环境名称。

        :param app_name: The app_name of this AlarmDataListRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def business_id(self):
        """Gets the business_id of this AlarmDataListRequest.

        应用id。

        :return: The business_id of this AlarmDataListRequest.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this AlarmDataListRequest.

        应用id。

        :param business_id: The business_id of this AlarmDataListRequest.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def monitor_item_id(self):
        """Gets the monitor_item_id of this AlarmDataListRequest.

        监控项id。

        :return: The monitor_item_id of this AlarmDataListRequest.
        :rtype: int
        """
        return self._monitor_item_id

    @monitor_item_id.setter
    def monitor_item_id(self, monitor_item_id):
        """Sets the monitor_item_id of this AlarmDataListRequest.

        监控项id。

        :param monitor_item_id: The monitor_item_id of this AlarmDataListRequest.
        :type monitor_item_id: int
        """
        self._monitor_item_id = monitor_item_id

    @property
    def status(self):
        """Gets the status of this AlarmDataListRequest.

        告警状态  RECOVER：已恢复 ABNORMAL：异常 ALERT：告警中。

        :return: The status of this AlarmDataListRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AlarmDataListRequest.

        告警状态  RECOVER：已恢复 ABNORMAL：异常 ALERT：告警中。

        :param status: The status of this AlarmDataListRequest.
        :type status: str
        """
        self._status = status

    @property
    def alarm_level(self):
        """Gets the alarm_level of this AlarmDataListRequest.

        告警级别  COMMON：轻微  CRITICAL：严重。

        :return: The alarm_level of this AlarmDataListRequest.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this AlarmDataListRequest.

        告警级别  COMMON：轻微  CRITICAL：严重。

        :param alarm_level: The alarm_level of this AlarmDataListRequest.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def keyword(self):
        """Gets the keyword of this AlarmDataListRequest.

        关键字。

        :return: The keyword of this AlarmDataListRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this AlarmDataListRequest.

        关键字。

        :param keyword: The keyword of this AlarmDataListRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def alarm_start_time(self):
        """Gets the alarm_start_time of this AlarmDataListRequest.

        告警开始时间。

        :return: The alarm_start_time of this AlarmDataListRequest.
        :rtype: str
        """
        return self._alarm_start_time

    @alarm_start_time.setter
    def alarm_start_time(self, alarm_start_time):
        """Sets the alarm_start_time of this AlarmDataListRequest.

        告警开始时间。

        :param alarm_start_time: The alarm_start_time of this AlarmDataListRequest.
        :type alarm_start_time: str
        """
        self._alarm_start_time = alarm_start_time

    @property
    def alarm_end_time(self):
        """Gets the alarm_end_time of this AlarmDataListRequest.

        告警结束时间。

        :return: The alarm_end_time of this AlarmDataListRequest.
        :rtype: str
        """
        return self._alarm_end_time

    @alarm_end_time.setter
    def alarm_end_time(self, alarm_end_time):
        """Sets the alarm_end_time of this AlarmDataListRequest.

        告警结束时间。

        :param alarm_end_time: The alarm_end_time of this AlarmDataListRequest.
        :type alarm_end_time: str
        """
        self._alarm_end_time = alarm_end_time

    @property
    def collector_id(self):
        """Gets the collector_id of this AlarmDataListRequest.

        采集器id。

        :return: The collector_id of this AlarmDataListRequest.
        :rtype: int
        """
        return self._collector_id

    @collector_id.setter
    def collector_id(self, collector_id):
        """Sets the collector_id of this AlarmDataListRequest.

        采集器id。

        :param collector_id: The collector_id of this AlarmDataListRequest.
        :type collector_id: int
        """
        self._collector_id = collector_id

    @property
    def ip_address(self):
        """Gets the ip_address of this AlarmDataListRequest.

        实例ip地址。

        :return: The ip_address of this AlarmDataListRequest.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this AlarmDataListRequest.

        实例ip地址。

        :param ip_address: The ip_address of this AlarmDataListRequest.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def env_list(self):
        """Gets the env_list of this AlarmDataListRequest.

        环境集合。

        :return: The env_list of this AlarmDataListRequest.
        :rtype: list[int]
        """
        return self._env_list

    @env_list.setter
    def env_list(self, env_list):
        """Sets the env_list of this AlarmDataListRequest.

        环境集合。

        :param env_list: The env_list of this AlarmDataListRequest.
        :type env_list: list[int]
        """
        self._env_list = env_list

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
        if not isinstance(other, AlarmDataListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
