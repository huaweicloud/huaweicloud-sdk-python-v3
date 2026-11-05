# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobBaselineInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_ids': 'list[str]'
    }

    attribute_map = {
        'job_ids': 'job_ids'
    }

    def __init__(self, job_ids=None):
        r"""JobBaselineInfoReq

        The model defined in huaweicloud sdk

        :param job_ids: **参数解释**： 待查询的作业ID列表。 **约束限制**： 必须传入。 **取值范围**： 列表元素个数为1~100个，每个元素长度为1~64个字符。 **默认取值**： 不涉及。
        :type job_ids: list[str]
        """
        
        

        self._job_ids = None
        self.discriminator = None

        self.job_ids = job_ids

    @property
    def job_ids(self):
        r"""Gets the job_ids of this JobBaselineInfoReq.

        **参数解释**： 待查询的作业ID列表。 **约束限制**： 必须传入。 **取值范围**： 列表元素个数为1~100个，每个元素长度为1~64个字符。 **默认取值**： 不涉及。

        :return: The job_ids of this JobBaselineInfoReq.
        :rtype: list[str]
        """
        return self._job_ids

    @job_ids.setter
    def job_ids(self, job_ids):
        r"""Sets the job_ids of this JobBaselineInfoReq.

        **参数解释**： 待查询的作业ID列表。 **约束限制**： 必须传入。 **取值范围**： 列表元素个数为1~100个，每个元素长度为1~64个字符。 **默认取值**： 不涉及。

        :param job_ids: The job_ids of this JobBaselineInfoReq.
        :type job_ids: list[str]
        """
        self._job_ids = job_ids

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
        if not isinstance(other, JobBaselineInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
