# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskResultDetailVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner': 'str',
        'case_result_statics': 'object',
        'task_result': 'TaskResultVo',
        'test_result_list': 'list[TaskResultVo]'
    }

    attribute_map = {
        'owner': 'owner',
        'case_result_statics': 'case_result_statics',
        'task_result': 'task_result',
        'test_result_list': 'test_result_list'
    }

    def __init__(self, owner=None, case_result_statics=None, task_result=None, test_result_list=None):
        r"""TaskResultDetailVo

        The model defined in huaweicloud sdk

        :param owner: 处理人名称
        :type owner: str
        :param case_result_statics: 用例结果统计信息
        :type case_result_statics: object
        :param task_result: 
        :type task_result: :class:`huaweicloudsdkcloudtest.v1.TaskResultVo`
        :param test_result_list: 实际的数据类型：单个对象，集合 或 NULL
        :type test_result_list: list[:class:`huaweicloudsdkcloudtest.v1.TaskResultVo`]
        """
        
        

        self._owner = None
        self._case_result_statics = None
        self._task_result = None
        self._test_result_list = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if case_result_statics is not None:
            self.case_result_statics = case_result_statics
        if task_result is not None:
            self.task_result = task_result
        if test_result_list is not None:
            self.test_result_list = test_result_list

    @property
    def owner(self):
        r"""Gets the owner of this TaskResultDetailVo.

        处理人名称

        :return: The owner of this TaskResultDetailVo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TaskResultDetailVo.

        处理人名称

        :param owner: The owner of this TaskResultDetailVo.
        :type owner: str
        """
        self._owner = owner

    @property
    def case_result_statics(self):
        r"""Gets the case_result_statics of this TaskResultDetailVo.

        用例结果统计信息

        :return: The case_result_statics of this TaskResultDetailVo.
        :rtype: object
        """
        return self._case_result_statics

    @case_result_statics.setter
    def case_result_statics(self, case_result_statics):
        r"""Sets the case_result_statics of this TaskResultDetailVo.

        用例结果统计信息

        :param case_result_statics: The case_result_statics of this TaskResultDetailVo.
        :type case_result_statics: object
        """
        self._case_result_statics = case_result_statics

    @property
    def task_result(self):
        r"""Gets the task_result of this TaskResultDetailVo.

        :return: The task_result of this TaskResultDetailVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TaskResultVo`
        """
        return self._task_result

    @task_result.setter
    def task_result(self, task_result):
        r"""Sets the task_result of this TaskResultDetailVo.

        :param task_result: The task_result of this TaskResultDetailVo.
        :type task_result: :class:`huaweicloudsdkcloudtest.v1.TaskResultVo`
        """
        self._task_result = task_result

    @property
    def test_result_list(self):
        r"""Gets the test_result_list of this TaskResultDetailVo.

        实际的数据类型：单个对象，集合 或 NULL

        :return: The test_result_list of this TaskResultDetailVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TaskResultVo`]
        """
        return self._test_result_list

    @test_result_list.setter
    def test_result_list(self, test_result_list):
        r"""Sets the test_result_list of this TaskResultDetailVo.

        实际的数据类型：单个对象，集合 或 NULL

        :param test_result_list: The test_result_list of this TaskResultDetailVo.
        :type test_result_list: list[:class:`huaweicloudsdkcloudtest.v1.TaskResultVo`]
        """
        self._test_result_list = test_result_list

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
        if not isinstance(other, TaskResultDetailVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
