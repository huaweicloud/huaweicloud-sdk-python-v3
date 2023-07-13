# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyExecutionPlanResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deployment_id': 'str'
    }

    attribute_map = {
        'deployment_id': 'deployment_id'
    }

    def __init__(self, deployment_id=None):
        """ApplyExecutionPlanResponse

        The model defined in huaweicloud sdk

        :param deployment_id: 标识部署的唯一Id，此Id由资源编排服务在触发部署、回滚等操作时生成，为UUID。
        :type deployment_id: str
        """
        
        super(ApplyExecutionPlanResponse, self).__init__()

        self._deployment_id = None
        self.discriminator = None

        if deployment_id is not None:
            self.deployment_id = deployment_id

    @property
    def deployment_id(self):
        """Gets the deployment_id of this ApplyExecutionPlanResponse.

        标识部署的唯一Id，此Id由资源编排服务在触发部署、回滚等操作时生成，为UUID。

        :return: The deployment_id of this ApplyExecutionPlanResponse.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this ApplyExecutionPlanResponse.

        标识部署的唯一Id，此Id由资源编排服务在触发部署、回滚等操作时生成，为UUID。

        :param deployment_id: The deployment_id of this ApplyExecutionPlanResponse.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

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
        if not isinstance(other, ApplyExecutionPlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
