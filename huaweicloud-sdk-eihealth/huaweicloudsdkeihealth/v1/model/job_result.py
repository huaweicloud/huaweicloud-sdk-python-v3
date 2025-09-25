# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'failed_count': 'int',
        'sub_tasks_duration': 'list[float]',
        'num_molecules': 'int',
        'success_count': 'int'
    }

    attribute_map = {
        'total_count': 'total_count',
        'failed_count': 'failed_count',
        'sub_tasks_duration': 'sub_tasks_duration',
        'num_molecules': 'num_molecules',
        'success_count': 'success_count'
    }

    def __init__(self, total_count=None, failed_count=None, sub_tasks_duration=None, num_molecules=None, success_count=None):
        r"""JobResult

        The model defined in huaweicloud sdk

        :param total_count: 输入总数
        :type total_count: int
        :param failed_count: 失败个数
        :type failed_count: int
        :param sub_tasks_duration: 子任务运行时长（秒）。
        :type sub_tasks_duration: list[float]
        :param num_molecules: **参数解释**： 分子聚类任务中的分子总数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type num_molecules: int
        :param success_count: **参数解释**： 聚类成功的分子数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type success_count: int
        """
        
        

        self._total_count = None
        self._failed_count = None
        self._sub_tasks_duration = None
        self._num_molecules = None
        self._success_count = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if failed_count is not None:
            self.failed_count = failed_count
        if sub_tasks_duration is not None:
            self.sub_tasks_duration = sub_tasks_duration
        if num_molecules is not None:
            self.num_molecules = num_molecules
        if success_count is not None:
            self.success_count = success_count

    @property
    def total_count(self):
        r"""Gets the total_count of this JobResult.

        输入总数

        :return: The total_count of this JobResult.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this JobResult.

        输入总数

        :param total_count: The total_count of this JobResult.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def failed_count(self):
        r"""Gets the failed_count of this JobResult.

        失败个数

        :return: The failed_count of this JobResult.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this JobResult.

        失败个数

        :param failed_count: The failed_count of this JobResult.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def sub_tasks_duration(self):
        r"""Gets the sub_tasks_duration of this JobResult.

        子任务运行时长（秒）。

        :return: The sub_tasks_duration of this JobResult.
        :rtype: list[float]
        """
        return self._sub_tasks_duration

    @sub_tasks_duration.setter
    def sub_tasks_duration(self, sub_tasks_duration):
        r"""Sets the sub_tasks_duration of this JobResult.

        子任务运行时长（秒）。

        :param sub_tasks_duration: The sub_tasks_duration of this JobResult.
        :type sub_tasks_duration: list[float]
        """
        self._sub_tasks_duration = sub_tasks_duration

    @property
    def num_molecules(self):
        r"""Gets the num_molecules of this JobResult.

        **参数解释**： 分子聚类任务中的分子总数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The num_molecules of this JobResult.
        :rtype: int
        """
        return self._num_molecules

    @num_molecules.setter
    def num_molecules(self, num_molecules):
        r"""Sets the num_molecules of this JobResult.

        **参数解释**： 分子聚类任务中的分子总数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param num_molecules: The num_molecules of this JobResult.
        :type num_molecules: int
        """
        self._num_molecules = num_molecules

    @property
    def success_count(self):
        r"""Gets the success_count of this JobResult.

        **参数解释**： 聚类成功的分子数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The success_count of this JobResult.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this JobResult.

        **参数解释**： 聚类成功的分子数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param success_count: The success_count of this JobResult.
        :type success_count: int
        """
        self._success_count = success_count

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
        if not isinstance(other, JobResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
