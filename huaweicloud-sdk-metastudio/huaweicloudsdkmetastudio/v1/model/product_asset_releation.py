# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductAssetReleation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_item': 'ProductMediaInfo',
        'text_item': 'ProductTextInfo',
        'action': 'str'
    }

    attribute_map = {
        'asset_item': 'asset_item',
        'text_item': 'text_item',
        'action': 'action'
    }

    def __init__(self, asset_item=None, text_item=None, action=None):
        r"""ProductAssetReleation

        The model defined in huaweicloud sdk

        :param asset_item: 
        :type asset_item: :class:`huaweicloudsdkmetastudio.v1.ProductMediaInfo`
        :param text_item: 
        :type text_item: :class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`
        :param action: 添加或删除资产关联 - LINK ：将资产纳入管理 - UNLINK ：将资产移除管理
        :type action: str
        """
        
        

        self._asset_item = None
        self._text_item = None
        self._action = None
        self.discriminator = None

        if asset_item is not None:
            self.asset_item = asset_item
        if text_item is not None:
            self.text_item = text_item
        if action is not None:
            self.action = action

    @property
    def asset_item(self):
        r"""Gets the asset_item of this ProductAssetReleation.

        :return: The asset_item of this ProductAssetReleation.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ProductMediaInfo`
        """
        return self._asset_item

    @asset_item.setter
    def asset_item(self, asset_item):
        r"""Sets the asset_item of this ProductAssetReleation.

        :param asset_item: The asset_item of this ProductAssetReleation.
        :type asset_item: :class:`huaweicloudsdkmetastudio.v1.ProductMediaInfo`
        """
        self._asset_item = asset_item

    @property
    def text_item(self):
        r"""Gets the text_item of this ProductAssetReleation.

        :return: The text_item of this ProductAssetReleation.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`
        """
        return self._text_item

    @text_item.setter
    def text_item(self, text_item):
        r"""Sets the text_item of this ProductAssetReleation.

        :param text_item: The text_item of this ProductAssetReleation.
        :type text_item: :class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`
        """
        self._text_item = text_item

    @property
    def action(self):
        r"""Gets the action of this ProductAssetReleation.

        添加或删除资产关联 - LINK ：将资产纳入管理 - UNLINK ：将资产移除管理

        :return: The action of this ProductAssetReleation.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ProductAssetReleation.

        添加或删除资产关联 - LINK ：将资产纳入管理 - UNLINK ：将资产移除管理

        :param action: The action of this ProductAssetReleation.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, ProductAssetReleation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
