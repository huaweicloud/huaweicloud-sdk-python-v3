# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CurrentSlot:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slot_id': 'str',
        'slot_name': 'str',
        'slot_values': 'list[SlotValue]',
        'slot_identification': 'str'
    }

    attribute_map = {
        'slot_id': 'slot_id',
        'slot_name': 'slot_name',
        'slot_values': 'slot_values',
        'slot_identification': 'slot_identification'
    }

    def __init__(self, slot_id=None, slot_name=None, slot_values=None, slot_identification=None):
        """CurrentSlot

        The model defined in huaweicloud sdk

        :param slot_id: 槽位ID。
        :type slot_id: str
        :param slot_name: 槽位名称。
        :type slot_name: str
        :param slot_values: 槽位值。
        :type slot_values: list[:class:`huaweicloudsdkcbs.v1.SlotValue`]
        :param slot_identification: 槽位标识。
        :type slot_identification: str
        """
        
        

        self._slot_id = None
        self._slot_name = None
        self._slot_values = None
        self._slot_identification = None
        self.discriminator = None

        self.slot_id = slot_id
        self.slot_name = slot_name
        self.slot_values = slot_values
        if slot_identification is not None:
            self.slot_identification = slot_identification

    @property
    def slot_id(self):
        """Gets the slot_id of this CurrentSlot.

        槽位ID。

        :return: The slot_id of this CurrentSlot.
        :rtype: str
        """
        return self._slot_id

    @slot_id.setter
    def slot_id(self, slot_id):
        """Sets the slot_id of this CurrentSlot.

        槽位ID。

        :param slot_id: The slot_id of this CurrentSlot.
        :type slot_id: str
        """
        self._slot_id = slot_id

    @property
    def slot_name(self):
        """Gets the slot_name of this CurrentSlot.

        槽位名称。

        :return: The slot_name of this CurrentSlot.
        :rtype: str
        """
        return self._slot_name

    @slot_name.setter
    def slot_name(self, slot_name):
        """Sets the slot_name of this CurrentSlot.

        槽位名称。

        :param slot_name: The slot_name of this CurrentSlot.
        :type slot_name: str
        """
        self._slot_name = slot_name

    @property
    def slot_values(self):
        """Gets the slot_values of this CurrentSlot.

        槽位值。

        :return: The slot_values of this CurrentSlot.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.SlotValue`]
        """
        return self._slot_values

    @slot_values.setter
    def slot_values(self, slot_values):
        """Sets the slot_values of this CurrentSlot.

        槽位值。

        :param slot_values: The slot_values of this CurrentSlot.
        :type slot_values: list[:class:`huaweicloudsdkcbs.v1.SlotValue`]
        """
        self._slot_values = slot_values

    @property
    def slot_identification(self):
        """Gets the slot_identification of this CurrentSlot.

        槽位标识。

        :return: The slot_identification of this CurrentSlot.
        :rtype: str
        """
        return self._slot_identification

    @slot_identification.setter
    def slot_identification(self, slot_identification):
        """Sets the slot_identification of this CurrentSlot.

        槽位标识。

        :param slot_identification: The slot_identification of this CurrentSlot.
        :type slot_identification: str
        """
        self._slot_identification = slot_identification

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
        if not isinstance(other, CurrentSlot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
