# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadPlanStageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workload_plan_stage': 'WorkloadPlanStageReqWorkloadPlanStage'
    }

    attribute_map = {
        'workload_plan_stage': 'workload_plan_stage'
    }

    def __init__(self, workload_plan_stage=None):
        """WorkloadPlanStageReq

        The model defined in huaweicloud sdk

        :param workload_plan_stage: 
        :type workload_plan_stage: :class:`huaweicloudsdkdws.v2.WorkloadPlanStageReqWorkloadPlanStage`
        """
        
        

        self._workload_plan_stage = None
        self.discriminator = None

        if workload_plan_stage is not None:
            self.workload_plan_stage = workload_plan_stage

    @property
    def workload_plan_stage(self):
        """Gets the workload_plan_stage of this WorkloadPlanStageReq.

        :return: The workload_plan_stage of this WorkloadPlanStageReq.
        :rtype: :class:`huaweicloudsdkdws.v2.WorkloadPlanStageReqWorkloadPlanStage`
        """
        return self._workload_plan_stage

    @workload_plan_stage.setter
    def workload_plan_stage(self, workload_plan_stage):
        """Sets the workload_plan_stage of this WorkloadPlanStageReq.

        :param workload_plan_stage: The workload_plan_stage of this WorkloadPlanStageReq.
        :type workload_plan_stage: :class:`huaweicloudsdkdws.v2.WorkloadPlanStageReqWorkloadPlanStage`
        """
        self._workload_plan_stage = workload_plan_stage

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
        if not isinstance(other, WorkloadPlanStageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
