# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTaskCaseSuccessLineDetailVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'date': 'int',
        'pass_rate': 'float',
        'task_id': 'str',
        'task_name': 'str'
    }

    attribute_map = {
        'date': 'date',
        'pass_rate': 'pass_rate',
        'task_id': 'task_id',
        'task_name': 'task_name'
    }

    def __init__(self, date=None, pass_rate=None, task_id=None, task_name=None):
        r"""SubTaskCaseSuccessLineDetailVo

        The model defined in huaweicloud sdk

        :param date: 统计时间
        :type date: int
        :param pass_rate: 成功率
        :type pass_rate: float
        :param task_id: 任务id
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        """
        
        

        self._date = None
        self._pass_rate = None
        self._task_id = None
        self._task_name = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if pass_rate is not None:
            self.pass_rate = pass_rate
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name

    @property
    def date(self):
        r"""Gets the date of this SubTaskCaseSuccessLineDetailVo.

        统计时间

        :return: The date of this SubTaskCaseSuccessLineDetailVo.
        :rtype: int
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this SubTaskCaseSuccessLineDetailVo.

        统计时间

        :param date: The date of this SubTaskCaseSuccessLineDetailVo.
        :type date: int
        """
        self._date = date

    @property
    def pass_rate(self):
        r"""Gets the pass_rate of this SubTaskCaseSuccessLineDetailVo.

        成功率

        :return: The pass_rate of this SubTaskCaseSuccessLineDetailVo.
        :rtype: float
        """
        return self._pass_rate

    @pass_rate.setter
    def pass_rate(self, pass_rate):
        r"""Sets the pass_rate of this SubTaskCaseSuccessLineDetailVo.

        成功率

        :param pass_rate: The pass_rate of this SubTaskCaseSuccessLineDetailVo.
        :type pass_rate: float
        """
        self._pass_rate = pass_rate

    @property
    def task_id(self):
        r"""Gets the task_id of this SubTaskCaseSuccessLineDetailVo.

        任务id

        :return: The task_id of this SubTaskCaseSuccessLineDetailVo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SubTaskCaseSuccessLineDetailVo.

        任务id

        :param task_id: The task_id of this SubTaskCaseSuccessLineDetailVo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this SubTaskCaseSuccessLineDetailVo.

        任务名称

        :return: The task_name of this SubTaskCaseSuccessLineDetailVo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this SubTaskCaseSuccessLineDetailVo.

        任务名称

        :param task_name: The task_name of this SubTaskCaseSuccessLineDetailVo.
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
        if not isinstance(other, SubTaskCaseSuccessLineDetailVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
