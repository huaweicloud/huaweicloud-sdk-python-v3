# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CapacityOrderResponseRankList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, id=None, name=None, value=None):
        r"""CapacityOrderResponseRankList

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 应用或组件或者分组id。 **取值范围：** 容量种类排名在前五个的应用或者组件或分组对应的id。
        :type id: str
        :param name: **参数解释：** 应用或组件或者分组的名称。 **取值范围：** 容量种类排名在前五个的应用或者组件或分组对应的名称。
        :type name: str
        :param value: **参数解释：** 应用或组件或者分组的容量值。 **取值范围：** 容量种类排名在前五个的应用或者组件或分组对应的容量值。
        :type value: str
        """
        
        

        self._id = None
        self._name = None
        self._value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def id(self):
        r"""Gets the id of this CapacityOrderResponseRankList.

        **参数解释：** 应用或组件或者分组id。 **取值范围：** 容量种类排名在前五个的应用或者组件或分组对应的id。

        :return: The id of this CapacityOrderResponseRankList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CapacityOrderResponseRankList.

        **参数解释：** 应用或组件或者分组id。 **取值范围：** 容量种类排名在前五个的应用或者组件或分组对应的id。

        :param id: The id of this CapacityOrderResponseRankList.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CapacityOrderResponseRankList.

        **参数解释：** 应用或组件或者分组的名称。 **取值范围：** 容量种类排名在前五个的应用或者组件或分组对应的名称。

        :return: The name of this CapacityOrderResponseRankList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CapacityOrderResponseRankList.

        **参数解释：** 应用或组件或者分组的名称。 **取值范围：** 容量种类排名在前五个的应用或者组件或分组对应的名称。

        :param name: The name of this CapacityOrderResponseRankList.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this CapacityOrderResponseRankList.

        **参数解释：** 应用或组件或者分组的容量值。 **取值范围：** 容量种类排名在前五个的应用或者组件或分组对应的容量值。

        :return: The value of this CapacityOrderResponseRankList.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CapacityOrderResponseRankList.

        **参数解释：** 应用或组件或者分组的容量值。 **取值范围：** 容量种类排名在前五个的应用或者组件或分组对应的容量值。

        :param value: The value of this CapacityOrderResponseRankList.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, CapacityOrderResponseRankList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
