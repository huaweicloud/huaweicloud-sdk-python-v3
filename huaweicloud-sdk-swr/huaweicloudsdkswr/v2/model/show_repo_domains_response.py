# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepoDomainsResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'repository': 'str',
        'access_domain': 'str',
        'permit': 'str',
        'deadline': 'str',
        'description': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'created': 'str',
        'updated': 'str',
        'status': 'bool'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'access_domain': 'access_domain',
        'permit': 'permit',
        'deadline': 'deadline',
        'description': 'description',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'created': 'created',
        'updated': 'updated',
        'status': 'status'
    }

    def __init__(self, namespace=None, repository=None, access_domain=None, permit=None, deadline=None, description=None, creator_id=None, creator_name=None, created=None, updated=None, status=None):
        """ShowRepoDomainsResponse

        The model defined in huaweicloud sdk

        :param namespace: 组织
        :type namespace: str
        :param repository: 镜像仓库
        :type repository: str
        :param access_domain: 共享租户名
        :type access_domain: str
        :param permit: 权限
        :type permit: str
        :param deadline: 截止时间
        :type deadline: str
        :param description: 描述
        :type description: str
        :param creator_id: 创建者ID
        :type creator_id: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param created: 镜像创建时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00
        :type created: str
        :param updated: 镜像更新时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00
        :type updated: str
        :param status: 是否过期：true:有效；false:过期
        :type status: bool
        """
        
        

        self._namespace = None
        self._repository = None
        self._access_domain = None
        self._permit = None
        self._deadline = None
        self._description = None
        self._creator_id = None
        self._creator_name = None
        self._created = None
        self._updated = None
        self._status = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.access_domain = access_domain
        self.permit = permit
        self.deadline = deadline
        self.description = description
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.created = created
        self.updated = updated
        self.status = status

    @property
    def namespace(self):
        """Gets the namespace of this ShowRepoDomainsResponse.

        组织

        :return: The namespace of this ShowRepoDomainsResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ShowRepoDomainsResponse.

        组织

        :param namespace: The namespace of this ShowRepoDomainsResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this ShowRepoDomainsResponse.

        镜像仓库

        :return: The repository of this ShowRepoDomainsResponse.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ShowRepoDomainsResponse.

        镜像仓库

        :param repository: The repository of this ShowRepoDomainsResponse.
        :type repository: str
        """
        self._repository = repository

    @property
    def access_domain(self):
        """Gets the access_domain of this ShowRepoDomainsResponse.

        共享租户名

        :return: The access_domain of this ShowRepoDomainsResponse.
        :rtype: str
        """
        return self._access_domain

    @access_domain.setter
    def access_domain(self, access_domain):
        """Sets the access_domain of this ShowRepoDomainsResponse.

        共享租户名

        :param access_domain: The access_domain of this ShowRepoDomainsResponse.
        :type access_domain: str
        """
        self._access_domain = access_domain

    @property
    def permit(self):
        """Gets the permit of this ShowRepoDomainsResponse.

        权限

        :return: The permit of this ShowRepoDomainsResponse.
        :rtype: str
        """
        return self._permit

    @permit.setter
    def permit(self, permit):
        """Sets the permit of this ShowRepoDomainsResponse.

        权限

        :param permit: The permit of this ShowRepoDomainsResponse.
        :type permit: str
        """
        self._permit = permit

    @property
    def deadline(self):
        """Gets the deadline of this ShowRepoDomainsResponse.

        截止时间

        :return: The deadline of this ShowRepoDomainsResponse.
        :rtype: str
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this ShowRepoDomainsResponse.

        截止时间

        :param deadline: The deadline of this ShowRepoDomainsResponse.
        :type deadline: str
        """
        self._deadline = deadline

    @property
    def description(self):
        """Gets the description of this ShowRepoDomainsResponse.

        描述

        :return: The description of this ShowRepoDomainsResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowRepoDomainsResponse.

        描述

        :param description: The description of this ShowRepoDomainsResponse.
        :type description: str
        """
        self._description = description

    @property
    def creator_id(self):
        """Gets the creator_id of this ShowRepoDomainsResponse.

        创建者ID

        :return: The creator_id of this ShowRepoDomainsResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ShowRepoDomainsResponse.

        创建者ID

        :param creator_id: The creator_id of this ShowRepoDomainsResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        """Gets the creator_name of this ShowRepoDomainsResponse.

        创建者名称

        :return: The creator_name of this ShowRepoDomainsResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ShowRepoDomainsResponse.

        创建者名称

        :param creator_name: The creator_name of this ShowRepoDomainsResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def created(self):
        """Gets the created of this ShowRepoDomainsResponse.

        镜像创建时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The created of this ShowRepoDomainsResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowRepoDomainsResponse.

        镜像创建时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param created: The created of this ShowRepoDomainsResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowRepoDomainsResponse.

        镜像更新时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The updated of this ShowRepoDomainsResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowRepoDomainsResponse.

        镜像更新时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param updated: The updated of this ShowRepoDomainsResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def status(self):
        """Gets the status of this ShowRepoDomainsResponse.

        是否过期：true:有效；false:过期

        :return: The status of this ShowRepoDomainsResponse.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowRepoDomainsResponse.

        是否过期：true:有效；false:过期

        :param status: The status of this ShowRepoDomainsResponse.
        :type status: bool
        """
        self._status = status

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
        if not isinstance(other, ShowRepoDomainsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
