# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Tracker:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, name=None, id=None):
        r"""Tracker

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 类型名称。 **取值范围：** - Task。 - Bug。 - Epic。 - Feature。 - Story。
        :type name: str
        :param id: **参数解释：** 类型id。 **取值范围：** 2（任务/Task） 3（缺陷/Bug） 5（Epic） 6（Feature） 7（Story）
        :type id: int
        """
        
        

        self._name = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def name(self):
        r"""Gets the name of this Tracker.

        **参数解释：** 类型名称。 **取值范围：** - Task。 - Bug。 - Epic。 - Feature。 - Story。

        :return: The name of this Tracker.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Tracker.

        **参数解释：** 类型名称。 **取值范围：** - Task。 - Bug。 - Epic。 - Feature。 - Story。

        :param name: The name of this Tracker.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this Tracker.

        **参数解释：** 类型id。 **取值范围：** 2（任务/Task） 3（缺陷/Bug） 5（Epic） 6（Feature） 7（Story）

        :return: The id of this Tracker.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Tracker.

        **参数解释：** 类型id。 **取值范围：** 2（任务/Task） 3（缺陷/Bug） 5（Epic） 6（Feature） 7（Story）

        :param id: The id of this Tracker.
        :type id: int
        """
        self._id = id

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
        if not isinstance(other, Tracker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
