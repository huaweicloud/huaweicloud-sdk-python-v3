# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MsgInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_channels': 'str',
        'alert_groups': 'str',
        'alert_level': 'int',
        'alert_num': 'int',
        'alert_time': 'datetime',
        'alert_type': 'str',
        'content': 'str',
        'id': 'str',
        'link': 'str',
        'location_names': 'str',
        'send_alert_type': 'str',
        'sub_task_case_id': 'str',
        'sub_task_case_start_time': 'datetime',
        'sub_task_id': 'str',
        'sub_task_start_time': 'datetime',
        'task_id': 'str',
        'task_name': 'str',
        'test_case_id': 'str',
        'test_case_name': 'str',
        'test_suite_type': 'int'
    }

    attribute_map = {
        'alert_channels': 'alert_channels',
        'alert_groups': 'alert_groups',
        'alert_level': 'alert_level',
        'alert_num': 'alert_num',
        'alert_time': 'alert_time',
        'alert_type': 'alert_type',
        'content': 'content',
        'id': 'id',
        'link': 'link',
        'location_names': 'location_names',
        'send_alert_type': 'send_alert_type',
        'sub_task_case_id': 'sub_task_case_id',
        'sub_task_case_start_time': 'sub_task_case_start_time',
        'sub_task_id': 'sub_task_id',
        'sub_task_start_time': 'sub_task_start_time',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'test_case_id': 'test_case_id',
        'test_case_name': 'test_case_name',
        'test_suite_type': 'test_suite_type'
    }

    def __init__(self, alert_channels=None, alert_groups=None, alert_level=None, alert_num=None, alert_time=None, alert_type=None, content=None, id=None, link=None, location_names=None, send_alert_type=None, sub_task_case_id=None, sub_task_case_start_time=None, sub_task_id=None, sub_task_start_time=None, task_id=None, task_name=None, test_case_id=None, test_case_name=None, test_suite_type=None):
        r"""MsgInfoVo

        The model defined in huaweicloud sdk

        :param alert_channels: 告警渠道
        :type alert_channels: str
        :param alert_groups: 告警分组
        :type alert_groups: str
        :param alert_level: 告警级别
        :type alert_level: int
        :param alert_num: 总告警次数
        :type alert_num: int
        :param alert_time: 告警时间
        :type alert_time: datetime
        :param alert_type: 告警类型
        :type alert_type: str
        :param content: 告警内容
        :type content: str
        :param id: MsgInfo的id
        :type id: str
        :param link: 链接
        :type link: str
        :param location_names: 执行机区域
        :type location_names: str
        :param send_alert_type: 发送告警类型
        :type send_alert_type: str
        :param sub_task_case_id: 子任务用例id
        :type sub_task_case_id: str
        :param sub_task_case_start_time: 子任务用例开始时间
        :type sub_task_case_start_time: datetime
        :param sub_task_id: 子任务id
        :type sub_task_id: str
        :param sub_task_start_time: 子任务开始时间
        :type sub_task_start_time: datetime
        :param task_id: 任务id
        :type task_id: str
        :param task_name: 任务名
        :type task_name: str
        :param test_case_id: 用例id
        :type test_case_id: str
        :param test_case_name: 用例名称
        :type test_case_name: str
        :param test_suite_type: 测试套类型
        :type test_suite_type: int
        """
        
        

        self._alert_channels = None
        self._alert_groups = None
        self._alert_level = None
        self._alert_num = None
        self._alert_time = None
        self._alert_type = None
        self._content = None
        self._id = None
        self._link = None
        self._location_names = None
        self._send_alert_type = None
        self._sub_task_case_id = None
        self._sub_task_case_start_time = None
        self._sub_task_id = None
        self._sub_task_start_time = None
        self._task_id = None
        self._task_name = None
        self._test_case_id = None
        self._test_case_name = None
        self._test_suite_type = None
        self.discriminator = None

        if alert_channels is not None:
            self.alert_channels = alert_channels
        if alert_groups is not None:
            self.alert_groups = alert_groups
        if alert_level is not None:
            self.alert_level = alert_level
        if alert_num is not None:
            self.alert_num = alert_num
        if alert_time is not None:
            self.alert_time = alert_time
        if alert_type is not None:
            self.alert_type = alert_type
        if content is not None:
            self.content = content
        if id is not None:
            self.id = id
        if link is not None:
            self.link = link
        if location_names is not None:
            self.location_names = location_names
        if send_alert_type is not None:
            self.send_alert_type = send_alert_type
        if sub_task_case_id is not None:
            self.sub_task_case_id = sub_task_case_id
        if sub_task_case_start_time is not None:
            self.sub_task_case_start_time = sub_task_case_start_time
        if sub_task_id is not None:
            self.sub_task_id = sub_task_id
        if sub_task_start_time is not None:
            self.sub_task_start_time = sub_task_start_time
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if test_case_id is not None:
            self.test_case_id = test_case_id
        if test_case_name is not None:
            self.test_case_name = test_case_name
        if test_suite_type is not None:
            self.test_suite_type = test_suite_type

    @property
    def alert_channels(self):
        r"""Gets the alert_channels of this MsgInfoVo.

        告警渠道

        :return: The alert_channels of this MsgInfoVo.
        :rtype: str
        """
        return self._alert_channels

    @alert_channels.setter
    def alert_channels(self, alert_channels):
        r"""Sets the alert_channels of this MsgInfoVo.

        告警渠道

        :param alert_channels: The alert_channels of this MsgInfoVo.
        :type alert_channels: str
        """
        self._alert_channels = alert_channels

    @property
    def alert_groups(self):
        r"""Gets the alert_groups of this MsgInfoVo.

        告警分组

        :return: The alert_groups of this MsgInfoVo.
        :rtype: str
        """
        return self._alert_groups

    @alert_groups.setter
    def alert_groups(self, alert_groups):
        r"""Sets the alert_groups of this MsgInfoVo.

        告警分组

        :param alert_groups: The alert_groups of this MsgInfoVo.
        :type alert_groups: str
        """
        self._alert_groups = alert_groups

    @property
    def alert_level(self):
        r"""Gets the alert_level of this MsgInfoVo.

        告警级别

        :return: The alert_level of this MsgInfoVo.
        :rtype: int
        """
        return self._alert_level

    @alert_level.setter
    def alert_level(self, alert_level):
        r"""Sets the alert_level of this MsgInfoVo.

        告警级别

        :param alert_level: The alert_level of this MsgInfoVo.
        :type alert_level: int
        """
        self._alert_level = alert_level

    @property
    def alert_num(self):
        r"""Gets the alert_num of this MsgInfoVo.

        总告警次数

        :return: The alert_num of this MsgInfoVo.
        :rtype: int
        """
        return self._alert_num

    @alert_num.setter
    def alert_num(self, alert_num):
        r"""Sets the alert_num of this MsgInfoVo.

        总告警次数

        :param alert_num: The alert_num of this MsgInfoVo.
        :type alert_num: int
        """
        self._alert_num = alert_num

    @property
    def alert_time(self):
        r"""Gets the alert_time of this MsgInfoVo.

        告警时间

        :return: The alert_time of this MsgInfoVo.
        :rtype: datetime
        """
        return self._alert_time

    @alert_time.setter
    def alert_time(self, alert_time):
        r"""Sets the alert_time of this MsgInfoVo.

        告警时间

        :param alert_time: The alert_time of this MsgInfoVo.
        :type alert_time: datetime
        """
        self._alert_time = alert_time

    @property
    def alert_type(self):
        r"""Gets the alert_type of this MsgInfoVo.

        告警类型

        :return: The alert_type of this MsgInfoVo.
        :rtype: str
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        r"""Sets the alert_type of this MsgInfoVo.

        告警类型

        :param alert_type: The alert_type of this MsgInfoVo.
        :type alert_type: str
        """
        self._alert_type = alert_type

    @property
    def content(self):
        r"""Gets the content of this MsgInfoVo.

        告警内容

        :return: The content of this MsgInfoVo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this MsgInfoVo.

        告警内容

        :param content: The content of this MsgInfoVo.
        :type content: str
        """
        self._content = content

    @property
    def id(self):
        r"""Gets the id of this MsgInfoVo.

        MsgInfo的id

        :return: The id of this MsgInfoVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MsgInfoVo.

        MsgInfo的id

        :param id: The id of this MsgInfoVo.
        :type id: str
        """
        self._id = id

    @property
    def link(self):
        r"""Gets the link of this MsgInfoVo.

        链接

        :return: The link of this MsgInfoVo.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this MsgInfoVo.

        链接

        :param link: The link of this MsgInfoVo.
        :type link: str
        """
        self._link = link

    @property
    def location_names(self):
        r"""Gets the location_names of this MsgInfoVo.

        执行机区域

        :return: The location_names of this MsgInfoVo.
        :rtype: str
        """
        return self._location_names

    @location_names.setter
    def location_names(self, location_names):
        r"""Sets the location_names of this MsgInfoVo.

        执行机区域

        :param location_names: The location_names of this MsgInfoVo.
        :type location_names: str
        """
        self._location_names = location_names

    @property
    def send_alert_type(self):
        r"""Gets the send_alert_type of this MsgInfoVo.

        发送告警类型

        :return: The send_alert_type of this MsgInfoVo.
        :rtype: str
        """
        return self._send_alert_type

    @send_alert_type.setter
    def send_alert_type(self, send_alert_type):
        r"""Sets the send_alert_type of this MsgInfoVo.

        发送告警类型

        :param send_alert_type: The send_alert_type of this MsgInfoVo.
        :type send_alert_type: str
        """
        self._send_alert_type = send_alert_type

    @property
    def sub_task_case_id(self):
        r"""Gets the sub_task_case_id of this MsgInfoVo.

        子任务用例id

        :return: The sub_task_case_id of this MsgInfoVo.
        :rtype: str
        """
        return self._sub_task_case_id

    @sub_task_case_id.setter
    def sub_task_case_id(self, sub_task_case_id):
        r"""Sets the sub_task_case_id of this MsgInfoVo.

        子任务用例id

        :param sub_task_case_id: The sub_task_case_id of this MsgInfoVo.
        :type sub_task_case_id: str
        """
        self._sub_task_case_id = sub_task_case_id

    @property
    def sub_task_case_start_time(self):
        r"""Gets the sub_task_case_start_time of this MsgInfoVo.

        子任务用例开始时间

        :return: The sub_task_case_start_time of this MsgInfoVo.
        :rtype: datetime
        """
        return self._sub_task_case_start_time

    @sub_task_case_start_time.setter
    def sub_task_case_start_time(self, sub_task_case_start_time):
        r"""Sets the sub_task_case_start_time of this MsgInfoVo.

        子任务用例开始时间

        :param sub_task_case_start_time: The sub_task_case_start_time of this MsgInfoVo.
        :type sub_task_case_start_time: datetime
        """
        self._sub_task_case_start_time = sub_task_case_start_time

    @property
    def sub_task_id(self):
        r"""Gets the sub_task_id of this MsgInfoVo.

        子任务id

        :return: The sub_task_id of this MsgInfoVo.
        :rtype: str
        """
        return self._sub_task_id

    @sub_task_id.setter
    def sub_task_id(self, sub_task_id):
        r"""Sets the sub_task_id of this MsgInfoVo.

        子任务id

        :param sub_task_id: The sub_task_id of this MsgInfoVo.
        :type sub_task_id: str
        """
        self._sub_task_id = sub_task_id

    @property
    def sub_task_start_time(self):
        r"""Gets the sub_task_start_time of this MsgInfoVo.

        子任务开始时间

        :return: The sub_task_start_time of this MsgInfoVo.
        :rtype: datetime
        """
        return self._sub_task_start_time

    @sub_task_start_time.setter
    def sub_task_start_time(self, sub_task_start_time):
        r"""Sets the sub_task_start_time of this MsgInfoVo.

        子任务开始时间

        :param sub_task_start_time: The sub_task_start_time of this MsgInfoVo.
        :type sub_task_start_time: datetime
        """
        self._sub_task_start_time = sub_task_start_time

    @property
    def task_id(self):
        r"""Gets the task_id of this MsgInfoVo.

        任务id

        :return: The task_id of this MsgInfoVo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this MsgInfoVo.

        任务id

        :param task_id: The task_id of this MsgInfoVo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this MsgInfoVo.

        任务名

        :return: The task_name of this MsgInfoVo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this MsgInfoVo.

        任务名

        :param task_name: The task_name of this MsgInfoVo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def test_case_id(self):
        r"""Gets the test_case_id of this MsgInfoVo.

        用例id

        :return: The test_case_id of this MsgInfoVo.
        :rtype: str
        """
        return self._test_case_id

    @test_case_id.setter
    def test_case_id(self, test_case_id):
        r"""Sets the test_case_id of this MsgInfoVo.

        用例id

        :param test_case_id: The test_case_id of this MsgInfoVo.
        :type test_case_id: str
        """
        self._test_case_id = test_case_id

    @property
    def test_case_name(self):
        r"""Gets the test_case_name of this MsgInfoVo.

        用例名称

        :return: The test_case_name of this MsgInfoVo.
        :rtype: str
        """
        return self._test_case_name

    @test_case_name.setter
    def test_case_name(self, test_case_name):
        r"""Sets the test_case_name of this MsgInfoVo.

        用例名称

        :param test_case_name: The test_case_name of this MsgInfoVo.
        :type test_case_name: str
        """
        self._test_case_name = test_case_name

    @property
    def test_suite_type(self):
        r"""Gets the test_suite_type of this MsgInfoVo.

        测试套类型

        :return: The test_suite_type of this MsgInfoVo.
        :rtype: int
        """
        return self._test_suite_type

    @test_suite_type.setter
    def test_suite_type(self, test_suite_type):
        r"""Sets the test_suite_type of this MsgInfoVo.

        测试套类型

        :param test_suite_type: The test_suite_type of this MsgInfoVo.
        :type test_suite_type: int
        """
        self._test_suite_type = test_suite_type

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
        if not isinstance(other, MsgInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
