# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStoreData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stores': 'list[StoreData]'
    }

    attribute_map = {
        'stores': 'stores'
    }

    def __init__(self, stores=None):
        r"""ListStoreData

        The model defined in huaweicloud sdk

        :param stores: **参数解释：** 列举store列表。 **约束限制：** 不涉及。
        :type stores: list[:class:`huaweicloudsdkdwr.v1.StoreData`]
        """
        
        

        self._stores = None
        self.discriminator = None

        self.stores = stores

    @property
    def stores(self):
        r"""Gets the stores of this ListStoreData.

        **参数解释：** 列举store列表。 **约束限制：** 不涉及。

        :return: The stores of this ListStoreData.
        :rtype: list[:class:`huaweicloudsdkdwr.v1.StoreData`]
        """
        return self._stores

    @stores.setter
    def stores(self, stores):
        r"""Sets the stores of this ListStoreData.

        **参数解释：** 列举store列表。 **约束限制：** 不涉及。

        :param stores: The stores of this ListStoreData.
        :type stores: list[:class:`huaweicloudsdkdwr.v1.StoreData`]
        """
        self._stores = stores

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
        if not isinstance(other, ListStoreData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
