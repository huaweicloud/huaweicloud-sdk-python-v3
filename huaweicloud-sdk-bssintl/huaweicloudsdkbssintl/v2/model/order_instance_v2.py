# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderInstanceV2:

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
        'resource_id': 'str',
        'resource_name': 'str',
        'region_code': 'str',
        'service_type_code': 'str',
        'resource_type_code': 'str',
        'resource_type_name': 'str',
        'service_type_name': 'str',
        'resource_spec_code': 'str',
        'project_id': 'str',
        'product_id': 'str',
        'parent_resource_id': 'str',
        'is_main_resource': 'int',
        'status': 'int',
        'effective_time': 'str',
        'expire_time': 'str',
        'expire_policy': 'int'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'region_code': 'region_code',
        'service_type_code': 'service_type_code',
        'resource_type_code': 'resource_type_code',
        'resource_type_name': 'resource_type_name',
        'service_type_name': 'service_type_name',
        'resource_spec_code': 'resource_spec_code',
        'project_id': 'project_id',
        'product_id': 'product_id',
        'parent_resource_id': 'parent_resource_id',
        'is_main_resource': 'is_main_resource',
        'status': 'status',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'expire_policy': 'expire_policy'
    }

    def __init__(self, id=None, resource_id=None, resource_name=None, region_code=None, service_type_code=None, resource_type_code=None, resource_type_name=None, service_type_name=None, resource_spec_code=None, project_id=None, product_id=None, parent_resource_id=None, is_main_resource=None, status=None, effective_time=None, expire_time=None, expire_policy=None):
        """OrderInstanceV2

        The model defined in huaweicloud sdk

        :param id: 标识要开通资源的内部ID，资源开通以后生成的ID为resource_id。
        :type id: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_name: 资源实例名。
        :type resource_name: str
        :param region_code: 云服务区编码，例如：“ap-southeast-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。
        :type region_code: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type service_type_code: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。
        :type resource_type_code: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type service_type_name: str
        :param resource_spec_code: 云服务产品的资源规格。如果是VM的资源规格，则需要在规格后面添加“.win”或“.linux”，例如“s2.small.1.linux”。
        :type resource_spec_code: str
        :param project_id: 资源项目ID。
        :type project_id: str
        :param product_id: 产品ID。
        :type product_id: str
        :param parent_resource_id: 父资源ID。
        :type parent_resource_id: str
        :param is_main_resource: 是否是主资源。 0：非主资源1：主资源
        :type is_main_resource: int
        :param status: 资源状态。 2：使用中3：已关闭（页面不展示这个状态）4：已冻结5：已过期
        :type status: int
        :param effective_time: 资源生效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type effective_time: str
        :param expire_time: 资源过期时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type expire_time: str
        :param expire_policy: 资源到期后的扣费策略： 0：到期进入宽限期1：到期转按需2：到期后自动删除（从生效中直接删除）3：到期后自动续费4：到期后冻结5：到期后删除（从保留期删除）  说明： 只有“3”表示该资源是自动续订，其他情况下，都是非自动续订下的到期策略。
        :type expire_policy: int
        """
        
        

        self._id = None
        self._resource_id = None
        self._resource_name = None
        self._region_code = None
        self._service_type_code = None
        self._resource_type_code = None
        self._resource_type_name = None
        self._service_type_name = None
        self._resource_spec_code = None
        self._project_id = None
        self._product_id = None
        self._parent_resource_id = None
        self._is_main_resource = None
        self._status = None
        self._effective_time = None
        self._expire_time = None
        self._expire_policy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if region_code is not None:
            self.region_code = region_code
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if service_type_name is not None:
            self.service_type_name = service_type_name
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if project_id is not None:
            self.project_id = project_id
        if product_id is not None:
            self.product_id = product_id
        if parent_resource_id is not None:
            self.parent_resource_id = parent_resource_id
        if is_main_resource is not None:
            self.is_main_resource = is_main_resource
        if status is not None:
            self.status = status
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if expire_policy is not None:
            self.expire_policy = expire_policy

    @property
    def id(self):
        """Gets the id of this OrderInstanceV2.

        标识要开通资源的内部ID，资源开通以后生成的ID为resource_id。

        :return: The id of this OrderInstanceV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderInstanceV2.

        标识要开通资源的内部ID，资源开通以后生成的ID为resource_id。

        :param id: The id of this OrderInstanceV2.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        """Gets the resource_id of this OrderInstanceV2.

        资源ID。

        :return: The resource_id of this OrderInstanceV2.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this OrderInstanceV2.

        资源ID。

        :param resource_id: The resource_id of this OrderInstanceV2.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this OrderInstanceV2.

        资源实例名。

        :return: The resource_name of this OrderInstanceV2.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this OrderInstanceV2.

        资源实例名。

        :param resource_name: The resource_name of this OrderInstanceV2.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def region_code(self):
        """Gets the region_code of this OrderInstanceV2.

        云服务区编码，例如：“ap-southeast-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region_code of this OrderInstanceV2.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this OrderInstanceV2.

        云服务区编码，例如：“ap-southeast-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region_code: The region_code of this OrderInstanceV2.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def service_type_code(self):
        """Gets the service_type_code of this OrderInstanceV2.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The service_type_code of this OrderInstanceV2.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this OrderInstanceV2.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param service_type_code: The service_type_code of this OrderInstanceV2.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this OrderInstanceV2.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :return: The resource_type_code of this OrderInstanceV2.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this OrderInstanceV2.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :param resource_type_code: The resource_type_code of this OrderInstanceV2.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this OrderInstanceV2.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this OrderInstanceV2.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this OrderInstanceV2.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this OrderInstanceV2.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def service_type_name(self):
        """Gets the service_type_name of this OrderInstanceV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The service_type_name of this OrderInstanceV2.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this OrderInstanceV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param service_type_name: The service_type_name of this OrderInstanceV2.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this OrderInstanceV2.

        云服务产品的资源规格。如果是VM的资源规格，则需要在规格后面添加“.win”或“.linux”，例如“s2.small.1.linux”。

        :return: The resource_spec_code of this OrderInstanceV2.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this OrderInstanceV2.

        云服务产品的资源规格。如果是VM的资源规格，则需要在规格后面添加“.win”或“.linux”，例如“s2.small.1.linux”。

        :param resource_spec_code: The resource_spec_code of this OrderInstanceV2.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def project_id(self):
        """Gets the project_id of this OrderInstanceV2.

        资源项目ID。

        :return: The project_id of this OrderInstanceV2.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this OrderInstanceV2.

        资源项目ID。

        :param project_id: The project_id of this OrderInstanceV2.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def product_id(self):
        """Gets the product_id of this OrderInstanceV2.

        产品ID。

        :return: The product_id of this OrderInstanceV2.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this OrderInstanceV2.

        产品ID。

        :param product_id: The product_id of this OrderInstanceV2.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def parent_resource_id(self):
        """Gets the parent_resource_id of this OrderInstanceV2.

        父资源ID。

        :return: The parent_resource_id of this OrderInstanceV2.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """Sets the parent_resource_id of this OrderInstanceV2.

        父资源ID。

        :param parent_resource_id: The parent_resource_id of this OrderInstanceV2.
        :type parent_resource_id: str
        """
        self._parent_resource_id = parent_resource_id

    @property
    def is_main_resource(self):
        """Gets the is_main_resource of this OrderInstanceV2.

        是否是主资源。 0：非主资源1：主资源

        :return: The is_main_resource of this OrderInstanceV2.
        :rtype: int
        """
        return self._is_main_resource

    @is_main_resource.setter
    def is_main_resource(self, is_main_resource):
        """Sets the is_main_resource of this OrderInstanceV2.

        是否是主资源。 0：非主资源1：主资源

        :param is_main_resource: The is_main_resource of this OrderInstanceV2.
        :type is_main_resource: int
        """
        self._is_main_resource = is_main_resource

    @property
    def status(self):
        """Gets the status of this OrderInstanceV2.

        资源状态。 2：使用中3：已关闭（页面不展示这个状态）4：已冻结5：已过期

        :return: The status of this OrderInstanceV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderInstanceV2.

        资源状态。 2：使用中3：已关闭（页面不展示这个状态）4：已冻结5：已过期

        :param status: The status of this OrderInstanceV2.
        :type status: int
        """
        self._status = status

    @property
    def effective_time(self):
        """Gets the effective_time of this OrderInstanceV2.

        资源生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The effective_time of this OrderInstanceV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this OrderInstanceV2.

        资源生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param effective_time: The effective_time of this OrderInstanceV2.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this OrderInstanceV2.

        资源过期时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The expire_time of this OrderInstanceV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this OrderInstanceV2.

        资源过期时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param expire_time: The expire_time of this OrderInstanceV2.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def expire_policy(self):
        """Gets the expire_policy of this OrderInstanceV2.

        资源到期后的扣费策略： 0：到期进入宽限期1：到期转按需2：到期后自动删除（从生效中直接删除）3：到期后自动续费4：到期后冻结5：到期后删除（从保留期删除）  说明： 只有“3”表示该资源是自动续订，其他情况下，都是非自动续订下的到期策略。

        :return: The expire_policy of this OrderInstanceV2.
        :rtype: int
        """
        return self._expire_policy

    @expire_policy.setter
    def expire_policy(self, expire_policy):
        """Sets the expire_policy of this OrderInstanceV2.

        资源到期后的扣费策略： 0：到期进入宽限期1：到期转按需2：到期后自动删除（从生效中直接删除）3：到期后自动续费4：到期后冻结5：到期后删除（从保留期删除）  说明： 只有“3”表示该资源是自动续订，其他情况下，都是非自动续订下的到期策略。

        :param expire_policy: The expire_policy of this OrderInstanceV2.
        :type expire_policy: int
        """
        self._expire_policy = expire_policy

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
        if not isinstance(other, OrderInstanceV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
