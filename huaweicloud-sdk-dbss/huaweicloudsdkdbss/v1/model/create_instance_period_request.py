# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstancePeriodRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'name': 'str',
        'vpc_id': 'str',
        'availability_zone': 'str',
        'enterprise_project_id': 'str',
        'nics': 'list[CreateInstancePeriodRequestNics]',
        'security_groups': 'list[CreateInstancePeriodRequestSecurityGroups]',
        'comment': 'str',
        'region': 'str',
        'cloud_service_type': 'str',
        'charging_mode': 'int',
        'period_type': 'int',
        'period_num': 'int',
        'subscription_num': 'int',
        'product_infos': 'list[CreateInstancePeriodRequestProductInfos]',
        'tags': 'list[KeyValueBean]',
        'promotion_info': 'str',
        'is_auto_renew': 'int'
    }

    attribute_map = {
        'flavor_ref': 'flavor_ref',
        'name': 'name',
        'vpc_id': 'vpc_id',
        'availability_zone': 'availability_zone',
        'enterprise_project_id': 'enterprise_project_id',
        'nics': 'nics',
        'security_groups': 'security_groups',
        'comment': 'comment',
        'region': 'region',
        'cloud_service_type': 'cloud_service_type',
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'subscription_num': 'subscription_num',
        'product_infos': 'product_infos',
        'tags': 'tags',
        'promotion_info': 'promotion_info',
        'is_auto_renew': 'is_auto_renew'
    }

    def __init__(self, flavor_ref=None, name=None, vpc_id=None, availability_zone=None, enterprise_project_id=None, nics=None, security_groups=None, comment=None, region=None, cloud_service_type=None, charging_mode=None, period_type=None, period_num=None, subscription_num=None, product_infos=None, tags=None, promotion_info=None, is_auto_renew=None):
        """CreateInstancePeriodRequest

        The model defined in huaweicloud sdk

        :param flavor_ref: 云服务器使用的规格ID
        :type flavor_ref: str
        :param name: 云服务器名称。 取值范围： • 只能由中文字符、英文字母、数字、下划线、中划线组成，且长度小于等于64个字符。 • 创建的云服务器数量大于1时，长度小于等于59个字符
        :type name: str
        :param vpc_id: VPC的ID
        :type vpc_id: str
        :param availability_zone: 云服务器对应可用分区信息。(两个主备分区，中间用“,”分割，例如az1.dc1,az2.dc2)
        :type availability_zone: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param nics: 云服务器对应的网卡信息
        :type nics: list[:class:`huaweicloudsdkdbss.v1.CreateInstancePeriodRequestNics`]
        :param security_groups: 云服务器对应安全组信息
        :type security_groups: list[:class:`huaweicloudsdkdbss.v1.CreateInstancePeriodRequestSecurityGroups`]
        :param comment: 备注信息
        :type comment: str
        :param region: 云服务器所在区域ID
        :type region: str
        :param cloud_service_type: 服务类型： 默认hws.service.type.dbss
        :type cloud_service_type: str
        :param charging_mode: 计费模式： • 0：包周期计费 • 1：按需计费
        :type charging_mode: int
        :param period_type: 订购周期类型： • 0：天； • 1：周； • 2：月； • 3：年； • 4：小时； • 5：绝对时间
        :type period_type: int
        :param period_num: 订购周期数
        :type period_num: int
        :param subscription_num: 订购数量： DBSS只支持订购1套，不支持多套
        :type subscription_num: int
        :param product_infos: 产品信息列表
        :type product_infos: list[:class:`huaweicloudsdkdbss.v1.CreateInstancePeriodRequestProductInfos`]
        :param tags: 资源标签
        :type tags: list[:class:`huaweicloudsdkdbss.v1.KeyValueBean`]
        :param promotion_info: 折扣信息
        :type promotion_info: str
        :param is_auto_renew: 自动续费 1表示自动续费，0表示不自动续费
        :type is_auto_renew: int
        """
        
        

        self._flavor_ref = None
        self._name = None
        self._vpc_id = None
        self._availability_zone = None
        self._enterprise_project_id = None
        self._nics = None
        self._security_groups = None
        self._comment = None
        self._region = None
        self._cloud_service_type = None
        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._subscription_num = None
        self._product_infos = None
        self._tags = None
        self._promotion_info = None
        self._is_auto_renew = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        self.name = name
        self.vpc_id = vpc_id
        self.availability_zone = availability_zone
        self.enterprise_project_id = enterprise_project_id
        self.nics = nics
        self.security_groups = security_groups
        if comment is not None:
            self.comment = comment
        self.region = region
        self.cloud_service_type = cloud_service_type
        self.charging_mode = charging_mode
        self.period_type = period_type
        self.period_num = period_num
        self.subscription_num = subscription_num
        self.product_infos = product_infos
        if tags is not None:
            self.tags = tags
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this CreateInstancePeriodRequest.

        云服务器使用的规格ID

        :return: The flavor_ref of this CreateInstancePeriodRequest.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this CreateInstancePeriodRequest.

        云服务器使用的规格ID

        :param flavor_ref: The flavor_ref of this CreateInstancePeriodRequest.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def name(self):
        """Gets the name of this CreateInstancePeriodRequest.

        云服务器名称。 取值范围： • 只能由中文字符、英文字母、数字、下划线、中划线组成，且长度小于等于64个字符。 • 创建的云服务器数量大于1时，长度小于等于59个字符

        :return: The name of this CreateInstancePeriodRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstancePeriodRequest.

        云服务器名称。 取值范围： • 只能由中文字符、英文字母、数字、下划线、中划线组成，且长度小于等于64个字符。 • 创建的云服务器数量大于1时，长度小于等于59个字符

        :param name: The name of this CreateInstancePeriodRequest.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstancePeriodRequest.

        VPC的ID

        :return: The vpc_id of this CreateInstancePeriodRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstancePeriodRequest.

        VPC的ID

        :param vpc_id: The vpc_id of this CreateInstancePeriodRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateInstancePeriodRequest.

        云服务器对应可用分区信息。(两个主备分区，中间用“,”分割，例如az1.dc1,az2.dc2)

        :return: The availability_zone of this CreateInstancePeriodRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateInstancePeriodRequest.

        云服务器对应可用分区信息。(两个主备分区，中间用“,”分割，例如az1.dc1,az2.dc2)

        :param availability_zone: The availability_zone of this CreateInstancePeriodRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateInstancePeriodRequest.

        企业项目ID

        :return: The enterprise_project_id of this CreateInstancePeriodRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateInstancePeriodRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateInstancePeriodRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def nics(self):
        """Gets the nics of this CreateInstancePeriodRequest.

        云服务器对应的网卡信息

        :return: The nics of this CreateInstancePeriodRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.CreateInstancePeriodRequestNics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this CreateInstancePeriodRequest.

        云服务器对应的网卡信息

        :param nics: The nics of this CreateInstancePeriodRequest.
        :type nics: list[:class:`huaweicloudsdkdbss.v1.CreateInstancePeriodRequestNics`]
        """
        self._nics = nics

    @property
    def security_groups(self):
        """Gets the security_groups of this CreateInstancePeriodRequest.

        云服务器对应安全组信息

        :return: The security_groups of this CreateInstancePeriodRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.CreateInstancePeriodRequestSecurityGroups`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CreateInstancePeriodRequest.

        云服务器对应安全组信息

        :param security_groups: The security_groups of this CreateInstancePeriodRequest.
        :type security_groups: list[:class:`huaweicloudsdkdbss.v1.CreateInstancePeriodRequestSecurityGroups`]
        """
        self._security_groups = security_groups

    @property
    def comment(self):
        """Gets the comment of this CreateInstancePeriodRequest.

        备注信息

        :return: The comment of this CreateInstancePeriodRequest.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateInstancePeriodRequest.

        备注信息

        :param comment: The comment of this CreateInstancePeriodRequest.
        :type comment: str
        """
        self._comment = comment

    @property
    def region(self):
        """Gets the region of this CreateInstancePeriodRequest.

        云服务器所在区域ID

        :return: The region of this CreateInstancePeriodRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateInstancePeriodRequest.

        云服务器所在区域ID

        :param region: The region of this CreateInstancePeriodRequest.
        :type region: str
        """
        self._region = region

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this CreateInstancePeriodRequest.

        服务类型： 默认hws.service.type.dbss

        :return: The cloud_service_type of this CreateInstancePeriodRequest.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this CreateInstancePeriodRequest.

        服务类型： 默认hws.service.type.dbss

        :param cloud_service_type: The cloud_service_type of this CreateInstancePeriodRequest.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def charging_mode(self):
        """Gets the charging_mode of this CreateInstancePeriodRequest.

        计费模式： • 0：包周期计费 • 1：按需计费

        :return: The charging_mode of this CreateInstancePeriodRequest.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this CreateInstancePeriodRequest.

        计费模式： • 0：包周期计费 • 1：按需计费

        :param charging_mode: The charging_mode of this CreateInstancePeriodRequest.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        """Gets the period_type of this CreateInstancePeriodRequest.

        订购周期类型： • 0：天； • 1：周； • 2：月； • 3：年； • 4：小时； • 5：绝对时间

        :return: The period_type of this CreateInstancePeriodRequest.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this CreateInstancePeriodRequest.

        订购周期类型： • 0：天； • 1：周； • 2：月； • 3：年； • 4：小时； • 5：绝对时间

        :param period_type: The period_type of this CreateInstancePeriodRequest.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this CreateInstancePeriodRequest.

        订购周期数

        :return: The period_num of this CreateInstancePeriodRequest.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this CreateInstancePeriodRequest.

        订购周期数

        :param period_num: The period_num of this CreateInstancePeriodRequest.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def subscription_num(self):
        """Gets the subscription_num of this CreateInstancePeriodRequest.

        订购数量： DBSS只支持订购1套，不支持多套

        :return: The subscription_num of this CreateInstancePeriodRequest.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        """Sets the subscription_num of this CreateInstancePeriodRequest.

        订购数量： DBSS只支持订购1套，不支持多套

        :param subscription_num: The subscription_num of this CreateInstancePeriodRequest.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

    @property
    def product_infos(self):
        """Gets the product_infos of this CreateInstancePeriodRequest.

        产品信息列表

        :return: The product_infos of this CreateInstancePeriodRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.CreateInstancePeriodRequestProductInfos`]
        """
        return self._product_infos

    @product_infos.setter
    def product_infos(self, product_infos):
        """Sets the product_infos of this CreateInstancePeriodRequest.

        产品信息列表

        :param product_infos: The product_infos of this CreateInstancePeriodRequest.
        :type product_infos: list[:class:`huaweicloudsdkdbss.v1.CreateInstancePeriodRequestProductInfos`]
        """
        self._product_infos = product_infos

    @property
    def tags(self):
        """Gets the tags of this CreateInstancePeriodRequest.

        资源标签

        :return: The tags of this CreateInstancePeriodRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.KeyValueBean`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateInstancePeriodRequest.

        资源标签

        :param tags: The tags of this CreateInstancePeriodRequest.
        :type tags: list[:class:`huaweicloudsdkdbss.v1.KeyValueBean`]
        """
        self._tags = tags

    @property
    def promotion_info(self):
        """Gets the promotion_info of this CreateInstancePeriodRequest.

        折扣信息

        :return: The promotion_info of this CreateInstancePeriodRequest.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        """Sets the promotion_info of this CreateInstancePeriodRequest.

        折扣信息

        :param promotion_info: The promotion_info of this CreateInstancePeriodRequest.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this CreateInstancePeriodRequest.

        自动续费 1表示自动续费，0表示不自动续费

        :return: The is_auto_renew of this CreateInstancePeriodRequest.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this CreateInstancePeriodRequest.

        自动续费 1表示自动续费，0表示不自动续费

        :param is_auto_renew: The is_auto_renew of this CreateInstancePeriodRequest.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

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
        if not isinstance(other, CreateInstancePeriodRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
