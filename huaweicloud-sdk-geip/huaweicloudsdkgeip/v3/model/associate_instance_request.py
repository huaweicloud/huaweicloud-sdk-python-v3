# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'binding_instance_service': 'str',
        'global_eip_id': 'str',
        'body': 'AssociateInstanceGlobalEipRequestBody'
    }

    attribute_map = {
        'binding_instance_service': 'binding-instance-service',
        'global_eip_id': 'global_eip_id',
        'body': 'body'
    }

    def __init__(self, binding_instance_service=None, global_eip_id=None, body=None):
        r"""AssociateInstanceRequest

        The model defined in huaweicloud sdk

        :param binding_instance_service: 绑定接口可以加，标识请求是从哪个服务调过来的
        :type binding_instance_service: str
        :param global_eip_id: 
        :type global_eip_id: str
        :param body: Body of the AssociateInstanceRequest
        :type body: :class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBody`
        """
        
        

        self._binding_instance_service = None
        self._global_eip_id = None
        self._body = None
        self.discriminator = None

        if binding_instance_service is not None:
            self.binding_instance_service = binding_instance_service
        self.global_eip_id = global_eip_id
        if body is not None:
            self.body = body

    @property
    def binding_instance_service(self):
        r"""Gets the binding_instance_service of this AssociateInstanceRequest.

        绑定接口可以加，标识请求是从哪个服务调过来的

        :return: The binding_instance_service of this AssociateInstanceRequest.
        :rtype: str
        """
        return self._binding_instance_service

    @binding_instance_service.setter
    def binding_instance_service(self, binding_instance_service):
        r"""Sets the binding_instance_service of this AssociateInstanceRequest.

        绑定接口可以加，标识请求是从哪个服务调过来的

        :param binding_instance_service: The binding_instance_service of this AssociateInstanceRequest.
        :type binding_instance_service: str
        """
        self._binding_instance_service = binding_instance_service

    @property
    def global_eip_id(self):
        r"""Gets the global_eip_id of this AssociateInstanceRequest.

        :return: The global_eip_id of this AssociateInstanceRequest.
        :rtype: str
        """
        return self._global_eip_id

    @global_eip_id.setter
    def global_eip_id(self, global_eip_id):
        r"""Sets the global_eip_id of this AssociateInstanceRequest.

        :param global_eip_id: The global_eip_id of this AssociateInstanceRequest.
        :type global_eip_id: str
        """
        self._global_eip_id = global_eip_id

    @property
    def body(self):
        r"""Gets the body of this AssociateInstanceRequest.

        :return: The body of this AssociateInstanceRequest.
        :rtype: :class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AssociateInstanceRequest.

        :param body: The body of this AssociateInstanceRequest.
        :type body: :class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBody`
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
        if not isinstance(other, AssociateInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
