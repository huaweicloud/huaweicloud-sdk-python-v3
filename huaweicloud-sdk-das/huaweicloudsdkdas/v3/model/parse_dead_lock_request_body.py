# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParseDeadLockRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dead_lock_id': 'str'
    }

    attribute_map = {
        'dead_lock_id': 'dead_lock_id'
    }

    def __init__(self, dead_lock_id=None):
        r"""ParseDeadLockRequestBody

        The model defined in huaweicloud sdk

        :param dead_lock_id: 死锁唯一标识
        :type dead_lock_id: str
        """
        
        

        self._dead_lock_id = None
        self.discriminator = None

        self.dead_lock_id = dead_lock_id

    @property
    def dead_lock_id(self):
        r"""Gets the dead_lock_id of this ParseDeadLockRequestBody.

        死锁唯一标识

        :return: The dead_lock_id of this ParseDeadLockRequestBody.
        :rtype: str
        """
        return self._dead_lock_id

    @dead_lock_id.setter
    def dead_lock_id(self, dead_lock_id):
        r"""Sets the dead_lock_id of this ParseDeadLockRequestBody.

        死锁唯一标识

        :param dead_lock_id: The dead_lock_id of this ParseDeadLockRequestBody.
        :type dead_lock_id: str
        """
        self._dead_lock_id = dead_lock_id

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
        if not isinstance(other, ParseDeadLockRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
