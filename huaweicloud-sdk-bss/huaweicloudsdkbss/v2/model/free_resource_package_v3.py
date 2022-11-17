# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FreeResourcePackageV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_instance_id': 'str',
        'order_id': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_scope': 'int',
        'effective_time': 'str',
        'expire_time': 'str',
        'status': 'int',
        'service_type_code': 'str',
        'service_type_name': 'str',
        'region_code': 'str',
        'source_type': 'int',
        'bundle_type': 'str',
        'quota_reuse_mode': 'int',
        'free_resources': 'list[FreeResourceV3]'
    }

    attribute_map = {
        'order_instance_id': 'order_instance_id',
        'order_id': 'order_id',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_scope': 'enterprise_project_scope',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'status': 'status',
        'service_type_code': 'service_type_code',
        'service_type_name': 'service_type_name',
        'region_code': 'region_code',
        'source_type': 'source_type',
        'bundle_type': 'bundle_type',
        'quota_reuse_mode': 'quota_reuse_mode',
        'free_resources': 'free_resources'
    }

    def __init__(self, order_instance_id=None, order_id=None, product_id=None, product_name=None, enterprise_project_id=None, enterprise_project_scope=None, effective_time=None, expire_time=None, status=None, service_type_code=None, service_type_name=None, region_code=None, source_type=None, bundle_type=None, quota_reuse_mode=None, free_resources=None):
        """FreeResourcePackageV3

        The model defined in huaweicloud sdk

        :param order_instance_id: 订购资源包产品后，系统生成的ID，是这个资源包列表的标识字段。
        :type order_instance_id: str
        :param order_id: 订单ID，如果source_type为“1：软开云赠送”，该字段为空。
        :type order_id: str
        :param product_id: 产品ID，即资源包ID。
        :type product_id: str
        :param product_name: 产品名称，即资源包名称。
        :type product_name: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param enterprise_project_scope: 企业项目应用范围： 0：应用所有1：应用到具体企业项目
        :type enterprise_project_scope: int
        :param effective_time: 生效时间，购买资源包的时间，格式UTC。
        :type effective_time: str
        :param expire_time: 失效时间，资源包到期时间，格式UTC。
        :type expire_time: str
        :param status: 状态： 0：未生效1：生效中2：已用完3：已失效4：已退订
        :type status: int
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type service_type_code: str
        :param service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type service_type_name: str
        :param region_code: 云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。
        :type region_code: str
        :param source_type: 资源包的来源类型： 0：订单1：软开云赠送
        :type source_type: int
        :param bundle_type: 套餐绑定类型： ATOMIC_PKG：原子套餐BUNDLE_PKG：组合套餐
        :type bundle_type: str
        :param quota_reuse_mode: 使用模式。 1：可重置表示购买的资源包能够按照一定的周期恢复使用量。例如购买一个1年的按需资源包，使用量是40G，可重置，重置周期为1个月，表示1年内每个月会给予40G的使用量。 2：不可重置表示购买的资源包的使用量不会恢复。例如购买一个1年的按需资源包，使用量是40G，不可重置，表示1年内一共给予40G的使用量。
        :type quota_reuse_mode: int
        :param free_resources: 资源套餐内的资源项信息（资源项ID级的详情），具体参见表3。
        :type free_resources: list[:class:`huaweicloudsdkbss.v2.FreeResourceV3`]
        """
        
        

        self._order_instance_id = None
        self._order_id = None
        self._product_id = None
        self._product_name = None
        self._enterprise_project_id = None
        self._enterprise_project_scope = None
        self._effective_time = None
        self._expire_time = None
        self._status = None
        self._service_type_code = None
        self._service_type_name = None
        self._region_code = None
        self._source_type = None
        self._bundle_type = None
        self._quota_reuse_mode = None
        self._free_resources = None
        self.discriminator = None

        if order_instance_id is not None:
            self.order_instance_id = order_instance_id
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_scope is not None:
            self.enterprise_project_scope = enterprise_project_scope
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if status is not None:
            self.status = status
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if service_type_name is not None:
            self.service_type_name = service_type_name
        if region_code is not None:
            self.region_code = region_code
        if source_type is not None:
            self.source_type = source_type
        if bundle_type is not None:
            self.bundle_type = bundle_type
        if quota_reuse_mode is not None:
            self.quota_reuse_mode = quota_reuse_mode
        if free_resources is not None:
            self.free_resources = free_resources

    @property
    def order_instance_id(self):
        """Gets the order_instance_id of this FreeResourcePackageV3.

        订购资源包产品后，系统生成的ID，是这个资源包列表的标识字段。

        :return: The order_instance_id of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._order_instance_id

    @order_instance_id.setter
    def order_instance_id(self, order_instance_id):
        """Sets the order_instance_id of this FreeResourcePackageV3.

        订购资源包产品后，系统生成的ID，是这个资源包列表的标识字段。

        :param order_instance_id: The order_instance_id of this FreeResourcePackageV3.
        :type order_instance_id: str
        """
        self._order_instance_id = order_instance_id

    @property
    def order_id(self):
        """Gets the order_id of this FreeResourcePackageV3.

        订单ID，如果source_type为“1：软开云赠送”，该字段为空。

        :return: The order_id of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this FreeResourcePackageV3.

        订单ID，如果source_type为“1：软开云赠送”，该字段为空。

        :param order_id: The order_id of this FreeResourcePackageV3.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this FreeResourcePackageV3.

        产品ID，即资源包ID。

        :return: The product_id of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this FreeResourcePackageV3.

        产品ID，即资源包ID。

        :param product_id: The product_id of this FreeResourcePackageV3.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this FreeResourcePackageV3.

        产品名称，即资源包名称。

        :return: The product_name of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this FreeResourcePackageV3.

        产品名称，即资源包名称。

        :param product_name: The product_name of this FreeResourcePackageV3.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this FreeResourcePackageV3.

        企业项目ID。

        :return: The enterprise_project_id of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this FreeResourcePackageV3.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this FreeResourcePackageV3.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_scope(self):
        """Gets the enterprise_project_scope of this FreeResourcePackageV3.

        企业项目应用范围： 0：应用所有1：应用到具体企业项目

        :return: The enterprise_project_scope of this FreeResourcePackageV3.
        :rtype: int
        """
        return self._enterprise_project_scope

    @enterprise_project_scope.setter
    def enterprise_project_scope(self, enterprise_project_scope):
        """Sets the enterprise_project_scope of this FreeResourcePackageV3.

        企业项目应用范围： 0：应用所有1：应用到具体企业项目

        :param enterprise_project_scope: The enterprise_project_scope of this FreeResourcePackageV3.
        :type enterprise_project_scope: int
        """
        self._enterprise_project_scope = enterprise_project_scope

    @property
    def effective_time(self):
        """Gets the effective_time of this FreeResourcePackageV3.

        生效时间，购买资源包的时间，格式UTC。

        :return: The effective_time of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this FreeResourcePackageV3.

        生效时间，购买资源包的时间，格式UTC。

        :param effective_time: The effective_time of this FreeResourcePackageV3.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this FreeResourcePackageV3.

        失效时间，资源包到期时间，格式UTC。

        :return: The expire_time of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this FreeResourcePackageV3.

        失效时间，资源包到期时间，格式UTC。

        :param expire_time: The expire_time of this FreeResourcePackageV3.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def status(self):
        """Gets the status of this FreeResourcePackageV3.

        状态： 0：未生效1：生效中2：已用完3：已失效4：已退订

        :return: The status of this FreeResourcePackageV3.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FreeResourcePackageV3.

        状态： 0：未生效1：生效中2：已用完3：已失效4：已退订

        :param status: The status of this FreeResourcePackageV3.
        :type status: int
        """
        self._status = status

    @property
    def service_type_code(self):
        """Gets the service_type_code of this FreeResourcePackageV3.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The service_type_code of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this FreeResourcePackageV3.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param service_type_code: The service_type_code of this FreeResourcePackageV3.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def service_type_name(self):
        """Gets the service_type_name of this FreeResourcePackageV3.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The service_type_name of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this FreeResourcePackageV3.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param service_type_name: The service_type_name of this FreeResourcePackageV3.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def region_code(self):
        """Gets the region_code of this FreeResourcePackageV3.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region_code of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this FreeResourcePackageV3.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region_code: The region_code of this FreeResourcePackageV3.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def source_type(self):
        """Gets the source_type of this FreeResourcePackageV3.

        资源包的来源类型： 0：订单1：软开云赠送

        :return: The source_type of this FreeResourcePackageV3.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this FreeResourcePackageV3.

        资源包的来源类型： 0：订单1：软开云赠送

        :param source_type: The source_type of this FreeResourcePackageV3.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def bundle_type(self):
        """Gets the bundle_type of this FreeResourcePackageV3.

        套餐绑定类型： ATOMIC_PKG：原子套餐BUNDLE_PKG：组合套餐

        :return: The bundle_type of this FreeResourcePackageV3.
        :rtype: str
        """
        return self._bundle_type

    @bundle_type.setter
    def bundle_type(self, bundle_type):
        """Sets the bundle_type of this FreeResourcePackageV3.

        套餐绑定类型： ATOMIC_PKG：原子套餐BUNDLE_PKG：组合套餐

        :param bundle_type: The bundle_type of this FreeResourcePackageV3.
        :type bundle_type: str
        """
        self._bundle_type = bundle_type

    @property
    def quota_reuse_mode(self):
        """Gets the quota_reuse_mode of this FreeResourcePackageV3.

        使用模式。 1：可重置表示购买的资源包能够按照一定的周期恢复使用量。例如购买一个1年的按需资源包，使用量是40G，可重置，重置周期为1个月，表示1年内每个月会给予40G的使用量。 2：不可重置表示购买的资源包的使用量不会恢复。例如购买一个1年的按需资源包，使用量是40G，不可重置，表示1年内一共给予40G的使用量。

        :return: The quota_reuse_mode of this FreeResourcePackageV3.
        :rtype: int
        """
        return self._quota_reuse_mode

    @quota_reuse_mode.setter
    def quota_reuse_mode(self, quota_reuse_mode):
        """Sets the quota_reuse_mode of this FreeResourcePackageV3.

        使用模式。 1：可重置表示购买的资源包能够按照一定的周期恢复使用量。例如购买一个1年的按需资源包，使用量是40G，可重置，重置周期为1个月，表示1年内每个月会给予40G的使用量。 2：不可重置表示购买的资源包的使用量不会恢复。例如购买一个1年的按需资源包，使用量是40G，不可重置，表示1年内一共给予40G的使用量。

        :param quota_reuse_mode: The quota_reuse_mode of this FreeResourcePackageV3.
        :type quota_reuse_mode: int
        """
        self._quota_reuse_mode = quota_reuse_mode

    @property
    def free_resources(self):
        """Gets the free_resources of this FreeResourcePackageV3.

        资源套餐内的资源项信息（资源项ID级的详情），具体参见表3。

        :return: The free_resources of this FreeResourcePackageV3.
        :rtype: list[:class:`huaweicloudsdkbss.v2.FreeResourceV3`]
        """
        return self._free_resources

    @free_resources.setter
    def free_resources(self, free_resources):
        """Sets the free_resources of this FreeResourcePackageV3.

        资源套餐内的资源项信息（资源项ID级的详情），具体参见表3。

        :param free_resources: The free_resources of this FreeResourcePackageV3.
        :type free_resources: list[:class:`huaweicloudsdkbss.v2.FreeResourceV3`]
        """
        self._free_resources = free_resources

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
        if not isinstance(other, FreeResourcePackageV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
