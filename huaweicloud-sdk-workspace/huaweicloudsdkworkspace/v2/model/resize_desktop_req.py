# coding: utf-8

import re
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
        'mode': 'str'
    }

    attribute_map = {
        'desktops': 'desktops',
        'product_id': 'product_id',
        'mode': 'mode'
    }

    def __init__(self, desktops=None, product_id=None, mode=None):
        """ResizeDesktopReq

        The model defined in huaweicloud sdk

        :param desktops: 桌面数据。支持批量按需类型桌面变更为同一规格。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.ResizeDesktopData`]
        :param product_id: 套餐id。批量变更时，则变更为同一规格的虚拟机。
        :type product_id: str
        :param mode: 是否支持开机状态下执行变更规格操作。固定传值STOP_DESKTOP，如果桌面处于开机状态，会先关机再变更规格。
        :type mode: str
        """
        
        

        self._desktops = None
        self._product_id = None
        self._mode = None
        self.discriminator = None

        self.desktops = desktops
        self.product_id = product_id
        self.mode = mode

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
