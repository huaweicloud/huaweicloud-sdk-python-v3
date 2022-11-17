# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeShareNameReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'change_name': 'ShareName'
    }

    attribute_map = {
        'change_name': 'change_name'
    }

    def __init__(self, change_name=None):
        """ChangeShareNameReq

        The model defined in huaweicloud sdk

        :param change_name: 
        :type change_name: :class:`huaweicloudsdksfsturbo.v1.ShareName`
        """
        
        

        self._change_name = None
        self.discriminator = None

        self.change_name = change_name

    @property
    def change_name(self):
        """Gets the change_name of this ChangeShareNameReq.

        :return: The change_name of this ChangeShareNameReq.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareName`
        """
        return self._change_name

    @change_name.setter
    def change_name(self, change_name):
        """Sets the change_name of this ChangeShareNameReq.

        :param change_name: The change_name of this ChangeShareNameReq.
        :type change_name: :class:`huaweicloudsdksfsturbo.v1.ShareName`
        """
        self._change_name = change_name

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
        if not isinstance(other, ChangeShareNameReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
