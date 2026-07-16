# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteOpsDatasetItemsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_ids': 'list[str]'
    }

    attribute_map = {
        'item_ids': 'item_ids'
    }

    def __init__(self, item_ids=None):
        r"""BatchDeleteOpsDatasetItemsRequestBody

        The model defined in huaweicloud sdk

        :param item_ids: **参数解释：** 待删除的数据条目唯一标识符列表。 **约束限制：** 必填参数；数组长度 1 到 1000。 **取值范围：** 符合 MongoDB ObjectID 规范的十六进制字符串列表。 **默认取值：** 不涉及。 
        :type item_ids: list[str]
        """
        
        

        self._item_ids = None
        self.discriminator = None

        self.item_ids = item_ids

    @property
    def item_ids(self):
        r"""Gets the item_ids of this BatchDeleteOpsDatasetItemsRequestBody.

        **参数解释：** 待删除的数据条目唯一标识符列表。 **约束限制：** 必填参数；数组长度 1 到 1000。 **取值范围：** 符合 MongoDB ObjectID 规范的十六进制字符串列表。 **默认取值：** 不涉及。 

        :return: The item_ids of this BatchDeleteOpsDatasetItemsRequestBody.
        :rtype: list[str]
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        r"""Sets the item_ids of this BatchDeleteOpsDatasetItemsRequestBody.

        **参数解释：** 待删除的数据条目唯一标识符列表。 **约束限制：** 必填参数；数组长度 1 到 1000。 **取值范围：** 符合 MongoDB ObjectID 规范的十六进制字符串列表。 **默认取值：** 不涉及。 

        :param item_ids: The item_ids of this BatchDeleteOpsDatasetItemsRequestBody.
        :type item_ids: list[str]
        """
        self._item_ids = item_ids

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
        if not isinstance(other, BatchDeleteOpsDatasetItemsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
