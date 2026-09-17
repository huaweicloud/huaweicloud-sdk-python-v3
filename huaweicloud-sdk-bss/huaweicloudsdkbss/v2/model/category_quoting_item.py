# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CategoryQuotingItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_id': 'str',
        'cloud_service_type': 'str',
        'cloud_service_type_name': 'str',
        'commercial_resource_type': 'str',
        'resource_type_code': 'str',
        'resource_type_name': 'str',
        'sku_family_code': 'str',
        'sku_family_name': 'str',
        'site_code': 'str',
        'region_code': 'str',
        'region_name': 'str',
        'az_code': 'str',
        'az_name': 'str',
        'step_no': 'str',
        'charging_mode': 'str',
        'discount_ratio': 'decimal.Decimal',
        'effective_time': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'item_id': 'item_id',
        'cloud_service_type': 'cloud_service_type',
        'cloud_service_type_name': 'cloud_service_type_name',
        'commercial_resource_type': 'commercial_resource_type',
        'resource_type_code': 'resource_type_code',
        'resource_type_name': 'resource_type_name',
        'sku_family_code': 'sku_family_code',
        'sku_family_name': 'sku_family_name',
        'site_code': 'site_code',
        'region_code': 'region_code',
        'region_name': 'region_name',
        'az_code': 'az_code',
        'az_name': 'az_name',
        'step_no': 'step_no',
        'charging_mode': 'charging_mode',
        'discount_ratio': 'discount_ratio',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time'
    }

    def __init__(self, item_id=None, cloud_service_type=None, cloud_service_type_name=None, commercial_resource_type=None, resource_type_code=None, resource_type_name=None, sku_family_code=None, sku_family_name=None, site_code=None, region_code=None, region_name=None, az_code=None, az_name=None, step_no=None, charging_mode=None, discount_ratio=None, effective_time=None, expire_time=None):
        r"""CategoryQuotingItem

        The model defined in huaweicloud sdk

        :param item_id: 报价项ID
        :type item_id: str
        :param cloud_service_type: 云服务编码
        :type cloud_service_type: str
        :param cloud_service_type_name: 云服务名称
        :type cloud_service_type_name: str
        :param commercial_resource_type: 商务资源类型
        :type commercial_resource_type: str
        :param resource_type_code: 资源类型编码
        :type resource_type_code: str
        :param resource_type_name: 资源类型名称
        :type resource_type_name: str
        :param sku_family_code: SKU族编码
        :type sku_family_code: str
        :param sku_family_name: SKU族名称
        :type sku_family_name: str
        :param site_code: 归属站点编码
        :type site_code: str
        :param region_code: 区域编码
        :type region_code: str
        :param region_name: 区域名称
        :type region_name: str
        :param az_code: 可用区AZ编码
        :type az_code: str
        :param az_name: 可用区AZ名称
        :type az_name: str
        :param step_no: 阶梯编号
        :type step_no: str
        :param charging_mode: 计费模式，ONDEMAND：按需、ONETIME：一次性、DAILY：包天、MONTHLY：包月、1_YEARLY：包1年、2_YEARLY：包2年、3_YEARLY：包3年、4_YEARLY：包4年、5_YEARLY：包5年、1_YEARLY_RI：包1年预留实例、3_YEARLY_RI：包3年预留实例
        :type charging_mode: str
        :param discount_ratio: 折扣率
        :type discount_ratio: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param effective_time: 报价项生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ
        :type effective_time: str
        :param expire_time: 报价项失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ
        :type expire_time: str
        """
        
        

        self._item_id = None
        self._cloud_service_type = None
        self._cloud_service_type_name = None
        self._commercial_resource_type = None
        self._resource_type_code = None
        self._resource_type_name = None
        self._sku_family_code = None
        self._sku_family_name = None
        self._site_code = None
        self._region_code = None
        self._region_name = None
        self._az_code = None
        self._az_name = None
        self._step_no = None
        self._charging_mode = None
        self._discount_ratio = None
        self._effective_time = None
        self._expire_time = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if cloud_service_type_name is not None:
            self.cloud_service_type_name = cloud_service_type_name
        if commercial_resource_type is not None:
            self.commercial_resource_type = commercial_resource_type
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if sku_family_code is not None:
            self.sku_family_code = sku_family_code
        if sku_family_name is not None:
            self.sku_family_name = sku_family_name
        if site_code is not None:
            self.site_code = site_code
        if region_code is not None:
            self.region_code = region_code
        if region_name is not None:
            self.region_name = region_name
        if az_code is not None:
            self.az_code = az_code
        if az_name is not None:
            self.az_name = az_name
        if step_no is not None:
            self.step_no = step_no
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if discount_ratio is not None:
            self.discount_ratio = discount_ratio
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def item_id(self):
        r"""Gets the item_id of this CategoryQuotingItem.

        报价项ID

        :return: The item_id of this CategoryQuotingItem.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this CategoryQuotingItem.

        报价项ID

        :param item_id: The item_id of this CategoryQuotingItem.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this CategoryQuotingItem.

        云服务编码

        :return: The cloud_service_type of this CategoryQuotingItem.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this CategoryQuotingItem.

        云服务编码

        :param cloud_service_type: The cloud_service_type of this CategoryQuotingItem.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def cloud_service_type_name(self):
        r"""Gets the cloud_service_type_name of this CategoryQuotingItem.

        云服务名称

        :return: The cloud_service_type_name of this CategoryQuotingItem.
        :rtype: str
        """
        return self._cloud_service_type_name

    @cloud_service_type_name.setter
    def cloud_service_type_name(self, cloud_service_type_name):
        r"""Sets the cloud_service_type_name of this CategoryQuotingItem.

        云服务名称

        :param cloud_service_type_name: The cloud_service_type_name of this CategoryQuotingItem.
        :type cloud_service_type_name: str
        """
        self._cloud_service_type_name = cloud_service_type_name

    @property
    def commercial_resource_type(self):
        r"""Gets the commercial_resource_type of this CategoryQuotingItem.

        商务资源类型

        :return: The commercial_resource_type of this CategoryQuotingItem.
        :rtype: str
        """
        return self._commercial_resource_type

    @commercial_resource_type.setter
    def commercial_resource_type(self, commercial_resource_type):
        r"""Sets the commercial_resource_type of this CategoryQuotingItem.

        商务资源类型

        :param commercial_resource_type: The commercial_resource_type of this CategoryQuotingItem.
        :type commercial_resource_type: str
        """
        self._commercial_resource_type = commercial_resource_type

    @property
    def resource_type_code(self):
        r"""Gets the resource_type_code of this CategoryQuotingItem.

        资源类型编码

        :return: The resource_type_code of this CategoryQuotingItem.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        r"""Sets the resource_type_code of this CategoryQuotingItem.

        资源类型编码

        :param resource_type_code: The resource_type_code of this CategoryQuotingItem.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this CategoryQuotingItem.

        资源类型名称

        :return: The resource_type_name of this CategoryQuotingItem.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this CategoryQuotingItem.

        资源类型名称

        :param resource_type_name: The resource_type_name of this CategoryQuotingItem.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def sku_family_code(self):
        r"""Gets the sku_family_code of this CategoryQuotingItem.

        SKU族编码

        :return: The sku_family_code of this CategoryQuotingItem.
        :rtype: str
        """
        return self._sku_family_code

    @sku_family_code.setter
    def sku_family_code(self, sku_family_code):
        r"""Sets the sku_family_code of this CategoryQuotingItem.

        SKU族编码

        :param sku_family_code: The sku_family_code of this CategoryQuotingItem.
        :type sku_family_code: str
        """
        self._sku_family_code = sku_family_code

    @property
    def sku_family_name(self):
        r"""Gets the sku_family_name of this CategoryQuotingItem.

        SKU族名称

        :return: The sku_family_name of this CategoryQuotingItem.
        :rtype: str
        """
        return self._sku_family_name

    @sku_family_name.setter
    def sku_family_name(self, sku_family_name):
        r"""Sets the sku_family_name of this CategoryQuotingItem.

        SKU族名称

        :param sku_family_name: The sku_family_name of this CategoryQuotingItem.
        :type sku_family_name: str
        """
        self._sku_family_name = sku_family_name

    @property
    def site_code(self):
        r"""Gets the site_code of this CategoryQuotingItem.

        归属站点编码

        :return: The site_code of this CategoryQuotingItem.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this CategoryQuotingItem.

        归属站点编码

        :param site_code: The site_code of this CategoryQuotingItem.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def region_code(self):
        r"""Gets the region_code of this CategoryQuotingItem.

        区域编码

        :return: The region_code of this CategoryQuotingItem.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this CategoryQuotingItem.

        区域编码

        :param region_code: The region_code of this CategoryQuotingItem.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def region_name(self):
        r"""Gets the region_name of this CategoryQuotingItem.

        区域名称

        :return: The region_name of this CategoryQuotingItem.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this CategoryQuotingItem.

        区域名称

        :param region_name: The region_name of this CategoryQuotingItem.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def az_code(self):
        r"""Gets the az_code of this CategoryQuotingItem.

        可用区AZ编码

        :return: The az_code of this CategoryQuotingItem.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this CategoryQuotingItem.

        可用区AZ编码

        :param az_code: The az_code of this CategoryQuotingItem.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def az_name(self):
        r"""Gets the az_name of this CategoryQuotingItem.

        可用区AZ名称

        :return: The az_name of this CategoryQuotingItem.
        :rtype: str
        """
        return self._az_name

    @az_name.setter
    def az_name(self, az_name):
        r"""Sets the az_name of this CategoryQuotingItem.

        可用区AZ名称

        :param az_name: The az_name of this CategoryQuotingItem.
        :type az_name: str
        """
        self._az_name = az_name

    @property
    def step_no(self):
        r"""Gets the step_no of this CategoryQuotingItem.

        阶梯编号

        :return: The step_no of this CategoryQuotingItem.
        :rtype: str
        """
        return self._step_no

    @step_no.setter
    def step_no(self, step_no):
        r"""Sets the step_no of this CategoryQuotingItem.

        阶梯编号

        :param step_no: The step_no of this CategoryQuotingItem.
        :type step_no: str
        """
        self._step_no = step_no

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CategoryQuotingItem.

        计费模式，ONDEMAND：按需、ONETIME：一次性、DAILY：包天、MONTHLY：包月、1_YEARLY：包1年、2_YEARLY：包2年、3_YEARLY：包3年、4_YEARLY：包4年、5_YEARLY：包5年、1_YEARLY_RI：包1年预留实例、3_YEARLY_RI：包3年预留实例

        :return: The charging_mode of this CategoryQuotingItem.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CategoryQuotingItem.

        计费模式，ONDEMAND：按需、ONETIME：一次性、DAILY：包天、MONTHLY：包月、1_YEARLY：包1年、2_YEARLY：包2年、3_YEARLY：包3年、4_YEARLY：包4年、5_YEARLY：包5年、1_YEARLY_RI：包1年预留实例、3_YEARLY_RI：包3年预留实例

        :param charging_mode: The charging_mode of this CategoryQuotingItem.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def discount_ratio(self):
        r"""Gets the discount_ratio of this CategoryQuotingItem.

        折扣率

        :return: The discount_ratio of this CategoryQuotingItem.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._discount_ratio

    @discount_ratio.setter
    def discount_ratio(self, discount_ratio):
        r"""Sets the discount_ratio of this CategoryQuotingItem.

        折扣率

        :param discount_ratio: The discount_ratio of this CategoryQuotingItem.
        :type discount_ratio: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._discount_ratio = discount_ratio

    @property
    def effective_time(self):
        r"""Gets the effective_time of this CategoryQuotingItem.

        报价项生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The effective_time of this CategoryQuotingItem.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this CategoryQuotingItem.

        报价项生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param effective_time: The effective_time of this CategoryQuotingItem.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CategoryQuotingItem.

        报价项失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The expire_time of this CategoryQuotingItem.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CategoryQuotingItem.

        报价项失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param expire_time: The expire_time of this CategoryQuotingItem.
        :type expire_time: str
        """
        self._expire_time = expire_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CategoryQuotingItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
