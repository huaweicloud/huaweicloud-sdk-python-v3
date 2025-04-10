# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelateTaskTestCasesVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'test_case_num': 'str',
        'test_case_name': 'str',
        'test_case_uri': 'str',
        'task_uri': 'str',
        'task_name': 'str',
        'task_num': 'str',
        'task_creator': 'str'
    }

    attribute_map = {
        'test_case_num': 'test_case_num',
        'test_case_name': 'test_case_name',
        'test_case_uri': 'test_case_uri',
        'task_uri': 'task_uri',
        'task_name': 'task_name',
        'task_num': 'task_num',
        'task_creator': 'task_creator'
    }

    def __init__(self, test_case_num=None, test_case_name=None, test_case_uri=None, task_uri=None, task_name=None, task_num=None, task_creator=None):
        r"""RelateTaskTestCasesVo

        The model defined in huaweicloud sdk

        :param test_case_num: 用例编号
        :type test_case_num: str
        :param test_case_name: 用例名
        :type test_case_name: str
        :param test_case_uri: 用例uri
        :type test_case_uri: str
        :param task_uri: 任务uri
        :type task_uri: str
        :param task_name: 任务名
        :type task_name: str
        :param task_num: 任务编号
        :type task_num: str
        :param task_creator: 任务创建人
        :type task_creator: str
        """
        
        

        self._test_case_num = None
        self._test_case_name = None
        self._test_case_uri = None
        self._task_uri = None
        self._task_name = None
        self._task_num = None
        self._task_creator = None
        self.discriminator = None

        if test_case_num is not None:
            self.test_case_num = test_case_num
        if test_case_name is not None:
            self.test_case_name = test_case_name
        if test_case_uri is not None:
            self.test_case_uri = test_case_uri
        if task_uri is not None:
            self.task_uri = task_uri
        if task_name is not None:
            self.task_name = task_name
        if task_num is not None:
            self.task_num = task_num
        if task_creator is not None:
            self.task_creator = task_creator

    @property
    def test_case_num(self):
        r"""Gets the test_case_num of this RelateTaskTestCasesVo.

        用例编号

        :return: The test_case_num of this RelateTaskTestCasesVo.
        :rtype: str
        """
        return self._test_case_num

    @test_case_num.setter
    def test_case_num(self, test_case_num):
        r"""Sets the test_case_num of this RelateTaskTestCasesVo.

        用例编号

        :param test_case_num: The test_case_num of this RelateTaskTestCasesVo.
        :type test_case_num: str
        """
        self._test_case_num = test_case_num

    @property
    def test_case_name(self):
        r"""Gets the test_case_name of this RelateTaskTestCasesVo.

        用例名

        :return: The test_case_name of this RelateTaskTestCasesVo.
        :rtype: str
        """
        return self._test_case_name

    @test_case_name.setter
    def test_case_name(self, test_case_name):
        r"""Sets the test_case_name of this RelateTaskTestCasesVo.

        用例名

        :param test_case_name: The test_case_name of this RelateTaskTestCasesVo.
        :type test_case_name: str
        """
        self._test_case_name = test_case_name

    @property
    def test_case_uri(self):
        r"""Gets the test_case_uri of this RelateTaskTestCasesVo.

        用例uri

        :return: The test_case_uri of this RelateTaskTestCasesVo.
        :rtype: str
        """
        return self._test_case_uri

    @test_case_uri.setter
    def test_case_uri(self, test_case_uri):
        r"""Sets the test_case_uri of this RelateTaskTestCasesVo.

        用例uri

        :param test_case_uri: The test_case_uri of this RelateTaskTestCasesVo.
        :type test_case_uri: str
        """
        self._test_case_uri = test_case_uri

    @property
    def task_uri(self):
        r"""Gets the task_uri of this RelateTaskTestCasesVo.

        任务uri

        :return: The task_uri of this RelateTaskTestCasesVo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this RelateTaskTestCasesVo.

        任务uri

        :param task_uri: The task_uri of this RelateTaskTestCasesVo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def task_name(self):
        r"""Gets the task_name of this RelateTaskTestCasesVo.

        任务名

        :return: The task_name of this RelateTaskTestCasesVo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this RelateTaskTestCasesVo.

        任务名

        :param task_name: The task_name of this RelateTaskTestCasesVo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_num(self):
        r"""Gets the task_num of this RelateTaskTestCasesVo.

        任务编号

        :return: The task_num of this RelateTaskTestCasesVo.
        :rtype: str
        """
        return self._task_num

    @task_num.setter
    def task_num(self, task_num):
        r"""Sets the task_num of this RelateTaskTestCasesVo.

        任务编号

        :param task_num: The task_num of this RelateTaskTestCasesVo.
        :type task_num: str
        """
        self._task_num = task_num

    @property
    def task_creator(self):
        r"""Gets the task_creator of this RelateTaskTestCasesVo.

        任务创建人

        :return: The task_creator of this RelateTaskTestCasesVo.
        :rtype: str
        """
        return self._task_creator

    @task_creator.setter
    def task_creator(self, task_creator):
        r"""Sets the task_creator of this RelateTaskTestCasesVo.

        任务创建人

        :param task_creator: The task_creator of this RelateTaskTestCasesVo.
        :type task_creator: str
        """
        self._task_creator = task_creator

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
        if not isinstance(other, RelateTaskTestCasesVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
