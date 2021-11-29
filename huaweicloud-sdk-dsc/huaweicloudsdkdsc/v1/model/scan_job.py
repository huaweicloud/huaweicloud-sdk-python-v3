# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScanJob:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'cycle': 'str',
        'id': 'str',
        'last_run_time': 'int',
        'last_scan_risk': 'str',
        'name': 'str',
        'open': 'bool',
        'rule_groups': 'list[str]',
        'status': 'str',
        'topic_urn': 'str',
        'use_nlp': 'bool',
        'start_time': 'int'
    }

    attribute_map = {
        'create_time': 'create_time',
        'cycle': 'cycle',
        'id': 'id',
        'last_run_time': 'last_run_time',
        'last_scan_risk': 'last_scan_risk',
        'name': 'name',
        'open': 'open',
        'rule_groups': 'rule_groups',
        'status': 'status',
        'topic_urn': 'topic_urn',
        'use_nlp': 'use_nlp',
        'start_time': 'start_time'
    }

    def __init__(self, create_time=None, cycle=None, id=None, last_run_time=None, last_scan_risk=None, name=None, open=None, rule_groups=None, status=None, topic_urn=None, use_nlp=None, start_time=None):
        """ScanJob - a model defined in huaweicloud sdk"""
        
        

        self._create_time = None
        self._cycle = None
        self._id = None
        self._last_run_time = None
        self._last_scan_risk = None
        self._name = None
        self._open = None
        self._rule_groups = None
        self._status = None
        self._topic_urn = None
        self._use_nlp = None
        self._start_time = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if cycle is not None:
            self.cycle = cycle
        if id is not None:
            self.id = id
        if last_run_time is not None:
            self.last_run_time = last_run_time
        if last_scan_risk is not None:
            self.last_scan_risk = last_scan_risk
        if name is not None:
            self.name = name
        if open is not None:
            self.open = open
        if rule_groups is not None:
            self.rule_groups = rule_groups
        if status is not None:
            self.status = status
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if use_nlp is not None:
            self.use_nlp = use_nlp
        if start_time is not None:
            self.start_time = start_time

    @property
    def create_time(self):
        """Gets the create_time of this ScanJob.

        任务创建时间

        :return: The create_time of this ScanJob.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScanJob.

        任务创建时间

        :param create_time: The create_time of this ScanJob.
        :type: int
        """
        self._create_time = create_time

    @property
    def cycle(self):
        """Gets the cycle of this ScanJob.

        任务执行方式

        :return: The cycle of this ScanJob.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ScanJob.

        任务执行方式

        :param cycle: The cycle of this ScanJob.
        :type: str
        """
        self._cycle = cycle

    @property
    def id(self):
        """Gets the id of this ScanJob.

        任务ID

        :return: The id of this ScanJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScanJob.

        任务ID

        :param id: The id of this ScanJob.
        :type: str
        """
        self._id = id

    @property
    def last_run_time(self):
        """Gets the last_run_time of this ScanJob.

        任务上一次执行时间

        :return: The last_run_time of this ScanJob.
        :rtype: int
        """
        return self._last_run_time

    @last_run_time.setter
    def last_run_time(self, last_run_time):
        """Sets the last_run_time of this ScanJob.

        任务上一次执行时间

        :param last_run_time: The last_run_time of this ScanJob.
        :type: int
        """
        self._last_run_time = last_run_time

    @property
    def last_scan_risk(self):
        """Gets the last_scan_risk of this ScanJob.

        任务上一次扫描风险等级结果

        :return: The last_scan_risk of this ScanJob.
        :rtype: str
        """
        return self._last_scan_risk

    @last_scan_risk.setter
    def last_scan_risk(self, last_scan_risk):
        """Sets the last_scan_risk of this ScanJob.

        任务上一次扫描风险等级结果

        :param last_scan_risk: The last_scan_risk of this ScanJob.
        :type: str
        """
        self._last_scan_risk = last_scan_risk

    @property
    def name(self):
        """Gets the name of this ScanJob.

        任务名称

        :return: The name of this ScanJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScanJob.

        任务名称

        :param name: The name of this ScanJob.
        :type: str
        """
        self._name = name

    @property
    def open(self):
        """Gets the open of this ScanJob.

        任务开启状态

        :return: The open of this ScanJob.
        :rtype: bool
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this ScanJob.

        任务开启状态

        :param open: The open of this ScanJob.
        :type: bool
        """
        self._open = open

    @property
    def rule_groups(self):
        """Gets the rule_groups of this ScanJob.

        任务使用的规则组

        :return: The rule_groups of this ScanJob.
        :rtype: list[str]
        """
        return self._rule_groups

    @rule_groups.setter
    def rule_groups(self, rule_groups):
        """Sets the rule_groups of this ScanJob.

        任务使用的规则组

        :param rule_groups: The rule_groups of this ScanJob.
        :type: list[str]
        """
        self._rule_groups = rule_groups

    @property
    def status(self):
        """Gets the status of this ScanJob.

        任务当前状态

        :return: The status of this ScanJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScanJob.

        任务当前状态

        :param status: The status of this ScanJob.
        :type: str
        """
        self._status = status

    @property
    def topic_urn(self):
        """Gets the topic_urn of this ScanJob.

        SMN服务通知主题

        :return: The topic_urn of this ScanJob.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this ScanJob.

        SMN服务通知主题

        :param topic_urn: The topic_urn of this ScanJob.
        :type: str
        """
        self._topic_urn = topic_urn

    @property
    def use_nlp(self):
        """Gets the use_nlp of this ScanJob.

        是否使用了NLP进行扫描

        :return: The use_nlp of this ScanJob.
        :rtype: bool
        """
        return self._use_nlp

    @use_nlp.setter
    def use_nlp(self, use_nlp):
        """Sets the use_nlp of this ScanJob.

        是否使用了NLP进行扫描

        :param use_nlp: The use_nlp of this ScanJob.
        :type: bool
        """
        self._use_nlp = use_nlp

    @property
    def start_time(self):
        """Gets the start_time of this ScanJob.

        任务启动时间

        :return: The start_time of this ScanJob.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScanJob.

        任务启动时间

        :param start_time: The start_time of this ScanJob.
        :type: int
        """
        self._start_time = start_time

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
        if not isinstance(other, ScanJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
