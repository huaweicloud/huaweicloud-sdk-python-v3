# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotaSetsRequest:

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
        'resource': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'resource': 'resource'
    }

    def __init__(self, tenant_id=None, resource=None):
        """ShowQuotaSetsRequest

        The model defined in huaweicloud sdk

        :param tenant_id: 租户ID。  可以从专属主机控制台查询，或者通过调用查询专属主机列表API获取。
        :type tenant_id: str
        :param resource: 配额类别。
        :type resource: str
        """
        
        

        self._tenant_id = None
        self._resource = None
        self.discriminator = None

        self.tenant_id = tenant_id
        if resource is not None:
            self.resource = resource

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ShowQuotaSetsRequest.

        租户ID。  可以从专属主机控制台查询，或者通过调用查询专属主机列表API获取。

        :return: The tenant_id of this ShowQuotaSetsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ShowQuotaSetsRequest.

        租户ID。  可以从专属主机控制台查询，或者通过调用查询专属主机列表API获取。

        :param tenant_id: The tenant_id of this ShowQuotaSetsRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def resource(self):
        """Gets the resource of this ShowQuotaSetsRequest.

        配额类别。

        :return: The resource of this ShowQuotaSetsRequest.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ShowQuotaSetsRequest.

        配额类别。

        :param resource: The resource of this ShowQuotaSetsRequest.
        :type resource: str
        """
        self._resource = resource

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
        if not isinstance(other, ShowQuotaSetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
