# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertificateBundingHostBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'hostname': 'str',
        'waf_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hostname': 'hostname',
        'waf_type': 'waf_type'
    }

    def __init__(self, id=None, hostname=None, waf_type=None):
        """CertificateBundingHostBody

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param hostname: 域名
        :type hostname: str
        :param waf_type: waf模式（分为云模式：cloud,独享模式：premium）
        :type waf_type: str
        """
        
        

        self._id = None
        self._hostname = None
        self._waf_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostname is not None:
            self.hostname = hostname
        if waf_type is not None:
            self.waf_type = waf_type

    @property
    def id(self):
        """Gets the id of this CertificateBundingHostBody.

        域名id

        :return: The id of this CertificateBundingHostBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CertificateBundingHostBody.

        域名id

        :param id: The id of this CertificateBundingHostBody.
        :type id: str
        """
        self._id = id

    @property
    def hostname(self):
        """Gets the hostname of this CertificateBundingHostBody.

        域名

        :return: The hostname of this CertificateBundingHostBody.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CertificateBundingHostBody.

        域名

        :param hostname: The hostname of this CertificateBundingHostBody.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def waf_type(self):
        """Gets the waf_type of this CertificateBundingHostBody.

        waf模式（分为云模式：cloud,独享模式：premium）

        :return: The waf_type of this CertificateBundingHostBody.
        :rtype: str
        """
        return self._waf_type

    @waf_type.setter
    def waf_type(self, waf_type):
        """Sets the waf_type of this CertificateBundingHostBody.

        waf模式（分为云模式：cloud,独享模式：premium）

        :param waf_type: The waf_type of this CertificateBundingHostBody.
        :type waf_type: str
        """
        self._waf_type = waf_type

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
        if not isinstance(other, CertificateBundingHostBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
