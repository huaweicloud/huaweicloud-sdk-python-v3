# coding: utf-8

import re
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
        'deployment_id': 'str',
        'force_delete': 'bool',
        'provider': 'str',
        'x_expired_time': 'int'
    }

    attribute_map = {
        'deployment_id': 'deployment_id',
        'force_delete': 'force_delete',
        'provider': 'provider',
        'x_expired_time': 'X-Expired-Time'
    }

    def __init__(self, deployment_id=None, force_delete=None, provider=None, x_expired_time=None):
        """DeleteDeploymentRequest

        The model defined in huaweicloud sdk

        :param deployment_id: 部署ID
        :type deployment_id: str
        :param force_delete: 强制删除，为true时表示前置删除
        :type force_delete: bool
        :param provider: 平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据
        :type provider: str
        :param x_expired_time: 离线场景超期时间，单位分钟，范围在1-86400
        :type x_expired_time: int
        """
        
        

        self._deployment_id = None
        self._force_delete = None
        self._provider = None
        self._x_expired_time = None
        self.discriminator = None

        self.deployment_id = deployment_id
        if force_delete is not None:
            self.force_delete = force_delete
        if provider is not None:
            self.provider = provider
        if x_expired_time is not None:
            self.x_expired_time = x_expired_time

    @property
    def deployment_id(self):
        """Gets the deployment_id of this DeleteDeploymentRequest.

        部署ID

        :return: The deployment_id of this DeleteDeploymentRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this DeleteDeploymentRequest.

        部署ID

        :param deployment_id: The deployment_id of this DeleteDeploymentRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def force_delete(self):
        """Gets the force_delete of this DeleteDeploymentRequest.

        强制删除，为true时表示前置删除

        :return: The force_delete of this DeleteDeploymentRequest.
        :rtype: bool
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        """Sets the force_delete of this DeleteDeploymentRequest.

        强制删除，为true时表示前置删除

        :param force_delete: The force_delete of this DeleteDeploymentRequest.
        :type force_delete: bool
        """
        self._force_delete = force_delete

    @property
    def provider(self):
        """Gets the provider of this DeleteDeploymentRequest.

        平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据

        :return: The provider of this DeleteDeploymentRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this DeleteDeploymentRequest.

        平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据

        :param provider: The provider of this DeleteDeploymentRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def x_expired_time(self):
        """Gets the x_expired_time of this DeleteDeploymentRequest.

        离线场景超期时间，单位分钟，范围在1-86400

        :return: The x_expired_time of this DeleteDeploymentRequest.
        :rtype: int
        """
        return self._x_expired_time

    @x_expired_time.setter
    def x_expired_time(self, x_expired_time):
        """Sets the x_expired_time of this DeleteDeploymentRequest.

        离线场景超期时间，单位分钟，范围在1-86400

        :param x_expired_time: The x_expired_time of this DeleteDeploymentRequest.
        :type x_expired_time: int
        """
        self._x_expired_time = x_expired_time

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
