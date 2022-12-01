# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTaskRequest:

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
        'body': 'TaskRequest'
    }

    attribute_map = {
        'deployment_id': 'deployment_id',
        'body': 'body'
    }

    def __init__(self, deployment_id=None, body=None):
        """CreateTaskRequest

        The model defined in huaweicloud sdk

        :param deployment_id: 部署ID，从专业版HiLens控制台部署管理[获取部署列表](getDeploymentListUsingGET.xml)获取
        :type deployment_id: str
        :param body: Body of the CreateTaskRequest
        :type body: :class:`huaweicloudsdkhilens.v3.TaskRequest`
        """
        
        

        self._deployment_id = None
        self._body = None
        self.discriminator = None

        self.deployment_id = deployment_id
        if body is not None:
            self.body = body

    @property
    def deployment_id(self):
        """Gets the deployment_id of this CreateTaskRequest.

        部署ID，从专业版HiLens控制台部署管理[获取部署列表](getDeploymentListUsingGET.xml)获取

        :return: The deployment_id of this CreateTaskRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this CreateTaskRequest.

        部署ID，从专业版HiLens控制台部署管理[获取部署列表](getDeploymentListUsingGET.xml)获取

        :param deployment_id: The deployment_id of this CreateTaskRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def body(self):
        """Gets the body of this CreateTaskRequest.

        :return: The body of this CreateTaskRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.TaskRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateTaskRequest.

        :param body: The body of this CreateTaskRequest.
        :type body: :class:`huaweicloudsdkhilens.v3.TaskRequest`
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
        if not isinstance(other, CreateTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
