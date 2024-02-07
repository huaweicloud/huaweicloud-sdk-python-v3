# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTenantVpcIgwRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'str',
        'body': 'CreateTenantVpcIgwRequestBody'
    }

    attribute_map = {
        'fields': 'fields',
        'body': 'body'
    }

    def __init__(self, fields=None, body=None):
        """CreateTenantVpcIgwRequest

        The model defined in huaweicloud sdk

        :param fields: 形式为\\\&quot;fields&#x3D;id&amp;fields&#x3D;project_id&amp;...\\\&quot;，支持字段：id/project_id/vpc_id/created_at/updated_at/name
        :type fields: str
        :param body: Body of the CreateTenantVpcIgwRequest
        :type body: :class:`huaweicloudsdkeip.v3.CreateTenantVpcIgwRequestBody`
        """
        
        

        self._fields = None
        self._body = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if body is not None:
            self.body = body

    @property
    def fields(self):
        """Gets the fields of this CreateTenantVpcIgwRequest.

        形式为\\\"fields=id&fields=project_id&...\\\"，支持字段：id/project_id/vpc_id/created_at/updated_at/name

        :return: The fields of this CreateTenantVpcIgwRequest.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CreateTenantVpcIgwRequest.

        形式为\\\"fields=id&fields=project_id&...\\\"，支持字段：id/project_id/vpc_id/created_at/updated_at/name

        :param fields: The fields of this CreateTenantVpcIgwRequest.
        :type fields: str
        """
        self._fields = fields

    @property
    def body(self):
        """Gets the body of this CreateTenantVpcIgwRequest.

        :return: The body of this CreateTenantVpcIgwRequest.
        :rtype: :class:`huaweicloudsdkeip.v3.CreateTenantVpcIgwRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateTenantVpcIgwRequest.

        :param body: The body of this CreateTenantVpcIgwRequest.
        :type body: :class:`huaweicloudsdkeip.v3.CreateTenantVpcIgwRequestBody`
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
        if not isinstance(other, CreateTenantVpcIgwRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
