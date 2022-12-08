# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceOrder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_key': 'int',
        'cloud_service_type': 'str',
        'region_id': 'str',
        'charging_mode': 'int',
        'period_type': 'int',
        'period_num': 'int',
        'end_time': 'str',
        'product_infos': 'list[ProductInfos]',
        'is_auto_renew': 'int',
        'subscription_num': 'int',
        'relative_resource_id': 'str'
    }

    attribute_map = {
        'instance_key': 'instance_key',
        'cloud_service_type': 'cloud_service_type',
        'region_id': 'region_id',
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'end_time': 'end_time',
        'product_infos': 'product_infos',
        'is_auto_renew': 'is_auto_renew',
        'subscription_num': 'subscription_num',
        'relative_resource_id': 'relative_resource_id'
    }

    def __init__(self, instance_key=None, cloud_service_type=None, region_id=None, charging_mode=None, period_type=None, period_num=None, end_time=None, product_infos=None, is_auto_renew=None, subscription_num=None, relative_resource_id=None):
        """CreateInstanceOrder

        The model defined in huaweicloud sdk

        :param instance_key: 实例的instance_id
        :type instance_key: int
        :param cloud_service_type: CBH云服务类型
        :type cloud_service_type: str
        :param region_id: region id
        :type region_id: str
        :param charging_mode: 计费模式
        :type charging_mode: int
        :param period_type: 订购周期类型
        :type period_type: int
        :param period_num: 订购周期数
        :type period_num: int
        :param end_time: 订购截止日期
        :type end_time: str
        :param product_infos: 产品信息
        :type product_infos: list[:class:`huaweicloudsdkcbh.v1.ProductInfos`]
        :param is_auto_renew: 是否支持续费0/1
        :type is_auto_renew: int
        :param subscription_num: 订购数量
        :type subscription_num: int
        :param relative_resource_id: 扩容新添
        :type relative_resource_id: str
        """
        
        

        self._instance_key = None
        self._cloud_service_type = None
        self._region_id = None
        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._end_time = None
        self._product_infos = None
        self._is_auto_renew = None
        self._subscription_num = None
        self._relative_resource_id = None
        self.discriminator = None

        self.instance_key = instance_key
        self.cloud_service_type = cloud_service_type
        self.region_id = region_id
        self.charging_mode = charging_mode
        self.period_type = period_type
        self.period_num = period_num
        if end_time is not None:
            self.end_time = end_time
        self.product_infos = product_infos
        self.is_auto_renew = is_auto_renew
        self.subscription_num = subscription_num
        if relative_resource_id is not None:
            self.relative_resource_id = relative_resource_id

    @property
    def instance_key(self):
        """Gets the instance_key of this CreateInstanceOrder.

        实例的instance_id

        :return: The instance_key of this CreateInstanceOrder.
        :rtype: int
        """
        return self._instance_key

    @instance_key.setter
    def instance_key(self, instance_key):
        """Sets the instance_key of this CreateInstanceOrder.

        实例的instance_id

        :param instance_key: The instance_key of this CreateInstanceOrder.
        :type instance_key: int
        """
        self._instance_key = instance_key

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this CreateInstanceOrder.

        CBH云服务类型

        :return: The cloud_service_type of this CreateInstanceOrder.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this CreateInstanceOrder.

        CBH云服务类型

        :param cloud_service_type: The cloud_service_type of this CreateInstanceOrder.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def region_id(self):
        """Gets the region_id of this CreateInstanceOrder.

        region id

        :return: The region_id of this CreateInstanceOrder.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateInstanceOrder.

        region id

        :param region_id: The region_id of this CreateInstanceOrder.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def charging_mode(self):
        """Gets the charging_mode of this CreateInstanceOrder.

        计费模式

        :return: The charging_mode of this CreateInstanceOrder.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this CreateInstanceOrder.

        计费模式

        :param charging_mode: The charging_mode of this CreateInstanceOrder.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        """Gets the period_type of this CreateInstanceOrder.

        订购周期类型

        :return: The period_type of this CreateInstanceOrder.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this CreateInstanceOrder.

        订购周期类型

        :param period_type: The period_type of this CreateInstanceOrder.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this CreateInstanceOrder.

        订购周期数

        :return: The period_num of this CreateInstanceOrder.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this CreateInstanceOrder.

        订购周期数

        :param period_num: The period_num of this CreateInstanceOrder.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def end_time(self):
        """Gets the end_time of this CreateInstanceOrder.

        订购截止日期

        :return: The end_time of this CreateInstanceOrder.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CreateInstanceOrder.

        订购截止日期

        :param end_time: The end_time of this CreateInstanceOrder.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def product_infos(self):
        """Gets the product_infos of this CreateInstanceOrder.

        产品信息

        :return: The product_infos of this CreateInstanceOrder.
        :rtype: list[:class:`huaweicloudsdkcbh.v1.ProductInfos`]
        """
        return self._product_infos

    @product_infos.setter
    def product_infos(self, product_infos):
        """Sets the product_infos of this CreateInstanceOrder.

        产品信息

        :param product_infos: The product_infos of this CreateInstanceOrder.
        :type product_infos: list[:class:`huaweicloudsdkcbh.v1.ProductInfos`]
        """
        self._product_infos = product_infos

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this CreateInstanceOrder.

        是否支持续费0/1

        :return: The is_auto_renew of this CreateInstanceOrder.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this CreateInstanceOrder.

        是否支持续费0/1

        :param is_auto_renew: The is_auto_renew of this CreateInstanceOrder.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def subscription_num(self):
        """Gets the subscription_num of this CreateInstanceOrder.

        订购数量

        :return: The subscription_num of this CreateInstanceOrder.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        """Sets the subscription_num of this CreateInstanceOrder.

        订购数量

        :param subscription_num: The subscription_num of this CreateInstanceOrder.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

    @property
    def relative_resource_id(self):
        """Gets the relative_resource_id of this CreateInstanceOrder.

        扩容新添

        :return: The relative_resource_id of this CreateInstanceOrder.
        :rtype: str
        """
        return self._relative_resource_id

    @relative_resource_id.setter
    def relative_resource_id(self, relative_resource_id):
        """Sets the relative_resource_id of this CreateInstanceOrder.

        扩容新添

        :param relative_resource_id: The relative_resource_id of this CreateInstanceOrder.
        :type relative_resource_id: str
        """
        self._relative_resource_id = relative_resource_id

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
        if not isinstance(other, CreateInstanceOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
