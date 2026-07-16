# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_type': 'str',
        'total_task_count': 'int',
        'free_task_quota_limit': 'int'
    }

    attribute_map = {
        'task_type': 'task_type',
        'total_task_count': 'total_task_count',
        'free_task_quota_limit': 'free_task_quota_limit'
    }

    def __init__(self, task_type=None, total_task_count=None, free_task_quota_limit=None):
        r"""QuotaItem

        The model defined in huaweicloud sdk

        :param task_type: **参数解释：** 任务的类型分类。 **约束限制：** 长度为0到10000个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type task_type: str
        :param total_task_count: **参数解释：** 当前已消耗的任务总数。 **约束限制：** 0到int64 最大值。 **取值范围：** 0到9223372036854775807。 **默认取值：** 0。 
        :type total_task_count: int
        :param free_task_quota_limit: **参数解释：** 免费任务的配额上限。 **约束限制：** 0到int64 最大值。 **取值范围：** 0到9223372036854775807。 **默认取值：** 0。 
        :type free_task_quota_limit: int
        """
        
        

        self._task_type = None
        self._total_task_count = None
        self._free_task_quota_limit = None
        self.discriminator = None

        self.task_type = task_type
        self.total_task_count = total_task_count
        self.free_task_quota_limit = free_task_quota_limit

    @property
    def task_type(self):
        r"""Gets the task_type of this QuotaItem.

        **参数解释：** 任务的类型分类。 **约束限制：** 长度为0到10000个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The task_type of this QuotaItem.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this QuotaItem.

        **参数解释：** 任务的类型分类。 **约束限制：** 长度为0到10000个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param task_type: The task_type of this QuotaItem.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def total_task_count(self):
        r"""Gets the total_task_count of this QuotaItem.

        **参数解释：** 当前已消耗的任务总数。 **约束限制：** 0到int64 最大值。 **取值范围：** 0到9223372036854775807。 **默认取值：** 0。 

        :return: The total_task_count of this QuotaItem.
        :rtype: int
        """
        return self._total_task_count

    @total_task_count.setter
    def total_task_count(self, total_task_count):
        r"""Sets the total_task_count of this QuotaItem.

        **参数解释：** 当前已消耗的任务总数。 **约束限制：** 0到int64 最大值。 **取值范围：** 0到9223372036854775807。 **默认取值：** 0。 

        :param total_task_count: The total_task_count of this QuotaItem.
        :type total_task_count: int
        """
        self._total_task_count = total_task_count

    @property
    def free_task_quota_limit(self):
        r"""Gets the free_task_quota_limit of this QuotaItem.

        **参数解释：** 免费任务的配额上限。 **约束限制：** 0到int64 最大值。 **取值范围：** 0到9223372036854775807。 **默认取值：** 0。 

        :return: The free_task_quota_limit of this QuotaItem.
        :rtype: int
        """
        return self._free_task_quota_limit

    @free_task_quota_limit.setter
    def free_task_quota_limit(self, free_task_quota_limit):
        r"""Sets the free_task_quota_limit of this QuotaItem.

        **参数解释：** 免费任务的配额上限。 **约束限制：** 0到int64 最大值。 **取值范围：** 0到9223372036854775807。 **默认取值：** 0。 

        :param free_task_quota_limit: The free_task_quota_limit of this QuotaItem.
        :type free_task_quota_limit: int
        """
        self._free_task_quota_limit = free_task_quota_limit

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
        if not isinstance(other, QuotaItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
