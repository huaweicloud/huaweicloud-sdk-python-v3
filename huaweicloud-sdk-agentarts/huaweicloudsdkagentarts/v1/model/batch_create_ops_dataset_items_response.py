# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateOpsDatasetItemsResponse(SdkResponse):

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
        r"""BatchCreateOpsDatasetItemsResponse

        The model defined in huaweicloud sdk

        :param item_ids: **参数解释：** 系统为新创建的数据条目生成的唯一标识符列表。 **取值范围：** 符合数据库标识符规范的字符串列表。 
        :type item_ids: list[str]
        """
        
        super().__init__()

        self._item_ids = None
        self.discriminator = None

        if item_ids is not None:
            self.item_ids = item_ids

    @property
    def item_ids(self):
        r"""Gets the item_ids of this BatchCreateOpsDatasetItemsResponse.

        **参数解释：** 系统为新创建的数据条目生成的唯一标识符列表。 **取值范围：** 符合数据库标识符规范的字符串列表。 

        :return: The item_ids of this BatchCreateOpsDatasetItemsResponse.
        :rtype: list[str]
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        r"""Sets the item_ids of this BatchCreateOpsDatasetItemsResponse.

        **参数解释：** 系统为新创建的数据条目生成的唯一标识符列表。 **取值范围：** 符合数据库标识符规范的字符串列表。 

        :param item_ids: The item_ids of this BatchCreateOpsDatasetItemsResponse.
        :type item_ids: list[str]
        """
        self._item_ids = item_ids

    def to_dict(self):
        import warnings
        warnings.warn("BatchCreateOpsDatasetItemsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, BatchCreateOpsDatasetItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
