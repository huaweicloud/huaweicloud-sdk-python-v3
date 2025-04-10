# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductMediaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'asset_type': 'str',
        'order': 'int'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_type': 'asset_type',
        'order': 'order'
    }

    def __init__(self, asset_id=None, asset_type=None, order=None):
        r"""ProductMediaInfo

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID
        :type asset_id: str
        :param asset_type: 资产类型 * IMAGE：图片 * VIDEO：视频 * AUDIO：音频
        :type asset_type: str
        :param order: **参数解释**： 资产次序。不设置或者0表示按照加入时间先后排序。业务上将次序最靠前的图片设置为商品封面。
        :type order: int
        """
        
        

        self._asset_id = None
        self._asset_type = None
        self._order = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if asset_type is not None:
            self.asset_type = asset_type
        if order is not None:
            self.order = order

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ProductMediaInfo.

        资产ID

        :return: The asset_id of this ProductMediaInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ProductMediaInfo.

        资产ID

        :param asset_id: The asset_id of this ProductMediaInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ProductMediaInfo.

        资产类型 * IMAGE：图片 * VIDEO：视频 * AUDIO：音频

        :return: The asset_type of this ProductMediaInfo.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ProductMediaInfo.

        资产类型 * IMAGE：图片 * VIDEO：视频 * AUDIO：音频

        :param asset_type: The asset_type of this ProductMediaInfo.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def order(self):
        r"""Gets the order of this ProductMediaInfo.

        **参数解释**： 资产次序。不设置或者0表示按照加入时间先后排序。业务上将次序最靠前的图片设置为商品封面。

        :return: The order of this ProductMediaInfo.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ProductMediaInfo.

        **参数解释**： 资产次序。不设置或者0表示按照加入时间先后排序。业务上将次序最靠前的图片设置为商品封面。

        :param order: The order of this ProductMediaInfo.
        :type order: int
        """
        self._order = order

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
        if not isinstance(other, ProductMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
