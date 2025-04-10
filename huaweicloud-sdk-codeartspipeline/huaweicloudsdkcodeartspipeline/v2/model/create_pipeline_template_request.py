# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePipelineTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'body': 'PipelineTemplateDTO'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'body': 'body'
    }

    def __init__(self, tenant_id=None, body=None):
        r"""CreatePipelineTemplateRequest

        The model defined in huaweicloud sdk

        :param tenant_id: 租户ID
        :type tenant_id: str
        :param body: Body of the CreatePipelineTemplateRequest
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineTemplateDTO`
        """
        
        

        self._tenant_id = None
        self._body = None
        self.discriminator = None

        self.tenant_id = tenant_id
        if body is not None:
            self.body = body

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CreatePipelineTemplateRequest.

        租户ID

        :return: The tenant_id of this CreatePipelineTemplateRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CreatePipelineTemplateRequest.

        租户ID

        :param tenant_id: The tenant_id of this CreatePipelineTemplateRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def body(self):
        r"""Gets the body of this CreatePipelineTemplateRequest.

        :return: The body of this CreatePipelineTemplateRequest.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineTemplateDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreatePipelineTemplateRequest.

        :param body: The body of this CreatePipelineTemplateRequest.
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineTemplateDTO`
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
        if not isinstance(other, CreatePipelineTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
