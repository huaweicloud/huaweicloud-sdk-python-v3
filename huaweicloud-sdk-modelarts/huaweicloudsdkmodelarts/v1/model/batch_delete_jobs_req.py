# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteJobsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[BatchDeleteJobItem]'
    }

    attribute_map = {
        'jobs': 'jobs'
    }

    def __init__(self, jobs=None):
        r"""BatchDeleteJobsReq

        The model defined in huaweicloud sdk

        :param jobs: **参数解释**：待删除的训练作业列表。 **约束限制**：列表元素数量不超过100，且所有作业必须属于同一工作空间。 **取值范围**：不涉及。
        :type jobs: list[:class:`huaweicloudsdkmodelarts.v1.BatchDeleteJobItem`]
        """
        
        

        self._jobs = None
        self.discriminator = None

        self.jobs = jobs

    @property
    def jobs(self):
        r"""Gets the jobs of this BatchDeleteJobsReq.

        **参数解释**：待删除的训练作业列表。 **约束限制**：列表元素数量不超过100，且所有作业必须属于同一工作空间。 **取值范围**：不涉及。

        :return: The jobs of this BatchDeleteJobsReq.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.BatchDeleteJobItem`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this BatchDeleteJobsReq.

        **参数解释**：待删除的训练作业列表。 **约束限制**：列表元素数量不超过100，且所有作业必须属于同一工作空间。 **取值范围**：不涉及。

        :param jobs: The jobs of this BatchDeleteJobsReq.
        :type jobs: list[:class:`huaweicloudsdkmodelarts.v1.BatchDeleteJobItem`]
        """
        self._jobs = jobs

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
        if not isinstance(other, BatchDeleteJobsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
