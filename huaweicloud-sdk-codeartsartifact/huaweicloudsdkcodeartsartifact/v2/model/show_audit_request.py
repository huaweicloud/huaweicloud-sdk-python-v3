# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditRequest:

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
        'module': 'str',
        'repo': 'str',
        'user_id': 'str',
        'instance_id': 'str',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'module': 'module',
        'repo': 'repo',
        'user_id': 'user_id',
        'instance_id': 'instance_id',
        'page_num': 'page_num',
        'page_size': 'page_size'
    }

    def __init__(self, tenant_id=None, project_id=None, module=None, repo=None, user_id=None, instance_id=None, page_num=None, page_size=None):
        r"""ShowAuditRequest

        The model defined in huaweicloud sdk

        :param tenant_id: 租户id
        :type tenant_id: str
        :param project_id: 项目id
        :type project_id: str
        :param module: 模块
        :type module: str
        :param repo: 仓库id
        :type repo: str
        :param user_id: 用户id
        :type user_id: str
        :param instance_id: 实例id
        :type instance_id: str
        :param page_num: 页码
        :type page_num: int
        :param page_size: 每页大小
        :type page_size: int
        """
        
        

        self._tenant_id = None
        self._project_id = None
        self._module = None
        self._repo = None
        self._user_id = None
        self._instance_id = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.project_id = project_id
        self.module = module
        self.repo = repo
        if user_id is not None:
            self.user_id = user_id
        if instance_id is not None:
            self.instance_id = instance_id
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowAuditRequest.

        租户id

        :return: The tenant_id of this ShowAuditRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowAuditRequest.

        租户id

        :param tenant_id: The tenant_id of this ShowAuditRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowAuditRequest.

        项目id

        :return: The project_id of this ShowAuditRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowAuditRequest.

        项目id

        :param project_id: The project_id of this ShowAuditRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def module(self):
        r"""Gets the module of this ShowAuditRequest.

        模块

        :return: The module of this ShowAuditRequest.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this ShowAuditRequest.

        模块

        :param module: The module of this ShowAuditRequest.
        :type module: str
        """
        self._module = module

    @property
    def repo(self):
        r"""Gets the repo of this ShowAuditRequest.

        仓库id

        :return: The repo of this ShowAuditRequest.
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        r"""Sets the repo of this ShowAuditRequest.

        仓库id

        :param repo: The repo of this ShowAuditRequest.
        :type repo: str
        """
        self._repo = repo

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowAuditRequest.

        用户id

        :return: The user_id of this ShowAuditRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowAuditRequest.

        用户id

        :param user_id: The user_id of this ShowAuditRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowAuditRequest.

        实例id

        :return: The instance_id of this ShowAuditRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowAuditRequest.

        实例id

        :param instance_id: The instance_id of this ShowAuditRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def page_num(self):
        r"""Gets the page_num of this ShowAuditRequest.

        页码

        :return: The page_num of this ShowAuditRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ShowAuditRequest.

        页码

        :param page_num: The page_num of this ShowAuditRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowAuditRequest.

        每页大小

        :return: The page_size of this ShowAuditRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowAuditRequest.

        每页大小

        :param page_size: The page_size of this ShowAuditRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ShowAuditRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
