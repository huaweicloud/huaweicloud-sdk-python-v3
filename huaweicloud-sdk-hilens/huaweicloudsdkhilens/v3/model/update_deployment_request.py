# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDeploymentRequest:

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
        'provider': 'str',
        'x_expired_time': 'int',
        'body': 'DeploymentUpdateRequest'
    }

    attribute_map = {
        'deployment_id': 'deployment_id',
        'provider': 'provider',
        'x_expired_time': 'X-Expired-Time',
        'body': 'body'
    }

    def __init__(self, deployment_id=None, provider=None, x_expired_time=None, body=None):
        """UpdateDeploymentRequest

        The model defined in huaweicloud sdk

        :param deployment_id: 部署ID
        :type deployment_id: str
        :param provider: 平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据。
        :type provider: str
        :param x_expired_time: 离线场景超期时间，单位分钟，范围在1-86400
        :type x_expired_time: int
        :param body: Body of the UpdateDeploymentRequest
        :type body: :class:`huaweicloudsdkhilens.v3.DeploymentUpdateRequest`
        """
        
        

        self._deployment_id = None
        self._provider = None
        self._x_expired_time = None
        self._body = None
        self.discriminator = None

        self.deployment_id = deployment_id
        if provider is not None:
            self.provider = provider
        if x_expired_time is not None:
            self.x_expired_time = x_expired_time
        if body is not None:
            self.body = body

    @property
    def deployment_id(self):
        """Gets the deployment_id of this UpdateDeploymentRequest.

        部署ID

        :return: The deployment_id of this UpdateDeploymentRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this UpdateDeploymentRequest.

        部署ID

        :param deployment_id: The deployment_id of this UpdateDeploymentRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def provider(self):
        """Gets the provider of this UpdateDeploymentRequest.

        平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据。

        :return: The provider of this UpdateDeploymentRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this UpdateDeploymentRequest.

        平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据。

        :param provider: The provider of this UpdateDeploymentRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def x_expired_time(self):
        """Gets the x_expired_time of this UpdateDeploymentRequest.

        离线场景超期时间，单位分钟，范围在1-86400

        :return: The x_expired_time of this UpdateDeploymentRequest.
        :rtype: int
        """
        return self._x_expired_time

    @x_expired_time.setter
    def x_expired_time(self, x_expired_time):
        """Sets the x_expired_time of this UpdateDeploymentRequest.

        离线场景超期时间，单位分钟，范围在1-86400

        :param x_expired_time: The x_expired_time of this UpdateDeploymentRequest.
        :type x_expired_time: int
        """
        self._x_expired_time = x_expired_time

    @property
    def body(self):
        """Gets the body of this UpdateDeploymentRequest.

        :return: The body of this UpdateDeploymentRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.DeploymentUpdateRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDeploymentRequest.

        :param body: The body of this UpdateDeploymentRequest.
        :type body: :class:`huaweicloudsdkhilens.v3.DeploymentUpdateRequest`
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
        if not isinstance(other, UpdateDeploymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
