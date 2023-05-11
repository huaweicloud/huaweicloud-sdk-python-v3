# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestartDeploymentsPodRequest:

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
        'pod_name': 'str',
        'ief_instance_id': 'str'
    }

    attribute_map = {
        'deployment_id': 'deployment_id',
        'pod_name': 'pod_name',
        'ief_instance_id': 'ief-instance-id'
    }

    def __init__(self, deployment_id=None, pod_name=None, ief_instance_id=None):
        """RestartDeploymentsPodRequest

        The model defined in huaweicloud sdk

        :param deployment_id: 应用部署ID
        :type deployment_id: str
        :param pod_name: 应用实例名称
        :type pod_name: str
        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        """
        
        

        self._deployment_id = None
        self._pod_name = None
        self._ief_instance_id = None
        self.discriminator = None

        self.deployment_id = deployment_id
        self.pod_name = pod_name
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id

    @property
    def deployment_id(self):
        """Gets the deployment_id of this RestartDeploymentsPodRequest.

        应用部署ID

        :return: The deployment_id of this RestartDeploymentsPodRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this RestartDeploymentsPodRequest.

        应用部署ID

        :param deployment_id: The deployment_id of this RestartDeploymentsPodRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def pod_name(self):
        """Gets the pod_name of this RestartDeploymentsPodRequest.

        应用实例名称

        :return: The pod_name of this RestartDeploymentsPodRequest.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this RestartDeploymentsPodRequest.

        应用实例名称

        :param pod_name: The pod_name of this RestartDeploymentsPodRequest.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this RestartDeploymentsPodRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this RestartDeploymentsPodRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this RestartDeploymentsPodRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this RestartDeploymentsPodRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

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
        if not isinstance(other, RestartDeploymentsPodRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
