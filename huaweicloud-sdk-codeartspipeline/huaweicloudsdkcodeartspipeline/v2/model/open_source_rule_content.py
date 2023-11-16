# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenSourceRuleContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_set': 'VersionSetProperty',
        'security': 'SecurityProperty',
        'license': 'LicenseProperty'
    }

    attribute_map = {
        'version_set': 'version_set',
        'security': 'security',
        'license': 'license'
    }

    def __init__(self, version_set=None, security=None, license=None):
        """OpenSourceRuleContent

        The model defined in huaweicloud sdk

        :param version_set: 
        :type version_set: :class:`huaweicloudsdkcodeartspipeline.v2.VersionSetProperty`
        :param security: 
        :type security: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityProperty`
        :param license: 
        :type license: :class:`huaweicloudsdkcodeartspipeline.v2.LicenseProperty`
        """
        
        

        self._version_set = None
        self._security = None
        self._license = None
        self.discriminator = None

        if version_set is not None:
            self.version_set = version_set
        if security is not None:
            self.security = security
        if license is not None:
            self.license = license

    @property
    def version_set(self):
        """Gets the version_set of this OpenSourceRuleContent.

        :return: The version_set of this OpenSourceRuleContent.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.VersionSetProperty`
        """
        return self._version_set

    @version_set.setter
    def version_set(self, version_set):
        """Sets the version_set of this OpenSourceRuleContent.

        :param version_set: The version_set of this OpenSourceRuleContent.
        :type version_set: :class:`huaweicloudsdkcodeartspipeline.v2.VersionSetProperty`
        """
        self._version_set = version_set

    @property
    def security(self):
        """Gets the security of this OpenSourceRuleContent.

        :return: The security of this OpenSourceRuleContent.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityProperty`
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this OpenSourceRuleContent.

        :param security: The security of this OpenSourceRuleContent.
        :type security: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityProperty`
        """
        self._security = security

    @property
    def license(self):
        """Gets the license of this OpenSourceRuleContent.

        :return: The license of this OpenSourceRuleContent.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.LicenseProperty`
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this OpenSourceRuleContent.

        :param license: The license of this OpenSourceRuleContent.
        :type license: :class:`huaweicloudsdkcodeartspipeline.v2.LicenseProperty`
        """
        self._license = license

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
        if not isinstance(other, OpenSourceRuleContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
