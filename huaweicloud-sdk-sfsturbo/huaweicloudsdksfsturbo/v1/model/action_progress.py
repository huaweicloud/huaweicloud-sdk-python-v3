# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creating': 'str'
    }

    attribute_map = {
        'creating': 'CREATING'
    }

    def __init__(self, creating=None):
        """ActionProgress

        The model defined in huaweicloud sdk

        :param creating: 创建文件系统的进度。
        :type creating: str
        """
        
        

        self._creating = None
        self.discriminator = None

        if creating is not None:
            self.creating = creating

    @property
    def creating(self):
        """Gets the creating of this ActionProgress.

        创建文件系统的进度。

        :return: The creating of this ActionProgress.
        :rtype: str
        """
        return self._creating

    @creating.setter
    def creating(self, creating):
        """Sets the creating of this ActionProgress.

        创建文件系统的进度。

        :param creating: The creating of this ActionProgress.
        :type creating: str
        """
        self._creating = creating

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
        if not isinstance(other, ActionProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
