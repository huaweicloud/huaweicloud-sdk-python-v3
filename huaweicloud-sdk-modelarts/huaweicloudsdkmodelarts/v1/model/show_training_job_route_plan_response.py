# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTrainingJobRoutePlanResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'status': 'str',
        'rank_mapping': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'rank_mapping': 'rank_mapping'
    }

    def __init__(self, job_id=None, status=None, rank_mapping=None):
        r"""ShowTrainingJobRoutePlanResponse

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**：训练作业ID。 **取值范围**：不涉及。
        :type job_id: str
        :param status: **参数解释**：路由规划状态。 **取值范围**： - success：路由规划成功 - failed：路由规划未执行或不满足条件，返回默认rank映射
        :type status: str
        :param rank_mapping: **参数解释**：rank映射结果，格式为\&quot;newRankId-workerId\&quot;，多个映射项之间以英文逗号分隔。 **约束限制**：当status为failed时，返回基于作业规格计算的默认顺序映射。 **取值范围**：不涉及。
        :type rank_mapping: str
        """
        
        super().__init__()

        self._job_id = None
        self._status = None
        self._rank_mapping = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if rank_mapping is not None:
            self.rank_mapping = rank_mapping

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowTrainingJobRoutePlanResponse.

        **参数解释**：训练作业ID。 **取值范围**：不涉及。

        :return: The job_id of this ShowTrainingJobRoutePlanResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowTrainingJobRoutePlanResponse.

        **参数解释**：训练作业ID。 **取值范围**：不涉及。

        :param job_id: The job_id of this ShowTrainingJobRoutePlanResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this ShowTrainingJobRoutePlanResponse.

        **参数解释**：路由规划状态。 **取值范围**： - success：路由规划成功 - failed：路由规划未执行或不满足条件，返回默认rank映射

        :return: The status of this ShowTrainingJobRoutePlanResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTrainingJobRoutePlanResponse.

        **参数解释**：路由规划状态。 **取值范围**： - success：路由规划成功 - failed：路由规划未执行或不满足条件，返回默认rank映射

        :param status: The status of this ShowTrainingJobRoutePlanResponse.
        :type status: str
        """
        self._status = status

    @property
    def rank_mapping(self):
        r"""Gets the rank_mapping of this ShowTrainingJobRoutePlanResponse.

        **参数解释**：rank映射结果，格式为\"newRankId-workerId\"，多个映射项之间以英文逗号分隔。 **约束限制**：当status为failed时，返回基于作业规格计算的默认顺序映射。 **取值范围**：不涉及。

        :return: The rank_mapping of this ShowTrainingJobRoutePlanResponse.
        :rtype: str
        """
        return self._rank_mapping

    @rank_mapping.setter
    def rank_mapping(self, rank_mapping):
        r"""Sets the rank_mapping of this ShowTrainingJobRoutePlanResponse.

        **参数解释**：rank映射结果，格式为\"newRankId-workerId\"，多个映射项之间以英文逗号分隔。 **约束限制**：当status为failed时，返回基于作业规格计算的默认顺序映射。 **取值范围**：不涉及。

        :param rank_mapping: The rank_mapping of this ShowTrainingJobRoutePlanResponse.
        :type rank_mapping: str
        """
        self._rank_mapping = rank_mapping

    def to_dict(self):
        import warnings
        warnings.warn("ShowTrainingJobRoutePlanResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowTrainingJobRoutePlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
