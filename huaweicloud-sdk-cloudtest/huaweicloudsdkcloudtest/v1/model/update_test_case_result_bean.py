# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTestCaseResultBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'testcase_id': 'str',
        'execute_id': 'str',
        'result_id': 'str',
        'end_time': 'int',
        'duration': 'int',
        'description': 'str'
    }

    attribute_map = {
        'testcase_id': 'testcase_id',
        'execute_id': 'execute_id',
        'result_id': 'result_id',
        'end_time': 'end_time',
        'duration': 'duration',
        'description': 'description'
    }

    def __init__(self, testcase_id=None, execute_id=None, result_id=None, end_time=None, duration=None, description=None):
        """UpdateTestCaseResultBean

        The model defined in huaweicloud sdk

        :param testcase_id: 测试用例唯一标识，列表中不允许存在重复的id，固定长度32位字符
        :type testcase_id: str
        :param execute_id: 注册服务执行id，该值不允许重复，不超过32位字符
        :type execute_id: str
        :param result_id: 测试用例结果，（0-成功，1-失败，5-执行中，6-停止）
        :type result_id: str
        :param end_time: 用例结束执行的时间戳，在执行结束时该字段必传
        :type end_time: int
        :param duration: 执行用例持续时长ms，更新状态时改字段必传
        :type duration: int
        :param description: 用于记录该次结果执行的备注信息
        :type description: str
        """
        
        

        self._testcase_id = None
        self._execute_id = None
        self._result_id = None
        self._end_time = None
        self._duration = None
        self._description = None
        self.discriminator = None

        self.testcase_id = testcase_id
        self.execute_id = execute_id
        self.result_id = result_id
        self.end_time = end_time
        if duration is not None:
            self.duration = duration
        if description is not None:
            self.description = description

    @property
    def testcase_id(self):
        """Gets the testcase_id of this UpdateTestCaseResultBean.

        测试用例唯一标识，列表中不允许存在重复的id，固定长度32位字符

        :return: The testcase_id of this UpdateTestCaseResultBean.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        """Sets the testcase_id of this UpdateTestCaseResultBean.

        测试用例唯一标识，列表中不允许存在重复的id，固定长度32位字符

        :param testcase_id: The testcase_id of this UpdateTestCaseResultBean.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def execute_id(self):
        """Gets the execute_id of this UpdateTestCaseResultBean.

        注册服务执行id，该值不允许重复，不超过32位字符

        :return: The execute_id of this UpdateTestCaseResultBean.
        :rtype: str
        """
        return self._execute_id

    @execute_id.setter
    def execute_id(self, execute_id):
        """Sets the execute_id of this UpdateTestCaseResultBean.

        注册服务执行id，该值不允许重复，不超过32位字符

        :param execute_id: The execute_id of this UpdateTestCaseResultBean.
        :type execute_id: str
        """
        self._execute_id = execute_id

    @property
    def result_id(self):
        """Gets the result_id of this UpdateTestCaseResultBean.

        测试用例结果，（0-成功，1-失败，5-执行中，6-停止）

        :return: The result_id of this UpdateTestCaseResultBean.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this UpdateTestCaseResultBean.

        测试用例结果，（0-成功，1-失败，5-执行中，6-停止）

        :param result_id: The result_id of this UpdateTestCaseResultBean.
        :type result_id: str
        """
        self._result_id = result_id

    @property
    def end_time(self):
        """Gets the end_time of this UpdateTestCaseResultBean.

        用例结束执行的时间戳，在执行结束时该字段必传

        :return: The end_time of this UpdateTestCaseResultBean.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this UpdateTestCaseResultBean.

        用例结束执行的时间戳，在执行结束时该字段必传

        :param end_time: The end_time of this UpdateTestCaseResultBean.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def duration(self):
        """Gets the duration of this UpdateTestCaseResultBean.

        执行用例持续时长ms，更新状态时改字段必传

        :return: The duration of this UpdateTestCaseResultBean.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this UpdateTestCaseResultBean.

        执行用例持续时长ms，更新状态时改字段必传

        :param duration: The duration of this UpdateTestCaseResultBean.
        :type duration: int
        """
        self._duration = duration

    @property
    def description(self):
        """Gets the description of this UpdateTestCaseResultBean.

        用于记录该次结果执行的备注信息

        :return: The description of this UpdateTestCaseResultBean.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTestCaseResultBean.

        用于记录该次结果执行的备注信息

        :param description: The description of this UpdateTestCaseResultBean.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateTestCaseResultBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
