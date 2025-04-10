# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbcOrderChange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service_console_url': 'str',
        'product_info': 'CbcProductInfoOrderChange',
        'resource_id': 'str',
        'is_auto_pay': 'bool',
        'promotion_info': 'str'
    }

    attribute_map = {
        'cloud_service_console_url': 'cloud_service_console_url',
        'product_info': 'product_info',
        'resource_id': 'resource_id',
        'is_auto_pay': 'is_auto_pay',
        'promotion_info': 'promotion_info'
    }

    def __init__(self, cloud_service_console_url=None, product_info=None, resource_id=None, is_auto_pay=None, promotion_info=None):
        r"""CbcOrderChange

        The model defined in huaweicloud sdk

        :param cloud_service_console_url: 云服务ConsoleURL。订单支付完成后，客户可以通过此URL跳转到云服务Console页面查看信息
        :type cloud_service_console_url: str
        :param product_info: 
        :type product_info: :class:`huaweicloudsdkcbr.v1.CbcProductInfoOrderChange`
        :param resource_id: 待变更的资源ID
        :type resource_id: str
        :param is_auto_pay: 是否自动支付，默认非自动支付：false
        :type is_auto_pay: bool
        :param promotion_info: 购买折扣
        :type promotion_info: str
        """
        
        

        self._cloud_service_console_url = None
        self._product_info = None
        self._resource_id = None
        self._is_auto_pay = None
        self._promotion_info = None
        self.discriminator = None

        if cloud_service_console_url is not None:
            self.cloud_service_console_url = cloud_service_console_url
        self.product_info = product_info
        self.resource_id = resource_id
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if promotion_info is not None:
            self.promotion_info = promotion_info

    @property
    def cloud_service_console_url(self):
        r"""Gets the cloud_service_console_url of this CbcOrderChange.

        云服务ConsoleURL。订单支付完成后，客户可以通过此URL跳转到云服务Console页面查看信息

        :return: The cloud_service_console_url of this CbcOrderChange.
        :rtype: str
        """
        return self._cloud_service_console_url

    @cloud_service_console_url.setter
    def cloud_service_console_url(self, cloud_service_console_url):
        r"""Sets the cloud_service_console_url of this CbcOrderChange.

        云服务ConsoleURL。订单支付完成后，客户可以通过此URL跳转到云服务Console页面查看信息

        :param cloud_service_console_url: The cloud_service_console_url of this CbcOrderChange.
        :type cloud_service_console_url: str
        """
        self._cloud_service_console_url = cloud_service_console_url

    @property
    def product_info(self):
        r"""Gets the product_info of this CbcOrderChange.

        :return: The product_info of this CbcOrderChange.
        :rtype: :class:`huaweicloudsdkcbr.v1.CbcProductInfoOrderChange`
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        r"""Sets the product_info of this CbcOrderChange.

        :param product_info: The product_info of this CbcOrderChange.
        :type product_info: :class:`huaweicloudsdkcbr.v1.CbcProductInfoOrderChange`
        """
        self._product_info = product_info

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CbcOrderChange.

        待变更的资源ID

        :return: The resource_id of this CbcOrderChange.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CbcOrderChange.

        待变更的资源ID

        :param resource_id: The resource_id of this CbcOrderChange.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this CbcOrderChange.

        是否自动支付，默认非自动支付：false

        :return: The is_auto_pay of this CbcOrderChange.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this CbcOrderChange.

        是否自动支付，默认非自动支付：false

        :param is_auto_pay: The is_auto_pay of this CbcOrderChange.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this CbcOrderChange.

        购买折扣

        :return: The promotion_info of this CbcOrderChange.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this CbcOrderChange.

        购买折扣

        :param promotion_info: The promotion_info of this CbcOrderChange.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

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
        if not isinstance(other, CbcOrderChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
