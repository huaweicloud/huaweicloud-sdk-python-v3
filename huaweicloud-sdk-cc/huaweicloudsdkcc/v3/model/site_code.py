# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteCode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_code': 'str'
    }

    attribute_map = {
        'site_code': 'site_code'
    }

    def __init__(self, site_code=None):
        r"""SiteCode

        The model defined in huaweicloud sdk

        :param site_code: 站点编码。
        :type site_code: str
        """
        
        

        self._site_code = None
        self.discriminator = None

        self.site_code = site_code

    @property
    def site_code(self):
        r"""Gets the site_code of this SiteCode.

        站点编码。

        :return: The site_code of this SiteCode.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this SiteCode.

        站点编码。

        :param site_code: The site_code of this SiteCode.
        :type site_code: str
        """
        self._site_code = site_code

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
        if not isinstance(other, SiteCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
