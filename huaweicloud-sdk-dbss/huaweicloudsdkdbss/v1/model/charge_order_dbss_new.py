# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChargeOrderDbssNew:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[ResourceTagInfoBean]',
        'asset_nums': 'int',
        'availability_zone': 'str',
        'charging_mode': 'int',
        'cloud_service_type': 'str',
        'comment': 'str',
        'composite_product_id': 'str',
        'deploy_mode': 'str',
        'discount_id': 'str',
        'enterprise_project_id': 'str',
        'flavor_ref': 'str',
        'hx_password': 'str',
        'image_business_type': 'int',
        'is_auto_renew': 'int',
        'name': 'str',
        'nics': 'list[Nic]',
        'outside_ins_config': 'OutsideInsConfig',
        'period_num': 'int',
        'period_type': 'int',
        'product_infos': 'list[ProductInfoBeanNew]',
        'promotion_activity_id': 'str',
        'promotion_info': 'str',
        'public_ip': 'PublicIp',
        'region_id': 'str',
        'security_groups': 'list[SecurityGroup]',
        'subscription_num': 'int',
        'vpc_id': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'asset_nums': 'asset_nums',
        'availability_zone': 'availability_zone',
        'charging_mode': 'charging_mode',
        'cloud_service_type': 'cloud_service_type',
        'comment': 'comment',
        'composite_product_id': 'composite_product_id',
        'deploy_mode': 'deploy_mode',
        'discount_id': 'discount_id',
        'enterprise_project_id': 'enterprise_project_id',
        'flavor_ref': 'flavor_ref',
        'hx_password': 'hx_password',
        'image_business_type': 'image_business_type',
        'is_auto_renew': 'is_auto_renew',
        'name': 'name',
        'nics': 'nics',
        'outside_ins_config': 'outside_ins_config',
        'period_num': 'period_num',
        'period_type': 'period_type',
        'product_infos': 'product_infos',
        'promotion_activity_id': 'promotion_activity_id',
        'promotion_info': 'promotion_info',
        'public_ip': 'public_ip',
        'region_id': 'region_id',
        'security_groups': 'security_groups',
        'subscription_num': 'subscription_num',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, tags=None, asset_nums=None, availability_zone=None, charging_mode=None, cloud_service_type=None, comment=None, composite_product_id=None, deploy_mode=None, discount_id=None, enterprise_project_id=None, flavor_ref=None, hx_password=None, image_business_type=None, is_auto_renew=None, name=None, nics=None, outside_ins_config=None, period_num=None, period_type=None, product_infos=None, promotion_activity_id=None, promotion_info=None, public_ip=None, region_id=None, security_groups=None, subscription_num=None, vpc_id=None):
        r"""ChargeOrderDbssNew

        The model defined in huaweicloud sdk

        :param tags: 资源标签列表
        :type tags: list[:class:`huaweicloudsdkdbss.v1.ResourceTagInfoBean`]
        :param asset_nums: 资产数量
        :type asset_nums: int
        :param availability_zone: 可用分区
        :type availability_zone: str
        :param charging_mode: 计费模式
        :type charging_mode: int
        :param cloud_service_type: 服务类型
        :type cloud_service_type: str
        :param comment: 备注信息
        :type comment: str
        :param composite_product_id: 组合套餐
        :type composite_product_id: str
        :param deploy_mode: 实例部署方式，默认为云上 - CLOUD： 云上 - OUTSIDE：云外
        :type deploy_mode: str
        :param discount_id: 折扣ID
        :type discount_id: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param flavor_ref: ECS规格ID
        :type flavor_ref: str
        :param hx_password: 前端登录密码
        :type hx_password: str
        :param image_business_type: 镜像业务类型
        :type image_business_type: int
        :param is_auto_renew: 自费续费  - 1：自动  - 0：不自动
        :type is_auto_renew: int
        :param name: 实例名称
        :type name: str
        :param nics: 网卡信息
        :type nics: list[:class:`huaweicloudsdkdbss.v1.Nic`]
        :param outside_ins_config: 
        :type outside_ins_config: :class:`huaweicloudsdkdbss.v1.OutsideInsConfig`
        :param period_num: 订购周期数目
        :type period_num: int
        :param period_type: 订购周期类型
        :type period_type: int
        :param product_infos: 产品列表
        :type product_infos: list[:class:`huaweicloudsdkdbss.v1.ProductInfoBeanNew`]
        :param promotion_activity_id: 促销ID
        :type promotion_activity_id: str
        :param promotion_info: 折扣信息
        :type promotion_info: str
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkdbss.v1.PublicIp`
        :param region_id: 区域ID
        :type region_id: str
        :param security_groups: 安全组信息
        :type security_groups: list[:class:`huaweicloudsdkdbss.v1.SecurityGroup`]
        :param subscription_num: 订购数量，当前仅支持1台
        :type subscription_num: int
        :param vpc_id: VPC ID
        :type vpc_id: str
        """
        
        

        self._tags = None
        self._asset_nums = None
        self._availability_zone = None
        self._charging_mode = None
        self._cloud_service_type = None
        self._comment = None
        self._composite_product_id = None
        self._deploy_mode = None
        self._discount_id = None
        self._enterprise_project_id = None
        self._flavor_ref = None
        self._hx_password = None
        self._image_business_type = None
        self._is_auto_renew = None
        self._name = None
        self._nics = None
        self._outside_ins_config = None
        self._period_num = None
        self._period_type = None
        self._product_infos = None
        self._promotion_activity_id = None
        self._promotion_info = None
        self._public_ip = None
        self._region_id = None
        self._security_groups = None
        self._subscription_num = None
        self._vpc_id = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        self.asset_nums = asset_nums
        self.availability_zone = availability_zone
        self.charging_mode = charging_mode
        self.cloud_service_type = cloud_service_type
        if comment is not None:
            self.comment = comment
        if composite_product_id is not None:
            self.composite_product_id = composite_product_id
        self.deploy_mode = deploy_mode
        if discount_id is not None:
            self.discount_id = discount_id
        self.enterprise_project_id = enterprise_project_id
        self.flavor_ref = flavor_ref
        self.hx_password = hx_password
        self.image_business_type = image_business_type
        self.is_auto_renew = is_auto_renew
        self.name = name
        self.nics = nics
        if outside_ins_config is not None:
            self.outside_ins_config = outside_ins_config
        self.period_num = period_num
        self.period_type = period_type
        self.product_infos = product_infos
        if promotion_activity_id is not None:
            self.promotion_activity_id = promotion_activity_id
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if public_ip is not None:
            self.public_ip = public_ip
        if region_id is not None:
            self.region_id = region_id
        self.security_groups = security_groups
        self.subscription_num = subscription_num
        self.vpc_id = vpc_id

    @property
    def tags(self):
        r"""Gets the tags of this ChargeOrderDbssNew.

        资源标签列表

        :return: The tags of this ChargeOrderDbssNew.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.ResourceTagInfoBean`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ChargeOrderDbssNew.

        资源标签列表

        :param tags: The tags of this ChargeOrderDbssNew.
        :type tags: list[:class:`huaweicloudsdkdbss.v1.ResourceTagInfoBean`]
        """
        self._tags = tags

    @property
    def asset_nums(self):
        r"""Gets the asset_nums of this ChargeOrderDbssNew.

        资产数量

        :return: The asset_nums of this ChargeOrderDbssNew.
        :rtype: int
        """
        return self._asset_nums

    @asset_nums.setter
    def asset_nums(self, asset_nums):
        r"""Sets the asset_nums of this ChargeOrderDbssNew.

        资产数量

        :param asset_nums: The asset_nums of this ChargeOrderDbssNew.
        :type asset_nums: int
        """
        self._asset_nums = asset_nums

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ChargeOrderDbssNew.

        可用分区

        :return: The availability_zone of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ChargeOrderDbssNew.

        可用分区

        :param availability_zone: The availability_zone of this ChargeOrderDbssNew.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ChargeOrderDbssNew.

        计费模式

        :return: The charging_mode of this ChargeOrderDbssNew.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ChargeOrderDbssNew.

        计费模式

        :param charging_mode: The charging_mode of this ChargeOrderDbssNew.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ChargeOrderDbssNew.

        服务类型

        :return: The cloud_service_type of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ChargeOrderDbssNew.

        服务类型

        :param cloud_service_type: The cloud_service_type of this ChargeOrderDbssNew.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def comment(self):
        r"""Gets the comment of this ChargeOrderDbssNew.

        备注信息

        :return: The comment of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this ChargeOrderDbssNew.

        备注信息

        :param comment: The comment of this ChargeOrderDbssNew.
        :type comment: str
        """
        self._comment = comment

    @property
    def composite_product_id(self):
        r"""Gets the composite_product_id of this ChargeOrderDbssNew.

        组合套餐

        :return: The composite_product_id of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._composite_product_id

    @composite_product_id.setter
    def composite_product_id(self, composite_product_id):
        r"""Sets the composite_product_id of this ChargeOrderDbssNew.

        组合套餐

        :param composite_product_id: The composite_product_id of this ChargeOrderDbssNew.
        :type composite_product_id: str
        """
        self._composite_product_id = composite_product_id

    @property
    def deploy_mode(self):
        r"""Gets the deploy_mode of this ChargeOrderDbssNew.

        实例部署方式，默认为云上 - CLOUD： 云上 - OUTSIDE：云外

        :return: The deploy_mode of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        r"""Sets the deploy_mode of this ChargeOrderDbssNew.

        实例部署方式，默认为云上 - CLOUD： 云上 - OUTSIDE：云外

        :param deploy_mode: The deploy_mode of this ChargeOrderDbssNew.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

    @property
    def discount_id(self):
        r"""Gets the discount_id of this ChargeOrderDbssNew.

        折扣ID

        :return: The discount_id of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        r"""Sets the discount_id of this ChargeOrderDbssNew.

        折扣ID

        :param discount_id: The discount_id of this ChargeOrderDbssNew.
        :type discount_id: str
        """
        self._discount_id = discount_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ChargeOrderDbssNew.

        企业项目ID

        :return: The enterprise_project_id of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ChargeOrderDbssNew.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ChargeOrderDbssNew.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this ChargeOrderDbssNew.

        ECS规格ID

        :return: The flavor_ref of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this ChargeOrderDbssNew.

        ECS规格ID

        :param flavor_ref: The flavor_ref of this ChargeOrderDbssNew.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def hx_password(self):
        r"""Gets the hx_password of this ChargeOrderDbssNew.

        前端登录密码

        :return: The hx_password of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._hx_password

    @hx_password.setter
    def hx_password(self, hx_password):
        r"""Sets the hx_password of this ChargeOrderDbssNew.

        前端登录密码

        :param hx_password: The hx_password of this ChargeOrderDbssNew.
        :type hx_password: str
        """
        self._hx_password = hx_password

    @property
    def image_business_type(self):
        r"""Gets the image_business_type of this ChargeOrderDbssNew.

        镜像业务类型

        :return: The image_business_type of this ChargeOrderDbssNew.
        :rtype: int
        """
        return self._image_business_type

    @image_business_type.setter
    def image_business_type(self, image_business_type):
        r"""Sets the image_business_type of this ChargeOrderDbssNew.

        镜像业务类型

        :param image_business_type: The image_business_type of this ChargeOrderDbssNew.
        :type image_business_type: int
        """
        self._image_business_type = image_business_type

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this ChargeOrderDbssNew.

        自费续费  - 1：自动  - 0：不自动

        :return: The is_auto_renew of this ChargeOrderDbssNew.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this ChargeOrderDbssNew.

        自费续费  - 1：自动  - 0：不自动

        :param is_auto_renew: The is_auto_renew of this ChargeOrderDbssNew.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def name(self):
        r"""Gets the name of this ChargeOrderDbssNew.

        实例名称

        :return: The name of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ChargeOrderDbssNew.

        实例名称

        :param name: The name of this ChargeOrderDbssNew.
        :type name: str
        """
        self._name = name

    @property
    def nics(self):
        r"""Gets the nics of this ChargeOrderDbssNew.

        网卡信息

        :return: The nics of this ChargeOrderDbssNew.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        r"""Sets the nics of this ChargeOrderDbssNew.

        网卡信息

        :param nics: The nics of this ChargeOrderDbssNew.
        :type nics: list[:class:`huaweicloudsdkdbss.v1.Nic`]
        """
        self._nics = nics

    @property
    def outside_ins_config(self):
        r"""Gets the outside_ins_config of this ChargeOrderDbssNew.

        :return: The outside_ins_config of this ChargeOrderDbssNew.
        :rtype: :class:`huaweicloudsdkdbss.v1.OutsideInsConfig`
        """
        return self._outside_ins_config

    @outside_ins_config.setter
    def outside_ins_config(self, outside_ins_config):
        r"""Sets the outside_ins_config of this ChargeOrderDbssNew.

        :param outside_ins_config: The outside_ins_config of this ChargeOrderDbssNew.
        :type outside_ins_config: :class:`huaweicloudsdkdbss.v1.OutsideInsConfig`
        """
        self._outside_ins_config = outside_ins_config

    @property
    def period_num(self):
        r"""Gets the period_num of this ChargeOrderDbssNew.

        订购周期数目

        :return: The period_num of this ChargeOrderDbssNew.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ChargeOrderDbssNew.

        订购周期数目

        :param period_num: The period_num of this ChargeOrderDbssNew.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def period_type(self):
        r"""Gets the period_type of this ChargeOrderDbssNew.

        订购周期类型

        :return: The period_type of this ChargeOrderDbssNew.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ChargeOrderDbssNew.

        订购周期类型

        :param period_type: The period_type of this ChargeOrderDbssNew.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def product_infos(self):
        r"""Gets the product_infos of this ChargeOrderDbssNew.

        产品列表

        :return: The product_infos of this ChargeOrderDbssNew.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.ProductInfoBeanNew`]
        """
        return self._product_infos

    @product_infos.setter
    def product_infos(self, product_infos):
        r"""Sets the product_infos of this ChargeOrderDbssNew.

        产品列表

        :param product_infos: The product_infos of this ChargeOrderDbssNew.
        :type product_infos: list[:class:`huaweicloudsdkdbss.v1.ProductInfoBeanNew`]
        """
        self._product_infos = product_infos

    @property
    def promotion_activity_id(self):
        r"""Gets the promotion_activity_id of this ChargeOrderDbssNew.

        促销ID

        :return: The promotion_activity_id of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._promotion_activity_id

    @promotion_activity_id.setter
    def promotion_activity_id(self, promotion_activity_id):
        r"""Sets the promotion_activity_id of this ChargeOrderDbssNew.

        促销ID

        :param promotion_activity_id: The promotion_activity_id of this ChargeOrderDbssNew.
        :type promotion_activity_id: str
        """
        self._promotion_activity_id = promotion_activity_id

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this ChargeOrderDbssNew.

        折扣信息

        :return: The promotion_info of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this ChargeOrderDbssNew.

        折扣信息

        :param promotion_info: The promotion_info of this ChargeOrderDbssNew.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ChargeOrderDbssNew.

        :return: The public_ip of this ChargeOrderDbssNew.
        :rtype: :class:`huaweicloudsdkdbss.v1.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ChargeOrderDbssNew.

        :param public_ip: The public_ip of this ChargeOrderDbssNew.
        :type public_ip: :class:`huaweicloudsdkdbss.v1.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def region_id(self):
        r"""Gets the region_id of this ChargeOrderDbssNew.

        区域ID

        :return: The region_id of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ChargeOrderDbssNew.

        区域ID

        :param region_id: The region_id of this ChargeOrderDbssNew.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def security_groups(self):
        r"""Gets the security_groups of this ChargeOrderDbssNew.

        安全组信息

        :return: The security_groups of this ChargeOrderDbssNew.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this ChargeOrderDbssNew.

        安全组信息

        :param security_groups: The security_groups of this ChargeOrderDbssNew.
        :type security_groups: list[:class:`huaweicloudsdkdbss.v1.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def subscription_num(self):
        r"""Gets the subscription_num of this ChargeOrderDbssNew.

        订购数量，当前仅支持1台

        :return: The subscription_num of this ChargeOrderDbssNew.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        r"""Sets the subscription_num of this ChargeOrderDbssNew.

        订购数量，当前仅支持1台

        :param subscription_num: The subscription_num of this ChargeOrderDbssNew.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ChargeOrderDbssNew.

        VPC ID

        :return: The vpc_id of this ChargeOrderDbssNew.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ChargeOrderDbssNew.

        VPC ID

        :param vpc_id: The vpc_id of this ChargeOrderDbssNew.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, ChargeOrderDbssNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
