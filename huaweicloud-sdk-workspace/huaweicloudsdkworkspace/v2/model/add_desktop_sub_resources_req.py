# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDesktopSubResourcesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_resource_sku': 'str',
        'order_id': 'str',
        'desktop_ids': 'list[str]'
    }

    attribute_map = {
        'sub_resource_sku': 'sub_resource_sku',
        'order_id': 'order_id',
        'desktop_ids': 'desktop_ids'
    }

    def __init__(self, sub_resource_sku=None, order_id=None, desktop_ids=None):
        r"""AddDesktopSubResourcesReq

        The model defined in huaweicloud sdk

        :param sub_resource_sku: 桌面协同资源SKU码。
        :type sub_resource_sku: str
        :param order_id: 订单ID。
        :type order_id: str
        :param desktop_ids: 桌面ID列表。
        :type desktop_ids: list[str]
        """
        
        

        self._sub_resource_sku = None
        self._order_id = None
        self._desktop_ids = None
        self.discriminator = None

        self.sub_resource_sku = sub_resource_sku
        if order_id is not None:
            self.order_id = order_id
        self.desktop_ids = desktop_ids

    @property
    def sub_resource_sku(self):
        r"""Gets the sub_resource_sku of this AddDesktopSubResourcesReq.

        桌面协同资源SKU码。

        :return: The sub_resource_sku of this AddDesktopSubResourcesReq.
        :rtype: str
        """
        return self._sub_resource_sku

    @sub_resource_sku.setter
    def sub_resource_sku(self, sub_resource_sku):
        r"""Sets the sub_resource_sku of this AddDesktopSubResourcesReq.

        桌面协同资源SKU码。

        :param sub_resource_sku: The sub_resource_sku of this AddDesktopSubResourcesReq.
        :type sub_resource_sku: str
        """
        self._sub_resource_sku = sub_resource_sku

    @property
    def order_id(self):
        r"""Gets the order_id of this AddDesktopSubResourcesReq.

        订单ID。

        :return: The order_id of this AddDesktopSubResourcesReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this AddDesktopSubResourcesReq.

        订单ID。

        :param order_id: The order_id of this AddDesktopSubResourcesReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this AddDesktopSubResourcesReq.

        桌面ID列表。

        :return: The desktop_ids of this AddDesktopSubResourcesReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this AddDesktopSubResourcesReq.

        桌面ID列表。

        :param desktop_ids: The desktop_ids of this AddDesktopSubResourcesReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

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
        if not isinstance(other, AddDesktopSubResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
