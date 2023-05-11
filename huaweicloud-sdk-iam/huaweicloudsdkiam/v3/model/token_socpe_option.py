# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TokenSocpeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'ScopeDomainOption',
        'project': 'ScopeProjectOption'
    }

    attribute_map = {
        'domain': 'domain',
        'project': 'project'
    }

    def __init__(self, domain=None, project=None):
        """TokenSocpeOption

        The model defined in huaweicloud sdk

        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.ScopeDomainOption`
        :param project: 
        :type project: :class:`huaweicloudsdkiam.v3.ScopeProjectOption`
        """
        
        

        self._domain = None
        self._project = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if project is not None:
            self.project = project

    @property
    def domain(self):
        """Gets the domain of this TokenSocpeOption.

        :return: The domain of this TokenSocpeOption.
        :rtype: :class:`huaweicloudsdkiam.v3.ScopeDomainOption`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this TokenSocpeOption.

        :param domain: The domain of this TokenSocpeOption.
        :type domain: :class:`huaweicloudsdkiam.v3.ScopeDomainOption`
        """
        self._domain = domain

    @property
    def project(self):
        """Gets the project of this TokenSocpeOption.

        :return: The project of this TokenSocpeOption.
        :rtype: :class:`huaweicloudsdkiam.v3.ScopeProjectOption`
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this TokenSocpeOption.

        :param project: The project of this TokenSocpeOption.
        :type project: :class:`huaweicloudsdkiam.v3.ScopeProjectOption`
        """
        self._project = project

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
        if not isinstance(other, TokenSocpeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
