# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentTargetsPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deployment_targets': 'DeploymentTargets'
    }

    attribute_map = {
        'deployment_targets': 'deployment_targets'
    }

    def __init__(self, deployment_targets=None):
        """DeploymentTargetsPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param deployment_targets: 
        :type deployment_targets: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        """
        
        

        self._deployment_targets = None
        self.discriminator = None

        self.deployment_targets = deployment_targets

    @property
    def deployment_targets(self):
        """Gets the deployment_targets of this DeploymentTargetsPrimitiveTypeHolder.

        :return: The deployment_targets of this DeploymentTargetsPrimitiveTypeHolder.
        :rtype: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        """
        return self._deployment_targets

    @deployment_targets.setter
    def deployment_targets(self, deployment_targets):
        """Sets the deployment_targets of this DeploymentTargetsPrimitiveTypeHolder.

        :param deployment_targets: The deployment_targets of this DeploymentTargetsPrimitiveTypeHolder.
        :type deployment_targets: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        """
        self._deployment_targets = deployment_targets

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
        if not isinstance(other, DeploymentTargetsPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
