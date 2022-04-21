# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTypes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_type_code': 'str',
        'resource_type_name': 'str',
        'resource_type_desc': 'str',
        'service_type_code': 'str'
    }

    attribute_map = {
        'resource_type_code': 'resource_type_code',
        'resource_type_name': 'resource_type_name',
        'resource_type_desc': 'resource_type_desc',
        'service_type_code': 'service_type_code'
    }

    def __init__(self, resource_type_code=None, resource_type_name=None, resource_type_desc=None, service_type_code=None):
        """ResourceTypes

        The model defined in huaweicloud sdk

        :param resource_type_code: 资源类型的编码。例如ECS的VM为“hws.resource.type.vm”。
        :type resource_type_code: str
        :param resource_type_name: 资源类型的名称。
        :type resource_type_name: str
        :param resource_type_desc: 资源类型的描述。
        :type resource_type_desc: str
        :param service_type_code: 资源类型归属的服务类型编码。例如：hws.service.type.offline。
        :type service_type_code: str
        """
        
        

        self._resource_type_code = None
        self._resource_type_name = None
        self._resource_type_desc = None
        self._service_type_code = None
        self.discriminator = None

        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if resource_type_desc is not None:
            self.resource_type_desc = resource_type_desc
        if service_type_code is not None:
            self.service_type_code = service_type_code

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this ResourceTypes.

        资源类型的编码。例如ECS的VM为“hws.resource.type.vm”。

        :return: The resource_type_code of this ResourceTypes.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this ResourceTypes.

        资源类型的编码。例如ECS的VM为“hws.resource.type.vm”。

        :param resource_type_code: The resource_type_code of this ResourceTypes.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this ResourceTypes.

        资源类型的名称。

        :return: The resource_type_name of this ResourceTypes.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this ResourceTypes.

        资源类型的名称。

        :param resource_type_name: The resource_type_name of this ResourceTypes.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def resource_type_desc(self):
        """Gets the resource_type_desc of this ResourceTypes.

        资源类型的描述。

        :return: The resource_type_desc of this ResourceTypes.
        :rtype: str
        """
        return self._resource_type_desc

    @resource_type_desc.setter
    def resource_type_desc(self, resource_type_desc):
        """Sets the resource_type_desc of this ResourceTypes.

        资源类型的描述。

        :param resource_type_desc: The resource_type_desc of this ResourceTypes.
        :type resource_type_desc: str
        """
        self._resource_type_desc = resource_type_desc

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ResourceTypes.

        资源类型归属的服务类型编码。例如：hws.service.type.offline。

        :return: The service_type_code of this ResourceTypes.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ResourceTypes.

        资源类型归属的服务类型编码。例如：hws.service.type.offline。

        :param service_type_code: The service_type_code of this ResourceTypes.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

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
        if not isinstance(other, ResourceTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
