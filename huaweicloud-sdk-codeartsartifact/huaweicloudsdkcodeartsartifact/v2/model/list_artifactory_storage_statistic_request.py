# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListArtifactoryStorageStatisticRequest:

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
        'repo': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'repo': 'repo',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'instance_id': 'instance_id'
    }

    def __init__(self, tenant_id=None, project_id=None, repo=None, start_time=None, end_time=None, instance_id=None):
        r"""ListArtifactoryStorageStatisticRequest

        The model defined in huaweicloud sdk

        :param tenant_id: 租户id
        :type tenant_id: str
        :param project_id: 项目id
        :type project_id: str
        :param repo: 仓库id
        :type repo: str
        :param start_time: 起始时间
        :type start_time: str
        :param end_time: 终止时间
        :type end_time: str
        :param instance_id: 实例id
        :type instance_id: str
        """
        
        

        self._tenant_id = None
        self._project_id = None
        self._repo = None
        self._start_time = None
        self._end_time = None
        self._instance_id = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.project_id = project_id
        if repo is not None:
            self.repo = repo
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ListArtifactoryStorageStatisticRequest.

        租户id

        :return: The tenant_id of this ListArtifactoryStorageStatisticRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ListArtifactoryStorageStatisticRequest.

        租户id

        :param tenant_id: The tenant_id of this ListArtifactoryStorageStatisticRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ListArtifactoryStorageStatisticRequest.

        项目id

        :return: The project_id of this ListArtifactoryStorageStatisticRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListArtifactoryStorageStatisticRequest.

        项目id

        :param project_id: The project_id of this ListArtifactoryStorageStatisticRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def repo(self):
        r"""Gets the repo of this ListArtifactoryStorageStatisticRequest.

        仓库id

        :return: The repo of this ListArtifactoryStorageStatisticRequest.
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        r"""Sets the repo of this ListArtifactoryStorageStatisticRequest.

        仓库id

        :param repo: The repo of this ListArtifactoryStorageStatisticRequest.
        :type repo: str
        """
        self._repo = repo

    @property
    def start_time(self):
        r"""Gets the start_time of this ListArtifactoryStorageStatisticRequest.

        起始时间

        :return: The start_time of this ListArtifactoryStorageStatisticRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListArtifactoryStorageStatisticRequest.

        起始时间

        :param start_time: The start_time of this ListArtifactoryStorageStatisticRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListArtifactoryStorageStatisticRequest.

        终止时间

        :return: The end_time of this ListArtifactoryStorageStatisticRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListArtifactoryStorageStatisticRequest.

        终止时间

        :param end_time: The end_time of this ListArtifactoryStorageStatisticRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListArtifactoryStorageStatisticRequest.

        实例id

        :return: The instance_id of this ListArtifactoryStorageStatisticRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListArtifactoryStorageStatisticRequest.

        实例id

        :param instance_id: The instance_id of this ListArtifactoryStorageStatisticRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListArtifactoryStorageStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
