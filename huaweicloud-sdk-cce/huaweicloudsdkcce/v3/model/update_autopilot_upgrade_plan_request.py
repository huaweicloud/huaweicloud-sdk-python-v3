# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAutopilotUpgradePlanRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'upgrade_plan_id': 'str',
        'body': 'DelayUpgradePlanRequestBody'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'upgrade_plan_id': 'upgrade_plan_id',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, upgrade_plan_id=None, body=None):
        r"""UpdateAutopilotUpgradePlanRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param upgrade_plan_id: 集群自动升级计划ID
        :type upgrade_plan_id: str
        :param body: Body of the UpdateAutopilotUpgradePlanRequest
        :type body: :class:`huaweicloudsdkcce.v3.DelayUpgradePlanRequestBody`
        """
        
        

        self._cluster_id = None
        self._upgrade_plan_id = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.upgrade_plan_id = upgrade_plan_id
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateAutopilotUpgradePlanRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this UpdateAutopilotUpgradePlanRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateAutopilotUpgradePlanRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this UpdateAutopilotUpgradePlanRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def upgrade_plan_id(self):
        r"""Gets the upgrade_plan_id of this UpdateAutopilotUpgradePlanRequest.

        集群自动升级计划ID

        :return: The upgrade_plan_id of this UpdateAutopilotUpgradePlanRequest.
        :rtype: str
        """
        return self._upgrade_plan_id

    @upgrade_plan_id.setter
    def upgrade_plan_id(self, upgrade_plan_id):
        r"""Sets the upgrade_plan_id of this UpdateAutopilotUpgradePlanRequest.

        集群自动升级计划ID

        :param upgrade_plan_id: The upgrade_plan_id of this UpdateAutopilotUpgradePlanRequest.
        :type upgrade_plan_id: str
        """
        self._upgrade_plan_id = upgrade_plan_id

    @property
    def body(self):
        r"""Gets the body of this UpdateAutopilotUpgradePlanRequest.

        :return: The body of this UpdateAutopilotUpgradePlanRequest.
        :rtype: :class:`huaweicloudsdkcce.v3.DelayUpgradePlanRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAutopilotUpgradePlanRequest.

        :param body: The body of this UpdateAutopilotUpgradePlanRequest.
        :type body: :class:`huaweicloudsdkcce.v3.DelayUpgradePlanRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateAutopilotUpgradePlanRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
