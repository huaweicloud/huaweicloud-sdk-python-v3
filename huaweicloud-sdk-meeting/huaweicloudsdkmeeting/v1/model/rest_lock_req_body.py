# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestLockReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_lock': 'int'
    }

    attribute_map = {
        'is_lock': 'isLock'
    }

    def __init__(self, is_lock=None):
        """RestLockReqBody

        The model defined in huaweicloud sdk

        :param is_lock: - 0: 解锁 - 1: 锁定
        :type is_lock: int
        """
        
        

        self._is_lock = None
        self.discriminator = None

        self.is_lock = is_lock

    @property
    def is_lock(self):
        """Gets the is_lock of this RestLockReqBody.

        - 0: 解锁 - 1: 锁定

        :return: The is_lock of this RestLockReqBody.
        :rtype: int
        """
        return self._is_lock

    @is_lock.setter
    def is_lock(self, is_lock):
        """Sets the is_lock of this RestLockReqBody.

        - 0: 解锁 - 1: 锁定

        :param is_lock: The is_lock of this RestLockReqBody.
        :type is_lock: int
        """
        self._is_lock = is_lock

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
        if not isinstance(other, RestLockReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
