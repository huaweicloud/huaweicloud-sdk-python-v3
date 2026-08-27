# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveModelConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[ModelConfigItem]'
    }

    attribute_map = {
        'items': 'items'
    }

    def __init__(self, items=None):
        r"""RemoveModelConfigReq

        The model defined in huaweicloud sdk

        :param items: 关联项列表，每项指定要移除的模型分组与资源的关联。
        :type items: list[:class:`huaweicloudsdkworkspace.v2.ModelConfigItem`]
        """
        
        

        self._items = None
        self.discriminator = None

        self.items = items

    @property
    def items(self):
        r"""Gets the items of this RemoveModelConfigReq.

        关联项列表，每项指定要移除的模型分组与资源的关联。

        :return: The items of this RemoveModelConfigReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ModelConfigItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this RemoveModelConfigReq.

        关联项列表，每项指定要移除的模型分组与资源的关联。

        :param items: The items of this RemoveModelConfigReq.
        :type items: list[:class:`huaweicloudsdkworkspace.v2.ModelConfigItem`]
        """
        self._items = items

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RemoveModelConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
