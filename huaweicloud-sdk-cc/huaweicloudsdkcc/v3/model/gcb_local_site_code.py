# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GcbLocalSiteCode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_site_code': 'str'
    }

    attribute_map = {
        'local_site_code': 'local_site_code'
    }

    def __init__(self, local_site_code=None):
        r"""GcbLocalSiteCode

        The model defined in huaweicloud sdk

        :param local_site_code: 功能说明：本端接入点的编码。
        :type local_site_code: str
        """
        
        

        self._local_site_code = None
        self.discriminator = None

        if local_site_code is not None:
            self.local_site_code = local_site_code

    @property
    def local_site_code(self):
        r"""Gets the local_site_code of this GcbLocalSiteCode.

        功能说明：本端接入点的编码。

        :return: The local_site_code of this GcbLocalSiteCode.
        :rtype: str
        """
        return self._local_site_code

    @local_site_code.setter
    def local_site_code(self, local_site_code):
        r"""Sets the local_site_code of this GcbLocalSiteCode.

        功能说明：本端接入点的编码。

        :param local_site_code: The local_site_code of this GcbLocalSiteCode.
        :type local_site_code: str
        """
        self._local_site_code = local_site_code

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
        if not isinstance(other, GcbLocalSiteCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
