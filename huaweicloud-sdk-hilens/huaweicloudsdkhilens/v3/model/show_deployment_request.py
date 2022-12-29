# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeploymentRequest:

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
        'provider': 'str'
    }

    attribute_map = {
        'deployment_id': 'deployment_id',
        'provider': 'provider'
    }

    def __init__(self, deployment_id=None, provider=None):
        """ShowDeploymentRequest

        The model defined in huaweicloud sdk

        :param deployment_id: 应用部署ID
        :type deployment_id: str
        :param provider: 平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据。
        :type provider: str
        """
        
        

        self._deployment_id = None
        self._provider = None
        self.discriminator = None

        self.deployment_id = deployment_id
        if provider is not None:
            self.provider = provider

    @property
    def deployment_id(self):
        """Gets the deployment_id of this ShowDeploymentRequest.

        应用部署ID

        :return: The deployment_id of this ShowDeploymentRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this ShowDeploymentRequest.

        应用部署ID

        :param deployment_id: The deployment_id of this ShowDeploymentRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def provider(self):
        """Gets the provider of this ShowDeploymentRequest.

        平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据。

        :return: The provider of this ShowDeploymentRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ShowDeploymentRequest.

        平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据。

        :param provider: The provider of this ShowDeploymentRequest.
        :type provider: str
        """
        self._provider = provider

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
        if not isinstance(other, ShowDeploymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
