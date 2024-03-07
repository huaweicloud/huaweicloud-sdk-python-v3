# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModelVersionUndoCheckOutDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_id': 'str',
        'modifier': 'str'
    }

    attribute_map = {
        'master_id': 'masterId',
        'modifier': 'modifier'
    }

    def __init__(self, master_id=None, modifier=None):
        """VersionModelVersionUndoCheckOutDTO

        The model defined in huaweicloud sdk

        :param master_id: 主对象ID。
        :type master_id: str
        :param modifier: 更新者。
        :type modifier: str
        """
        
        

        self._master_id = None
        self._modifier = None
        self.discriminator = None

        self.master_id = master_id
        if modifier is not None:
            self.modifier = modifier

    @property
    def master_id(self):
        """Gets the master_id of this VersionModelVersionUndoCheckOutDTO.

        主对象ID。

        :return: The master_id of this VersionModelVersionUndoCheckOutDTO.
        :rtype: str
        """
        return self._master_id

    @master_id.setter
    def master_id(self, master_id):
        """Sets the master_id of this VersionModelVersionUndoCheckOutDTO.

        主对象ID。

        :param master_id: The master_id of this VersionModelVersionUndoCheckOutDTO.
        :type master_id: str
        """
        self._master_id = master_id

    @property
    def modifier(self):
        """Gets the modifier of this VersionModelVersionUndoCheckOutDTO.

        更新者。

        :return: The modifier of this VersionModelVersionUndoCheckOutDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this VersionModelVersionUndoCheckOutDTO.

        更新者。

        :param modifier: The modifier of this VersionModelVersionUndoCheckOutDTO.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, VersionModelVersionUndoCheckOutDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
