# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdOuInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ou_name': 'str',
        'ou_dn': 'str'
    }

    attribute_map = {
        'ou_name': 'ou_name',
        'ou_dn': 'ou_dn'
    }

    def __init__(self, ou_name=None, ou_dn=None):
        r"""AdOuInfo

        The model defined in huaweicloud sdk

        :param ou_name: 名称。
        :type ou_name: str
        :param ou_dn: 域名地址。
        :type ou_dn: str
        """
        
        

        self._ou_name = None
        self._ou_dn = None
        self.discriminator = None

        if ou_name is not None:
            self.ou_name = ou_name
        if ou_dn is not None:
            self.ou_dn = ou_dn

    @property
    def ou_name(self):
        r"""Gets the ou_name of this AdOuInfo.

        名称。

        :return: The ou_name of this AdOuInfo.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        r"""Sets the ou_name of this AdOuInfo.

        名称。

        :param ou_name: The ou_name of this AdOuInfo.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def ou_dn(self):
        r"""Gets the ou_dn of this AdOuInfo.

        域名地址。

        :return: The ou_dn of this AdOuInfo.
        :rtype: str
        """
        return self._ou_dn

    @ou_dn.setter
    def ou_dn(self, ou_dn):
        r"""Sets the ou_dn of this AdOuInfo.

        域名地址。

        :param ou_dn: The ou_dn of this AdOuInfo.
        :type ou_dn: str
        """
        self._ou_dn = ou_dn

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
        if not isinstance(other, AdOuInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
