# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeDesktopPoolReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'flavor_id': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'flavor_id': 'flavor_id',
        'mode': 'mode'
    }

    def __init__(self, product_id=None, flavor_id=None, mode=None):
        r"""ResizeDesktopPoolReq

        The model defined in huaweicloud sdk

        :param product_id: 目标规格产品ID。
        :type product_id: str
        :param flavor_id: 产品规格ID。可用区是边缘可用区时，必填此参数。
        :type flavor_id: str
        :param mode: 是否支持开机状态下执行变更规格操作。固定传值STOP_DESKTOP，如果桌面处于开机状态，会先关机再变更规格。
        :type mode: str
        """
        
        

        self._product_id = None
        self._flavor_id = None
        self._mode = None
        self.discriminator = None

        self.product_id = product_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if mode is not None:
            self.mode = mode

    @property
    def product_id(self):
        r"""Gets the product_id of this ResizeDesktopPoolReq.

        目标规格产品ID。

        :return: The product_id of this ResizeDesktopPoolReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ResizeDesktopPoolReq.

        目标规格产品ID。

        :param product_id: The product_id of this ResizeDesktopPoolReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ResizeDesktopPoolReq.

        产品规格ID。可用区是边缘可用区时，必填此参数。

        :return: The flavor_id of this ResizeDesktopPoolReq.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ResizeDesktopPoolReq.

        产品规格ID。可用区是边缘可用区时，必填此参数。

        :param flavor_id: The flavor_id of this ResizeDesktopPoolReq.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def mode(self):
        r"""Gets the mode of this ResizeDesktopPoolReq.

        是否支持开机状态下执行变更规格操作。固定传值STOP_DESKTOP，如果桌面处于开机状态，会先关机再变更规格。

        :return: The mode of this ResizeDesktopPoolReq.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ResizeDesktopPoolReq.

        是否支持开机状态下执行变更规格操作。固定传值STOP_DESKTOP，如果桌面处于开机状态，会先关机再变更规格。

        :param mode: The mode of this ResizeDesktopPoolReq.
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
        if not isinstance(other, ResizeDesktopPoolReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
