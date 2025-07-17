# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndexDesc:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index_name': 'str',
        'field_name': 'str',
        'index_params': 'dict(str, object)',
        'index_state': 'str'
    }

    attribute_map = {
        'index_name': 'index_name',
        'field_name': 'field_name',
        'index_params': 'index_params',
        'index_state': 'index_state'
    }

    def __init__(self, index_name=None, field_name=None, index_params=None, index_state=None):
        r"""IndexDesc

        The model defined in huaweicloud sdk

        :param index_name: **参数解释：** 描述的索引名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type index_name: str
        :param field_name: **参数解释：** 索引对应的字段名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type field_name: str
        :param index_params: **参数解释：** 索引的参数信息。详情请查阅CreateIndex接口中 index_params结构中params字段的描述。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type index_params: dict(str, object)
        :param index_state: **参数解释：** 索引状态。 **约束限制：** 不涉及。 **取值范围：** -\&quot;InProgress\&quot;：索引正在构建中或还未开始构建。 -\&quot;Finished\&quot;：索引构建完成。 -\&quot;Failed\&quot;：索引构建失败。 **默认取值:** 不涉及。
        :type index_state: str
        """
        
        

        self._index_name = None
        self._field_name = None
        self._index_params = None
        self._index_state = None
        self.discriminator = None

        self.index_name = index_name
        self.field_name = field_name
        self.index_params = index_params
        self.index_state = index_state

    @property
    def index_name(self):
        r"""Gets the index_name of this IndexDesc.

        **参数解释：** 描述的索引名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The index_name of this IndexDesc.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        r"""Sets the index_name of this IndexDesc.

        **参数解释：** 描述的索引名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param index_name: The index_name of this IndexDesc.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def field_name(self):
        r"""Gets the field_name of this IndexDesc.

        **参数解释：** 索引对应的字段名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The field_name of this IndexDesc.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this IndexDesc.

        **参数解释：** 索引对应的字段名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param field_name: The field_name of this IndexDesc.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def index_params(self):
        r"""Gets the index_params of this IndexDesc.

        **参数解释：** 索引的参数信息。详情请查阅CreateIndex接口中 index_params结构中params字段的描述。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The index_params of this IndexDesc.
        :rtype: dict(str, object)
        """
        return self._index_params

    @index_params.setter
    def index_params(self, index_params):
        r"""Sets the index_params of this IndexDesc.

        **参数解释：** 索引的参数信息。详情请查阅CreateIndex接口中 index_params结构中params字段的描述。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param index_params: The index_params of this IndexDesc.
        :type index_params: dict(str, object)
        """
        self._index_params = index_params

    @property
    def index_state(self):
        r"""Gets the index_state of this IndexDesc.

        **参数解释：** 索引状态。 **约束限制：** 不涉及。 **取值范围：** -\"InProgress\"：索引正在构建中或还未开始构建。 -\"Finished\"：索引构建完成。 -\"Failed\"：索引构建失败。 **默认取值:** 不涉及。

        :return: The index_state of this IndexDesc.
        :rtype: str
        """
        return self._index_state

    @index_state.setter
    def index_state(self, index_state):
        r"""Sets the index_state of this IndexDesc.

        **参数解释：** 索引状态。 **约束限制：** 不涉及。 **取值范围：** -\"InProgress\"：索引正在构建中或还未开始构建。 -\"Finished\"：索引构建完成。 -\"Failed\"：索引构建失败。 **默认取值:** 不涉及。

        :param index_state: The index_state of this IndexDesc.
        :type index_state: str
        """
        self._index_state = index_state

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
        if not isinstance(other, IndexDesc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
