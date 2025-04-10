# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteChatCompletionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'deployment_id': 'str',
        'body': 'ChatCompletionReq'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'deployment_id': 'deployment_id',
        'body': 'body'
    }

    def __init__(self, pool_id=None, deployment_id=None, body=None):
        r"""ExecuteChatCompletionRequest

        The model defined in huaweicloud sdk

        :param pool_id: 资源池ID
        :type pool_id: str
        :param deployment_id: 模型的部署ID
        :type deployment_id: str
        :param body: Body of the ExecuteChatCompletionRequest
        :type body: :class:`huaweicloudsdkpangulargemodels.v2.ChatCompletionReq`
        """
        
        

        self._pool_id = None
        self._deployment_id = None
        self._body = None
        self.discriminator = None

        self.pool_id = pool_id
        self.deployment_id = deployment_id
        if body is not None:
            self.body = body

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ExecuteChatCompletionRequest.

        资源池ID

        :return: The pool_id of this ExecuteChatCompletionRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ExecuteChatCompletionRequest.

        资源池ID

        :param pool_id: The pool_id of this ExecuteChatCompletionRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this ExecuteChatCompletionRequest.

        模型的部署ID

        :return: The deployment_id of this ExecuteChatCompletionRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this ExecuteChatCompletionRequest.

        模型的部署ID

        :param deployment_id: The deployment_id of this ExecuteChatCompletionRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def body(self):
        r"""Gets the body of this ExecuteChatCompletionRequest.

        :return: The body of this ExecuteChatCompletionRequest.
        :rtype: :class:`huaweicloudsdkpangulargemodels.v2.ChatCompletionReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ExecuteChatCompletionRequest.

        :param body: The body of this ExecuteChatCompletionRequest.
        :type body: :class:`huaweicloudsdkpangulargemodels.v2.ChatCompletionReq`
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
        if not isinstance(other, ExecuteChatCompletionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
