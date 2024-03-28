# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GcbShowLocalArea:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_area': 'str'
    }

    attribute_map = {
        'local_area': 'local_area'
    }

    def __init__(self, local_area=None):
        """GcbShowLocalArea

        The model defined in huaweicloud sdk

        :param local_area: 功能说明：本端接入点的中英文名。通过HEADER里面的x-language控制，默认英文，zh-cn返回中文。
        :type local_area: str
        """
        
        

        self._local_area = None
        self.discriminator = None

        if local_area is not None:
            self.local_area = local_area

    @property
    def local_area(self):
        """Gets the local_area of this GcbShowLocalArea.

        功能说明：本端接入点的中英文名。通过HEADER里面的x-language控制，默认英文，zh-cn返回中文。

        :return: The local_area of this GcbShowLocalArea.
        :rtype: str
        """
        return self._local_area

    @local_area.setter
    def local_area(self, local_area):
        """Sets the local_area of this GcbShowLocalArea.

        功能说明：本端接入点的中英文名。通过HEADER里面的x-language控制，默认英文，zh-cn返回中文。

        :param local_area: The local_area of this GcbShowLocalArea.
        :type local_area: str
        """
        self._local_area = local_area

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
        if not isinstance(other, GcbShowLocalArea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
