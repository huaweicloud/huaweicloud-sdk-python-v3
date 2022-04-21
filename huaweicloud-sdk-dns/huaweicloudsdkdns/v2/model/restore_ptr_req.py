# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestorePtrReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ptrdname': 'str'
    }

    attribute_map = {
        'ptrdname': 'ptrdname'
    }

    def __init__(self, ptrdname=None):
        """RestorePtrReq

        The model defined in huaweicloud sdk

        :param ptrdname: PTR记录对应的域名。  此处值为null。
        :type ptrdname: str
        """
        
        

        self._ptrdname = None
        self.discriminator = None

        self.ptrdname = ptrdname

    @property
    def ptrdname(self):
        """Gets the ptrdname of this RestorePtrReq.

        PTR记录对应的域名。  此处值为null。

        :return: The ptrdname of this RestorePtrReq.
        :rtype: str
        """
        return self._ptrdname

    @ptrdname.setter
    def ptrdname(self, ptrdname):
        """Sets the ptrdname of this RestorePtrReq.

        PTR记录对应的域名。  此处值为null。

        :param ptrdname: The ptrdname of this RestorePtrReq.
        :type ptrdname: str
        """
        self._ptrdname = ptrdname

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
        if not isinstance(other, RestorePtrReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
