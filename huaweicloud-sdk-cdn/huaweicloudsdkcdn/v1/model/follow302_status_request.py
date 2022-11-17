# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Follow302StatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'follow302_status': 'str'
    }

    attribute_map = {
        'follow302_status': 'follow302_status'
    }

    def __init__(self, follow302_status=None):
        """Follow302StatusRequest

        The model defined in huaweicloud sdk

        :param follow302_status: follow302状态（\&quot;off\&quot;/\&quot;on\&quot;）
        :type follow302_status: str
        """
        
        

        self._follow302_status = None
        self.discriminator = None

        self.follow302_status = follow302_status

    @property
    def follow302_status(self):
        """Gets the follow302_status of this Follow302StatusRequest.

        follow302状态（\"off\"/\"on\"）

        :return: The follow302_status of this Follow302StatusRequest.
        :rtype: str
        """
        return self._follow302_status

    @follow302_status.setter
    def follow302_status(self, follow302_status):
        """Sets the follow302_status of this Follow302StatusRequest.

        follow302状态（\"off\"/\"on\"）

        :param follow302_status: The follow302_status of this Follow302StatusRequest.
        :type follow302_status: str
        """
        self._follow302_status = follow302_status

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
        if not isinstance(other, Follow302StatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
