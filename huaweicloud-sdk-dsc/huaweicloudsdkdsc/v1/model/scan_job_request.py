# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScanJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_ids': 'list[str]',
        'cycle': 'str',
        'name': 'str',
        'open': 'bool',
        'rule_group_ids': 'list[str]',
        'start_time': 'int',
        'time_zone': 'str',
        'topic_urn': 'str',
        'use_nlp': 'bool'
    }

    attribute_map = {
        'asset_ids': 'asset_ids',
        'cycle': 'cycle',
        'name': 'name',
        'open': 'open',
        'rule_group_ids': 'rule_group_ids',
        'start_time': 'start_time',
        'time_zone': 'time_zone',
        'topic_urn': 'topic_urn',
        'use_nlp': 'use_nlp'
    }

    def __init__(self, asset_ids=None, cycle=None, name=None, open=None, rule_group_ids=None, start_time=None, time_zone=None, topic_urn=None, use_nlp=None):
        """ScanJobRequest

        The model defined in huaweicloud sdk

        :param asset_ids: 资产ID列表
        :type asset_ids: list[str]
        :param cycle: 扫描周期，日(DAY)，周(WEEK)，月(MONTH)，单次扫描(ONCE)
        :type cycle: str
        :param name: 扫描任务名
        :type name: str
        :param open: 是否开启任务
        :type open: bool
        :param rule_group_ids: 规则组ID列表
        :type rule_group_ids: list[str]
        :param start_time: 扫描任务开始时间
        :type start_time: int
        :param time_zone: 时区
        :type time_zone: str
        :param topic_urn: 主题的唯一资源标识符
        :type topic_urn: str
        :param use_nlp: 是否用nlp
        :type use_nlp: bool
        """
        
        

        self._asset_ids = None
        self._cycle = None
        self._name = None
        self._open = None
        self._rule_group_ids = None
        self._start_time = None
        self._time_zone = None
        self._topic_urn = None
        self._use_nlp = None
        self.discriminator = None

        if asset_ids is not None:
            self.asset_ids = asset_ids
        if cycle is not None:
            self.cycle = cycle
        if name is not None:
            self.name = name
        if open is not None:
            self.open = open
        if rule_group_ids is not None:
            self.rule_group_ids = rule_group_ids
        if start_time is not None:
            self.start_time = start_time
        if time_zone is not None:
            self.time_zone = time_zone
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if use_nlp is not None:
            self.use_nlp = use_nlp

    @property
    def asset_ids(self):
        """Gets the asset_ids of this ScanJobRequest.

        资产ID列表

        :return: The asset_ids of this ScanJobRequest.
        :rtype: list[str]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        """Sets the asset_ids of this ScanJobRequest.

        资产ID列表

        :param asset_ids: The asset_ids of this ScanJobRequest.
        :type asset_ids: list[str]
        """
        self._asset_ids = asset_ids

    @property
    def cycle(self):
        """Gets the cycle of this ScanJobRequest.

        扫描周期，日(DAY)，周(WEEK)，月(MONTH)，单次扫描(ONCE)

        :return: The cycle of this ScanJobRequest.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ScanJobRequest.

        扫描周期，日(DAY)，周(WEEK)，月(MONTH)，单次扫描(ONCE)

        :param cycle: The cycle of this ScanJobRequest.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def name(self):
        """Gets the name of this ScanJobRequest.

        扫描任务名

        :return: The name of this ScanJobRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScanJobRequest.

        扫描任务名

        :param name: The name of this ScanJobRequest.
        :type name: str
        """
        self._name = name

    @property
    def open(self):
        """Gets the open of this ScanJobRequest.

        是否开启任务

        :return: The open of this ScanJobRequest.
        :rtype: bool
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this ScanJobRequest.

        是否开启任务

        :param open: The open of this ScanJobRequest.
        :type open: bool
        """
        self._open = open

    @property
    def rule_group_ids(self):
        """Gets the rule_group_ids of this ScanJobRequest.

        规则组ID列表

        :return: The rule_group_ids of this ScanJobRequest.
        :rtype: list[str]
        """
        return self._rule_group_ids

    @rule_group_ids.setter
    def rule_group_ids(self, rule_group_ids):
        """Sets the rule_group_ids of this ScanJobRequest.

        规则组ID列表

        :param rule_group_ids: The rule_group_ids of this ScanJobRequest.
        :type rule_group_ids: list[str]
        """
        self._rule_group_ids = rule_group_ids

    @property
    def start_time(self):
        """Gets the start_time of this ScanJobRequest.

        扫描任务开始时间

        :return: The start_time of this ScanJobRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScanJobRequest.

        扫描任务开始时间

        :param start_time: The start_time of this ScanJobRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def time_zone(self):
        """Gets the time_zone of this ScanJobRequest.

        时区

        :return: The time_zone of this ScanJobRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ScanJobRequest.

        时区

        :param time_zone: The time_zone of this ScanJobRequest.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def topic_urn(self):
        """Gets the topic_urn of this ScanJobRequest.

        主题的唯一资源标识符

        :return: The topic_urn of this ScanJobRequest.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this ScanJobRequest.

        主题的唯一资源标识符

        :param topic_urn: The topic_urn of this ScanJobRequest.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def use_nlp(self):
        """Gets the use_nlp of this ScanJobRequest.

        是否用nlp

        :return: The use_nlp of this ScanJobRequest.
        :rtype: bool
        """
        return self._use_nlp

    @use_nlp.setter
    def use_nlp(self, use_nlp):
        """Sets the use_nlp of this ScanJobRequest.

        是否用nlp

        :param use_nlp: The use_nlp of this ScanJobRequest.
        :type use_nlp: bool
        """
        self._use_nlp = use_nlp

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
        if not isinstance(other, ScanJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
