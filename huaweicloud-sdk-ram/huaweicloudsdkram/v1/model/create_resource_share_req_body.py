# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourceShareReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'allow_external_principals': 'bool',
        'permission_ids': 'list[str]',
        'principals': 'list[str]',
        'resource_urns': 'list[str]',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'allow_external_principals': 'allow_external_principals',
        'permission_ids': 'permission_ids',
        'principals': 'principals',
        'resource_urns': 'resource_urns',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, allow_external_principals=None, permission_ids=None, principals=None, resource_urns=None, tags=None):
        r"""CreateResourceShareReqBody

        The model defined in huaweicloud sdk

        :param name: 资源共享实例的名称。
        :type name: str
        :param description: 资源共享实例的描述。
        :type description: str
        :param allow_external_principals: 资源共享实例是否支持共享给组织外账号。
        :type allow_external_principals: bool
        :param permission_ids: 资源共享实例关联的RAM权限列表。一种资源类型只能关联一个RAM权限。如果您没有指定权限ID，RAM将自动为每个资源类型关联默认权限。
        :type permission_ids: list[str]
        :param principals: 资源共享实例关联的一个或多个资源使用者的列表。
        :type principals: list[str]
        :param resource_urns: 资源共享实例关联的一个或多个共享资源URN的列表。
        :type resource_urns: list[str]
        :param tags: 资源共享标签列表。
        :type tags: list[:class:`huaweicloudsdkram.v1.Tag`]
        """
        
        

        self._name = None
        self._description = None
        self._allow_external_principals = None
        self._permission_ids = None
        self._principals = None
        self._resource_urns = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if allow_external_principals is not None:
            self.allow_external_principals = allow_external_principals
        if permission_ids is not None:
            self.permission_ids = permission_ids
        if principals is not None:
            self.principals = principals
        if resource_urns is not None:
            self.resource_urns = resource_urns
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateResourceShareReqBody.

        资源共享实例的名称。

        :return: The name of this CreateResourceShareReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateResourceShareReqBody.

        资源共享实例的名称。

        :param name: The name of this CreateResourceShareReqBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateResourceShareReqBody.

        资源共享实例的描述。

        :return: The description of this CreateResourceShareReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateResourceShareReqBody.

        资源共享实例的描述。

        :param description: The description of this CreateResourceShareReqBody.
        :type description: str
        """
        self._description = description

    @property
    def allow_external_principals(self):
        r"""Gets the allow_external_principals of this CreateResourceShareReqBody.

        资源共享实例是否支持共享给组织外账号。

        :return: The allow_external_principals of this CreateResourceShareReqBody.
        :rtype: bool
        """
        return self._allow_external_principals

    @allow_external_principals.setter
    def allow_external_principals(self, allow_external_principals):
        r"""Sets the allow_external_principals of this CreateResourceShareReqBody.

        资源共享实例是否支持共享给组织外账号。

        :param allow_external_principals: The allow_external_principals of this CreateResourceShareReqBody.
        :type allow_external_principals: bool
        """
        self._allow_external_principals = allow_external_principals

    @property
    def permission_ids(self):
        r"""Gets the permission_ids of this CreateResourceShareReqBody.

        资源共享实例关联的RAM权限列表。一种资源类型只能关联一个RAM权限。如果您没有指定权限ID，RAM将自动为每个资源类型关联默认权限。

        :return: The permission_ids of this CreateResourceShareReqBody.
        :rtype: list[str]
        """
        return self._permission_ids

    @permission_ids.setter
    def permission_ids(self, permission_ids):
        r"""Sets the permission_ids of this CreateResourceShareReqBody.

        资源共享实例关联的RAM权限列表。一种资源类型只能关联一个RAM权限。如果您没有指定权限ID，RAM将自动为每个资源类型关联默认权限。

        :param permission_ids: The permission_ids of this CreateResourceShareReqBody.
        :type permission_ids: list[str]
        """
        self._permission_ids = permission_ids

    @property
    def principals(self):
        r"""Gets the principals of this CreateResourceShareReqBody.

        资源共享实例关联的一个或多个资源使用者的列表。

        :return: The principals of this CreateResourceShareReqBody.
        :rtype: list[str]
        """
        return self._principals

    @principals.setter
    def principals(self, principals):
        r"""Sets the principals of this CreateResourceShareReqBody.

        资源共享实例关联的一个或多个资源使用者的列表。

        :param principals: The principals of this CreateResourceShareReqBody.
        :type principals: list[str]
        """
        self._principals = principals

    @property
    def resource_urns(self):
        r"""Gets the resource_urns of this CreateResourceShareReqBody.

        资源共享实例关联的一个或多个共享资源URN的列表。

        :return: The resource_urns of this CreateResourceShareReqBody.
        :rtype: list[str]
        """
        return self._resource_urns

    @resource_urns.setter
    def resource_urns(self, resource_urns):
        r"""Sets the resource_urns of this CreateResourceShareReqBody.

        资源共享实例关联的一个或多个共享资源URN的列表。

        :param resource_urns: The resource_urns of this CreateResourceShareReqBody.
        :type resource_urns: list[str]
        """
        self._resource_urns = resource_urns

    @property
    def tags(self):
        r"""Gets the tags of this CreateResourceShareReqBody.

        资源共享标签列表。

        :return: The tags of this CreateResourceShareReqBody.
        :rtype: list[:class:`huaweicloudsdkram.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateResourceShareReqBody.

        资源共享标签列表。

        :param tags: The tags of this CreateResourceShareReqBody.
        :type tags: list[:class:`huaweicloudsdkram.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateResourceShareReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
