# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'resource_size': 'int',
        'usage_factor': 'str',
        'usage_value': 'float',
        'usage_measure_id': 'int',
        'resource_size_measure_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'resource_size': 'resource_size',
        'usage_factor': 'usage_factor',
        'usage_value': 'usage_value',
        'usage_measure_id': 'usage_measure_id',
        'resource_size_measure_id': 'resource_size_measure_id'
    }

    def __init__(self, id=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, resource_size=None, usage_factor=None, usage_value=None, usage_measure_id=None, resource_size_measure_id=None):
        """ProductInfo

        The model defined in huaweicloud sdk

        :param id: ID标识，同一次询价中不能重复，用于标识返回询价结果和请求的映射关系。
        :type id: str
        :param cloud_service_type: 用户购买云服务产品的云服务类型，例如EC2，云服务类型为hws.service.type.ec2。
        :type cloud_service_type: str
        :param resource_type: 用户购买云服务产品的资源类型，例如EC2中的VM，资源类型为hws.resource.type.vm。
        :type resource_type: str
        :param resource_spec_code: 用户购买云服务产品的资源规格，例如VM的小型规格，资源规格为m1.tiny。
        :type resource_spec_code: str
        :param resource_size: 资源容量度量标识。
        :type resource_size: int
        :param usage_factor: 使用量因子，按需计费必填，取值和话单中的使用量因子一致，云服务和使用量因子对应关系如下： - Duration：云服务器 - flow：流量
        :type usage_factor: str
        :param usage_value: 使用量值，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时。
        :type usage_value: float
        :param usage_measure_id: 使用量单位标识，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时。 - 4：小时 - 10：GB - 11：MB - 13：Byte - 17：FLOW_GB
        :type usage_measure_id: int
        :param resource_size_measure_id: 资源容量大小，例如购买的卷大小或带宽大小。
        :type resource_size_measure_id: int
        """
        
        

        self._id = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._resource_size = None
        self._usage_factor = None
        self._usage_value = None
        self._usage_measure_id = None
        self._resource_size_measure_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_size is not None:
            self.resource_size = resource_size
        if usage_factor is not None:
            self.usage_factor = usage_factor
        if usage_value is not None:
            self.usage_value = usage_value
        if usage_measure_id is not None:
            self.usage_measure_id = usage_measure_id
        if resource_size_measure_id is not None:
            self.resource_size_measure_id = resource_size_measure_id

    @property
    def id(self):
        """Gets the id of this ProductInfo.

        ID标识，同一次询价中不能重复，用于标识返回询价结果和请求的映射关系。

        :return: The id of this ProductInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductInfo.

        ID标识，同一次询价中不能重复，用于标识返回询价结果和请求的映射关系。

        :param id: The id of this ProductInfo.
        :type id: str
        """
        self._id = id

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this ProductInfo.

        用户购买云服务产品的云服务类型，例如EC2，云服务类型为hws.service.type.ec2。

        :return: The cloud_service_type of this ProductInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this ProductInfo.

        用户购买云服务产品的云服务类型，例如EC2，云服务类型为hws.service.type.ec2。

        :param cloud_service_type: The cloud_service_type of this ProductInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this ProductInfo.

        用户购买云服务产品的资源类型，例如EC2中的VM，资源类型为hws.resource.type.vm。

        :return: The resource_type of this ProductInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ProductInfo.

        用户购买云服务产品的资源类型，例如EC2中的VM，资源类型为hws.resource.type.vm。

        :param resource_type: The resource_type of this ProductInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this ProductInfo.

        用户购买云服务产品的资源规格，例如VM的小型规格，资源规格为m1.tiny。

        :return: The resource_spec_code of this ProductInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this ProductInfo.

        用户购买云服务产品的资源规格，例如VM的小型规格，资源规格为m1.tiny。

        :param resource_spec_code: The resource_spec_code of this ProductInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_size(self):
        """Gets the resource_size of this ProductInfo.

        资源容量度量标识。

        :return: The resource_size of this ProductInfo.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        """Sets the resource_size of this ProductInfo.

        资源容量度量标识。

        :param resource_size: The resource_size of this ProductInfo.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def usage_factor(self):
        """Gets the usage_factor of this ProductInfo.

        使用量因子，按需计费必填，取值和话单中的使用量因子一致，云服务和使用量因子对应关系如下： - Duration：云服务器 - flow：流量

        :return: The usage_factor of this ProductInfo.
        :rtype: str
        """
        return self._usage_factor

    @usage_factor.setter
    def usage_factor(self, usage_factor):
        """Sets the usage_factor of this ProductInfo.

        使用量因子，按需计费必填，取值和话单中的使用量因子一致，云服务和使用量因子对应关系如下： - Duration：云服务器 - flow：流量

        :param usage_factor: The usage_factor of this ProductInfo.
        :type usage_factor: str
        """
        self._usage_factor = usage_factor

    @property
    def usage_value(self):
        """Gets the usage_value of this ProductInfo.

        使用量值，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时。

        :return: The usage_value of this ProductInfo.
        :rtype: float
        """
        return self._usage_value

    @usage_value.setter
    def usage_value(self, usage_value):
        """Sets the usage_value of this ProductInfo.

        使用量值，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时。

        :param usage_value: The usage_value of this ProductInfo.
        :type usage_value: float
        """
        self._usage_value = usage_value

    @property
    def usage_measure_id(self):
        """Gets the usage_measure_id of this ProductInfo.

        使用量单位标识，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时。 - 4：小时 - 10：GB - 11：MB - 13：Byte - 17：FLOW_GB

        :return: The usage_measure_id of this ProductInfo.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        """Sets the usage_measure_id of this ProductInfo.

        使用量单位标识，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时。 - 4：小时 - 10：GB - 11：MB - 13：Byte - 17：FLOW_GB

        :param usage_measure_id: The usage_measure_id of this ProductInfo.
        :type usage_measure_id: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def resource_size_measure_id(self):
        """Gets the resource_size_measure_id of this ProductInfo.

        资源容量大小，例如购买的卷大小或带宽大小。

        :return: The resource_size_measure_id of this ProductInfo.
        :rtype: int
        """
        return self._resource_size_measure_id

    @resource_size_measure_id.setter
    def resource_size_measure_id(self, resource_size_measure_id):
        """Sets the resource_size_measure_id of this ProductInfo.

        资源容量大小，例如购买的卷大小或带宽大小。

        :param resource_size_measure_id: The resource_size_measure_id of this ProductInfo.
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
        if not isinstance(other, ProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
