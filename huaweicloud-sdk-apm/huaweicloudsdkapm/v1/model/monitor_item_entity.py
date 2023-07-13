# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MonitorItemEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category_id': 'int',
        'collector_name': 'str',
        'display_name': 'str',
        'show_in_total': 'bool',
        'monitor_item_id': 'int',
        'disabled': 'bool',
        'collector_id': 'int',
        'sequence': 'int',
        'collect_interval': 'int'
    }

    attribute_map = {
        'category_id': 'category_id',
        'collector_name': 'collector_name',
        'display_name': 'display_name',
        'show_in_total': 'show_in_total',
        'monitor_item_id': 'monitor_item_id',
        'disabled': 'disabled',
        'collector_id': 'collector_id',
        'sequence': 'sequence',
        'collect_interval': 'collect_interval'
    }

    def __init__(self, category_id=None, collector_name=None, display_name=None, show_in_total=None, monitor_item_id=None, disabled=None, collector_id=None, sequence=None, collect_interval=None):
        """MonitorItemEntity

        The model defined in huaweicloud sdk

        :param category_id: 采集器类别id。
        :type category_id: int
        :param collector_name: 采集器名称。
        :type collector_name: str
        :param display_name: 采集器类别展示名称。
        :type display_name: str
        :param show_in_total: 是否展示标题。
        :type show_in_total: bool
        :param monitor_item_id: 监控项id。
        :type monitor_item_id: int
        :param disabled: 是否禁用。
        :type disabled: bool
        :param collector_id: 采集器id。
        :type collector_id: int
        :param sequence: 序列号。
        :type sequence: int
        :param collect_interval: 默认数据采集间隔。
        :type collect_interval: int
        """
        
        

        self._category_id = None
        self._collector_name = None
        self._display_name = None
        self._show_in_total = None
        self._monitor_item_id = None
        self._disabled = None
        self._collector_id = None
        self._sequence = None
        self._collect_interval = None
        self.discriminator = None

        if category_id is not None:
            self.category_id = category_id
        if collector_name is not None:
            self.collector_name = collector_name
        if display_name is not None:
            self.display_name = display_name
        if show_in_total is not None:
            self.show_in_total = show_in_total
        if monitor_item_id is not None:
            self.monitor_item_id = monitor_item_id
        if disabled is not None:
            self.disabled = disabled
        if collector_id is not None:
            self.collector_id = collector_id
        if sequence is not None:
            self.sequence = sequence
        if collect_interval is not None:
            self.collect_interval = collect_interval

    @property
    def category_id(self):
        """Gets the category_id of this MonitorItemEntity.

        采集器类别id。

        :return: The category_id of this MonitorItemEntity.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this MonitorItemEntity.

        采集器类别id。

        :param category_id: The category_id of this MonitorItemEntity.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def collector_name(self):
        """Gets the collector_name of this MonitorItemEntity.

        采集器名称。

        :return: The collector_name of this MonitorItemEntity.
        :rtype: str
        """
        return self._collector_name

    @collector_name.setter
    def collector_name(self, collector_name):
        """Sets the collector_name of this MonitorItemEntity.

        采集器名称。

        :param collector_name: The collector_name of this MonitorItemEntity.
        :type collector_name: str
        """
        self._collector_name = collector_name

    @property
    def display_name(self):
        """Gets the display_name of this MonitorItemEntity.

        采集器类别展示名称。

        :return: The display_name of this MonitorItemEntity.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this MonitorItemEntity.

        采集器类别展示名称。

        :param display_name: The display_name of this MonitorItemEntity.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def show_in_total(self):
        """Gets the show_in_total of this MonitorItemEntity.

        是否展示标题。

        :return: The show_in_total of this MonitorItemEntity.
        :rtype: bool
        """
        return self._show_in_total

    @show_in_total.setter
    def show_in_total(self, show_in_total):
        """Sets the show_in_total of this MonitorItemEntity.

        是否展示标题。

        :param show_in_total: The show_in_total of this MonitorItemEntity.
        :type show_in_total: bool
        """
        self._show_in_total = show_in_total

    @property
    def monitor_item_id(self):
        """Gets the monitor_item_id of this MonitorItemEntity.

        监控项id。

        :return: The monitor_item_id of this MonitorItemEntity.
        :rtype: int
        """
        return self._monitor_item_id

    @monitor_item_id.setter
    def monitor_item_id(self, monitor_item_id):
        """Sets the monitor_item_id of this MonitorItemEntity.

        监控项id。

        :param monitor_item_id: The monitor_item_id of this MonitorItemEntity.
        :type monitor_item_id: int
        """
        self._monitor_item_id = monitor_item_id

    @property
    def disabled(self):
        """Gets the disabled of this MonitorItemEntity.

        是否禁用。

        :return: The disabled of this MonitorItemEntity.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this MonitorItemEntity.

        是否禁用。

        :param disabled: The disabled of this MonitorItemEntity.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def collector_id(self):
        """Gets the collector_id of this MonitorItemEntity.

        采集器id。

        :return: The collector_id of this MonitorItemEntity.
        :rtype: int
        """
        return self._collector_id

    @collector_id.setter
    def collector_id(self, collector_id):
        """Sets the collector_id of this MonitorItemEntity.

        采集器id。

        :param collector_id: The collector_id of this MonitorItemEntity.
        :type collector_id: int
        """
        self._collector_id = collector_id

    @property
    def sequence(self):
        """Gets the sequence of this MonitorItemEntity.

        序列号。

        :return: The sequence of this MonitorItemEntity.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this MonitorItemEntity.

        序列号。

        :param sequence: The sequence of this MonitorItemEntity.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def collect_interval(self):
        """Gets the collect_interval of this MonitorItemEntity.

        默认数据采集间隔。

        :return: The collect_interval of this MonitorItemEntity.
        :rtype: int
        """
        return self._collect_interval

    @collect_interval.setter
    def collect_interval(self, collect_interval):
        """Sets the collect_interval of this MonitorItemEntity.

        默认数据采集间隔。

        :param collect_interval: The collect_interval of this MonitorItemEntity.
        :type collect_interval: int
        """
        self._collect_interval = collect_interval

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
        if not isinstance(other, MonitorItemEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
