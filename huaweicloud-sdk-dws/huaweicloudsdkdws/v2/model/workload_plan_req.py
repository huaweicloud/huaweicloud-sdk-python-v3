# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadPlanReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plan_name': 'str',
        'logical_cluster_name': 'str'
    }

    attribute_map = {
        'plan_name': 'plan_name',
        'logical_cluster_name': 'logical_cluster_name'
    }

    def __init__(self, plan_name=None, logical_cluster_name=None):
        """WorkloadPlanReq

        The model defined in huaweicloud sdk

        :param plan_name: 计划名称
        :type plan_name: str
        :param logical_cluster_name: 逻辑集群名称
        :type logical_cluster_name: str
        """
        
        

        self._plan_name = None
        self._logical_cluster_name = None
        self.discriminator = None

        self.plan_name = plan_name
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name

    @property
    def plan_name(self):
        """Gets the plan_name of this WorkloadPlanReq.

        计划名称

        :return: The plan_name of this WorkloadPlanReq.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this WorkloadPlanReq.

        计划名称

        :param plan_name: The plan_name of this WorkloadPlanReq.
        :type plan_name: str
        """
        self._plan_name = plan_name

    @property
    def logical_cluster_name(self):
        """Gets the logical_cluster_name of this WorkloadPlanReq.

        逻辑集群名称

        :return: The logical_cluster_name of this WorkloadPlanReq.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        """Sets the logical_cluster_name of this WorkloadPlanReq.

        逻辑集群名称

        :param logical_cluster_name: The logical_cluster_name of this WorkloadPlanReq.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

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
        if not isinstance(other, WorkloadPlanReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
