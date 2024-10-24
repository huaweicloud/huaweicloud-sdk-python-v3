# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkNodeResourceDemand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'resource': 'ResourceDemand'
    }

    attribute_map = {
        'name': 'name',
        'resource': 'resource'
    }

    def __init__(self, name=None, resource=None):
        """WorkNodeResourceDemand

        The model defined in huaweicloud sdk

        :param name: 资源配置名称
        :type name: str
        :param resource: 
        :type resource: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDemand`
        """
        
        

        self._name = None
        self._resource = None
        self.discriminator = None

        self.name = name
        self.resource = resource

    @property
    def name(self):
        """Gets the name of this WorkNodeResourceDemand.

        资源配置名称

        :return: The name of this WorkNodeResourceDemand.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkNodeResourceDemand.

        资源配置名称

        :param name: The name of this WorkNodeResourceDemand.
        :type name: str
        """
        self._name = name

    @property
    def resource(self):
        """Gets the resource of this WorkNodeResourceDemand.

        :return: The resource of this WorkNodeResourceDemand.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDemand`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this WorkNodeResourceDemand.

        :param resource: The resource of this WorkNodeResourceDemand.
        :type resource: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDemand`
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
        if not isinstance(other, WorkNodeResourceDemand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
