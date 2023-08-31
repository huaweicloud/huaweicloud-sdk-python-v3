# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchHaTypeBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active_equipment_id': 'str',
        'standby_equipment_id': 'str'
    }

    attribute_map = {
        'active_equipment_id': 'active_equipment_id',
        'standby_equipment_id': 'standby_equipment_id'
    }

    def __init__(self, active_equipment_id=None, standby_equipment_id=None):
        """SwitchHaTypeBody

        The model defined in huaweicloud sdk

        :param active_equipment_id: 主设备ID
        :type active_equipment_id: str
        :param standby_equipment_id: 备设备ID
        :type standby_equipment_id: str
        """
        
        

        self._active_equipment_id = None
        self._standby_equipment_id = None
        self.discriminator = None

        self.active_equipment_id = active_equipment_id
        self.standby_equipment_id = standby_equipment_id

    @property
    def active_equipment_id(self):
        """Gets the active_equipment_id of this SwitchHaTypeBody.

        主设备ID

        :return: The active_equipment_id of this SwitchHaTypeBody.
        :rtype: str
        """
        return self._active_equipment_id

    @active_equipment_id.setter
    def active_equipment_id(self, active_equipment_id):
        """Sets the active_equipment_id of this SwitchHaTypeBody.

        主设备ID

        :param active_equipment_id: The active_equipment_id of this SwitchHaTypeBody.
        :type active_equipment_id: str
        """
        self._active_equipment_id = active_equipment_id

    @property
    def standby_equipment_id(self):
        """Gets the standby_equipment_id of this SwitchHaTypeBody.

        备设备ID

        :return: The standby_equipment_id of this SwitchHaTypeBody.
        :rtype: str
        """
        return self._standby_equipment_id

    @standby_equipment_id.setter
    def standby_equipment_id(self, standby_equipment_id):
        """Sets the standby_equipment_id of this SwitchHaTypeBody.

        备设备ID

        :param standby_equipment_id: The standby_equipment_id of this SwitchHaTypeBody.
        :type standby_equipment_id: str
        """
        self._standby_equipment_id = standby_equipment_id

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
        if not isinstance(other, SwitchHaTypeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
