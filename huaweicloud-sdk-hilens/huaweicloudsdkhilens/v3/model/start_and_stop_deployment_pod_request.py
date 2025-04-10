# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartAndStopDeploymentPodRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deployment_id': 'str',
        'pod_id': 'str',
        'action': 'str'
    }

    attribute_map = {
        'deployment_id': 'deployment_id',
        'pod_id': 'pod_id',
        'action': 'action'
    }

    def __init__(self, deployment_id=None, pod_id=None, action=None):
        r"""StartAndStopDeploymentPodRequest

        The model defined in huaweicloud sdk

        :param deployment_id: 部署ID，可以在部署详情中获取指定ID
        :type deployment_id: str
        :param pod_id: 节点ID, 可以在部署详情中获取指定ID
        :type pod_id: str
        :param action: 操作请求，分别为，pause停止，resume启动
        :type action: str
        """
        
        

        self._deployment_id = None
        self._pod_id = None
        self._action = None
        self.discriminator = None

        self.deployment_id = deployment_id
        self.pod_id = pod_id
        self.action = action

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this StartAndStopDeploymentPodRequest.

        部署ID，可以在部署详情中获取指定ID

        :return: The deployment_id of this StartAndStopDeploymentPodRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this StartAndStopDeploymentPodRequest.

        部署ID，可以在部署详情中获取指定ID

        :param deployment_id: The deployment_id of this StartAndStopDeploymentPodRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def pod_id(self):
        r"""Gets the pod_id of this StartAndStopDeploymentPodRequest.

        节点ID, 可以在部署详情中获取指定ID

        :return: The pod_id of this StartAndStopDeploymentPodRequest.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this StartAndStopDeploymentPodRequest.

        节点ID, 可以在部署详情中获取指定ID

        :param pod_id: The pod_id of this StartAndStopDeploymentPodRequest.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def action(self):
        r"""Gets the action of this StartAndStopDeploymentPodRequest.

        操作请求，分别为，pause停止，resume启动

        :return: The action of this StartAndStopDeploymentPodRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this StartAndStopDeploymentPodRequest.

        操作请求，分别为，pause停止，resume启动

        :param action: The action of this StartAndStopDeploymentPodRequest.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, StartAndStopDeploymentPodRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
