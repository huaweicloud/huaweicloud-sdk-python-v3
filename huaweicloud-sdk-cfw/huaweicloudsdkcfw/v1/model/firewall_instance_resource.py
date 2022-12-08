# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallInstanceResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'resource_size': 'int',
        'resource_size_measure_id': 'int'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'resource_size': 'resource_size',
        'resource_size_measure_id': 'resource_size_measure_id'
    }

    def __init__(self, resource_id=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, resource_size=None, resource_size_measure_id=None):
        """FirewallInstanceResource

        The model defined in huaweicloud sdk

        :param resource_id: 资源id
        :type resource_id: str
        :param cloud_service_type: 服务类型，用于CBC使用，特指：hws.service.type.cfw
        :type cloud_service_type: str
        :param resource_type: 资源类型，包括: 1、云防火墙:hws.resource.type.cfw 2、EIP:hws.resource.type.cfw.exp.eip 3、带宽:hws.resource.type.cfw.exp.bandwidth 4、VPC:hws.resource.type.cfw.exp.vpc 5、日志存储:hws.resource.type.cfw.exp.logaudit
        :type resource_type: str
        :param resource_spec_code: 库存单位码
        :type resource_spec_code: str
        :param resource_size: 资源数量
        :type resource_size: int
        :param resource_size_measure_id: 资源单位
        :type resource_size_measure_id: int
        """
        
        

        self._resource_id = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._resource_size = None
        self._resource_size_measure_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_size is not None:
            self.resource_size = resource_size
        if resource_size_measure_id is not None:
            self.resource_size_measure_id = resource_size_measure_id

    @property
    def resource_id(self):
        """Gets the resource_id of this FirewallInstanceResource.

        资源id

        :return: The resource_id of this FirewallInstanceResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this FirewallInstanceResource.

        资源id

        :param resource_id: The resource_id of this FirewallInstanceResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this FirewallInstanceResource.

        服务类型，用于CBC使用，特指：hws.service.type.cfw

        :return: The cloud_service_type of this FirewallInstanceResource.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this FirewallInstanceResource.

        服务类型，用于CBC使用，特指：hws.service.type.cfw

        :param cloud_service_type: The cloud_service_type of this FirewallInstanceResource.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this FirewallInstanceResource.

        资源类型，包括: 1、云防火墙:hws.resource.type.cfw 2、EIP:hws.resource.type.cfw.exp.eip 3、带宽:hws.resource.type.cfw.exp.bandwidth 4、VPC:hws.resource.type.cfw.exp.vpc 5、日志存储:hws.resource.type.cfw.exp.logaudit

        :return: The resource_type of this FirewallInstanceResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FirewallInstanceResource.

        资源类型，包括: 1、云防火墙:hws.resource.type.cfw 2、EIP:hws.resource.type.cfw.exp.eip 3、带宽:hws.resource.type.cfw.exp.bandwidth 4、VPC:hws.resource.type.cfw.exp.vpc 5、日志存储:hws.resource.type.cfw.exp.logaudit

        :param resource_type: The resource_type of this FirewallInstanceResource.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this FirewallInstanceResource.

        库存单位码

        :return: The resource_spec_code of this FirewallInstanceResource.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this FirewallInstanceResource.

        库存单位码

        :param resource_spec_code: The resource_spec_code of this FirewallInstanceResource.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_size(self):
        """Gets the resource_size of this FirewallInstanceResource.

        资源数量

        :return: The resource_size of this FirewallInstanceResource.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        """Sets the resource_size of this FirewallInstanceResource.

        资源数量

        :param resource_size: The resource_size of this FirewallInstanceResource.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def resource_size_measure_id(self):
        """Gets the resource_size_measure_id of this FirewallInstanceResource.

        资源单位

        :return: The resource_size_measure_id of this FirewallInstanceResource.
        :rtype: int
        """
        return self._resource_size_measure_id

    @resource_size_measure_id.setter
    def resource_size_measure_id(self, resource_size_measure_id):
        """Sets the resource_size_measure_id of this FirewallInstanceResource.

        资源单位

        :param resource_size_measure_id: The resource_size_measure_id of this FirewallInstanceResource.
        :type resource_size_measure_id: int
        """
        self._resource_size_measure_id = resource_size_measure_id

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
        if not isinstance(other, FirewallInstanceResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
