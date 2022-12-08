# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductOrderInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'period_type': 'str',
        'period_num': 'int',
        'resource_id': 'str',
        'product_info': 'list[ProductInfoBean]'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'resource_id': 'resource_id',
        'product_info': 'product_info'
    }

    def __init__(self, tenant_id=None, period_type=None, period_num=None, resource_id=None, product_info=None):
        """ProductOrderInfo

        The model defined in huaweicloud sdk

        :param tenant_id: 租户ID
        :type tenant_id: str
        :param period_type: 订购周期类型
        :type period_type: str
        :param period_num: 订购周期数量
        :type period_num: int
        :param resource_id: 资源ID
        :type resource_id: str
        :param product_info: 产品信息
        :type product_info: list[:class:`huaweicloudsdkdsc.v1.ProductInfoBean`]
        """
        
        

        self._tenant_id = None
        self._period_type = None
        self._period_num = None
        self._resource_id = None
        self._product_info = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if resource_id is not None:
            self.resource_id = resource_id
        if product_info is not None:
            self.product_info = product_info

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ProductOrderInfo.

        租户ID

        :return: The tenant_id of this ProductOrderInfo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ProductOrderInfo.

        租户ID

        :param tenant_id: The tenant_id of this ProductOrderInfo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def period_type(self):
        """Gets the period_type of this ProductOrderInfo.

        订购周期类型

        :return: The period_type of this ProductOrderInfo.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this ProductOrderInfo.

        订购周期类型

        :param period_type: The period_type of this ProductOrderInfo.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this ProductOrderInfo.

        订购周期数量

        :return: The period_num of this ProductOrderInfo.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this ProductOrderInfo.

        订购周期数量

        :param period_num: The period_num of this ProductOrderInfo.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def resource_id(self):
        """Gets the resource_id of this ProductOrderInfo.

        资源ID

        :return: The resource_id of this ProductOrderInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ProductOrderInfo.

        资源ID

        :param resource_id: The resource_id of this ProductOrderInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def product_info(self):
        """Gets the product_info of this ProductOrderInfo.

        产品信息

        :return: The product_info of this ProductOrderInfo.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.ProductInfoBean`]
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        """Sets the product_info of this ProductOrderInfo.

        产品信息

        :param product_info: The product_info of this ProductOrderInfo.
        :type product_info: list[:class:`huaweicloudsdkdsc.v1.ProductInfoBean`]
        """
        self._product_info = product_info

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
        if not isinstance(other, ProductOrderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
