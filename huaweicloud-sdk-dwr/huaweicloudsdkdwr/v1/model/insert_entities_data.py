# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsertEntitiesData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'insert_count': 'int',
        'insert_ids': 'list[object]'
    }

    attribute_map = {
        'insert_count': 'insert_count',
        'insert_ids': 'insert_ids'
    }

    def __init__(self, insert_count=None, insert_ids=None):
        r"""InsertEntitiesData

        The model defined in huaweicloud sdk

        :param insert_count: **参数解释：** 插入的entity数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type insert_count: int
        :param insert_ids: **参数解释：** 插入成功的entity的primary_key。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type insert_ids: list[object]
        """
        
        

        self._insert_count = None
        self._insert_ids = None
        self.discriminator = None

        self.insert_count = insert_count
        if insert_ids is not None:
            self.insert_ids = insert_ids

    @property
    def insert_count(self):
        r"""Gets the insert_count of this InsertEntitiesData.

        **参数解释：** 插入的entity数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The insert_count of this InsertEntitiesData.
        :rtype: int
        """
        return self._insert_count

    @insert_count.setter
    def insert_count(self, insert_count):
        r"""Sets the insert_count of this InsertEntitiesData.

        **参数解释：** 插入的entity数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param insert_count: The insert_count of this InsertEntitiesData.
        :type insert_count: int
        """
        self._insert_count = insert_count

    @property
    def insert_ids(self):
        r"""Gets the insert_ids of this InsertEntitiesData.

        **参数解释：** 插入成功的entity的primary_key。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The insert_ids of this InsertEntitiesData.
        :rtype: list[object]
        """
        return self._insert_ids

    @insert_ids.setter
    def insert_ids(self, insert_ids):
        r"""Sets the insert_ids of this InsertEntitiesData.

        **参数解释：** 插入成功的entity的primary_key。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param insert_ids: The insert_ids of this InsertEntitiesData.
        :type insert_ids: list[object]
        """
        self._insert_ids = insert_ids

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
        if not isinstance(other, InsertEntitiesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
