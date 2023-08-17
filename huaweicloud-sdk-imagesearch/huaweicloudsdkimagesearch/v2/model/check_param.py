# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_id': 'str',
        'limit': 'int',
        'last_item': 'SearchAfterParam',
        'custom_tags': 'dict(str, list[str])',
        'custom_num_tags': 'dict(str, RangeParam)'
    }

    attribute_map = {
        'item_id': 'item_id',
        'limit': 'limit',
        'last_item': 'last_item',
        'custom_tags': 'custom_tags',
        'custom_num_tags': 'custom_num_tags'
    }

    def __init__(self, item_id=None, limit=None, last_item=None, custom_tags=None, custom_num_tags=None):
        """CheckParam

        The model defined in huaweicloud sdk

        :param item_id: 数据的服务实例级唯一标识，字符长度范围为[1, 256]。 - item_id/custom_tags/custom_num_tags中必须给定至少一个参数，以支持对服务实例中的数据进行指定ID检查或条件检查。 - 如给定item_id参数，则进行指定ID检查，否则进行条件检查。
        :type item_id: str
        :param limit: 返回检查结果的数量，默认为10，取值范围为[1, 100]。仅对条件检查生效。
        :type limit: int
        :param last_item: 
        :type last_item: :class:`huaweicloudsdkimagesearch.v2.SearchAfterParam`
        :param custom_tags: 自定义字符标签，用于对服务实例中的数据进行条件查找。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 标签值列表，列表内多个标签值为“或”关系，即满足一个即可。列表长度范围为[1, 32]，标签值类型为字符串，字符长度范围为[1, 64]。
        :type custom_tags: dict(str, list[str])
        :param custom_num_tags: 自定义数值标签，用于对服务实例中的数据进行条件查找。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。针对没有设置该数值标签的数据，会直接过滤。 - value: 标签值的取值范围，标签值在给定的取值范围内即视为符合条件。
        :type custom_num_tags: dict(str, RangeParam)
        """
        
        

        self._item_id = None
        self._limit = None
        self._last_item = None
        self._custom_tags = None
        self._custom_num_tags = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if limit is not None:
            self.limit = limit
        if last_item is not None:
            self.last_item = last_item
        if custom_tags is not None:
            self.custom_tags = custom_tags
        if custom_num_tags is not None:
            self.custom_num_tags = custom_num_tags

    @property
    def item_id(self):
        """Gets the item_id of this CheckParam.

        数据的服务实例级唯一标识，字符长度范围为[1, 256]。 - item_id/custom_tags/custom_num_tags中必须给定至少一个参数，以支持对服务实例中的数据进行指定ID检查或条件检查。 - 如给定item_id参数，则进行指定ID检查，否则进行条件检查。

        :return: The item_id of this CheckParam.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this CheckParam.

        数据的服务实例级唯一标识，字符长度范围为[1, 256]。 - item_id/custom_tags/custom_num_tags中必须给定至少一个参数，以支持对服务实例中的数据进行指定ID检查或条件检查。 - 如给定item_id参数，则进行指定ID检查，否则进行条件检查。

        :param item_id: The item_id of this CheckParam.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def limit(self):
        """Gets the limit of this CheckParam.

        返回检查结果的数量，默认为10，取值范围为[1, 100]。仅对条件检查生效。

        :return: The limit of this CheckParam.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CheckParam.

        返回检查结果的数量，默认为10，取值范围为[1, 100]。仅对条件检查生效。

        :param limit: The limit of this CheckParam.
        :type limit: int
        """
        self._limit = limit

    @property
    def last_item(self):
        """Gets the last_item of this CheckParam.

        :return: The last_item of this CheckParam.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.SearchAfterParam`
        """
        return self._last_item

    @last_item.setter
    def last_item(self, last_item):
        """Sets the last_item of this CheckParam.

        :param last_item: The last_item of this CheckParam.
        :type last_item: :class:`huaweicloudsdkimagesearch.v2.SearchAfterParam`
        """
        self._last_item = last_item

    @property
    def custom_tags(self):
        """Gets the custom_tags of this CheckParam.

        自定义字符标签，用于对服务实例中的数据进行条件查找。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 标签值列表，列表内多个标签值为“或”关系，即满足一个即可。列表长度范围为[1, 32]，标签值类型为字符串，字符长度范围为[1, 64]。

        :return: The custom_tags of this CheckParam.
        :rtype: dict(str, list[str])
        """
        return self._custom_tags

    @custom_tags.setter
    def custom_tags(self, custom_tags):
        """Sets the custom_tags of this CheckParam.

        自定义字符标签，用于对服务实例中的数据进行条件查找。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 标签值列表，列表内多个标签值为“或”关系，即满足一个即可。列表长度范围为[1, 32]，标签值类型为字符串，字符长度范围为[1, 64]。

        :param custom_tags: The custom_tags of this CheckParam.
        :type custom_tags: dict(str, list[str])
        """
        self._custom_tags = custom_tags

    @property
    def custom_num_tags(self):
        """Gets the custom_num_tags of this CheckParam.

        自定义数值标签，用于对服务实例中的数据进行条件查找。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。针对没有设置该数值标签的数据，会直接过滤。 - value: 标签值的取值范围，标签值在给定的取值范围内即视为符合条件。

        :return: The custom_num_tags of this CheckParam.
        :rtype: dict(str, RangeParam)
        """
        return self._custom_num_tags

    @custom_num_tags.setter
    def custom_num_tags(self, custom_num_tags):
        """Sets the custom_num_tags of this CheckParam.

        自定义数值标签，用于对服务实例中的数据进行条件查找。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。针对没有设置该数值标签的数据，会直接过滤。 - value: 标签值的取值范围，标签值在给定的取值范围内即视为符合条件。

        :param custom_num_tags: The custom_num_tags of this CheckParam.
        :type custom_num_tags: dict(str, RangeParam)
        """
        self._custom_num_tags = custom_num_tags

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
        if not isinstance(other, CheckParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
