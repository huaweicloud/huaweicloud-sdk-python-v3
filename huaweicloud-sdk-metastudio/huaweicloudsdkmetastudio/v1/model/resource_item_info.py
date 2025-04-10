# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceItemInfo:

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
        'order_id': 'str',
        'bound_asset': 'BoundAssetInfo',
        'resource_expire_time': 'str',
        'resource_type': 'str',
        'business_type': 'str',
        'sub_resource_type': 'str',
        'is_sub_resource': 'bool',
        'charging_mode': 'str',
        'resource_source': 'str',
        'amount': 'float',
        'usage': 'float',
        'status': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'order_id': 'order_id',
        'bound_asset': 'bound_asset',
        'resource_expire_time': 'resource_expire_time',
        'resource_type': 'resource_type',
        'business_type': 'business_type',
        'sub_resource_type': 'sub_resource_type',
        'is_sub_resource': 'is_sub_resource',
        'charging_mode': 'charging_mode',
        'resource_source': 'resource_source',
        'amount': 'amount',
        'usage': 'usage',
        'status': 'status',
        'unit': 'unit'
    }

    def __init__(self, resource_id=None, order_id=None, bound_asset=None, resource_expire_time=None, resource_type=None, business_type=None, sub_resource_type=None, is_sub_resource=None, charging_mode=None, resource_source=None, amount=None, usage=None, status=None, unit=None):
        r"""ResourceItemInfo

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID。
        :type resource_id: str
        :param order_id: cloudServiceId的订单id。 云服务购买清单等场景必填（purchaseMode取值为3、4），每个CloudService生成一个订单；此场景如果为空，则报错。 其他场景，为空。
        :type order_id: str
        :param bound_asset: 
        :type bound_asset: :class:`huaweicloudsdkmetastudio.v1.BoundAssetInfo`
        :param resource_expire_time: 资源截止时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type resource_expire_time: str
        :param resource_type: 资源类型。详见[资源类型](metastudio_02_0042.xml)。
        :type resource_type: str
        :param business_type: 业务类型。 * VOICE_CLONE：声音制作 * SYNTHETICS_SOUND：声音合成 * ASSET_MANAGER：资产管理 * MODELING_2D：形象制作 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作 * CHAT_2D：分身数字人智能交互 * BUSINESS_CARD_2D：分身数字人名片 * PICTURE_2D：照片数字人视频 * MODELING_3D：3D照片建模 * VDS_3D：3D视觉驱动 * TTSA_3D：3D语音驱动 * FLEXUS_2D：flexus版本资源
        :type business_type: str
        :param sub_resource_type: 子资源类型。当前只有flexus套餐包存在该字段 * voice_clone_flexus: 语音克隆Flexus版 * modeling_count_2d_model_flexus: 分身数字人形象制作Flexus版 * video_time_flexus_2d_model: 分身数字人Flexus版本视频制作
        :type sub_resource_type: str
        :param is_sub_resource: 是否子资源。子资源描述的是子资源的数量和单位
        :type is_sub_resource: bool
        :param charging_mode: 计费类型。 * PERIODIC: 包周期 * ONE_TIME：一次性 * ON_DEMAND：按需
        :type charging_mode: str
        :param resource_source: 资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配
        :type resource_source: str
        :param amount: 总量
        :type amount: float
        :param usage: 使用量
        :type usage: float
        :param status: 资源状态 0:正常 1:冻结
        :type status: int
        :param unit: 单位。 * NUM：个数(形象/声音) * MIN：分钟（视频制作） * HOUR：小时 （直播） * CHANNEL：路（直播/交互） * GB：GB(资产管理) * MILLION_WORDS：百万字 * TEN_THOUSAND_WORDS：万字 * TIME：次
        :type unit: str
        """
        
        

        self._resource_id = None
        self._order_id = None
        self._bound_asset = None
        self._resource_expire_time = None
        self._resource_type = None
        self._business_type = None
        self._sub_resource_type = None
        self._is_sub_resource = None
        self._charging_mode = None
        self._resource_source = None
        self._amount = None
        self._usage = None
        self._status = None
        self._unit = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if order_id is not None:
            self.order_id = order_id
        if bound_asset is not None:
            self.bound_asset = bound_asset
        if resource_expire_time is not None:
            self.resource_expire_time = resource_expire_time
        if resource_type is not None:
            self.resource_type = resource_type
        if business_type is not None:
            self.business_type = business_type
        if sub_resource_type is not None:
            self.sub_resource_type = sub_resource_type
        if is_sub_resource is not None:
            self.is_sub_resource = is_sub_resource
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_source is not None:
            self.resource_source = resource_source
        if amount is not None:
            self.amount = amount
        if usage is not None:
            self.usage = usage
        if status is not None:
            self.status = status
        if unit is not None:
            self.unit = unit

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceItemInfo.

        资源ID。

        :return: The resource_id of this ResourceItemInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceItemInfo.

        资源ID。

        :param resource_id: The resource_id of this ResourceItemInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def order_id(self):
        r"""Gets the order_id of this ResourceItemInfo.

        cloudServiceId的订单id。 云服务购买清单等场景必填（purchaseMode取值为3、4），每个CloudService生成一个订单；此场景如果为空，则报错。 其他场景，为空。

        :return: The order_id of this ResourceItemInfo.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ResourceItemInfo.

        cloudServiceId的订单id。 云服务购买清单等场景必填（purchaseMode取值为3、4），每个CloudService生成一个订单；此场景如果为空，则报错。 其他场景，为空。

        :param order_id: The order_id of this ResourceItemInfo.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def bound_asset(self):
        r"""Gets the bound_asset of this ResourceItemInfo.

        :return: The bound_asset of this ResourceItemInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BoundAssetInfo`
        """
        return self._bound_asset

    @bound_asset.setter
    def bound_asset(self, bound_asset):
        r"""Sets the bound_asset of this ResourceItemInfo.

        :param bound_asset: The bound_asset of this ResourceItemInfo.
        :type bound_asset: :class:`huaweicloudsdkmetastudio.v1.BoundAssetInfo`
        """
        self._bound_asset = bound_asset

    @property
    def resource_expire_time(self):
        r"""Gets the resource_expire_time of this ResourceItemInfo.

        资源截止时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The resource_expire_time of this ResourceItemInfo.
        :rtype: str
        """
        return self._resource_expire_time

    @resource_expire_time.setter
    def resource_expire_time(self, resource_expire_time):
        r"""Sets the resource_expire_time of this ResourceItemInfo.

        资源截止时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param resource_expire_time: The resource_expire_time of this ResourceItemInfo.
        :type resource_expire_time: str
        """
        self._resource_expire_time = resource_expire_time

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceItemInfo.

        资源类型。详见[资源类型](metastudio_02_0042.xml)。

        :return: The resource_type of this ResourceItemInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceItemInfo.

        资源类型。详见[资源类型](metastudio_02_0042.xml)。

        :param resource_type: The resource_type of this ResourceItemInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def business_type(self):
        r"""Gets the business_type of this ResourceItemInfo.

        业务类型。 * VOICE_CLONE：声音制作 * SYNTHETICS_SOUND：声音合成 * ASSET_MANAGER：资产管理 * MODELING_2D：形象制作 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作 * CHAT_2D：分身数字人智能交互 * BUSINESS_CARD_2D：分身数字人名片 * PICTURE_2D：照片数字人视频 * MODELING_3D：3D照片建模 * VDS_3D：3D视觉驱动 * TTSA_3D：3D语音驱动 * FLEXUS_2D：flexus版本资源

        :return: The business_type of this ResourceItemInfo.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this ResourceItemInfo.

        业务类型。 * VOICE_CLONE：声音制作 * SYNTHETICS_SOUND：声音合成 * ASSET_MANAGER：资产管理 * MODELING_2D：形象制作 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作 * CHAT_2D：分身数字人智能交互 * BUSINESS_CARD_2D：分身数字人名片 * PICTURE_2D：照片数字人视频 * MODELING_3D：3D照片建模 * VDS_3D：3D视觉驱动 * TTSA_3D：3D语音驱动 * FLEXUS_2D：flexus版本资源

        :param business_type: The business_type of this ResourceItemInfo.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def sub_resource_type(self):
        r"""Gets the sub_resource_type of this ResourceItemInfo.

        子资源类型。当前只有flexus套餐包存在该字段 * voice_clone_flexus: 语音克隆Flexus版 * modeling_count_2d_model_flexus: 分身数字人形象制作Flexus版 * video_time_flexus_2d_model: 分身数字人Flexus版本视频制作

        :return: The sub_resource_type of this ResourceItemInfo.
        :rtype: str
        """
        return self._sub_resource_type

    @sub_resource_type.setter
    def sub_resource_type(self, sub_resource_type):
        r"""Sets the sub_resource_type of this ResourceItemInfo.

        子资源类型。当前只有flexus套餐包存在该字段 * voice_clone_flexus: 语音克隆Flexus版 * modeling_count_2d_model_flexus: 分身数字人形象制作Flexus版 * video_time_flexus_2d_model: 分身数字人Flexus版本视频制作

        :param sub_resource_type: The sub_resource_type of this ResourceItemInfo.
        :type sub_resource_type: str
        """
        self._sub_resource_type = sub_resource_type

    @property
    def is_sub_resource(self):
        r"""Gets the is_sub_resource of this ResourceItemInfo.

        是否子资源。子资源描述的是子资源的数量和单位

        :return: The is_sub_resource of this ResourceItemInfo.
        :rtype: bool
        """
        return self._is_sub_resource

    @is_sub_resource.setter
    def is_sub_resource(self, is_sub_resource):
        r"""Sets the is_sub_resource of this ResourceItemInfo.

        是否子资源。子资源描述的是子资源的数量和单位

        :param is_sub_resource: The is_sub_resource of this ResourceItemInfo.
        :type is_sub_resource: bool
        """
        self._is_sub_resource = is_sub_resource

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ResourceItemInfo.

        计费类型。 * PERIODIC: 包周期 * ONE_TIME：一次性 * ON_DEMAND：按需

        :return: The charging_mode of this ResourceItemInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ResourceItemInfo.

        计费类型。 * PERIODIC: 包周期 * ONE_TIME：一次性 * ON_DEMAND：按需

        :param charging_mode: The charging_mode of this ResourceItemInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_source(self):
        r"""Gets the resource_source of this ResourceItemInfo.

        资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配

        :return: The resource_source of this ResourceItemInfo.
        :rtype: str
        """
        return self._resource_source

    @resource_source.setter
    def resource_source(self, resource_source):
        r"""Sets the resource_source of this ResourceItemInfo.

        资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配

        :param resource_source: The resource_source of this ResourceItemInfo.
        :type resource_source: str
        """
        self._resource_source = resource_source

    @property
    def amount(self):
        r"""Gets the amount of this ResourceItemInfo.

        总量

        :return: The amount of this ResourceItemInfo.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this ResourceItemInfo.

        总量

        :param amount: The amount of this ResourceItemInfo.
        :type amount: float
        """
        self._amount = amount

    @property
    def usage(self):
        r"""Gets the usage of this ResourceItemInfo.

        使用量

        :return: The usage of this ResourceItemInfo.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this ResourceItemInfo.

        使用量

        :param usage: The usage of this ResourceItemInfo.
        :type usage: float
        """
        self._usage = usage

    @property
    def status(self):
        r"""Gets the status of this ResourceItemInfo.

        资源状态 0:正常 1:冻结

        :return: The status of this ResourceItemInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResourceItemInfo.

        资源状态 0:正常 1:冻结

        :param status: The status of this ResourceItemInfo.
        :type status: int
        """
        self._status = status

    @property
    def unit(self):
        r"""Gets the unit of this ResourceItemInfo.

        单位。 * NUM：个数(形象/声音) * MIN：分钟（视频制作） * HOUR：小时 （直播） * CHANNEL：路（直播/交互） * GB：GB(资产管理) * MILLION_WORDS：百万字 * TEN_THOUSAND_WORDS：万字 * TIME：次

        :return: The unit of this ResourceItemInfo.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ResourceItemInfo.

        单位。 * NUM：个数(形象/声音) * MIN：分钟（视频制作） * HOUR：小时 （直播） * CHANNEL：路（直播/交互） * GB：GB(资产管理) * MILLION_WORDS：百万字 * TEN_THOUSAND_WORDS：万字 * TIME：次

        :param unit: The unit of this ResourceItemInfo.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, ResourceItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
