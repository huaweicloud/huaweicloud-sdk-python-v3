# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsModelDeploymentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'status_count': 'OpsDeployTaskStatusCount',
        'deployments': 'list[OpsModelDeploymentInfo]'
    }

    attribute_map = {
        'total': 'total',
        'status_count': 'status_count',
        'deployments': 'deployments'
    }

    def __init__(self, total=None, status_count=None, deployments=None):
        r"""ListOpsModelDeploymentsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释：** 满足条件的部署记录总数，用于计算分页总页数，单位：个（记录总数）。  **取值范围：** 大于等于0的整数。
        :type total: int
        :param status_count: 
        :type status_count: :class:`huaweicloudsdkagentarts.v1.OpsDeployTaskStatusCount`
        :param deployments: **参数解释：** 部署任务列表。  **取值范围：** 符合OpsModelDeploymentInfo定义的对象数组。
        :type deployments: list[:class:`huaweicloudsdkagentarts.v1.OpsModelDeploymentInfo`]
        """
        
        super().__init__()

        self._total = None
        self._status_count = None
        self._deployments = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if status_count is not None:
            self.status_count = status_count
        if deployments is not None:
            self.deployments = deployments

    @property
    def total(self):
        r"""Gets the total of this ListOpsModelDeploymentsResponse.

        **参数解释：** 满足条件的部署记录总数，用于计算分页总页数，单位：个（记录总数）。  **取值范围：** 大于等于0的整数。

        :return: The total of this ListOpsModelDeploymentsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOpsModelDeploymentsResponse.

        **参数解释：** 满足条件的部署记录总数，用于计算分页总页数，单位：个（记录总数）。  **取值范围：** 大于等于0的整数。

        :param total: The total of this ListOpsModelDeploymentsResponse.
        :type total: int
        """
        self._total = total

    @property
    def status_count(self):
        r"""Gets the status_count of this ListOpsModelDeploymentsResponse.

        :return: The status_count of this ListOpsModelDeploymentsResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsDeployTaskStatusCount`
        """
        return self._status_count

    @status_count.setter
    def status_count(self, status_count):
        r"""Sets the status_count of this ListOpsModelDeploymentsResponse.

        :param status_count: The status_count of this ListOpsModelDeploymentsResponse.
        :type status_count: :class:`huaweicloudsdkagentarts.v1.OpsDeployTaskStatusCount`
        """
        self._status_count = status_count

    @property
    def deployments(self):
        r"""Gets the deployments of this ListOpsModelDeploymentsResponse.

        **参数解释：** 部署任务列表。  **取值范围：** 符合OpsModelDeploymentInfo定义的对象数组。

        :return: The deployments of this ListOpsModelDeploymentsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsModelDeploymentInfo`]
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        r"""Sets the deployments of this ListOpsModelDeploymentsResponse.

        **参数解释：** 部署任务列表。  **取值范围：** 符合OpsModelDeploymentInfo定义的对象数组。

        :param deployments: The deployments of this ListOpsModelDeploymentsResponse.
        :type deployments: list[:class:`huaweicloudsdkagentarts.v1.OpsModelDeploymentInfo`]
        """
        self._deployments = deployments

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsModelDeploymentsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsModelDeploymentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
