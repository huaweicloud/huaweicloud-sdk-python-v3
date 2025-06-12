# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteTaskVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flag': 'bool',
        'uri': 'str',
        'task_result_vo': 'TaskResultVo',
        'update_case_uri_list': 'list[str]',
        'test_case_result_list': 'list[TestResultVo]'
    }

    attribute_map = {
        'flag': 'flag',
        'uri': 'uri',
        'task_result_vo': 'task_result_vo',
        'update_case_uri_list': 'update_case_uri_list',
        'test_case_result_list': 'test_case_result_list'
    }

    def __init__(self, flag=None, uri=None, task_result_vo=None, update_case_uri_list=None, test_case_result_list=None):
        r"""ExecuteTaskVo

        The model defined in huaweicloud sdk

        :param flag: 标志
        :type flag: bool
        :param uri: URI
        :type uri: str
        :param task_result_vo: 
        :type task_result_vo: :class:`huaweicloudsdkcloudtest.v1.TaskResultVo`
        :param update_case_uri_list: 更新用例
        :type update_case_uri_list: list[str]
        :param test_case_result_list: 用例结果列表
        :type test_case_result_list: list[:class:`huaweicloudsdkcloudtest.v1.TestResultVo`]
        """
        
        

        self._flag = None
        self._uri = None
        self._task_result_vo = None
        self._update_case_uri_list = None
        self._test_case_result_list = None
        self.discriminator = None

        if flag is not None:
            self.flag = flag
        if uri is not None:
            self.uri = uri
        if task_result_vo is not None:
            self.task_result_vo = task_result_vo
        if update_case_uri_list is not None:
            self.update_case_uri_list = update_case_uri_list
        if test_case_result_list is not None:
            self.test_case_result_list = test_case_result_list

    @property
    def flag(self):
        r"""Gets the flag of this ExecuteTaskVo.

        标志

        :return: The flag of this ExecuteTaskVo.
        :rtype: bool
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        r"""Sets the flag of this ExecuteTaskVo.

        标志

        :param flag: The flag of this ExecuteTaskVo.
        :type flag: bool
        """
        self._flag = flag

    @property
    def uri(self):
        r"""Gets the uri of this ExecuteTaskVo.

        URI

        :return: The uri of this ExecuteTaskVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this ExecuteTaskVo.

        URI

        :param uri: The uri of this ExecuteTaskVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def task_result_vo(self):
        r"""Gets the task_result_vo of this ExecuteTaskVo.

        :return: The task_result_vo of this ExecuteTaskVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TaskResultVo`
        """
        return self._task_result_vo

    @task_result_vo.setter
    def task_result_vo(self, task_result_vo):
        r"""Sets the task_result_vo of this ExecuteTaskVo.

        :param task_result_vo: The task_result_vo of this ExecuteTaskVo.
        :type task_result_vo: :class:`huaweicloudsdkcloudtest.v1.TaskResultVo`
        """
        self._task_result_vo = task_result_vo

    @property
    def update_case_uri_list(self):
        r"""Gets the update_case_uri_list of this ExecuteTaskVo.

        更新用例

        :return: The update_case_uri_list of this ExecuteTaskVo.
        :rtype: list[str]
        """
        return self._update_case_uri_list

    @update_case_uri_list.setter
    def update_case_uri_list(self, update_case_uri_list):
        r"""Sets the update_case_uri_list of this ExecuteTaskVo.

        更新用例

        :param update_case_uri_list: The update_case_uri_list of this ExecuteTaskVo.
        :type update_case_uri_list: list[str]
        """
        self._update_case_uri_list = update_case_uri_list

    @property
    def test_case_result_list(self):
        r"""Gets the test_case_result_list of this ExecuteTaskVo.

        用例结果列表

        :return: The test_case_result_list of this ExecuteTaskVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestResultVo`]
        """
        return self._test_case_result_list

    @test_case_result_list.setter
    def test_case_result_list(self, test_case_result_list):
        r"""Sets the test_case_result_list of this ExecuteTaskVo.

        用例结果列表

        :param test_case_result_list: The test_case_result_list of this ExecuteTaskVo.
        :type test_case_result_list: list[:class:`huaweicloudsdkcloudtest.v1.TestResultVo`]
        """
        self._test_case_result_list = test_case_result_list

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
        if not isinstance(other, ExecuteTaskVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
