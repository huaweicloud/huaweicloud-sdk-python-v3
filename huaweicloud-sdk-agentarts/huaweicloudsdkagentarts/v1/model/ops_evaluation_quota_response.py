# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsEvaluationQuotaResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'free_quota_limit': 'int',
        'free_used': 'int',
        'total_quota_limit': 'int',
        'total_used_count': 'int'
    }

    attribute_map = {
        'type': 'type',
        'free_quota_limit': 'free_quota_limit',
        'free_used': 'free_used',
        'total_quota_limit': 'total_quota_limit',
        'total_used_count': 'total_used_count'
    }

    def __init__(self, type=None, free_quota_limit=None, free_used=None, total_quota_limit=None, total_used_count=None):
        r"""OpsEvaluationQuotaResponse

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 配额维度标识。取值范围：evaluation_task_count, parallel_online_evaluation_task_count, synthesis_task_count, parallel_synthesis_task_count, dataset_count, evaluator_count, label_count。
        :type type: str
        :param free_quota_limit: **参数解释：** 免费配额上限。仅evaluation_task_count和synthesis_task_count有值，其他维度返回null。
        :type free_quota_limit: int
        :param free_used: **参数解释：** 免费配额已用数量。仅evaluation_task_count和synthesis_task_count有值，其他维度返回null。
        :type free_used: int
        :param total_quota_limit: **参数解释：** 总配额上限，从ServiceCM平台获取。
        :type total_quota_limit: int
        :param total_used_count: **参数解释：** 总配额已用数量，统计未删除状态的数据。
        :type total_used_count: int
        """
        
        

        self._type = None
        self._free_quota_limit = None
        self._free_used = None
        self._total_quota_limit = None
        self._total_used_count = None
        self.discriminator = None

        self.type = type
        if free_quota_limit is not None:
            self.free_quota_limit = free_quota_limit
        if free_used is not None:
            self.free_used = free_used
        self.total_quota_limit = total_quota_limit
        self.total_used_count = total_used_count

    @property
    def type(self):
        r"""Gets the type of this OpsEvaluationQuotaResponse.

        **参数解释：** 配额维度标识。取值范围：evaluation_task_count, parallel_online_evaluation_task_count, synthesis_task_count, parallel_synthesis_task_count, dataset_count, evaluator_count, label_count。

        :return: The type of this OpsEvaluationQuotaResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsEvaluationQuotaResponse.

        **参数解释：** 配额维度标识。取值范围：evaluation_task_count, parallel_online_evaluation_task_count, synthesis_task_count, parallel_synthesis_task_count, dataset_count, evaluator_count, label_count。

        :param type: The type of this OpsEvaluationQuotaResponse.
        :type type: str
        """
        self._type = type

    @property
    def free_quota_limit(self):
        r"""Gets the free_quota_limit of this OpsEvaluationQuotaResponse.

        **参数解释：** 免费配额上限。仅evaluation_task_count和synthesis_task_count有值，其他维度返回null。

        :return: The free_quota_limit of this OpsEvaluationQuotaResponse.
        :rtype: int
        """
        return self._free_quota_limit

    @free_quota_limit.setter
    def free_quota_limit(self, free_quota_limit):
        r"""Sets the free_quota_limit of this OpsEvaluationQuotaResponse.

        **参数解释：** 免费配额上限。仅evaluation_task_count和synthesis_task_count有值，其他维度返回null。

        :param free_quota_limit: The free_quota_limit of this OpsEvaluationQuotaResponse.
        :type free_quota_limit: int
        """
        self._free_quota_limit = free_quota_limit

    @property
    def free_used(self):
        r"""Gets the free_used of this OpsEvaluationQuotaResponse.

        **参数解释：** 免费配额已用数量。仅evaluation_task_count和synthesis_task_count有值，其他维度返回null。

        :return: The free_used of this OpsEvaluationQuotaResponse.
        :rtype: int
        """
        return self._free_used

    @free_used.setter
    def free_used(self, free_used):
        r"""Sets the free_used of this OpsEvaluationQuotaResponse.

        **参数解释：** 免费配额已用数量。仅evaluation_task_count和synthesis_task_count有值，其他维度返回null。

        :param free_used: The free_used of this OpsEvaluationQuotaResponse.
        :type free_used: int
        """
        self._free_used = free_used

    @property
    def total_quota_limit(self):
        r"""Gets the total_quota_limit of this OpsEvaluationQuotaResponse.

        **参数解释：** 总配额上限，从ServiceCM平台获取。

        :return: The total_quota_limit of this OpsEvaluationQuotaResponse.
        :rtype: int
        """
        return self._total_quota_limit

    @total_quota_limit.setter
    def total_quota_limit(self, total_quota_limit):
        r"""Sets the total_quota_limit of this OpsEvaluationQuotaResponse.

        **参数解释：** 总配额上限，从ServiceCM平台获取。

        :param total_quota_limit: The total_quota_limit of this OpsEvaluationQuotaResponse.
        :type total_quota_limit: int
        """
        self._total_quota_limit = total_quota_limit

    @property
    def total_used_count(self):
        r"""Gets the total_used_count of this OpsEvaluationQuotaResponse.

        **参数解释：** 总配额已用数量，统计未删除状态的数据。

        :return: The total_used_count of this OpsEvaluationQuotaResponse.
        :rtype: int
        """
        return self._total_used_count

    @total_used_count.setter
    def total_used_count(self, total_used_count):
        r"""Sets the total_used_count of this OpsEvaluationQuotaResponse.

        **参数解释：** 总配额已用数量，统计未删除状态的数据。

        :param total_used_count: The total_used_count of this OpsEvaluationQuotaResponse.
        :type total_used_count: int
        """
        self._total_used_count = total_used_count

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
        if not isinstance(other, OpsEvaluationQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
