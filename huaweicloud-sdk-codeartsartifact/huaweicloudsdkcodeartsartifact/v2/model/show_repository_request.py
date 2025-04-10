# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'project_id': 'str',
        'repo_id': 'str',
        'region': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'repo_id': 'repo_id',
        'region': 'region'
    }

    def __init__(self, tenant_id=None, project_id=None, repo_id=None, region=None):
        r"""ShowRepositoryRequest

        The model defined in huaweicloud sdk

        :param tenant_id: 租户id
        :type tenant_id: str
        :param project_id: 项目id
        :type project_id: str
        :param repo_id: 仓库id
        :type repo_id: str
        :param region: 服务区
        :type region: str
        """
        
        

        self._tenant_id = None
        self._project_id = None
        self._repo_id = None
        self._region = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.project_id = project_id
        self.repo_id = repo_id
        if region is not None:
            self.region = region

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowRepositoryRequest.

        租户id

        :return: The tenant_id of this ShowRepositoryRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowRepositoryRequest.

        租户id

        :param tenant_id: The tenant_id of this ShowRepositoryRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowRepositoryRequest.

        项目id

        :return: The project_id of this ShowRepositoryRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowRepositoryRequest.

        项目id

        :param project_id: The project_id of this ShowRepositoryRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def repo_id(self):
        r"""Gets the repo_id of this ShowRepositoryRequest.

        仓库id

        :return: The repo_id of this ShowRepositoryRequest.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this ShowRepositoryRequest.

        仓库id

        :param repo_id: The repo_id of this ShowRepositoryRequest.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def region(self):
        r"""Gets the region of this ShowRepositoryRequest.

        服务区

        :return: The region of this ShowRepositoryRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowRepositoryRequest.

        服务区

        :param region: The region of this ShowRepositoryRequest.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, ShowRepositoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
