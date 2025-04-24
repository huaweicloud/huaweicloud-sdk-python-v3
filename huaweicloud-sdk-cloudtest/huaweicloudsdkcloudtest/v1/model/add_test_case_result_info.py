# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddTestCaseResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'name': 'str',
        'description': 'str',
        'result': 'str',
        'status': 'str',
        'preparation': 'str',
        'steps': 'list[TestCaseStepResultInfo]',
        'release_dev': 'str',
        'task_uri': 'str',
        'task_result_uri': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'description': 'description',
        'result': 'result',
        'status': 'status',
        'preparation': 'preparation',
        'steps': 'steps',
        'release_dev': 'release_dev',
        'task_uri': 'task_uri',
        'task_result_uri': 'task_result_uri'
    }

    def __init__(self, uri=None, name=None, description=None, result=None, status=None, preparation=None, steps=None, release_dev=None, task_uri=None, task_result_uri=None):
        r"""AddTestCaseResultInfo

        The model defined in huaweicloud sdk

        :param uri: 主键
        :type uri: str
        :param name: 结果名字
        :type name: str
        :param description: 描述
        :type description: str
        :param result: 用例结果
        :type result: str
        :param status: 任务状态
        :type status: str
        :param preparation: 前置条件
        :type preparation: str
        :param steps: 用例步骤结果信息
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseStepResultInfo`]
        :param release_dev: 版本号
        :type release_dev: str
        :param task_uri: 任务URI
        :type task_uri: str
        :param task_result_uri: 测试套结果URI
        :type task_result_uri: str
        """
        
        

        self._uri = None
        self._name = None
        self._description = None
        self._result = None
        self._status = None
        self._preparation = None
        self._steps = None
        self._release_dev = None
        self._task_uri = None
        self._task_result_uri = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if result is not None:
            self.result = result
        if status is not None:
            self.status = status
        if preparation is not None:
            self.preparation = preparation
        if steps is not None:
            self.steps = steps
        if release_dev is not None:
            self.release_dev = release_dev
        if task_uri is not None:
            self.task_uri = task_uri
        if task_result_uri is not None:
            self.task_result_uri = task_result_uri

    @property
    def uri(self):
        r"""Gets the uri of this AddTestCaseResultInfo.

        主键

        :return: The uri of this AddTestCaseResultInfo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this AddTestCaseResultInfo.

        主键

        :param uri: The uri of this AddTestCaseResultInfo.
        :type uri: str
        """
        self._uri = uri

    @property
    def name(self):
        r"""Gets the name of this AddTestCaseResultInfo.

        结果名字

        :return: The name of this AddTestCaseResultInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddTestCaseResultInfo.

        结果名字

        :param name: The name of this AddTestCaseResultInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AddTestCaseResultInfo.

        描述

        :return: The description of this AddTestCaseResultInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddTestCaseResultInfo.

        描述

        :param description: The description of this AddTestCaseResultInfo.
        :type description: str
        """
        self._description = description

    @property
    def result(self):
        r"""Gets the result of this AddTestCaseResultInfo.

        用例结果

        :return: The result of this AddTestCaseResultInfo.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this AddTestCaseResultInfo.

        用例结果

        :param result: The result of this AddTestCaseResultInfo.
        :type result: str
        """
        self._result = result

    @property
    def status(self):
        r"""Gets the status of this AddTestCaseResultInfo.

        任务状态

        :return: The status of this AddTestCaseResultInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AddTestCaseResultInfo.

        任务状态

        :param status: The status of this AddTestCaseResultInfo.
        :type status: str
        """
        self._status = status

    @property
    def preparation(self):
        r"""Gets the preparation of this AddTestCaseResultInfo.

        前置条件

        :return: The preparation of this AddTestCaseResultInfo.
        :rtype: str
        """
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        r"""Sets the preparation of this AddTestCaseResultInfo.

        前置条件

        :param preparation: The preparation of this AddTestCaseResultInfo.
        :type preparation: str
        """
        self._preparation = preparation

    @property
    def steps(self):
        r"""Gets the steps of this AddTestCaseResultInfo.

        用例步骤结果信息

        :return: The steps of this AddTestCaseResultInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseStepResultInfo`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this AddTestCaseResultInfo.

        用例步骤结果信息

        :param steps: The steps of this AddTestCaseResultInfo.
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseStepResultInfo`]
        """
        self._steps = steps

    @property
    def release_dev(self):
        r"""Gets the release_dev of this AddTestCaseResultInfo.

        版本号

        :return: The release_dev of this AddTestCaseResultInfo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this AddTestCaseResultInfo.

        版本号

        :param release_dev: The release_dev of this AddTestCaseResultInfo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def task_uri(self):
        r"""Gets the task_uri of this AddTestCaseResultInfo.

        任务URI

        :return: The task_uri of this AddTestCaseResultInfo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this AddTestCaseResultInfo.

        任务URI

        :param task_uri: The task_uri of this AddTestCaseResultInfo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def task_result_uri(self):
        r"""Gets the task_result_uri of this AddTestCaseResultInfo.

        测试套结果URI

        :return: The task_result_uri of this AddTestCaseResultInfo.
        :rtype: str
        """
        return self._task_result_uri

    @task_result_uri.setter
    def task_result_uri(self, task_result_uri):
        r"""Sets the task_result_uri of this AddTestCaseResultInfo.

        测试套结果URI

        :param task_result_uri: The task_result_uri of this AddTestCaseResultInfo.
        :type task_result_uri: str
        """
        self._task_result_uri = task_result_uri

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
        if not isinstance(other, AddTestCaseResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
