# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedistributionConf:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parallel_jobs': 'int',
        'priority_policy': 'str'
    }

    attribute_map = {
        'parallel_jobs': 'parallel_jobs',
        'priority_policy': 'priority_policy'
    }

    def __init__(self, parallel_jobs=None, priority_policy=None):
        r"""RedistributionConf

        The model defined in huaweicloud sdk

        :param parallel_jobs: **参数解释**： 并发数，默认并发数为4。 **约束限制**： 不涉及。 **取值范围**： 1~200 **默认取值**： 不涉及。
        :type parallel_jobs: int
        :param priority_policy: **参数解释**： 重分布优先级策略。 **约束限制**： 不涉及。 **取值范围**： - default：默认策略 - small：小表优先 - large：大表优先  **默认取值**： 不涉及。
        :type priority_policy: str
        """
        
        

        self._parallel_jobs = None
        self._priority_policy = None
        self.discriminator = None

        self.parallel_jobs = parallel_jobs
        self.priority_policy = priority_policy

    @property
    def parallel_jobs(self):
        r"""Gets the parallel_jobs of this RedistributionConf.

        **参数解释**： 并发数，默认并发数为4。 **约束限制**： 不涉及。 **取值范围**： 1~200 **默认取值**： 不涉及。

        :return: The parallel_jobs of this RedistributionConf.
        :rtype: int
        """
        return self._parallel_jobs

    @parallel_jobs.setter
    def parallel_jobs(self, parallel_jobs):
        r"""Sets the parallel_jobs of this RedistributionConf.

        **参数解释**： 并发数，默认并发数为4。 **约束限制**： 不涉及。 **取值范围**： 1~200 **默认取值**： 不涉及。

        :param parallel_jobs: The parallel_jobs of this RedistributionConf.
        :type parallel_jobs: int
        """
        self._parallel_jobs = parallel_jobs

    @property
    def priority_policy(self):
        r"""Gets the priority_policy of this RedistributionConf.

        **参数解释**： 重分布优先级策略。 **约束限制**： 不涉及。 **取值范围**： - default：默认策略 - small：小表优先 - large：大表优先  **默认取值**： 不涉及。

        :return: The priority_policy of this RedistributionConf.
        :rtype: str
        """
        return self._priority_policy

    @priority_policy.setter
    def priority_policy(self, priority_policy):
        r"""Sets the priority_policy of this RedistributionConf.

        **参数解释**： 重分布优先级策略。 **约束限制**： 不涉及。 **取值范围**： - default：默认策略 - small：小表优先 - large：大表优先  **默认取值**： 不涉及。

        :param priority_policy: The priority_policy of this RedistributionConf.
        :type priority_policy: str
        """
        self._priority_policy = priority_policy

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
        if not isinstance(other, RedistributionConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
