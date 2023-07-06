# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulInfoCveList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cve_id': 'str',
        'cvss': 'float'
    }

    attribute_map = {
        'cve_id': 'cve_id',
        'cvss': 'cvss'
    }

    def __init__(self, cve_id=None, cvss=None):
        """VulInfoCveList

        The model defined in huaweicloud sdk

        :param cve_id: CVE ID
        :type cve_id: str
        :param cvss: CVSS分值
        :type cvss: float
        """
        
        

        self._cve_id = None
        self._cvss = None
        self.discriminator = None

        if cve_id is not None:
            self.cve_id = cve_id
        if cvss is not None:
            self.cvss = cvss

    @property
    def cve_id(self):
        """Gets the cve_id of this VulInfoCveList.

        CVE ID

        :return: The cve_id of this VulInfoCveList.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        """Sets the cve_id of this VulInfoCveList.

        CVE ID

        :param cve_id: The cve_id of this VulInfoCveList.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def cvss(self):
        """Gets the cvss of this VulInfoCveList.

        CVSS分值

        :return: The cvss of this VulInfoCveList.
        :rtype: float
        """
        return self._cvss

    @cvss.setter
    def cvss(self, cvss):
        """Sets the cvss of this VulInfoCveList.

        CVSS分值

        :param cvss: The cvss of this VulInfoCveList.
        :type cvss: float
        """
        self._cvss = cvss

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
        if not isinstance(other, VulInfoCveList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
