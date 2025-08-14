# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportResourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'str',
        'business_id': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'business_id': 'business_id'
    }

    def __init__(self, resource=None, business_id=None):
        r"""ExportResourceRequest

        The model defined in huaweicloud sdk

        :param resource: 资源名称
        :type resource: str
        :param business_id: 业务id,比如问答模板是传入skill_id
        :type business_id: str
        """
        
        

        self._resource = None
        self._business_id = None
        self.discriminator = None

        self.resource = resource
        if business_id is not None:
            self.business_id = business_id

    @property
    def resource(self):
        r"""Gets the resource of this ExportResourceRequest.

        资源名称

        :return: The resource of this ExportResourceRequest.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ExportResourceRequest.

        资源名称

        :param resource: The resource of this ExportResourceRequest.
        :type resource: str
        """
        self._resource = resource

    @property
    def business_id(self):
        r"""Gets the business_id of this ExportResourceRequest.

        业务id,比如问答模板是传入skill_id

        :return: The business_id of this ExportResourceRequest.
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        r"""Sets the business_id of this ExportResourceRequest.

        业务id,比如问答模板是传入skill_id

        :param business_id: The business_id of this ExportResourceRequest.
        :type business_id: str
        """
        self._business_id = business_id

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
        if not isinstance(other, ExportResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
