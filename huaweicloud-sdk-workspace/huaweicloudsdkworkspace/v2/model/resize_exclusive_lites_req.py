# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeExclusiveLitesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'order_id': 'str',
        'enterprise_project_id': 'str',
        'product_id': 'str',
        'new_quantity': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'order_id': 'order_id',
        'enterprise_project_id': 'enterprise_project_id',
        'product_id': 'product_id',
        'new_quantity': 'new_quantity'
    }

    def __init__(self, host_id=None, order_id=None, enterprise_project_id=None, product_id=None, new_quantity=None):
        """ResizeExclusiveLitesReq

        The model defined in huaweicloud sdk

        :param host_id: 专享主机的hostId。
        :type host_id: str
        :param order_id: 订单ID，包周期专享主机变更桌面路数时使用。
        :type order_id: str
        :param enterprise_project_id: 企业项目ID，默认\&quot;0\&quot;
        :type enterprise_project_id: str
        :param product_id: 产品套餐ID。
        :type product_id: str
        :param new_quantity: 扩容后的桌面个数，单位为个/次。
        :type new_quantity: int
        """
        
        

        self._host_id = None
        self._order_id = None
        self._enterprise_project_id = None
        self._product_id = None
        self._new_quantity = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if order_id is not None:
            self.order_id = order_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.product_id = product_id
        self.new_quantity = new_quantity

    @property
    def host_id(self):
        """Gets the host_id of this ResizeExclusiveLitesReq.

        专享主机的hostId。

        :return: The host_id of this ResizeExclusiveLitesReq.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ResizeExclusiveLitesReq.

        专享主机的hostId。

        :param host_id: The host_id of this ResizeExclusiveLitesReq.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def order_id(self):
        """Gets the order_id of this ResizeExclusiveLitesReq.

        订单ID，包周期专享主机变更桌面路数时使用。

        :return: The order_id of this ResizeExclusiveLitesReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ResizeExclusiveLitesReq.

        订单ID，包周期专享主机变更桌面路数时使用。

        :param order_id: The order_id of this ResizeExclusiveLitesReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ResizeExclusiveLitesReq.

        企业项目ID，默认\"0\"

        :return: The enterprise_project_id of this ResizeExclusiveLitesReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ResizeExclusiveLitesReq.

        企业项目ID，默认\"0\"

        :param enterprise_project_id: The enterprise_project_id of this ResizeExclusiveLitesReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def product_id(self):
        """Gets the product_id of this ResizeExclusiveLitesReq.

        产品套餐ID。

        :return: The product_id of this ResizeExclusiveLitesReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ResizeExclusiveLitesReq.

        产品套餐ID。

        :param product_id: The product_id of this ResizeExclusiveLitesReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def new_quantity(self):
        """Gets the new_quantity of this ResizeExclusiveLitesReq.

        扩容后的桌面个数，单位为个/次。

        :return: The new_quantity of this ResizeExclusiveLitesReq.
        :rtype: int
        """
        return self._new_quantity

    @new_quantity.setter
    def new_quantity(self, new_quantity):
        """Sets the new_quantity of this ResizeExclusiveLitesReq.

        扩容后的桌面个数，单位为个/次。

        :param new_quantity: The new_quantity of this ResizeExclusiveLitesReq.
        :type new_quantity: int
        """
        self._new_quantity = new_quantity

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
        if not isinstance(other, ResizeExclusiveLitesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
