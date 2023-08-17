# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'force': 'bool',
        'item_id': 'str',
        'custom_tags': 'dict(str, list[str])',
        'custom_num_tags': 'dict(str, RangeParam)'
    }

    attribute_map = {
        'force': 'force',
        'item_id': 'item_id',
        'custom_tags': 'custom_tags',
        'custom_num_tags': 'custom_num_tags'
    }

    def __init__(self, force=None, item_id=None, custom_tags=None, custom_num_tags=None):
        """DeleteParam

        The model defined in huaweicloud sdk

        :param force: 是否幂等删除数据，默认为false。仅对指定ID删除生效。 - false: 数据不存在时返回错误信息。 - true: 数据不存在时返回成功，用于幂等删除场景。
        :type force: bool
        :param item_id: 数据的服务实例级唯一标识，字符长度范围为[1, 256]。 - item_id/custom_tags/custom_num_tags中必须给定至少一个参数，以支持对服务实例中的数据进行指定ID删除或条件删除。 - 如给定item_id参数，则进行指定ID删除，否则进行条件删除。
        :type item_id: str
        :param custom_tags: 自定义字符标签，用于对服务实例中的数据进行条件删除。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 标签值列表，列表内多个标签值为“或”关系，即满足一个即可。列表长度范围为[1, 32]，标签值类型为字符串，字符长度范围为[1, 64]。
        :type custom_tags: dict(str, list[str])
        :param custom_num_tags: 自定义数值标签，用于对服务实例中的数据进行custom_num_tags条件删除。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。针对没有设置该数值标签的数据，会直接过滤。 - value: 标签值的取值范围，标签值在给定的取值范围内即视为符合条件。
        :type custom_num_tags: dict(str, RangeParam)
        """
        
        

        self._force = None
        self._item_id = None
        self._custom_tags = None
        self._custom_num_tags = None
        self.discriminator = None

        if force is not None:
            self.force = force
        if item_id is not None:
            self.item_id = item_id
        if custom_tags is not None:
            self.custom_tags = custom_tags
        if custom_num_tags is not None:
            self.custom_num_tags = custom_num_tags

    @property
    def force(self):
        """Gets the force of this DeleteParam.

        是否幂等删除数据，默认为false。仅对指定ID删除生效。 - false: 数据不存在时返回错误信息。 - true: 数据不存在时返回成功，用于幂等删除场景。

        :return: The force of this DeleteParam.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this DeleteParam.

        是否幂等删除数据，默认为false。仅对指定ID删除生效。 - false: 数据不存在时返回错误信息。 - true: 数据不存在时返回成功，用于幂等删除场景。

        :param force: The force of this DeleteParam.
        :type force: bool
        """
        self._force = force

    @property
    def item_id(self):
        """Gets the item_id of this DeleteParam.

        数据的服务实例级唯一标识，字符长度范围为[1, 256]。 - item_id/custom_tags/custom_num_tags中必须给定至少一个参数，以支持对服务实例中的数据进行指定ID删除或条件删除。 - 如给定item_id参数，则进行指定ID删除，否则进行条件删除。

        :return: The item_id of this DeleteParam.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this DeleteParam.

        数据的服务实例级唯一标识，字符长度范围为[1, 256]。 - item_id/custom_tags/custom_num_tags中必须给定至少一个参数，以支持对服务实例中的数据进行指定ID删除或条件删除。 - 如给定item_id参数，则进行指定ID删除，否则进行条件删除。

        :param item_id: The item_id of this DeleteParam.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def custom_tags(self):
        """Gets the custom_tags of this DeleteParam.

        自定义字符标签，用于对服务实例中的数据进行条件删除。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 标签值列表，列表内多个标签值为“或”关系，即满足一个即可。列表长度范围为[1, 32]，标签值类型为字符串，字符长度范围为[1, 64]。

        :return: The custom_tags of this DeleteParam.
        :rtype: dict(str, list[str])
        """
        return self._custom_tags

    @custom_tags.setter
    def custom_tags(self, custom_tags):
        """Sets the custom_tags of this DeleteParam.

        自定义字符标签，用于对服务实例中的数据进行条件删除。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 标签值列表，列表内多个标签值为“或”关系，即满足一个即可。列表长度范围为[1, 32]，标签值类型为字符串，字符长度范围为[1, 64]。

        :param custom_tags: The custom_tags of this DeleteParam.
        :type custom_tags: dict(str, list[str])
        """
        self._custom_tags = custom_tags

    @property
    def custom_num_tags(self):
        """Gets the custom_num_tags of this DeleteParam.

        自定义数值标签，用于对服务实例中的数据进行custom_num_tags条件删除。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。针对没有设置该数值标签的数据，会直接过滤。 - value: 标签值的取值范围，标签值在给定的取值范围内即视为符合条件。

        :return: The custom_num_tags of this DeleteParam.
        :rtype: dict(str, RangeParam)
        """
        return self._custom_num_tags

    @custom_num_tags.setter
    def custom_num_tags(self, custom_num_tags):
        """Sets the custom_num_tags of this DeleteParam.

        自定义数值标签，用于对服务实例中的数据进行custom_num_tags条件删除。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。针对没有设置该数值标签的数据，会直接过滤。 - value: 标签值的取值范围，标签值在给定的取值范围内即视为符合条件。

        :param custom_num_tags: The custom_num_tags of this DeleteParam.
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
        if not isinstance(other, DeleteParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
