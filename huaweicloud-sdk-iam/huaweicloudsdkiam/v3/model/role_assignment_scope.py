# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleAssignmentScope:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project': 'RoleProjectAssignmentId',
        'domain': 'RoleDomainAssignmentId',
        'enterprise_project': 'RoleEnterpriseProjectAssignmentId'
    }

    attribute_map = {
        'project': 'project',
        'domain': 'domain',
        'enterprise_project': 'enterprise_project'
    }

    def __init__(self, project=None, domain=None, enterprise_project=None):
        """RoleAssignmentScope

        The model defined in huaweicloud sdk

        :param project: 
        :type project: :class:`huaweicloudsdkiam.v3.RoleProjectAssignmentId`
        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.RoleDomainAssignmentId`
        :param enterprise_project: 
        :type enterprise_project: :class:`huaweicloudsdkiam.v3.RoleEnterpriseProjectAssignmentId`
        """
        
        

        self._project = None
        self._domain = None
        self._enterprise_project = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if domain is not None:
            self.domain = domain
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project

    @property
    def project(self):
        """Gets the project of this RoleAssignmentScope.

        :return: The project of this RoleAssignmentScope.
        :rtype: :class:`huaweicloudsdkiam.v3.RoleProjectAssignmentId`
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this RoleAssignmentScope.

        :param project: The project of this RoleAssignmentScope.
        :type project: :class:`huaweicloudsdkiam.v3.RoleProjectAssignmentId`
        """
        self._project = project

    @property
    def domain(self):
        """Gets the domain of this RoleAssignmentScope.

        :return: The domain of this RoleAssignmentScope.
        :rtype: :class:`huaweicloudsdkiam.v3.RoleDomainAssignmentId`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this RoleAssignmentScope.

        :param domain: The domain of this RoleAssignmentScope.
        :type domain: :class:`huaweicloudsdkiam.v3.RoleDomainAssignmentId`
        """
        self._domain = domain

    @property
    def enterprise_project(self):
        """Gets the enterprise_project of this RoleAssignmentScope.

        :return: The enterprise_project of this RoleAssignmentScope.
        :rtype: :class:`huaweicloudsdkiam.v3.RoleEnterpriseProjectAssignmentId`
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        """Sets the enterprise_project of this RoleAssignmentScope.

        :param enterprise_project: The enterprise_project of this RoleAssignmentScope.
        :type enterprise_project: :class:`huaweicloudsdkiam.v3.RoleEnterpriseProjectAssignmentId`
        """
        self._enterprise_project = enterprise_project

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
        if not isinstance(other, RoleAssignmentScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
