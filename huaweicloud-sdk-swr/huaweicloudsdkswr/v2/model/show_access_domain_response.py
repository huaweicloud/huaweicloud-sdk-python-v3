# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAccessDomainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'exist': 'bool',
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
        'exist': 'exist',
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

    def __init__(self, exist=None, namespace=None, repository=None, access_domain=None, permit=None, deadline=None, description=None, creator_id=None, creator_name=None, created=None, updated=None, status=None):
        """ShowAccessDomainResponse

        The model defined in huaweicloud sdk

        :param exist: true：存在；false：不存在
        :type exist: bool
        :param namespace: 组织名称
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param access_domain: 共享帐号名
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
        :param created: 镜像创建时间，UTC时间格式，时间为UTC标准时间
        :type created: str
        :param updated: 镜像更新时间，UTC时间格式，时间为UTC标准时间
        :type updated: str
        :param status: 是否过期，true：有效；false：过期
        :type status: bool
        """
        
        super(ShowAccessDomainResponse, self).__init__()

        self._exist = None
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

        if exist is not None:
            self.exist = exist
        if namespace is not None:
            self.namespace = namespace
        if repository is not None:
            self.repository = repository
        if access_domain is not None:
            self.access_domain = access_domain
        if permit is not None:
            self.permit = permit
        if deadline is not None:
            self.deadline = deadline
        if description is not None:
            self.description = description
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if status is not None:
            self.status = status

    @property
    def exist(self):
        """Gets the exist of this ShowAccessDomainResponse.

        true：存在；false：不存在

        :return: The exist of this ShowAccessDomainResponse.
        :rtype: bool
        """
        return self._exist

    @exist.setter
    def exist(self, exist):
        """Sets the exist of this ShowAccessDomainResponse.

        true：存在；false：不存在

        :param exist: The exist of this ShowAccessDomainResponse.
        :type exist: bool
        """
        self._exist = exist

    @property
    def namespace(self):
        """Gets the namespace of this ShowAccessDomainResponse.

        组织名称

        :return: The namespace of this ShowAccessDomainResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ShowAccessDomainResponse.

        组织名称

        :param namespace: The namespace of this ShowAccessDomainResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this ShowAccessDomainResponse.

        镜像仓库名称

        :return: The repository of this ShowAccessDomainResponse.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ShowAccessDomainResponse.

        镜像仓库名称

        :param repository: The repository of this ShowAccessDomainResponse.
        :type repository: str
        """
        self._repository = repository

    @property
    def access_domain(self):
        """Gets the access_domain of this ShowAccessDomainResponse.

        共享帐号名

        :return: The access_domain of this ShowAccessDomainResponse.
        :rtype: str
        """
        return self._access_domain

    @access_domain.setter
    def access_domain(self, access_domain):
        """Sets the access_domain of this ShowAccessDomainResponse.

        共享帐号名

        :param access_domain: The access_domain of this ShowAccessDomainResponse.
        :type access_domain: str
        """
        self._access_domain = access_domain

    @property
    def permit(self):
        """Gets the permit of this ShowAccessDomainResponse.

        权限

        :return: The permit of this ShowAccessDomainResponse.
        :rtype: str
        """
        return self._permit

    @permit.setter
    def permit(self, permit):
        """Sets the permit of this ShowAccessDomainResponse.

        权限

        :param permit: The permit of this ShowAccessDomainResponse.
        :type permit: str
        """
        self._permit = permit

    @property
    def deadline(self):
        """Gets the deadline of this ShowAccessDomainResponse.

        截止时间

        :return: The deadline of this ShowAccessDomainResponse.
        :rtype: str
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this ShowAccessDomainResponse.

        截止时间

        :param deadline: The deadline of this ShowAccessDomainResponse.
        :type deadline: str
        """
        self._deadline = deadline

    @property
    def description(self):
        """Gets the description of this ShowAccessDomainResponse.

        描述

        :return: The description of this ShowAccessDomainResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowAccessDomainResponse.

        描述

        :param description: The description of this ShowAccessDomainResponse.
        :type description: str
        """
        self._description = description

    @property
    def creator_id(self):
        """Gets the creator_id of this ShowAccessDomainResponse.

        创建者ID

        :return: The creator_id of this ShowAccessDomainResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ShowAccessDomainResponse.

        创建者ID

        :param creator_id: The creator_id of this ShowAccessDomainResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        """Gets the creator_name of this ShowAccessDomainResponse.

        创建者名称

        :return: The creator_name of this ShowAccessDomainResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ShowAccessDomainResponse.

        创建者名称

        :param creator_name: The creator_name of this ShowAccessDomainResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def created(self):
        """Gets the created of this ShowAccessDomainResponse.

        镜像创建时间，UTC时间格式，时间为UTC标准时间

        :return: The created of this ShowAccessDomainResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowAccessDomainResponse.

        镜像创建时间，UTC时间格式，时间为UTC标准时间

        :param created: The created of this ShowAccessDomainResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowAccessDomainResponse.

        镜像更新时间，UTC时间格式，时间为UTC标准时间

        :return: The updated of this ShowAccessDomainResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowAccessDomainResponse.

        镜像更新时间，UTC时间格式，时间为UTC标准时间

        :param updated: The updated of this ShowAccessDomainResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def status(self):
        """Gets the status of this ShowAccessDomainResponse.

        是否过期，true：有效；false：过期

        :return: The status of this ShowAccessDomainResponse.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowAccessDomainResponse.

        是否过期，true：有效；false：过期

        :param status: The status of this ShowAccessDomainResponse.
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
        if not isinstance(other, ShowAccessDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
