# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UsageType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'name': 'str',
        'resource_type_code': 'str',
        'service_type_code': 'str',
        'resource_type_name': 'str',
        'service_type_name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'resource_type_code': 'resource_type_code',
        'service_type_code': 'service_type_code',
        'resource_type_name': 'resource_type_name',
        'service_type_name': 'service_type_name'
    }

    def __init__(self, code=None, name=None, resource_type_code=None, service_type_code=None, resource_type_name=None, service_type_name=None):
        """UsageType

        The model defined in huaweicloud sdk

        :param code: 使用量类型编码。如：reqNumber。
        :type code: str
        :param name: 使用量类型名称。如：调用次数。
        :type name: str
        :param resource_type_code: 资源类型编码。例如ECS的VM为“hws.resource.type.vm”。
        :type resource_type_code: str
        :param service_type_code: 云服务类型编码。例如OBS的云服务类型编码为“hws.service.type.obs”。
        :type service_type_code: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type service_type_name: str
        """
        
        

        self._code = None
        self._name = None
        self._resource_type_code = None
        self._service_type_code = None
        self._resource_type_name = None
        self._service_type_name = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if service_type_name is not None:
            self.service_type_name = service_type_name

    @property
    def code(self):
        """Gets the code of this UsageType.

        使用量类型编码。如：reqNumber。

        :return: The code of this UsageType.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this UsageType.

        使用量类型编码。如：reqNumber。

        :param code: The code of this UsageType.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this UsageType.

        使用量类型名称。如：调用次数。

        :return: The name of this UsageType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UsageType.

        使用量类型名称。如：调用次数。

        :param name: The name of this UsageType.
        :type name: str
        """
        self._name = name

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this UsageType.

        资源类型编码。例如ECS的VM为“hws.resource.type.vm”。

        :return: The resource_type_code of this UsageType.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this UsageType.

        资源类型编码。例如ECS的VM为“hws.resource.type.vm”。

        :param resource_type_code: The resource_type_code of this UsageType.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def service_type_code(self):
        """Gets the service_type_code of this UsageType.

        云服务类型编码。例如OBS的云服务类型编码为“hws.service.type.obs”。

        :return: The service_type_code of this UsageType.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this UsageType.

        云服务类型编码。例如OBS的云服务类型编码为“hws.service.type.obs”。

        :param service_type_code: The service_type_code of this UsageType.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this UsageType.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this UsageType.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this UsageType.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this UsageType.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def service_type_name(self):
        """Gets the service_type_name of this UsageType.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The service_type_name of this UsageType.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this UsageType.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param service_type_name: The service_type_name of this UsageType.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

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
        if not isinstance(other, UsageType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
