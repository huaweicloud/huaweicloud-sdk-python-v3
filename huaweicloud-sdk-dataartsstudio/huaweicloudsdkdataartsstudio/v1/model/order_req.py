# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'commodity_id': 'str',
        'product_id': 'str',
        'period_type': 'int',
        'period_num': 'int',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'security_group_id': 'str',
        'net_id': 'str',
        'instance_name': 'str',
        'eps_id': 'str',
        'is_auto_renew': 'int',
        'promotion_info': 'str',
        'extesion_package_type': 'str',
        'binding_instance_id': 'str',
        'cdm_version': 'str',
        'resource_spec_code': 'str',
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'tags': 'list[TmsTagDTO]'
    }

    attribute_map = {
        'region_id': 'region_id',
        'commodity_id': 'commodity_id',
        'product_id': 'product_id',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'security_group_id': 'security_group_id',
        'net_id': 'net_id',
        'instance_name': 'instance_name',
        'eps_id': 'eps_id',
        'is_auto_renew': 'is_auto_renew',
        'promotion_info': 'promotion_info',
        'extesion_package_type': 'extesion_package_type',
        'binding_instance_id': 'binding_instance_id',
        'cdm_version': 'cdm_version',
        'resource_spec_code': 'resource_spec_code',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'tags': 'tags'
    }

    def __init__(self, region_id=None, commodity_id=None, product_id=None, period_type=None, period_num=None, availability_zone=None, vpc_id=None, security_group_id=None, net_id=None, instance_name=None, eps_id=None, is_auto_renew=None, promotion_info=None, extesion_package_type=None, binding_instance_id=None, cdm_version=None, resource_spec_code=None, cloud_service_type=None, resource_type=None, tags=None):
        r"""OrderReq

        The model defined in huaweicloud sdk

        :param region_id: 区域Id
        :type region_id: str
        :param commodity_id: 订单Id
        :type commodity_id: str
        :param product_id: 产品Id
        :type product_id: str
        :param period_type: 购买周期类型（日月年）
        :type period_type: int
        :param period_num: 购买周期数
        :type period_num: int
        :param availability_zone: 可用区
        :type availability_zone: str
        :param vpc_id: 虚拟网卡Id
        :type vpc_id: str
        :param security_group_id: 安全组Id
        :type security_group_id: str
        :param net_id: 子网Id
        :type net_id: str
        :param instance_name: 实例名
        :type instance_name: str
        :param eps_id: 企业项目Id
        :type eps_id: str
        :param is_auto_renew: 是否续订
        :type is_auto_renew: int
        :param promotion_info: 促销信息
        :type promotion_info: str
        :param extesion_package_type: 实例附加增量包类型
        :type extesion_package_type: str
        :param binding_instance_id: 增量包绑定的实例id
        :type binding_instance_id: str
        :param cdm_version: cdm版本号
        :type cdm_version: str
        :param resource_spec_code: 实例规格编码
        :type resource_spec_code: str
        :param cloud_service_type: 云服务类型
        :type cloud_service_type: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param tags: tms标签
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.TmsTagDTO`]
        """
        
        

        self._region_id = None
        self._commodity_id = None
        self._product_id = None
        self._period_type = None
        self._period_num = None
        self._availability_zone = None
        self._vpc_id = None
        self._security_group_id = None
        self._net_id = None
        self._instance_name = None
        self._eps_id = None
        self._is_auto_renew = None
        self._promotion_info = None
        self._extesion_package_type = None
        self._binding_instance_id = None
        self._cdm_version = None
        self._resource_spec_code = None
        self._cloud_service_type = None
        self._resource_type = None
        self._tags = None
        self.discriminator = None

        self.region_id = region_id
        if commodity_id is not None:
            self.commodity_id = commodity_id
        if product_id is not None:
            self.product_id = product_id
        self.period_type = period_type
        self.period_num = period_num
        self.availability_zone = availability_zone
        self.vpc_id = vpc_id
        self.security_group_id = security_group_id
        self.net_id = net_id
        self.instance_name = instance_name
        self.eps_id = eps_id
        self.is_auto_renew = is_auto_renew
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if extesion_package_type is not None:
            self.extesion_package_type = extesion_package_type
        if binding_instance_id is not None:
            self.binding_instance_id = binding_instance_id
        if cdm_version is not None:
            self.cdm_version = cdm_version
        self.resource_spec_code = resource_spec_code
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if tags is not None:
            self.tags = tags

    @property
    def region_id(self):
        r"""Gets the region_id of this OrderReq.

        区域Id

        :return: The region_id of this OrderReq.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this OrderReq.

        区域Id

        :param region_id: The region_id of this OrderReq.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def commodity_id(self):
        r"""Gets the commodity_id of this OrderReq.

        订单Id

        :return: The commodity_id of this OrderReq.
        :rtype: str
        """
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, commodity_id):
        r"""Sets the commodity_id of this OrderReq.

        订单Id

        :param commodity_id: The commodity_id of this OrderReq.
        :type commodity_id: str
        """
        self._commodity_id = commodity_id

    @property
    def product_id(self):
        r"""Gets the product_id of this OrderReq.

        产品Id

        :return: The product_id of this OrderReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this OrderReq.

        产品Id

        :param product_id: The product_id of this OrderReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def period_type(self):
        r"""Gets the period_type of this OrderReq.

        购买周期类型（日月年）

        :return: The period_type of this OrderReq.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this OrderReq.

        购买周期类型（日月年）

        :param period_type: The period_type of this OrderReq.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this OrderReq.

        购买周期数

        :return: The period_num of this OrderReq.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this OrderReq.

        购买周期数

        :param period_num: The period_num of this OrderReq.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this OrderReq.

        可用区

        :return: The availability_zone of this OrderReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this OrderReq.

        可用区

        :param availability_zone: The availability_zone of this OrderReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this OrderReq.

        虚拟网卡Id

        :return: The vpc_id of this OrderReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this OrderReq.

        虚拟网卡Id

        :param vpc_id: The vpc_id of this OrderReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this OrderReq.

        安全组Id

        :return: The security_group_id of this OrderReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this OrderReq.

        安全组Id

        :param security_group_id: The security_group_id of this OrderReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def net_id(self):
        r"""Gets the net_id of this OrderReq.

        子网Id

        :return: The net_id of this OrderReq.
        :rtype: str
        """
        return self._net_id

    @net_id.setter
    def net_id(self, net_id):
        r"""Sets the net_id of this OrderReq.

        子网Id

        :param net_id: The net_id of this OrderReq.
        :type net_id: str
        """
        self._net_id = net_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this OrderReq.

        实例名

        :return: The instance_name of this OrderReq.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this OrderReq.

        实例名

        :param instance_name: The instance_name of this OrderReq.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def eps_id(self):
        r"""Gets the eps_id of this OrderReq.

        企业项目Id

        :return: The eps_id of this OrderReq.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this OrderReq.

        企业项目Id

        :param eps_id: The eps_id of this OrderReq.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this OrderReq.

        是否续订

        :return: The is_auto_renew of this OrderReq.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this OrderReq.

        是否续订

        :param is_auto_renew: The is_auto_renew of this OrderReq.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this OrderReq.

        促销信息

        :return: The promotion_info of this OrderReq.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this OrderReq.

        促销信息

        :param promotion_info: The promotion_info of this OrderReq.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def extesion_package_type(self):
        r"""Gets the extesion_package_type of this OrderReq.

        实例附加增量包类型

        :return: The extesion_package_type of this OrderReq.
        :rtype: str
        """
        return self._extesion_package_type

    @extesion_package_type.setter
    def extesion_package_type(self, extesion_package_type):
        r"""Sets the extesion_package_type of this OrderReq.

        实例附加增量包类型

        :param extesion_package_type: The extesion_package_type of this OrderReq.
        :type extesion_package_type: str
        """
        self._extesion_package_type = extesion_package_type

    @property
    def binding_instance_id(self):
        r"""Gets the binding_instance_id of this OrderReq.

        增量包绑定的实例id

        :return: The binding_instance_id of this OrderReq.
        :rtype: str
        """
        return self._binding_instance_id

    @binding_instance_id.setter
    def binding_instance_id(self, binding_instance_id):
        r"""Sets the binding_instance_id of this OrderReq.

        增量包绑定的实例id

        :param binding_instance_id: The binding_instance_id of this OrderReq.
        :type binding_instance_id: str
        """
        self._binding_instance_id = binding_instance_id

    @property
    def cdm_version(self):
        r"""Gets the cdm_version of this OrderReq.

        cdm版本号

        :return: The cdm_version of this OrderReq.
        :rtype: str
        """
        return self._cdm_version

    @cdm_version.setter
    def cdm_version(self, cdm_version):
        r"""Sets the cdm_version of this OrderReq.

        cdm版本号

        :param cdm_version: The cdm_version of this OrderReq.
        :type cdm_version: str
        """
        self._cdm_version = cdm_version

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this OrderReq.

        实例规格编码

        :return: The resource_spec_code of this OrderReq.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this OrderReq.

        实例规格编码

        :param resource_spec_code: The resource_spec_code of this OrderReq.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this OrderReq.

        云服务类型

        :return: The cloud_service_type of this OrderReq.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this OrderReq.

        云服务类型

        :param cloud_service_type: The cloud_service_type of this OrderReq.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this OrderReq.

        资源类型

        :return: The resource_type of this OrderReq.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this OrderReq.

        资源类型

        :param resource_type: The resource_type of this OrderReq.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def tags(self):
        r"""Gets the tags of this OrderReq.

        tms标签

        :return: The tags of this OrderReq.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TmsTagDTO`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this OrderReq.

        tms标签

        :param tags: The tags of this OrderReq.
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.TmsTagDTO`]
        """
        self._tags = tags

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
        if not isinstance(other, OrderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
