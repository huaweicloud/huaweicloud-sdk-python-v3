# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTenantVpcIgwRequest:

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
        'vpc_igw_id': 'str',
        'body': 'UpdateTenantVpcIgwRequestBody'
    }

    attribute_map = {
        'fields': 'fields',
        'vpc_igw_id': 'vpc_igw_id',
        'body': 'body'
    }

    def __init__(self, fields=None, vpc_igw_id=None, body=None):
        """UpdateTenantVpcIgwRequest

        The model defined in huaweicloud sdk

        :param fields: 形式为\\\&quot;fields&#x3D;id&amp;fields&#x3D;project_id&amp;...\\\&quot;，支持字段：id/project_id/vpc_id/created_at/updated_at/name
        :type fields: str
        :param vpc_igw_id: vpc-igw的uuid
        :type vpc_igw_id: str
        :param body: Body of the UpdateTenantVpcIgwRequest
        :type body: :class:`huaweicloudsdkeip.v3.UpdateTenantVpcIgwRequestBody`
        """
        
        

        self._fields = None
        self._vpc_igw_id = None
        self._body = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        self.vpc_igw_id = vpc_igw_id
        if body is not None:
            self.body = body

    @property
    def fields(self):
        """Gets the fields of this UpdateTenantVpcIgwRequest.

        形式为\\\"fields=id&fields=project_id&...\\\"，支持字段：id/project_id/vpc_id/created_at/updated_at/name

        :return: The fields of this UpdateTenantVpcIgwRequest.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this UpdateTenantVpcIgwRequest.

        形式为\\\"fields=id&fields=project_id&...\\\"，支持字段：id/project_id/vpc_id/created_at/updated_at/name

        :param fields: The fields of this UpdateTenantVpcIgwRequest.
        :type fields: str
        """
        self._fields = fields

    @property
    def vpc_igw_id(self):
        """Gets the vpc_igw_id of this UpdateTenantVpcIgwRequest.

        vpc-igw的uuid

        :return: The vpc_igw_id of this UpdateTenantVpcIgwRequest.
        :rtype: str
        """
        return self._vpc_igw_id

    @vpc_igw_id.setter
    def vpc_igw_id(self, vpc_igw_id):
        """Sets the vpc_igw_id of this UpdateTenantVpcIgwRequest.

        vpc-igw的uuid

        :param vpc_igw_id: The vpc_igw_id of this UpdateTenantVpcIgwRequest.
        :type vpc_igw_id: str
        """
        self._vpc_igw_id = vpc_igw_id

    @property
    def body(self):
        """Gets the body of this UpdateTenantVpcIgwRequest.

        :return: The body of this UpdateTenantVpcIgwRequest.
        :rtype: :class:`huaweicloudsdkeip.v3.UpdateTenantVpcIgwRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateTenantVpcIgwRequest.

        :param body: The body of this UpdateTenantVpcIgwRequest.
        :type body: :class:`huaweicloudsdkeip.v3.UpdateTenantVpcIgwRequestBody`
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
        if not isinstance(other, UpdateTenantVpcIgwRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
