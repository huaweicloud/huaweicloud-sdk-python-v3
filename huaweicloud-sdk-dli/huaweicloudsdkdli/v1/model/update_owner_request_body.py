# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOwnerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_owner': 'str'
    }

    attribute_map = {
        'new_owner': 'new_owner'
    }

    def __init__(self, new_owner=None):
        r"""UpdateOwnerRequestBody

        The model defined in huaweicloud sdk

        :param new_owner: 新owner名称。
        :type new_owner: str
        """
        
        

        self._new_owner = None
        self.discriminator = None

        self.new_owner = new_owner

    @property
    def new_owner(self):
        r"""Gets the new_owner of this UpdateOwnerRequestBody.

        新owner名称。

        :return: The new_owner of this UpdateOwnerRequestBody.
        :rtype: str
        """
        return self._new_owner

    @new_owner.setter
    def new_owner(self, new_owner):
        r"""Sets the new_owner of this UpdateOwnerRequestBody.

        新owner名称。

        :param new_owner: The new_owner of this UpdateOwnerRequestBody.
        :type new_owner: str
        """
        self._new_owner = new_owner

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
        if not isinstance(other, UpdateOwnerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
