# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceResponse:

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
        'status': 'int',
        'expire_time': 'str',
        'resource_size': 'int'
    }

    attribute_map = {
        'resource_id': 'resourceId',
        'cloud_service_type': 'cloudServiceType',
        'resource_type': 'resourceType',
        'resource_spec_code': 'resourceSpecCode',
        'status': 'status',
        'expire_time': 'expireTime',
        'resource_size': 'resourceSize'
    }

    def __init__(self, resource_id=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, status=None, expire_time=None, resource_size=None):
        """ResourceResponse

        The model defined in huaweicloud sdk

        :param resource_id: 资源id
        :type resource_id: str
        :param cloud_service_type: 云服务产品对应的云服务类型
        :type cloud_service_type: str
        :param resource_type: 云服务产品的资源类型   - hws.resource.type.waf.payperuserequest : Web应用防火墙按需请求   - hws.resource.type.waf.payperusedomain：Web应用防火墙按需域名   - hws.resource.type.waf.payperuserule: Web应用防火墙按需规则
        :type resource_type: str
        :param resource_spec_code: 云服务产品的资源规格
        :type resource_spec_code: str
        :param status: 资源状态   - 0：解冻/正常   - 1：冻结   - 2：删除
        :type status: int
        :param expire_time: 资源到期时间
        :type expire_time: str
        :param resource_size: 资源数量
        :type resource_size: int
        """
        
        

        self._resource_id = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._status = None
        self._expire_time = None
        self._resource_size = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if status is not None:
            self.status = status
        if expire_time is not None:
            self.expire_time = expire_time
        if resource_size is not None:
            self.resource_size = resource_size

    @property
    def resource_id(self):
        """Gets the resource_id of this ResourceResponse.

        资源id

        :return: The resource_id of this ResourceResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResourceResponse.

        资源id

        :param resource_id: The resource_id of this ResourceResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this ResourceResponse.

        云服务产品对应的云服务类型

        :return: The cloud_service_type of this ResourceResponse.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this ResourceResponse.

        云服务产品对应的云服务类型

        :param cloud_service_type: The cloud_service_type of this ResourceResponse.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this ResourceResponse.

        云服务产品的资源类型   - hws.resource.type.waf.payperuserequest : Web应用防火墙按需请求   - hws.resource.type.waf.payperusedomain：Web应用防火墙按需域名   - hws.resource.type.waf.payperuserule: Web应用防火墙按需规则

        :return: The resource_type of this ResourceResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ResourceResponse.

        云服务产品的资源类型   - hws.resource.type.waf.payperuserequest : Web应用防火墙按需请求   - hws.resource.type.waf.payperusedomain：Web应用防火墙按需域名   - hws.resource.type.waf.payperuserule: Web应用防火墙按需规则

        :param resource_type: The resource_type of this ResourceResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this ResourceResponse.

        云服务产品的资源规格

        :return: The resource_spec_code of this ResourceResponse.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this ResourceResponse.

        云服务产品的资源规格

        :param resource_spec_code: The resource_spec_code of this ResourceResponse.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def status(self):
        """Gets the status of this ResourceResponse.

        资源状态   - 0：解冻/正常   - 1：冻结   - 2：删除

        :return: The status of this ResourceResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResourceResponse.

        资源状态   - 0：解冻/正常   - 1：冻结   - 2：删除

        :param status: The status of this ResourceResponse.
        :type status: int
        """
        self._status = status

    @property
    def expire_time(self):
        """Gets the expire_time of this ResourceResponse.

        资源到期时间

        :return: The expire_time of this ResourceResponse.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this ResourceResponse.

        资源到期时间

        :param expire_time: The expire_time of this ResourceResponse.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def resource_size(self):
        """Gets the resource_size of this ResourceResponse.

        资源数量

        :return: The resource_size of this ResourceResponse.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        """Sets the resource_size of this ResourceResponse.

        资源数量

        :param resource_size: The resource_size of this ResourceResponse.
        :type resource_size: int
        """
        self._resource_size = resource_size

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
        if not isinstance(other, ResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
