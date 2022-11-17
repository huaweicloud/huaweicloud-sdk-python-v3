# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AffinityPodAffinity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'preferred_during_scheduling_ignored_during_execution': 'list[WeightPodAffinityTerms]',
        'required_during_scheduling_ignored_during_execution': 'list[PodAffinityTerm]'
    }

    attribute_map = {
        'preferred_during_scheduling_ignored_during_execution': 'preferredDuringSchedulingIgnoredDuringExecution',
        'required_during_scheduling_ignored_during_execution': 'requiredDuringSchedulingIgnoredDuringExecution'
    }

    def __init__(self, preferred_during_scheduling_ignored_during_execution=None, required_during_scheduling_ignored_during_execution=None):
        """AffinityPodAffinity

        The model defined in huaweicloud sdk

        :param preferred_during_scheduling_ignored_during_execution: 优先使用定义的规则调度，且不会影响已经在节点上运行的Pod。即优先选择调度到满足规则的节点，但也可能会调度到不满足规则的节点。
        :type preferred_during_scheduling_ignored_during_execution: list[:class:`huaweicloudsdkief.v1.WeightPodAffinityTerms`]
        :param required_during_scheduling_ignored_during_execution: 强制使用定义的规则调度，且不会影响已经在节点上运行的Pod。即强制选择调度到满足规则的节点，不会调度到不满足规则的节点。
        :type required_during_scheduling_ignored_during_execution: list[:class:`huaweicloudsdkief.v1.PodAffinityTerm`]
        """
        
        

        self._preferred_during_scheduling_ignored_during_execution = None
        self._required_during_scheduling_ignored_during_execution = None
        self.discriminator = None

        if preferred_during_scheduling_ignored_during_execution is not None:
            self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution
        if required_during_scheduling_ignored_during_execution is not None:
            self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution

    @property
    def preferred_during_scheduling_ignored_during_execution(self):
        """Gets the preferred_during_scheduling_ignored_during_execution of this AffinityPodAffinity.

        优先使用定义的规则调度，且不会影响已经在节点上运行的Pod。即优先选择调度到满足规则的节点，但也可能会调度到不满足规则的节点。

        :return: The preferred_during_scheduling_ignored_during_execution of this AffinityPodAffinity.
        :rtype: list[:class:`huaweicloudsdkief.v1.WeightPodAffinityTerms`]
        """
        return self._preferred_during_scheduling_ignored_during_execution

    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(self, preferred_during_scheduling_ignored_during_execution):
        """Sets the preferred_during_scheduling_ignored_during_execution of this AffinityPodAffinity.

        优先使用定义的规则调度，且不会影响已经在节点上运行的Pod。即优先选择调度到满足规则的节点，但也可能会调度到不满足规则的节点。

        :param preferred_during_scheduling_ignored_during_execution: The preferred_during_scheduling_ignored_during_execution of this AffinityPodAffinity.
        :type preferred_during_scheduling_ignored_during_execution: list[:class:`huaweicloudsdkief.v1.WeightPodAffinityTerms`]
        """
        self._preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    @property
    def required_during_scheduling_ignored_during_execution(self):
        """Gets the required_during_scheduling_ignored_during_execution of this AffinityPodAffinity.

        强制使用定义的规则调度，且不会影响已经在节点上运行的Pod。即强制选择调度到满足规则的节点，不会调度到不满足规则的节点。

        :return: The required_during_scheduling_ignored_during_execution of this AffinityPodAffinity.
        :rtype: list[:class:`huaweicloudsdkief.v1.PodAffinityTerm`]
        """
        return self._required_during_scheduling_ignored_during_execution

    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(self, required_during_scheduling_ignored_during_execution):
        """Sets the required_during_scheduling_ignored_during_execution of this AffinityPodAffinity.

        强制使用定义的规则调度，且不会影响已经在节点上运行的Pod。即强制选择调度到满足规则的节点，不会调度到不满足规则的节点。

        :param required_during_scheduling_ignored_during_execution: The required_during_scheduling_ignored_during_execution of this AffinityPodAffinity.
        :type required_during_scheduling_ignored_during_execution: list[:class:`huaweicloudsdkief.v1.PodAffinityTerm`]
        """
        self._required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution

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
        if not isinstance(other, AffinityPodAffinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
