# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPtrRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ptr_id': 'str'
    }

    attribute_map = {
        'ptr_id': 'ptr_id'
    }

    def __init__(self, ptr_id=None):
        r"""ShowPtrRequest

        The model defined in huaweicloud sdk

        :param ptr_id: 反向解析ID。
        :type ptr_id: str
        """
        
        

        self._ptr_id = None
        self.discriminator = None

        self.ptr_id = ptr_id

    @property
    def ptr_id(self):
        r"""Gets the ptr_id of this ShowPtrRequest.

        反向解析ID。

        :return: The ptr_id of this ShowPtrRequest.
        :rtype: str
        """
        return self._ptr_id

    @ptr_id.setter
    def ptr_id(self, ptr_id):
        r"""Sets the ptr_id of this ShowPtrRequest.

        反向解析ID。

        :param ptr_id: The ptr_id of this ShowPtrRequest.
        :type ptr_id: str
        """
        self._ptr_id = ptr_id

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
        if not isinstance(other, ShowPtrRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
