# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelinesPageLatestRunArtifactParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'branch_filter': 'str',
        'package_name': 'str',
        'organization': 'str'
    }

    attribute_map = {
        'version': 'version',
        'branch_filter': 'branch_filter',
        'package_name': 'package_name',
        'organization': 'organization'
    }

    def __init__(self, version=None, branch_filter=None, package_name=None, organization=None):
        """ListPipelinesPageLatestRunArtifactParams

        The model defined in huaweicloud sdk

        :param version: 包版本
        :type version: str
        :param branch_filter: 过滤分支
        :type branch_filter: str
        :param package_name: 包名称
        :type package_name: str
        :param organization: docker组织
        :type organization: str
        """
        
        

        self._version = None
        self._branch_filter = None
        self._package_name = None
        self._organization = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if branch_filter is not None:
            self.branch_filter = branch_filter
        if package_name is not None:
            self.package_name = package_name
        if organization is not None:
            self.organization = organization

    @property
    def version(self):
        """Gets the version of this ListPipelinesPageLatestRunArtifactParams.

        包版本

        :return: The version of this ListPipelinesPageLatestRunArtifactParams.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListPipelinesPageLatestRunArtifactParams.

        包版本

        :param version: The version of this ListPipelinesPageLatestRunArtifactParams.
        :type version: str
        """
        self._version = version

    @property
    def branch_filter(self):
        """Gets the branch_filter of this ListPipelinesPageLatestRunArtifactParams.

        过滤分支

        :return: The branch_filter of this ListPipelinesPageLatestRunArtifactParams.
        :rtype: str
        """
        return self._branch_filter

    @branch_filter.setter
    def branch_filter(self, branch_filter):
        """Sets the branch_filter of this ListPipelinesPageLatestRunArtifactParams.

        过滤分支

        :param branch_filter: The branch_filter of this ListPipelinesPageLatestRunArtifactParams.
        :type branch_filter: str
        """
        self._branch_filter = branch_filter

    @property
    def package_name(self):
        """Gets the package_name of this ListPipelinesPageLatestRunArtifactParams.

        包名称

        :return: The package_name of this ListPipelinesPageLatestRunArtifactParams.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this ListPipelinesPageLatestRunArtifactParams.

        包名称

        :param package_name: The package_name of this ListPipelinesPageLatestRunArtifactParams.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def organization(self):
        """Gets the organization of this ListPipelinesPageLatestRunArtifactParams.

        docker组织

        :return: The organization of this ListPipelinesPageLatestRunArtifactParams.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ListPipelinesPageLatestRunArtifactParams.

        docker组织

        :param organization: The organization of this ListPipelinesPageLatestRunArtifactParams.
        :type organization: str
        """
        self._organization = organization

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
        if not isinstance(other, ListPipelinesPageLatestRunArtifactParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
