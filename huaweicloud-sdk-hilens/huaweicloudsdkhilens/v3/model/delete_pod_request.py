# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePodRequest:

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
        'force_delete': 'bool',
        'pod_id': 'str'
    }

    attribute_map = {
        'deployment_id': 'deployment_id',
        'force_delete': 'force_delete',
        'pod_id': 'pod_id'
    }

    def __init__(self, deployment_id=None, force_delete=None, pod_id=None):
        """DeletePodRequest

        The model defined in huaweicloud sdk

        :param deployment_id: 应用部署ID
        :type deployment_id: str
        :param force_delete: 是否强制删除，为true的时候为强制删除
        :type force_delete: bool
        :param pod_id: 实例ID
        :type pod_id: str
        """
        
        

        self._deployment_id = None
        self._force_delete = None
        self._pod_id = None
        self.discriminator = None

        self.deployment_id = deployment_id
        if force_delete is not None:
            self.force_delete = force_delete
        self.pod_id = pod_id

    @property
    def deployment_id(self):
        """Gets the deployment_id of this DeletePodRequest.

        应用部署ID

        :return: The deployment_id of this DeletePodRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this DeletePodRequest.

        应用部署ID

        :param deployment_id: The deployment_id of this DeletePodRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def force_delete(self):
        """Gets the force_delete of this DeletePodRequest.

        是否强制删除，为true的时候为强制删除

        :return: The force_delete of this DeletePodRequest.
        :rtype: bool
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        """Sets the force_delete of this DeletePodRequest.

        是否强制删除，为true的时候为强制删除

        :param force_delete: The force_delete of this DeletePodRequest.
        :type force_delete: bool
        """
        self._force_delete = force_delete

    @property
    def pod_id(self):
        """Gets the pod_id of this DeletePodRequest.

        实例ID

        :return: The pod_id of this DeletePodRequest.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        """Sets the pod_id of this DeletePodRequest.

        实例ID

        :param pod_id: The pod_id of this DeletePodRequest.
        :type pod_id: str
        """
        self._pod_id = pod_id

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
        if not isinstance(other, DeletePodRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
