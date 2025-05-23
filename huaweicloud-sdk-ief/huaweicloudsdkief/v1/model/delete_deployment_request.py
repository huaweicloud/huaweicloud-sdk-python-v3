# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDeploymentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ief_instance_id': 'str',
        'deployment_id': 'str',
        'force_delete': 'str'
    }

    attribute_map = {
        'ief_instance_id': 'ief-instance-id',
        'deployment_id': 'deployment_id',
        'force_delete': 'force_delete'
    }

    def __init__(self, ief_instance_id=None, deployment_id=None, force_delete=None):
        r"""DeleteDeploymentRequest

        The model defined in huaweicloud sdk

        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param deployment_id: 应用部署ID
        :type deployment_id: str
        :param force_delete: 是否强制删除。默认为false。 如果强制删除，则会忽略边缘节点是否有残留应用，直接删除云端应用。 如果不强制删除，则会等待边缘节点的应用删除成功后，再删除云端应用。
        :type force_delete: str
        """
        
        

        self._ief_instance_id = None
        self._deployment_id = None
        self._force_delete = None
        self.discriminator = None

        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        self.deployment_id = deployment_id
        if force_delete is not None:
            self.force_delete = force_delete

    @property
    def ief_instance_id(self):
        r"""Gets the ief_instance_id of this DeleteDeploymentRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this DeleteDeploymentRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        r"""Sets the ief_instance_id of this DeleteDeploymentRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this DeleteDeploymentRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this DeleteDeploymentRequest.

        应用部署ID

        :return: The deployment_id of this DeleteDeploymentRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this DeleteDeploymentRequest.

        应用部署ID

        :param deployment_id: The deployment_id of this DeleteDeploymentRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def force_delete(self):
        r"""Gets the force_delete of this DeleteDeploymentRequest.

        是否强制删除。默认为false。 如果强制删除，则会忽略边缘节点是否有残留应用，直接删除云端应用。 如果不强制删除，则会等待边缘节点的应用删除成功后，再删除云端应用。

        :return: The force_delete of this DeleteDeploymentRequest.
        :rtype: str
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        r"""Sets the force_delete of this DeleteDeploymentRequest.

        是否强制删除。默认为false。 如果强制删除，则会忽略边缘节点是否有残留应用，直接删除云端应用。 如果不强制删除，则会等待边缘节点的应用删除成功后，再删除云端应用。

        :param force_delete: The force_delete of this DeleteDeploymentRequest.
        :type force_delete: str
        """
        self._force_delete = force_delete

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
        if not isinstance(other, DeleteDeploymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
