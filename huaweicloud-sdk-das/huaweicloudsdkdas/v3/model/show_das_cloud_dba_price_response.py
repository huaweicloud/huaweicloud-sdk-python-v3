# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDasCloudDbaPriceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_price': 'float',
        'original_base_price': 'float',
        'storage_price': 'float',
        'original_storage_price': 'float',
        'dump_price': 'float',
        'original_dump_price': 'float',
        'measure_id': 'int',
        'currency': 'str',
        'configure_price': 'float'
    }

    attribute_map = {
        'base_price': 'base_price',
        'original_base_price': 'original_base_price',
        'storage_price': 'storage_price',
        'original_storage_price': 'original_storage_price',
        'dump_price': 'dump_price',
        'original_dump_price': 'original_dump_price',
        'measure_id': 'measure_id',
        'currency': 'currency',
        'configure_price': 'configure_price'
    }

    def __init__(self, base_price=None, original_base_price=None, storage_price=None, original_storage_price=None, dump_price=None, original_dump_price=None, measure_id=None, currency=None, configure_price=None):
        r"""ShowDasCloudDbaPriceResponse

        The model defined in huaweicloud sdk

        :param base_price: 基础费用
        :type base_price: float
        :param original_base_price: 基础费用-原价
        :type original_base_price: float
        :param storage_price: 存储费用
        :type storage_price: float
        :param original_storage_price: 存储费用-原价
        :type original_storage_price: float
        :param dump_price: 转储费用
        :type dump_price: float
        :param original_dump_price: 转储费用-原价
        :type original_dump_price: float
        :param measure_id: 度量单位标识,1:元
        :type measure_id: int
        :param currency: 币种，比如CNY
        :type currency: str
        :param configure_price: 配置费用-当前为0
        :type configure_price: float
        """
        
        super().__init__()

        self._base_price = None
        self._original_base_price = None
        self._storage_price = None
        self._original_storage_price = None
        self._dump_price = None
        self._original_dump_price = None
        self._measure_id = None
        self._currency = None
        self._configure_price = None
        self.discriminator = None

        if base_price is not None:
            self.base_price = base_price
        if original_base_price is not None:
            self.original_base_price = original_base_price
        if storage_price is not None:
            self.storage_price = storage_price
        if original_storage_price is not None:
            self.original_storage_price = original_storage_price
        if dump_price is not None:
            self.dump_price = dump_price
        if original_dump_price is not None:
            self.original_dump_price = original_dump_price
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency
        if configure_price is not None:
            self.configure_price = configure_price

    @property
    def base_price(self):
        r"""Gets the base_price of this ShowDasCloudDbaPriceResponse.

        基础费用

        :return: The base_price of this ShowDasCloudDbaPriceResponse.
        :rtype: float
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        r"""Sets the base_price of this ShowDasCloudDbaPriceResponse.

        基础费用

        :param base_price: The base_price of this ShowDasCloudDbaPriceResponse.
        :type base_price: float
        """
        self._base_price = base_price

    @property
    def original_base_price(self):
        r"""Gets the original_base_price of this ShowDasCloudDbaPriceResponse.

        基础费用-原价

        :return: The original_base_price of this ShowDasCloudDbaPriceResponse.
        :rtype: float
        """
        return self._original_base_price

    @original_base_price.setter
    def original_base_price(self, original_base_price):
        r"""Sets the original_base_price of this ShowDasCloudDbaPriceResponse.

        基础费用-原价

        :param original_base_price: The original_base_price of this ShowDasCloudDbaPriceResponse.
        :type original_base_price: float
        """
        self._original_base_price = original_base_price

    @property
    def storage_price(self):
        r"""Gets the storage_price of this ShowDasCloudDbaPriceResponse.

        存储费用

        :return: The storage_price of this ShowDasCloudDbaPriceResponse.
        :rtype: float
        """
        return self._storage_price

    @storage_price.setter
    def storage_price(self, storage_price):
        r"""Sets the storage_price of this ShowDasCloudDbaPriceResponse.

        存储费用

        :param storage_price: The storage_price of this ShowDasCloudDbaPriceResponse.
        :type storage_price: float
        """
        self._storage_price = storage_price

    @property
    def original_storage_price(self):
        r"""Gets the original_storage_price of this ShowDasCloudDbaPriceResponse.

        存储费用-原价

        :return: The original_storage_price of this ShowDasCloudDbaPriceResponse.
        :rtype: float
        """
        return self._original_storage_price

    @original_storage_price.setter
    def original_storage_price(self, original_storage_price):
        r"""Sets the original_storage_price of this ShowDasCloudDbaPriceResponse.

        存储费用-原价

        :param original_storage_price: The original_storage_price of this ShowDasCloudDbaPriceResponse.
        :type original_storage_price: float
        """
        self._original_storage_price = original_storage_price

    @property
    def dump_price(self):
        r"""Gets the dump_price of this ShowDasCloudDbaPriceResponse.

        转储费用

        :return: The dump_price of this ShowDasCloudDbaPriceResponse.
        :rtype: float
        """
        return self._dump_price

    @dump_price.setter
    def dump_price(self, dump_price):
        r"""Sets the dump_price of this ShowDasCloudDbaPriceResponse.

        转储费用

        :param dump_price: The dump_price of this ShowDasCloudDbaPriceResponse.
        :type dump_price: float
        """
        self._dump_price = dump_price

    @property
    def original_dump_price(self):
        r"""Gets the original_dump_price of this ShowDasCloudDbaPriceResponse.

        转储费用-原价

        :return: The original_dump_price of this ShowDasCloudDbaPriceResponse.
        :rtype: float
        """
        return self._original_dump_price

    @original_dump_price.setter
    def original_dump_price(self, original_dump_price):
        r"""Sets the original_dump_price of this ShowDasCloudDbaPriceResponse.

        转储费用-原价

        :param original_dump_price: The original_dump_price of this ShowDasCloudDbaPriceResponse.
        :type original_dump_price: float
        """
        self._original_dump_price = original_dump_price

    @property
    def measure_id(self):
        r"""Gets the measure_id of this ShowDasCloudDbaPriceResponse.

        度量单位标识,1:元

        :return: The measure_id of this ShowDasCloudDbaPriceResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this ShowDasCloudDbaPriceResponse.

        度量单位标识,1:元

        :param measure_id: The measure_id of this ShowDasCloudDbaPriceResponse.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        r"""Gets the currency of this ShowDasCloudDbaPriceResponse.

        币种，比如CNY

        :return: The currency of this ShowDasCloudDbaPriceResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this ShowDasCloudDbaPriceResponse.

        币种，比如CNY

        :param currency: The currency of this ShowDasCloudDbaPriceResponse.
        :type currency: str
        """
        self._currency = currency

    @property
    def configure_price(self):
        r"""Gets the configure_price of this ShowDasCloudDbaPriceResponse.

        配置费用-当前为0

        :return: The configure_price of this ShowDasCloudDbaPriceResponse.
        :rtype: float
        """
        return self._configure_price

    @configure_price.setter
    def configure_price(self, configure_price):
        r"""Sets the configure_price of this ShowDasCloudDbaPriceResponse.

        配置费用-当前为0

        :param configure_price: The configure_price of this ShowDasCloudDbaPriceResponse.
        :type configure_price: float
        """
        self._configure_price = configure_price

    def to_dict(self):
        import warnings
        warnings.warn("ShowDasCloudDbaPriceResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowDasCloudDbaPriceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
