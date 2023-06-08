# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployApplicationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_id': 'str',
        'app_id': 'str',
        'body': 'DeployApplicationRequestBody'
    }

    attribute_map = {
        'env_id': 'env_id',
        'app_id': 'app_id',
        'body': 'body'
    }

    def __init__(self, env_id=None, app_id=None, body=None):
        """DeployApplicationRequest

        The model defined in huaweicloud sdk

        :param env_id: 运行服务ID。
        :type env_id: str
        :param app_id: 待部署应用的ID。
        :type app_id: str
        :param body: Body of the DeployApplicationRequest
        :type body: :class:`huaweicloudsdkidme.v1.DeployApplicationRequestBody`
        """
        
        

        self._env_id = None
        self._app_id = None
        self._body = None
        self.discriminator = None

        self.env_id = env_id
        self.app_id = app_id
        if body is not None:
            self.body = body

    @property
    def env_id(self):
        """Gets the env_id of this DeployApplicationRequest.

        运行服务ID。

        :return: The env_id of this DeployApplicationRequest.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this DeployApplicationRequest.

        运行服务ID。

        :param env_id: The env_id of this DeployApplicationRequest.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def app_id(self):
        """Gets the app_id of this DeployApplicationRequest.

        待部署应用的ID。

        :return: The app_id of this DeployApplicationRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this DeployApplicationRequest.

        待部署应用的ID。

        :param app_id: The app_id of this DeployApplicationRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def body(self):
        """Gets the body of this DeployApplicationRequest.

        :return: The body of this DeployApplicationRequest.
        :rtype: :class:`huaweicloudsdkidme.v1.DeployApplicationRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeployApplicationRequest.

        :param body: The body of this DeployApplicationRequest.
        :type body: :class:`huaweicloudsdkidme.v1.DeployApplicationRequestBody`
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
        if not isinstance(other, DeployApplicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
