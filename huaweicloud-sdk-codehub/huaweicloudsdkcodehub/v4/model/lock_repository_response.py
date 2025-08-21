# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LockRepositoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'locked': 'str'
    }

    attribute_map = {
        'locked': 'locked'
    }

    def __init__(self, locked=None):
        r"""LockRepositoryResponse

        The model defined in huaweicloud sdk

        :param locked: 锁定状态 - true 已锁定 - false 未锁定 
        :type locked: str
        """
        
        super(LockRepositoryResponse, self).__init__()

        self._locked = None
        self.discriminator = None

        if locked is not None:
            self.locked = locked

    @property
    def locked(self):
        r"""Gets the locked of this LockRepositoryResponse.

        锁定状态 - true 已锁定 - false 未锁定 

        :return: The locked of this LockRepositoryResponse.
        :rtype: str
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        r"""Sets the locked of this LockRepositoryResponse.

        锁定状态 - true 已锁定 - false 未锁定 

        :param locked: The locked of this LockRepositoryResponse.
        :type locked: str
        """
        self._locked = locked

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
        if not isinstance(other, LockRepositoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
