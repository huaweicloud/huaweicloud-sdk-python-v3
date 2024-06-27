# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTaskCaseSuccessLineVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'detail': 'list[SubTaskCaseSuccessLineDetailVo]',
        'task_id': 'str',
        'task_name': 'str'
    }

    attribute_map = {
        'detail': 'detail',
        'task_id': 'task_id',
        'task_name': 'task_name'
    }

    def __init__(self, detail=None, task_id=None, task_name=None):
        """SubTaskCaseSuccessLineVo

        The model defined in huaweicloud sdk

        :param detail: 用例成功率统计信息
        :type detail: list[:class:`huaweicloudsdkcloudtest.v1.SubTaskCaseSuccessLineDetailVo`]
        :param task_id: 任务id
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        """
        
        

        self._detail = None
        self._task_id = None
        self._task_name = None
        self.discriminator = None

        if detail is not None:
            self.detail = detail
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name

    @property
    def detail(self):
        """Gets the detail of this SubTaskCaseSuccessLineVo.

        用例成功率统计信息

        :return: The detail of this SubTaskCaseSuccessLineVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.SubTaskCaseSuccessLineDetailVo`]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this SubTaskCaseSuccessLineVo.

        用例成功率统计信息

        :param detail: The detail of this SubTaskCaseSuccessLineVo.
        :type detail: list[:class:`huaweicloudsdkcloudtest.v1.SubTaskCaseSuccessLineDetailVo`]
        """
        self._detail = detail

    @property
    def task_id(self):
        """Gets the task_id of this SubTaskCaseSuccessLineVo.

        任务id

        :return: The task_id of this SubTaskCaseSuccessLineVo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this SubTaskCaseSuccessLineVo.

        任务id

        :param task_id: The task_id of this SubTaskCaseSuccessLineVo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this SubTaskCaseSuccessLineVo.

        任务名称

        :return: The task_name of this SubTaskCaseSuccessLineVo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this SubTaskCaseSuccessLineVo.

        任务名称

        :param task_name: The task_name of this SubTaskCaseSuccessLineVo.
        :type task_name: str
        """
        self._task_name = task_name

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
        if not isinstance(other, SubTaskCaseSuccessLineVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
