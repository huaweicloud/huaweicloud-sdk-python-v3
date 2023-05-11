# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPipelineTemplateDetailRequest:

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
        'template_id': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'template_id': 'template_id'
    }

    def __init__(self, tenant_id=None, template_id=None):
        """ShowPipelineTemplateDetailRequest

        The model defined in huaweicloud sdk

        :param tenant_id: 租户ID
        :type tenant_id: str
        :param template_id: 模板ID
        :type template_id: str
        """
        
        

        self._tenant_id = None
        self._template_id = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.template_id = template_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ShowPipelineTemplateDetailRequest.

        租户ID

        :return: The tenant_id of this ShowPipelineTemplateDetailRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ShowPipelineTemplateDetailRequest.

        租户ID

        :param tenant_id: The tenant_id of this ShowPipelineTemplateDetailRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def template_id(self):
        """Gets the template_id of this ShowPipelineTemplateDetailRequest.

        模板ID

        :return: The template_id of this ShowPipelineTemplateDetailRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ShowPipelineTemplateDetailRequest.

        模板ID

        :param template_id: The template_id of this ShowPipelineTemplateDetailRequest.
        :type template_id: str
        """
        self._template_id = template_id

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
        if not isinstance(other, ShowPipelineTemplateDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
