# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadPlanInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'project_id': 'str',
        'cluster_id': 'str',
        'plan_id': 'str',
        'plan_name': 'str',
        'current_stage': 'str',
        'logical_cluster_name': 'str',
        'stage_list': 'list[PlanStage]'
    }

    attribute_map = {
        'status': 'status',
        'project_id': 'project_id',
        'cluster_id': 'cluster_id',
        'plan_id': 'plan_id',
        'plan_name': 'plan_name',
        'current_stage': 'current_stage',
        'logical_cluster_name': 'logical_cluster_name',
        'stage_list': 'stage_list'
    }

    def __init__(self, status=None, project_id=None, cluster_id=None, plan_id=None, plan_name=None, current_stage=None, logical_cluster_name=None, stage_list=None):
        """WorkloadPlanInfo

        The model defined in huaweicloud sdk

        :param status: 计划状态。
        :type status: str
        :param project_id: 项目ID。
        :type project_id: str
        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param plan_id: 计划ID。
        :type plan_id: str
        :param plan_name: 计划名称。
        :type plan_name: str
        :param current_stage: 当前计划阶段。
        :type current_stage: str
        :param logical_cluster_name: 逻辑集群名称。
        :type logical_cluster_name: str
        :param stage_list: 计划阶段列表。
        :type stage_list: list[:class:`huaweicloudsdkdws.v2.PlanStage`]
        """
        
        

        self._status = None
        self._project_id = None
        self._cluster_id = None
        self._plan_id = None
        self._plan_name = None
        self._current_stage = None
        self._logical_cluster_name = None
        self._stage_list = None
        self.discriminator = None

        if status is not None:
            self.status = status
        self.project_id = project_id
        self.cluster_id = cluster_id
        self.plan_id = plan_id
        self.plan_name = plan_name
        if current_stage is not None:
            self.current_stage = current_stage
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        if stage_list is not None:
            self.stage_list = stage_list

    @property
    def status(self):
        """Gets the status of this WorkloadPlanInfo.

        计划状态。

        :return: The status of this WorkloadPlanInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkloadPlanInfo.

        计划状态。

        :param status: The status of this WorkloadPlanInfo.
        :type status: str
        """
        self._status = status

    @property
    def project_id(self):
        """Gets the project_id of this WorkloadPlanInfo.

        项目ID。

        :return: The project_id of this WorkloadPlanInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this WorkloadPlanInfo.

        项目ID。

        :param project_id: The project_id of this WorkloadPlanInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this WorkloadPlanInfo.

        集群ID。

        :return: The cluster_id of this WorkloadPlanInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this WorkloadPlanInfo.

        集群ID。

        :param cluster_id: The cluster_id of this WorkloadPlanInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def plan_id(self):
        """Gets the plan_id of this WorkloadPlanInfo.

        计划ID。

        :return: The plan_id of this WorkloadPlanInfo.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this WorkloadPlanInfo.

        计划ID。

        :param plan_id: The plan_id of this WorkloadPlanInfo.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def plan_name(self):
        """Gets the plan_name of this WorkloadPlanInfo.

        计划名称。

        :return: The plan_name of this WorkloadPlanInfo.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this WorkloadPlanInfo.

        计划名称。

        :param plan_name: The plan_name of this WorkloadPlanInfo.
        :type plan_name: str
        """
        self._plan_name = plan_name

    @property
    def current_stage(self):
        """Gets the current_stage of this WorkloadPlanInfo.

        当前计划阶段。

        :return: The current_stage of this WorkloadPlanInfo.
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
        """Sets the current_stage of this WorkloadPlanInfo.

        当前计划阶段。

        :param current_stage: The current_stage of this WorkloadPlanInfo.
        :type current_stage: str
        """
        self._current_stage = current_stage

    @property
    def logical_cluster_name(self):
        """Gets the logical_cluster_name of this WorkloadPlanInfo.

        逻辑集群名称。

        :return: The logical_cluster_name of this WorkloadPlanInfo.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        """Sets the logical_cluster_name of this WorkloadPlanInfo.

        逻辑集群名称。

        :param logical_cluster_name: The logical_cluster_name of this WorkloadPlanInfo.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def stage_list(self):
        """Gets the stage_list of this WorkloadPlanInfo.

        计划阶段列表。

        :return: The stage_list of this WorkloadPlanInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.PlanStage`]
        """
        return self._stage_list

    @stage_list.setter
    def stage_list(self, stage_list):
        """Sets the stage_list of this WorkloadPlanInfo.

        计划阶段列表。

        :param stage_list: The stage_list of this WorkloadPlanInfo.
        :type stage_list: list[:class:`huaweicloudsdkdws.v2.PlanStage`]
        """
        self._stage_list = stage_list

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
        if not isinstance(other, WorkloadPlanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
