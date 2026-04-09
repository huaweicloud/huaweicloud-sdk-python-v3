# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddTestCaseResultInTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'AddTestCaseResultInfo',
        'task_uri': 'str',
        'task_result_uri': 'str',
        'test_case_uris': 'list[str]',
        'is_asyn': 'bool'
    }

    attribute_map = {
        'result': 'result',
        'task_uri': 'task_uri',
        'task_result_uri': 'task_result_uri',
        'test_case_uris': 'test_case_uris',
        'is_asyn': 'isAsyn'
    }

    def __init__(self, result=None, task_uri=None, task_result_uri=None, test_case_uris=None, is_asyn=None):
        r"""BatchAddTestCaseResultInTaskInfo

        The model defined in huaweicloud sdk

        :param result: 
        :type result: :class:`huaweicloudsdkcloudtest.v1.AddTestCaseResultInfo`
        :param task_uri: 任务uri
        :type task_uri: str
        :param task_result_uri: 测试套结果URI
        :type task_result_uri: str
        :param test_case_uris: 用例uri列表
        :type test_case_uris: list[str]
        :param is_asyn: 是否异步执行
        :type is_asyn: bool
        """
        
        

        self._result = None
        self._task_uri = None
        self._task_result_uri = None
        self._test_case_uris = None
        self._is_asyn = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if task_uri is not None:
            self.task_uri = task_uri
        if task_result_uri is not None:
            self.task_result_uri = task_result_uri
        if test_case_uris is not None:
            self.test_case_uris = test_case_uris
        if is_asyn is not None:
            self.is_asyn = is_asyn

    @property
    def result(self):
        r"""Gets the result of this BatchAddTestCaseResultInTaskInfo.

        :return: The result of this BatchAddTestCaseResultInTaskInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AddTestCaseResultInfo`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this BatchAddTestCaseResultInTaskInfo.

        :param result: The result of this BatchAddTestCaseResultInTaskInfo.
        :type result: :class:`huaweicloudsdkcloudtest.v1.AddTestCaseResultInfo`
        """
        self._result = result

    @property
    def task_uri(self):
        r"""Gets the task_uri of this BatchAddTestCaseResultInTaskInfo.

        任务uri

        :return: The task_uri of this BatchAddTestCaseResultInTaskInfo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this BatchAddTestCaseResultInTaskInfo.

        任务uri

        :param task_uri: The task_uri of this BatchAddTestCaseResultInTaskInfo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def task_result_uri(self):
        r"""Gets the task_result_uri of this BatchAddTestCaseResultInTaskInfo.

        测试套结果URI

        :return: The task_result_uri of this BatchAddTestCaseResultInTaskInfo.
        :rtype: str
        """
        return self._task_result_uri

    @task_result_uri.setter
    def task_result_uri(self, task_result_uri):
        r"""Sets the task_result_uri of this BatchAddTestCaseResultInTaskInfo.

        测试套结果URI

        :param task_result_uri: The task_result_uri of this BatchAddTestCaseResultInTaskInfo.
        :type task_result_uri: str
        """
        self._task_result_uri = task_result_uri

    @property
    def test_case_uris(self):
        r"""Gets the test_case_uris of this BatchAddTestCaseResultInTaskInfo.

        用例uri列表

        :return: The test_case_uris of this BatchAddTestCaseResultInTaskInfo.
        :rtype: list[str]
        """
        return self._test_case_uris

    @test_case_uris.setter
    def test_case_uris(self, test_case_uris):
        r"""Sets the test_case_uris of this BatchAddTestCaseResultInTaskInfo.

        用例uri列表

        :param test_case_uris: The test_case_uris of this BatchAddTestCaseResultInTaskInfo.
        :type test_case_uris: list[str]
        """
        self._test_case_uris = test_case_uris

    @property
    def is_asyn(self):
        r"""Gets the is_asyn of this BatchAddTestCaseResultInTaskInfo.

        是否异步执行

        :return: The is_asyn of this BatchAddTestCaseResultInTaskInfo.
        :rtype: bool
        """
        return self._is_asyn

    @is_asyn.setter
    def is_asyn(self, is_asyn):
        r"""Sets the is_asyn of this BatchAddTestCaseResultInTaskInfo.

        是否异步执行

        :param is_asyn: The is_asyn of this BatchAddTestCaseResultInTaskInfo.
        :type is_asyn: bool
        """
        self._is_asyn = is_asyn

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchAddTestCaseResultInTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
