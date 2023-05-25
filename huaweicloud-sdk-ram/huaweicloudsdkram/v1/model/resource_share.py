# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceShare:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'allow_external_principals': 'bool',
        'owning_account_id': 'str',
        'status': 'str',
        'tags': 'list[Tag]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'allow_external_principals': 'allow_external_principals',
        'owning_account_id': 'owning_account_id',
        'status': 'status',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, allow_external_principals=None, owning_account_id=None, status=None, tags=None, created_at=None, updated_at=None):
        """ResourceShare

        The model defined in huaweicloud sdk

        :param id: 资源共享实例的ID。
        :type id: str
        :param name: 资源共享实例的名称。
        :type name: str
        :param description: 资源共享实例的描述。
        :type description: str
        :param allow_external_principals: 资源共享实例是否支持共享给组织外账号。
        :type allow_external_principals: bool
        :param owning_account_id: 资源共享实例的所有者ID。
        :type owning_account_id: str
        :param status: 资源共享实例的状态。
        :type status: str
        :param tags: 资源共享实例的标签列表。
        :type tags: list[:class:`huaweicloudsdkram.v1.Tag`]
        :param created_at: 创建资源共享实例的时间。
        :type created_at: datetime
        :param updated_at: 最后一次更新资源共享实例的时间。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._allow_external_principals = None
        self._owning_account_id = None
        self._status = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        if allow_external_principals is not None:
            self.allow_external_principals = allow_external_principals
        self.owning_account_id = owning_account_id
        self.status = status
        if tags is not None:
            self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ResourceShare.

        资源共享实例的ID。

        :return: The id of this ResourceShare.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceShare.

        资源共享实例的ID。

        :param id: The id of this ResourceShare.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ResourceShare.

        资源共享实例的名称。

        :return: The name of this ResourceShare.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceShare.

        资源共享实例的名称。

        :param name: The name of this ResourceShare.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ResourceShare.

        资源共享实例的描述。

        :return: The description of this ResourceShare.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResourceShare.

        资源共享实例的描述。

        :param description: The description of this ResourceShare.
        :type description: str
        """
        self._description = description

    @property
    def allow_external_principals(self):
        """Gets the allow_external_principals of this ResourceShare.

        资源共享实例是否支持共享给组织外账号。

        :return: The allow_external_principals of this ResourceShare.
        :rtype: bool
        """
        return self._allow_external_principals

    @allow_external_principals.setter
    def allow_external_principals(self, allow_external_principals):
        """Sets the allow_external_principals of this ResourceShare.

        资源共享实例是否支持共享给组织外账号。

        :param allow_external_principals: The allow_external_principals of this ResourceShare.
        :type allow_external_principals: bool
        """
        self._allow_external_principals = allow_external_principals

    @property
    def owning_account_id(self):
        """Gets the owning_account_id of this ResourceShare.

        资源共享实例的所有者ID。

        :return: The owning_account_id of this ResourceShare.
        :rtype: str
        """
        return self._owning_account_id

    @owning_account_id.setter
    def owning_account_id(self, owning_account_id):
        """Sets the owning_account_id of this ResourceShare.

        资源共享实例的所有者ID。

        :param owning_account_id: The owning_account_id of this ResourceShare.
        :type owning_account_id: str
        """
        self._owning_account_id = owning_account_id

    @property
    def status(self):
        """Gets the status of this ResourceShare.

        资源共享实例的状态。

        :return: The status of this ResourceShare.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResourceShare.

        资源共享实例的状态。

        :param status: The status of this ResourceShare.
        :type status: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ResourceShare.

        资源共享实例的标签列表。

        :return: The tags of this ResourceShare.
        :rtype: list[:class:`huaweicloudsdkram.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResourceShare.

        资源共享实例的标签列表。

        :param tags: The tags of this ResourceShare.
        :type tags: list[:class:`huaweicloudsdkram.v1.Tag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        """Gets the created_at of this ResourceShare.

        创建资源共享实例的时间。

        :return: The created_at of this ResourceShare.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ResourceShare.

        创建资源共享实例的时间。

        :param created_at: The created_at of this ResourceShare.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ResourceShare.

        最后一次更新资源共享实例的时间。

        :return: The updated_at of this ResourceShare.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ResourceShare.

        最后一次更新资源共享实例的时间。

        :param updated_at: The updated_at of this ResourceShare.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ResourceShare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
