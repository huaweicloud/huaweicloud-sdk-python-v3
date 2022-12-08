# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeriodOrderRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'int',
        'cloud_service_type': 'str',
        'composite_product_id': 'str',
        'discount_id': 'str',
        'is_auto_renew': 'int',
        'period_num': 'int',
        'period_type': 'int',
        'product_infos': 'list[ProductInfoBean]',
        'promotion_activity_id': 'str',
        'promotion_info': 'str',
        'region_id': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'charging_mode': 'chargingMode',
        'cloud_service_type': 'cloudServiceType',
        'composite_product_id': 'compositeProductId',
        'discount_id': 'discountId',
        'is_auto_renew': 'isAutoRenew',
        'period_num': 'periodNum',
        'period_type': 'periodType',
        'product_infos': 'productInfos',
        'promotion_activity_id': 'promotionActivityId',
        'promotion_info': 'promotionInfo',
        'region_id': 'regionId',
        'zone': 'zone'
    }

    def __init__(self, charging_mode=None, cloud_service_type=None, composite_product_id=None, discount_id=None, is_auto_renew=None, period_num=None, period_type=None, product_infos=None, promotion_activity_id=None, promotion_info=None, region_id=None, zone=None):
        """PeriodOrderRequest

        The model defined in huaweicloud sdk

        :param charging_mode: 计费模式，0：包周期计费，1：按需计费，2：一次性计费
        :type charging_mode: int
        :param cloud_service_type: 云服务类型
        :type cloud_service_type: str
        :param composite_product_id: 组合套餐ID
        :type composite_product_id: str
        :param discount_id: 折扣ID
        :type discount_id: str
        :param is_auto_renew: 是否自动续费
        :type is_auto_renew: int
        :param period_num: 订购周期数目
        :type period_num: int
        :param period_type: 订购周期类型，2：月，3：年
        :type period_type: int
        :param product_infos: 产品信息列表
        :type product_infos: list[:class:`huaweicloudsdkdsc.v1.ProductInfoBean`]
        :param promotion_activity_id: 促销ID
        :type promotion_activity_id: str
        :param promotion_info: 促销信息
        :type promotion_info: str
        :param region_id: 当前项目所在region的id，如：xx-xx-1。
        :type region_id: str
        :param zone: 所属国家区域
        :type zone: str
        """
        
        

        self._charging_mode = None
        self._cloud_service_type = None
        self._composite_product_id = None
        self._discount_id = None
        self._is_auto_renew = None
        self._period_num = None
        self._period_type = None
        self._product_infos = None
        self._promotion_activity_id = None
        self._promotion_info = None
        self._region_id = None
        self._zone = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if composite_product_id is not None:
            self.composite_product_id = composite_product_id
        if discount_id is not None:
            self.discount_id = discount_id
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if period_num is not None:
            self.period_num = period_num
        if period_type is not None:
            self.period_type = period_type
        if product_infos is not None:
            self.product_infos = product_infos
        if promotion_activity_id is not None:
            self.promotion_activity_id = promotion_activity_id
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if region_id is not None:
            self.region_id = region_id
        if zone is not None:
            self.zone = zone

    @property
    def charging_mode(self):
        """Gets the charging_mode of this PeriodOrderRequest.

        计费模式，0：包周期计费，1：按需计费，2：一次性计费

        :return: The charging_mode of this PeriodOrderRequest.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this PeriodOrderRequest.

        计费模式，0：包周期计费，1：按需计费，2：一次性计费

        :param charging_mode: The charging_mode of this PeriodOrderRequest.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this PeriodOrderRequest.

        云服务类型

        :return: The cloud_service_type of this PeriodOrderRequest.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this PeriodOrderRequest.

        云服务类型

        :param cloud_service_type: The cloud_service_type of this PeriodOrderRequest.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def composite_product_id(self):
        """Gets the composite_product_id of this PeriodOrderRequest.

        组合套餐ID

        :return: The composite_product_id of this PeriodOrderRequest.
        :rtype: str
        """
        return self._composite_product_id

    @composite_product_id.setter
    def composite_product_id(self, composite_product_id):
        """Sets the composite_product_id of this PeriodOrderRequest.

        组合套餐ID

        :param composite_product_id: The composite_product_id of this PeriodOrderRequest.
        :type composite_product_id: str
        """
        self._composite_product_id = composite_product_id

    @property
    def discount_id(self):
        """Gets the discount_id of this PeriodOrderRequest.

        折扣ID

        :return: The discount_id of this PeriodOrderRequest.
        :rtype: str
        """
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        """Sets the discount_id of this PeriodOrderRequest.

        折扣ID

        :param discount_id: The discount_id of this PeriodOrderRequest.
        :type discount_id: str
        """
        self._discount_id = discount_id

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this PeriodOrderRequest.

        是否自动续费

        :return: The is_auto_renew of this PeriodOrderRequest.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this PeriodOrderRequest.

        是否自动续费

        :param is_auto_renew: The is_auto_renew of this PeriodOrderRequest.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def period_num(self):
        """Gets the period_num of this PeriodOrderRequest.

        订购周期数目

        :return: The period_num of this PeriodOrderRequest.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this PeriodOrderRequest.

        订购周期数目

        :param period_num: The period_num of this PeriodOrderRequest.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def period_type(self):
        """Gets the period_type of this PeriodOrderRequest.

        订购周期类型，2：月，3：年

        :return: The period_type of this PeriodOrderRequest.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this PeriodOrderRequest.

        订购周期类型，2：月，3：年

        :param period_type: The period_type of this PeriodOrderRequest.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def product_infos(self):
        """Gets the product_infos of this PeriodOrderRequest.

        产品信息列表

        :return: The product_infos of this PeriodOrderRequest.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.ProductInfoBean`]
        """
        return self._product_infos

    @product_infos.setter
    def product_infos(self, product_infos):
        """Sets the product_infos of this PeriodOrderRequest.

        产品信息列表

        :param product_infos: The product_infos of this PeriodOrderRequest.
        :type product_infos: list[:class:`huaweicloudsdkdsc.v1.ProductInfoBean`]
        """
        self._product_infos = product_infos

    @property
    def promotion_activity_id(self):
        """Gets the promotion_activity_id of this PeriodOrderRequest.

        促销ID

        :return: The promotion_activity_id of this PeriodOrderRequest.
        :rtype: str
        """
        return self._promotion_activity_id

    @promotion_activity_id.setter
    def promotion_activity_id(self, promotion_activity_id):
        """Sets the promotion_activity_id of this PeriodOrderRequest.

        促销ID

        :param promotion_activity_id: The promotion_activity_id of this PeriodOrderRequest.
        :type promotion_activity_id: str
        """
        self._promotion_activity_id = promotion_activity_id

    @property
    def promotion_info(self):
        """Gets the promotion_info of this PeriodOrderRequest.

        促销信息

        :return: The promotion_info of this PeriodOrderRequest.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        """Sets the promotion_info of this PeriodOrderRequest.

        促销信息

        :param promotion_info: The promotion_info of this PeriodOrderRequest.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def region_id(self):
        """Gets the region_id of this PeriodOrderRequest.

        当前项目所在region的id，如：xx-xx-1。

        :return: The region_id of this PeriodOrderRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PeriodOrderRequest.

        当前项目所在region的id，如：xx-xx-1。

        :param region_id: The region_id of this PeriodOrderRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def zone(self):
        """Gets the zone of this PeriodOrderRequest.

        所属国家区域

        :return: The zone of this PeriodOrderRequest.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this PeriodOrderRequest.

        所属国家区域

        :param zone: The zone of this PeriodOrderRequest.
        :type zone: str
        """
        self._zone = zone

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
        if not isinstance(other, PeriodOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
