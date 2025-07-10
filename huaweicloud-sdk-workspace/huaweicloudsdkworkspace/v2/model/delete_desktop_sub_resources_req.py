# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDesktopSubResourcesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]',
        'sub_resource_type': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'sub_resource_type': 'sub_resource_type',
        'order_id': 'order_id'
    }

    def __init__(self, desktop_ids=None, sub_resource_type=None, order_id=None):
        r"""DeleteDesktopSubResourcesReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 桌面ID列表。
        :type desktop_ids: list[str]
        :param sub_resource_type: 待删除附属资源类型。DESKTOP_SHARER：桌面协同资源。
        :type sub_resource_type: str
        :param order_id: 订单ID。
        :type order_id: str
        """
        
        

        self._desktop_ids = None
        self._sub_resource_type = None
        self._order_id = None
        self.discriminator = None

        self.desktop_ids = desktop_ids
        self.sub_resource_type = sub_resource_type
        if order_id is not None:
            self.order_id = order_id

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this DeleteDesktopSubResourcesReq.

        桌面ID列表。

        :return: The desktop_ids of this DeleteDesktopSubResourcesReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this DeleteDesktopSubResourcesReq.

        桌面ID列表。

        :param desktop_ids: The desktop_ids of this DeleteDesktopSubResourcesReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def sub_resource_type(self):
        r"""Gets the sub_resource_type of this DeleteDesktopSubResourcesReq.

        待删除附属资源类型。DESKTOP_SHARER：桌面协同资源。

        :return: The sub_resource_type of this DeleteDesktopSubResourcesReq.
        :rtype: str
        """
        return self._sub_resource_type

    @sub_resource_type.setter
    def sub_resource_type(self, sub_resource_type):
        r"""Sets the sub_resource_type of this DeleteDesktopSubResourcesReq.

        待删除附属资源类型。DESKTOP_SHARER：桌面协同资源。

        :param sub_resource_type: The sub_resource_type of this DeleteDesktopSubResourcesReq.
        :type sub_resource_type: str
        """
        self._sub_resource_type = sub_resource_type

    @property
    def order_id(self):
        r"""Gets the order_id of this DeleteDesktopSubResourcesReq.

        订单ID。

        :return: The order_id of this DeleteDesktopSubResourcesReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this DeleteDesktopSubResourcesReq.

        订单ID。

        :param order_id: The order_id of this DeleteDesktopSubResourcesReq.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, DeleteDesktopSubResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
