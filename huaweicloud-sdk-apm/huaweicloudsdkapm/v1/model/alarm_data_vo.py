# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmDataVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'gmt_create': 'str',
        'region_alarm_event_id': 'int',
        'business_name': 'str',
        'app_name': 'str',
        'version_number': 'int',
        'alarm_rule_type': 'str',
        'gmt_modify': 'str',
        'process_unit': 'str',
        'region': 'str',
        'instance_id': 'int',
        'ip_address': 'str',
        'instance_name': 'str',
        'env_id': 'int',
        'business_id': 'int',
        'template_id': 'int',
        'alarm_rule_id': 'int',
        'monitor_item_id': 'int',
        'collector_id': 'int',
        'collector_name': 'str',
        'alarm_rule_name': 'str',
        'alarm_rule_expression': 'str',
        'alarm_first_time': 'str',
        'alarm_last_time': 'str',
        'alarm_level': 'str',
        'restrain_key': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'gmt_create': 'gmt_create',
        'region_alarm_event_id': 'region_alarm_event_id',
        'business_name': 'business_name',
        'app_name': 'app_name',
        'version_number': 'version_number',
        'alarm_rule_type': 'alarm_rule_type',
        'gmt_modify': 'gmt_modify',
        'process_unit': 'process_unit',
        'region': 'region',
        'instance_id': 'instance_id',
        'ip_address': 'ip_address',
        'instance_name': 'instance_name',
        'env_id': 'env_id',
        'business_id': 'business_id',
        'template_id': 'template_id',
        'alarm_rule_id': 'alarm_rule_id',
        'monitor_item_id': 'monitor_item_id',
        'collector_id': 'collector_id',
        'collector_name': 'collector_name',
        'alarm_rule_name': 'alarm_rule_name',
        'alarm_rule_expression': 'alarm_rule_expression',
        'alarm_first_time': 'alarm_first_time',
        'alarm_last_time': 'alarm_last_time',
        'alarm_level': 'alarm_level',
        'restrain_key': 'restrain_key',
        'status': 'status'
    }

    def __init__(self, id=None, gmt_create=None, region_alarm_event_id=None, business_name=None, app_name=None, version_number=None, alarm_rule_type=None, gmt_modify=None, process_unit=None, region=None, instance_id=None, ip_address=None, instance_name=None, env_id=None, business_id=None, template_id=None, alarm_rule_id=None, monitor_item_id=None, collector_id=None, collector_name=None, alarm_rule_name=None, alarm_rule_expression=None, alarm_first_time=None, alarm_last_time=None, alarm_level=None, restrain_key=None, status=None):
        """AlarmDataVO

        The model defined in huaweicloud sdk

        :param id: 告警通知id。
        :type id: int
        :param gmt_create: 创建时间。
        :type gmt_create: str
        :param region_alarm_event_id: region中事件的id。
        :type region_alarm_event_id: int
        :param business_name: 应用名称。
        :type business_name: str
        :param app_name: 组件名称。
        :type app_name: str
        :param version_number: 版本。
        :type version_number: int
        :param alarm_rule_type: 告警规则类别。
        :type alarm_rule_type: str
        :param gmt_modify: 修改时间。
        :type gmt_modify: str
        :param process_unit: 处理单元。
        :type process_unit: str
        :param region: 区域名称。
        :type region: str
        :param instance_id: 实例id。
        :type instance_id: int
        :param ip_address: 实例ip地址。
        :type ip_address: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param env_id: 环境id。
        :type env_id: int
        :param business_id: 应用id。
        :type business_id: int
        :param template_id: 模板id。
        :type template_id: int
        :param alarm_rule_id: 告警规则id。
        :type alarm_rule_id: int
        :param monitor_item_id: 监控项id。
        :type monitor_item_id: int
        :param collector_id: 采集器id。
        :type collector_id: int
        :param collector_name: 采集器名称。
        :type collector_name: str
        :param alarm_rule_name: 告警规则名称。
        :type alarm_rule_name: str
        :param alarm_rule_expression: 告警表达式。
        :type alarm_rule_expression: str
        :param alarm_first_time: 开始报警时间。
        :type alarm_first_time: str
        :param alarm_last_time: 最后一次报警时间。
        :type alarm_last_time: str
        :param alarm_level: 告警级别。
        :type alarm_level: str
        :param restrain_key: 唯一告警标识符。
        :type restrain_key: str
        :param status: 告警状态。
        :type status: str
        """
        
        

        self._id = None
        self._gmt_create = None
        self._region_alarm_event_id = None
        self._business_name = None
        self._app_name = None
        self._version_number = None
        self._alarm_rule_type = None
        self._gmt_modify = None
        self._process_unit = None
        self._region = None
        self._instance_id = None
        self._ip_address = None
        self._instance_name = None
        self._env_id = None
        self._business_id = None
        self._template_id = None
        self._alarm_rule_id = None
        self._monitor_item_id = None
        self._collector_id = None
        self._collector_name = None
        self._alarm_rule_name = None
        self._alarm_rule_expression = None
        self._alarm_first_time = None
        self._alarm_last_time = None
        self._alarm_level = None
        self._restrain_key = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if gmt_create is not None:
            self.gmt_create = gmt_create
        if region_alarm_event_id is not None:
            self.region_alarm_event_id = region_alarm_event_id
        if business_name is not None:
            self.business_name = business_name
        if app_name is not None:
            self.app_name = app_name
        if version_number is not None:
            self.version_number = version_number
        if alarm_rule_type is not None:
            self.alarm_rule_type = alarm_rule_type
        if gmt_modify is not None:
            self.gmt_modify = gmt_modify
        if process_unit is not None:
            self.process_unit = process_unit
        if region is not None:
            self.region = region
        if instance_id is not None:
            self.instance_id = instance_id
        if ip_address is not None:
            self.ip_address = ip_address
        if instance_name is not None:
            self.instance_name = instance_name
        if env_id is not None:
            self.env_id = env_id
        if business_id is not None:
            self.business_id = business_id
        if template_id is not None:
            self.template_id = template_id
        if alarm_rule_id is not None:
            self.alarm_rule_id = alarm_rule_id
        if monitor_item_id is not None:
            self.monitor_item_id = monitor_item_id
        if collector_id is not None:
            self.collector_id = collector_id
        if collector_name is not None:
            self.collector_name = collector_name
        if alarm_rule_name is not None:
            self.alarm_rule_name = alarm_rule_name
        if alarm_rule_expression is not None:
            self.alarm_rule_expression = alarm_rule_expression
        if alarm_first_time is not None:
            self.alarm_first_time = alarm_first_time
        if alarm_last_time is not None:
            self.alarm_last_time = alarm_last_time
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if restrain_key is not None:
            self.restrain_key = restrain_key
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this AlarmDataVO.

        告警通知id。

        :return: The id of this AlarmDataVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlarmDataVO.

        告警通知id。

        :param id: The id of this AlarmDataVO.
        :type id: int
        """
        self._id = id

    @property
    def gmt_create(self):
        """Gets the gmt_create of this AlarmDataVO.

        创建时间。

        :return: The gmt_create of this AlarmDataVO.
        :rtype: str
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        """Sets the gmt_create of this AlarmDataVO.

        创建时间。

        :param gmt_create: The gmt_create of this AlarmDataVO.
        :type gmt_create: str
        """
        self._gmt_create = gmt_create

    @property
    def region_alarm_event_id(self):
        """Gets the region_alarm_event_id of this AlarmDataVO.

        region中事件的id。

        :return: The region_alarm_event_id of this AlarmDataVO.
        :rtype: int
        """
        return self._region_alarm_event_id

    @region_alarm_event_id.setter
    def region_alarm_event_id(self, region_alarm_event_id):
        """Sets the region_alarm_event_id of this AlarmDataVO.

        region中事件的id。

        :param region_alarm_event_id: The region_alarm_event_id of this AlarmDataVO.
        :type region_alarm_event_id: int
        """
        self._region_alarm_event_id = region_alarm_event_id

    @property
    def business_name(self):
        """Gets the business_name of this AlarmDataVO.

        应用名称。

        :return: The business_name of this AlarmDataVO.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this AlarmDataVO.

        应用名称。

        :param business_name: The business_name of this AlarmDataVO.
        :type business_name: str
        """
        self._business_name = business_name

    @property
    def app_name(self):
        """Gets the app_name of this AlarmDataVO.

        组件名称。

        :return: The app_name of this AlarmDataVO.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AlarmDataVO.

        组件名称。

        :param app_name: The app_name of this AlarmDataVO.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def version_number(self):
        """Gets the version_number of this AlarmDataVO.

        版本。

        :return: The version_number of this AlarmDataVO.
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this AlarmDataVO.

        版本。

        :param version_number: The version_number of this AlarmDataVO.
        :type version_number: int
        """
        self._version_number = version_number

    @property
    def alarm_rule_type(self):
        """Gets the alarm_rule_type of this AlarmDataVO.

        告警规则类别。

        :return: The alarm_rule_type of this AlarmDataVO.
        :rtype: str
        """
        return self._alarm_rule_type

    @alarm_rule_type.setter
    def alarm_rule_type(self, alarm_rule_type):
        """Sets the alarm_rule_type of this AlarmDataVO.

        告警规则类别。

        :param alarm_rule_type: The alarm_rule_type of this AlarmDataVO.
        :type alarm_rule_type: str
        """
        self._alarm_rule_type = alarm_rule_type

    @property
    def gmt_modify(self):
        """Gets the gmt_modify of this AlarmDataVO.

        修改时间。

        :return: The gmt_modify of this AlarmDataVO.
        :rtype: str
        """
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, gmt_modify):
        """Sets the gmt_modify of this AlarmDataVO.

        修改时间。

        :param gmt_modify: The gmt_modify of this AlarmDataVO.
        :type gmt_modify: str
        """
        self._gmt_modify = gmt_modify

    @property
    def process_unit(self):
        """Gets the process_unit of this AlarmDataVO.

        处理单元。

        :return: The process_unit of this AlarmDataVO.
        :rtype: str
        """
        return self._process_unit

    @process_unit.setter
    def process_unit(self, process_unit):
        """Sets the process_unit of this AlarmDataVO.

        处理单元。

        :param process_unit: The process_unit of this AlarmDataVO.
        :type process_unit: str
        """
        self._process_unit = process_unit

    @property
    def region(self):
        """Gets the region of this AlarmDataVO.

        区域名称。

        :return: The region of this AlarmDataVO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AlarmDataVO.

        区域名称。

        :param region: The region of this AlarmDataVO.
        :type region: str
        """
        self._region = region

    @property
    def instance_id(self):
        """Gets the instance_id of this AlarmDataVO.

        实例id。

        :return: The instance_id of this AlarmDataVO.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AlarmDataVO.

        实例id。

        :param instance_id: The instance_id of this AlarmDataVO.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def ip_address(self):
        """Gets the ip_address of this AlarmDataVO.

        实例ip地址。

        :return: The ip_address of this AlarmDataVO.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this AlarmDataVO.

        实例ip地址。

        :param ip_address: The ip_address of this AlarmDataVO.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def instance_name(self):
        """Gets the instance_name of this AlarmDataVO.

        实例名称。

        :return: The instance_name of this AlarmDataVO.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this AlarmDataVO.

        实例名称。

        :param instance_name: The instance_name of this AlarmDataVO.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def env_id(self):
        """Gets the env_id of this AlarmDataVO.

        环境id。

        :return: The env_id of this AlarmDataVO.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this AlarmDataVO.

        环境id。

        :param env_id: The env_id of this AlarmDataVO.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def business_id(self):
        """Gets the business_id of this AlarmDataVO.

        应用id。

        :return: The business_id of this AlarmDataVO.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this AlarmDataVO.

        应用id。

        :param business_id: The business_id of this AlarmDataVO.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def template_id(self):
        """Gets the template_id of this AlarmDataVO.

        模板id。

        :return: The template_id of this AlarmDataVO.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this AlarmDataVO.

        模板id。

        :param template_id: The template_id of this AlarmDataVO.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def alarm_rule_id(self):
        """Gets the alarm_rule_id of this AlarmDataVO.

        告警规则id。

        :return: The alarm_rule_id of this AlarmDataVO.
        :rtype: int
        """
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, alarm_rule_id):
        """Sets the alarm_rule_id of this AlarmDataVO.

        告警规则id。

        :param alarm_rule_id: The alarm_rule_id of this AlarmDataVO.
        :type alarm_rule_id: int
        """
        self._alarm_rule_id = alarm_rule_id

    @property
    def monitor_item_id(self):
        """Gets the monitor_item_id of this AlarmDataVO.

        监控项id。

        :return: The monitor_item_id of this AlarmDataVO.
        :rtype: int
        """
        return self._monitor_item_id

    @monitor_item_id.setter
    def monitor_item_id(self, monitor_item_id):
        """Sets the monitor_item_id of this AlarmDataVO.

        监控项id。

        :param monitor_item_id: The monitor_item_id of this AlarmDataVO.
        :type monitor_item_id: int
        """
        self._monitor_item_id = monitor_item_id

    @property
    def collector_id(self):
        """Gets the collector_id of this AlarmDataVO.

        采集器id。

        :return: The collector_id of this AlarmDataVO.
        :rtype: int
        """
        return self._collector_id

    @collector_id.setter
    def collector_id(self, collector_id):
        """Sets the collector_id of this AlarmDataVO.

        采集器id。

        :param collector_id: The collector_id of this AlarmDataVO.
        :type collector_id: int
        """
        self._collector_id = collector_id

    @property
    def collector_name(self):
        """Gets the collector_name of this AlarmDataVO.

        采集器名称。

        :return: The collector_name of this AlarmDataVO.
        :rtype: str
        """
        return self._collector_name

    @collector_name.setter
    def collector_name(self, collector_name):
        """Sets the collector_name of this AlarmDataVO.

        采集器名称。

        :param collector_name: The collector_name of this AlarmDataVO.
        :type collector_name: str
        """
        self._collector_name = collector_name

    @property
    def alarm_rule_name(self):
        """Gets the alarm_rule_name of this AlarmDataVO.

        告警规则名称。

        :return: The alarm_rule_name of this AlarmDataVO.
        :rtype: str
        """
        return self._alarm_rule_name

    @alarm_rule_name.setter
    def alarm_rule_name(self, alarm_rule_name):
        """Sets the alarm_rule_name of this AlarmDataVO.

        告警规则名称。

        :param alarm_rule_name: The alarm_rule_name of this AlarmDataVO.
        :type alarm_rule_name: str
        """
        self._alarm_rule_name = alarm_rule_name

    @property
    def alarm_rule_expression(self):
        """Gets the alarm_rule_expression of this AlarmDataVO.

        告警表达式。

        :return: The alarm_rule_expression of this AlarmDataVO.
        :rtype: str
        """
        return self._alarm_rule_expression

    @alarm_rule_expression.setter
    def alarm_rule_expression(self, alarm_rule_expression):
        """Sets the alarm_rule_expression of this AlarmDataVO.

        告警表达式。

        :param alarm_rule_expression: The alarm_rule_expression of this AlarmDataVO.
        :type alarm_rule_expression: str
        """
        self._alarm_rule_expression = alarm_rule_expression

    @property
    def alarm_first_time(self):
        """Gets the alarm_first_time of this AlarmDataVO.

        开始报警时间。

        :return: The alarm_first_time of this AlarmDataVO.
        :rtype: str
        """
        return self._alarm_first_time

    @alarm_first_time.setter
    def alarm_first_time(self, alarm_first_time):
        """Sets the alarm_first_time of this AlarmDataVO.

        开始报警时间。

        :param alarm_first_time: The alarm_first_time of this AlarmDataVO.
        :type alarm_first_time: str
        """
        self._alarm_first_time = alarm_first_time

    @property
    def alarm_last_time(self):
        """Gets the alarm_last_time of this AlarmDataVO.

        最后一次报警时间。

        :return: The alarm_last_time of this AlarmDataVO.
        :rtype: str
        """
        return self._alarm_last_time

    @alarm_last_time.setter
    def alarm_last_time(self, alarm_last_time):
        """Sets the alarm_last_time of this AlarmDataVO.

        最后一次报警时间。

        :param alarm_last_time: The alarm_last_time of this AlarmDataVO.
        :type alarm_last_time: str
        """
        self._alarm_last_time = alarm_last_time

    @property
    def alarm_level(self):
        """Gets the alarm_level of this AlarmDataVO.

        告警级别。

        :return: The alarm_level of this AlarmDataVO.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this AlarmDataVO.

        告警级别。

        :param alarm_level: The alarm_level of this AlarmDataVO.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def restrain_key(self):
        """Gets the restrain_key of this AlarmDataVO.

        唯一告警标识符。

        :return: The restrain_key of this AlarmDataVO.
        :rtype: str
        """
        return self._restrain_key

    @restrain_key.setter
    def restrain_key(self, restrain_key):
        """Sets the restrain_key of this AlarmDataVO.

        唯一告警标识符。

        :param restrain_key: The restrain_key of this AlarmDataVO.
        :type restrain_key: str
        """
        self._restrain_key = restrain_key

    @property
    def status(self):
        """Gets the status of this AlarmDataVO.

        告警状态。

        :return: The status of this AlarmDataVO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AlarmDataVO.

        告警状态。

        :param status: The status of this AlarmDataVO.
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
        if not isinstance(other, AlarmDataVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
