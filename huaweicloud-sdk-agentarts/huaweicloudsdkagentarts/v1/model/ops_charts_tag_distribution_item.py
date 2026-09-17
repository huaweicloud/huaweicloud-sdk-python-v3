# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsChartsTagDistributionItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_id': 'str',
        'tag_name': 'str',
        'tag_type': 'str',
        'item_list': 'list[OpsChartsTagValueCount]'
    }

    attribute_map = {
        'tag_id': 'tag_id',
        'tag_name': 'tag_name',
        'tag_type': 'tag_type',
        'item_list': 'item_list'
    }

    def __init__(self, tag_id=None, tag_name=None, tag_type=None, item_list=None):
        r"""OpsChartsTagDistributionItem

        The model defined in huaweicloud sdk

        :param tag_id: 标签ID。
        :type tag_id: str
        :param tag_name: 标签名称。
        :type tag_name: str
        :param tag_type: 标签类型。
        :type tag_type: str
        :param item_list: 标签值分布列表。
        :type item_list: list[:class:`huaweicloudsdkagentarts.v1.OpsChartsTagValueCount`]
        """
        
        

        self._tag_id = None
        self._tag_name = None
        self._tag_type = None
        self._item_list = None
        self.discriminator = None

        if tag_id is not None:
            self.tag_id = tag_id
        if tag_name is not None:
            self.tag_name = tag_name
        if tag_type is not None:
            self.tag_type = tag_type
        if item_list is not None:
            self.item_list = item_list

    @property
    def tag_id(self):
        r"""Gets the tag_id of this OpsChartsTagDistributionItem.

        标签ID。

        :return: The tag_id of this OpsChartsTagDistributionItem.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this OpsChartsTagDistributionItem.

        标签ID。

        :param tag_id: The tag_id of this OpsChartsTagDistributionItem.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def tag_name(self):
        r"""Gets the tag_name of this OpsChartsTagDistributionItem.

        标签名称。

        :return: The tag_name of this OpsChartsTagDistributionItem.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        r"""Sets the tag_name of this OpsChartsTagDistributionItem.

        标签名称。

        :param tag_name: The tag_name of this OpsChartsTagDistributionItem.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def tag_type(self):
        r"""Gets the tag_type of this OpsChartsTagDistributionItem.

        标签类型。

        :return: The tag_type of this OpsChartsTagDistributionItem.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        r"""Sets the tag_type of this OpsChartsTagDistributionItem.

        标签类型。

        :param tag_type: The tag_type of this OpsChartsTagDistributionItem.
        :type tag_type: str
        """
        self._tag_type = tag_type

    @property
    def item_list(self):
        r"""Gets the item_list of this OpsChartsTagDistributionItem.

        标签值分布列表。

        :return: The item_list of this OpsChartsTagDistributionItem.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsChartsTagValueCount`]
        """
        return self._item_list

    @item_list.setter
    def item_list(self, item_list):
        r"""Sets the item_list of this OpsChartsTagDistributionItem.

        标签值分布列表。

        :param item_list: The item_list of this OpsChartsTagDistributionItem.
        :type item_list: list[:class:`huaweicloudsdkagentarts.v1.OpsChartsTagValueCount`]
        """
        self._item_list = item_list

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
        if not isinstance(other, OpsChartsTagDistributionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
