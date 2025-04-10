# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFileTreeRequest:

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
        'repo_name': 'str',
        'path': 'str',
        'instance_id': 'str',
        'is_recycle_bin': 'bool'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'repo_name': 'repo_name',
        'path': 'path',
        'instance_id': 'instance_id',
        'is_recycle_bin': 'is_recycle_bin'
    }

    def __init__(self, tenant_id=None, project_id=None, repo_name=None, path=None, instance_id=None, is_recycle_bin=None):
        r"""ShowFileTreeRequest

        The model defined in huaweicloud sdk

        :param tenant_id: 租户id
        :type tenant_id: str
        :param project_id: 项目id
        :type project_id: str
        :param repo_name: 仓库名称
        :type repo_name: str
        :param path: 仓库中路径
        :type path: str
        :param instance_id: 实例id
        :type instance_id: str
        :param is_recycle_bin: 是否是回收站文件
        :type is_recycle_bin: bool
        """
        
        

        self._tenant_id = None
        self._project_id = None
        self._repo_name = None
        self._path = None
        self._instance_id = None
        self._is_recycle_bin = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.project_id = project_id
        self.repo_name = repo_name
        self.path = path
        if instance_id is not None:
            self.instance_id = instance_id
        if is_recycle_bin is not None:
            self.is_recycle_bin = is_recycle_bin

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowFileTreeRequest.

        租户id

        :return: The tenant_id of this ShowFileTreeRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowFileTreeRequest.

        租户id

        :param tenant_id: The tenant_id of this ShowFileTreeRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowFileTreeRequest.

        项目id

        :return: The project_id of this ShowFileTreeRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowFileTreeRequest.

        项目id

        :param project_id: The project_id of this ShowFileTreeRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def repo_name(self):
        r"""Gets the repo_name of this ShowFileTreeRequest.

        仓库名称

        :return: The repo_name of this ShowFileTreeRequest.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this ShowFileTreeRequest.

        仓库名称

        :param repo_name: The repo_name of this ShowFileTreeRequest.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def path(self):
        r"""Gets the path of this ShowFileTreeRequest.

        仓库中路径

        :return: The path of this ShowFileTreeRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowFileTreeRequest.

        仓库中路径

        :param path: The path of this ShowFileTreeRequest.
        :type path: str
        """
        self._path = path

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowFileTreeRequest.

        实例id

        :return: The instance_id of this ShowFileTreeRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowFileTreeRequest.

        实例id

        :param instance_id: The instance_id of this ShowFileTreeRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def is_recycle_bin(self):
        r"""Gets the is_recycle_bin of this ShowFileTreeRequest.

        是否是回收站文件

        :return: The is_recycle_bin of this ShowFileTreeRequest.
        :rtype: bool
        """
        return self._is_recycle_bin

    @is_recycle_bin.setter
    def is_recycle_bin(self, is_recycle_bin):
        r"""Sets the is_recycle_bin of this ShowFileTreeRequest.

        是否是回收站文件

        :param is_recycle_bin: The is_recycle_bin of this ShowFileTreeRequest.
        :type is_recycle_bin: bool
        """
        self._is_recycle_bin = is_recycle_bin

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
        if not isinstance(other, ShowFileTreeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
