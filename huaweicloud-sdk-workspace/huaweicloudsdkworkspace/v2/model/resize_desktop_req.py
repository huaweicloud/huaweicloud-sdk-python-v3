# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeDesktopReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktops': 'list[ResizeDesktopData]',
        'product_id': 'str',
        'flavor_id': 'str',
        'mode': 'str',
        'dedicated_host_id': 'str',
        'order_id': 'str',
        'extend_param': 'ResizeDesktopExtendParam'
    }

    attribute_map = {
        'desktops': 'desktops',
        'product_id': 'product_id',
        'flavor_id': 'flavor_id',
        'mode': 'mode',
        'dedicated_host_id': 'dedicated_host_id',
        'order_id': 'order_id',
        'extend_param': 'extend_param'
    }

    def __init__(self, desktops=None, product_id=None, flavor_id=None, mode=None, dedicated_host_id=None, order_id=None, extend_param=None):
        """ResizeDesktopReq

        The model defined in huaweicloud sdk

        :param desktops: 桌面数据。支持批量按需类型桌面变更为同一规格。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.ResizeDesktopData`]
        :param product_id: 套餐id。批量变更时，则变更为同一规格的虚拟机。
        :type product_id: str
        :param flavor_id: 套餐flavorId。批量变更时，则变更为同一规格的虚拟机。
        :type flavor_id: str
        :param mode: 是否支持开机状态下执行变更规格操作。固定传值STOP_DESKTOP，如果桌面处于开机状态，会先关机再变更规格。
        :type mode: str
        :param dedicated_host_id: 专属主机ID。
        :type dedicated_host_id: str
        :param order_id: 订单ID，包周期变更规格时使用。
        :type order_id: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopExtendParam`
        """
        
        

        self._desktops = None
        self._product_id = None
        self._flavor_id = None
        self._mode = None
        self._dedicated_host_id = None
        self._order_id = None
        self._extend_param = None
        self.discriminator = None

        self.desktops = desktops
        self.product_id = product_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        self.mode = mode
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if order_id is not None:
            self.order_id = order_id
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def desktops(self):
        """Gets the desktops of this ResizeDesktopReq.

        桌面数据。支持批量按需类型桌面变更为同一规格。

        :return: The desktops of this ResizeDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ResizeDesktopData`]
        """
        return self._desktops

    @desktops.setter
    def desktops(self, desktops):
        """Sets the desktops of this ResizeDesktopReq.

        桌面数据。支持批量按需类型桌面变更为同一规格。

        :param desktops: The desktops of this ResizeDesktopReq.
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.ResizeDesktopData`]
        """
        self._desktops = desktops

    @property
    def product_id(self):
        """Gets the product_id of this ResizeDesktopReq.

        套餐id。批量变更时，则变更为同一规格的虚拟机。

        :return: The product_id of this ResizeDesktopReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ResizeDesktopReq.

        套餐id。批量变更时，则变更为同一规格的虚拟机。

        :param product_id: The product_id of this ResizeDesktopReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def flavor_id(self):
        """Gets the flavor_id of this ResizeDesktopReq.

        套餐flavorId。批量变更时，则变更为同一规格的虚拟机。

        :return: The flavor_id of this ResizeDesktopReq.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this ResizeDesktopReq.

        套餐flavorId。批量变更时，则变更为同一规格的虚拟机。

        :param flavor_id: The flavor_id of this ResizeDesktopReq.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def mode(self):
        """Gets the mode of this ResizeDesktopReq.

        是否支持开机状态下执行变更规格操作。固定传值STOP_DESKTOP，如果桌面处于开机状态，会先关机再变更规格。

        :return: The mode of this ResizeDesktopReq.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ResizeDesktopReq.

        是否支持开机状态下执行变更规格操作。固定传值STOP_DESKTOP，如果桌面处于开机状态，会先关机再变更规格。

        :param mode: The mode of this ResizeDesktopReq.
        :type mode: str
        """
        self._mode = mode

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this ResizeDesktopReq.

        专属主机ID。

        :return: The dedicated_host_id of this ResizeDesktopReq.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this ResizeDesktopReq.

        专属主机ID。

        :param dedicated_host_id: The dedicated_host_id of this ResizeDesktopReq.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def order_id(self):
        """Gets the order_id of this ResizeDesktopReq.

        订单ID，包周期变更规格时使用。

        :return: The order_id of this ResizeDesktopReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ResizeDesktopReq.

        订单ID，包周期变更规格时使用。

        :param order_id: The order_id of this ResizeDesktopReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def extend_param(self):
        """Gets the extend_param of this ResizeDesktopReq.

        :return: The extend_param of this ResizeDesktopReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this ResizeDesktopReq.

        :param extend_param: The extend_param of this ResizeDesktopReq.
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, ResizeDesktopReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
