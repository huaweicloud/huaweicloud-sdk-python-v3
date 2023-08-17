# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateParam:

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
        'desc': 'str',
        'custom_tags': 'dict(str, str)',
        'custom_num_tags': 'dict(str, float)'
    }

    attribute_map = {
        'item_id': 'item_id',
        'desc': 'desc',
        'custom_tags': 'custom_tags',
        'custom_num_tags': 'custom_num_tags'
    }

    def __init__(self, item_id=None, desc=None, custom_tags=None, custom_num_tags=None):
        """UpdateParam

        The model defined in huaweicloud sdk

        :param item_id: 数据的服务实例级唯一标识，字符长度范围为[1, 256]。
        :type item_id: str
        :param desc: 数据的描述信息，字符长度范围为[1, 2048]。
        :type desc: str
        :param custom_tags: 数据的自定义字符标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为字符串，字符长度范围为[1, 64]。
        :type custom_tags: dict(str, str)
        :param custom_num_tags: 数据的自定义数值标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为数值，格式为double。
        :type custom_num_tags: dict(str, float)
        """
        
        

        self._item_id = None
        self._desc = None
        self._custom_tags = None
        self._custom_num_tags = None
        self.discriminator = None

        self.item_id = item_id
        if desc is not None:
            self.desc = desc
        if custom_tags is not None:
            self.custom_tags = custom_tags
        if custom_num_tags is not None:
            self.custom_num_tags = custom_num_tags

    @property
    def item_id(self):
        """Gets the item_id of this UpdateParam.

        数据的服务实例级唯一标识，字符长度范围为[1, 256]。

        :return: The item_id of this UpdateParam.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this UpdateParam.

        数据的服务实例级唯一标识，字符长度范围为[1, 256]。

        :param item_id: The item_id of this UpdateParam.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def desc(self):
        """Gets the desc of this UpdateParam.

        数据的描述信息，字符长度范围为[1, 2048]。

        :return: The desc of this UpdateParam.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this UpdateParam.

        数据的描述信息，字符长度范围为[1, 2048]。

        :param desc: The desc of this UpdateParam.
        :type desc: str
        """
        self._desc = desc

    @property
    def custom_tags(self):
        """Gets the custom_tags of this UpdateParam.

        数据的自定义字符标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为字符串，字符长度范围为[1, 64]。

        :return: The custom_tags of this UpdateParam.
        :rtype: dict(str, str)
        """
        return self._custom_tags

    @custom_tags.setter
    def custom_tags(self, custom_tags):
        """Sets the custom_tags of this UpdateParam.

        数据的自定义字符标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为字符串，字符长度范围为[1, 64]。

        :param custom_tags: The custom_tags of this UpdateParam.
        :type custom_tags: dict(str, str)
        """
        self._custom_tags = custom_tags

    @property
    def custom_num_tags(self):
        """Gets the custom_num_tags of this UpdateParam.

        数据的自定义数值标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为数值，格式为double。

        :return: The custom_num_tags of this UpdateParam.
        :rtype: dict(str, float)
        """
        return self._custom_num_tags

    @custom_num_tags.setter
    def custom_num_tags(self, custom_num_tags):
        """Sets the custom_num_tags of this UpdateParam.

        数据的自定义数值标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为数值，格式为double。

        :param custom_num_tags: The custom_num_tags of this UpdateParam.
        :type custom_num_tags: dict(str, float)
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
        if not isinstance(other, UpdateParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
