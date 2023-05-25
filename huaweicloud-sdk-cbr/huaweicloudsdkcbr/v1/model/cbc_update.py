# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbcUpdate:

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
        'product_info': 'CbcProductInfoUpdate',
        'resource_id': 'str',
        'promotion_info': 'str'
    }

    attribute_map = {
        'cloud_service_console_url': 'cloudServiceConsoleURL',
        'product_info': 'productInfo',
        'resource_id': 'resourceId',
        'promotion_info': 'promotion_info'
    }

    def __init__(self, cloud_service_console_url=None, product_info=None, resource_id=None, promotion_info=None):
        """CbcUpdate

        The model defined in huaweicloud sdk

        :param cloud_service_console_url: 云服务ConsoleURL。订单支付完成后，客户可以通过此URL跳转到云服务Console页面查看信息
        :type cloud_service_console_url: str
        :param product_info: 
        :type product_info: :class:`huaweicloudsdkcbr.v1.CbcProductInfoUpdate`
        :param resource_id: 待变更的资源ID
        :type resource_id: str
        :param promotion_info: 购买折扣
        :type promotion_info: str
        """
        
        

        self._cloud_service_console_url = None
        self._product_info = None
        self._resource_id = None
        self._promotion_info = None
        self.discriminator = None

        if cloud_service_console_url is not None:
            self.cloud_service_console_url = cloud_service_console_url
        self.product_info = product_info
        self.resource_id = resource_id
        if promotion_info is not None:
            self.promotion_info = promotion_info

    @property
    def cloud_service_console_url(self):
        """Gets the cloud_service_console_url of this CbcUpdate.

        云服务ConsoleURL。订单支付完成后，客户可以通过此URL跳转到云服务Console页面查看信息

        :return: The cloud_service_console_url of this CbcUpdate.
        :rtype: str
        """
        return self._cloud_service_console_url

    @cloud_service_console_url.setter
    def cloud_service_console_url(self, cloud_service_console_url):
        """Sets the cloud_service_console_url of this CbcUpdate.

        云服务ConsoleURL。订单支付完成后，客户可以通过此URL跳转到云服务Console页面查看信息

        :param cloud_service_console_url: The cloud_service_console_url of this CbcUpdate.
        :type cloud_service_console_url: str
        """
        self._cloud_service_console_url = cloud_service_console_url

    @property
    def product_info(self):
        """Gets the product_info of this CbcUpdate.

        :return: The product_info of this CbcUpdate.
        :rtype: :class:`huaweicloudsdkcbr.v1.CbcProductInfoUpdate`
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        """Sets the product_info of this CbcUpdate.

        :param product_info: The product_info of this CbcUpdate.
        :type product_info: :class:`huaweicloudsdkcbr.v1.CbcProductInfoUpdate`
        """
        self._product_info = product_info

    @property
    def resource_id(self):
        """Gets the resource_id of this CbcUpdate.

        待变更的资源ID

        :return: The resource_id of this CbcUpdate.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CbcUpdate.

        待变更的资源ID

        :param resource_id: The resource_id of this CbcUpdate.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def promotion_info(self):
        """Gets the promotion_info of this CbcUpdate.

        购买折扣

        :return: The promotion_info of this CbcUpdate.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        """Sets the promotion_info of this CbcUpdate.

        购买折扣

        :param promotion_info: The promotion_info of this CbcUpdate.
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
        if not isinstance(other, CbcUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
