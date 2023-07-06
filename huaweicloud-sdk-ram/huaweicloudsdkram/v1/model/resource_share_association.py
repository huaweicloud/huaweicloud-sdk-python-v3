# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceShareAssociation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'associated_entity': 'str',
        'association_type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'external': 'bool',
        'resource_share_id': 'str',
        'resource_share_name': 'str',
        'status': 'str',
        'status_message': 'str'
    }

    attribute_map = {
        'associated_entity': 'associated_entity',
        'association_type': 'association_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'external': 'external',
        'resource_share_id': 'resource_share_id',
        'resource_share_name': 'resource_share_name',
        'status': 'status',
        'status_message': 'status_message'
    }

    def __init__(self, associated_entity=None, association_type=None, created_at=None, updated_at=None, external=None, resource_share_id=None, resource_share_name=None, status=None, status_message=None):
        """ResourceShareAssociation

        The model defined in huaweicloud sdk

        :param associated_entity: 绑定的实体。这可以是共享资源的URN、帐号ID、共享资源目录的URN或文件夹的URN之一。
        :type associated_entity: str
        :param association_type: 绑定中包含的实体类型。
        :type association_type: str
        :param created_at: 绑定被创建的时间。
        :type created_at: datetime
        :param updated_at: 最后一次更新绑定的时间。
        :type updated_at: datetime
        :param external: 标识资源使用者是否和共享的拥有者属于同一个组织
        :type external: bool
        :param resource_share_id: 资源共享实例的ID。
        :type resource_share_id: str
        :param resource_share_name: 资源共享实例的名称。
        :type resource_share_name: str
        :param status: 绑定的当前状态。
        :type status: str
        :param status_message: 绑定的当前状态的描述。
        :type status_message: str
        """
        
        

        self._associated_entity = None
        self._association_type = None
        self._created_at = None
        self._updated_at = None
        self._external = None
        self._resource_share_id = None
        self._resource_share_name = None
        self._status = None
        self._status_message = None
        self.discriminator = None

        self.associated_entity = associated_entity
        self.association_type = association_type
        self.created_at = created_at
        self.updated_at = updated_at
        if external is not None:
            self.external = external
        self.resource_share_id = resource_share_id
        self.resource_share_name = resource_share_name
        self.status = status
        if status_message is not None:
            self.status_message = status_message

    @property
    def associated_entity(self):
        """Gets the associated_entity of this ResourceShareAssociation.

        绑定的实体。这可以是共享资源的URN、帐号ID、共享资源目录的URN或文件夹的URN之一。

        :return: The associated_entity of this ResourceShareAssociation.
        :rtype: str
        """
        return self._associated_entity

    @associated_entity.setter
    def associated_entity(self, associated_entity):
        """Sets the associated_entity of this ResourceShareAssociation.

        绑定的实体。这可以是共享资源的URN、帐号ID、共享资源目录的URN或文件夹的URN之一。

        :param associated_entity: The associated_entity of this ResourceShareAssociation.
        :type associated_entity: str
        """
        self._associated_entity = associated_entity

    @property
    def association_type(self):
        """Gets the association_type of this ResourceShareAssociation.

        绑定中包含的实体类型。

        :return: The association_type of this ResourceShareAssociation.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """Sets the association_type of this ResourceShareAssociation.

        绑定中包含的实体类型。

        :param association_type: The association_type of this ResourceShareAssociation.
        :type association_type: str
        """
        self._association_type = association_type

    @property
    def created_at(self):
        """Gets the created_at of this ResourceShareAssociation.

        绑定被创建的时间。

        :return: The created_at of this ResourceShareAssociation.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ResourceShareAssociation.

        绑定被创建的时间。

        :param created_at: The created_at of this ResourceShareAssociation.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ResourceShareAssociation.

        最后一次更新绑定的时间。

        :return: The updated_at of this ResourceShareAssociation.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ResourceShareAssociation.

        最后一次更新绑定的时间。

        :param updated_at: The updated_at of this ResourceShareAssociation.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def external(self):
        """Gets the external of this ResourceShareAssociation.

        标识资源使用者是否和共享的拥有者属于同一个组织

        :return: The external of this ResourceShareAssociation.
        :rtype: bool
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this ResourceShareAssociation.

        标识资源使用者是否和共享的拥有者属于同一个组织

        :param external: The external of this ResourceShareAssociation.
        :type external: bool
        """
        self._external = external

    @property
    def resource_share_id(self):
        """Gets the resource_share_id of this ResourceShareAssociation.

        资源共享实例的ID。

        :return: The resource_share_id of this ResourceShareAssociation.
        :rtype: str
        """
        return self._resource_share_id

    @resource_share_id.setter
    def resource_share_id(self, resource_share_id):
        """Sets the resource_share_id of this ResourceShareAssociation.

        资源共享实例的ID。

        :param resource_share_id: The resource_share_id of this ResourceShareAssociation.
        :type resource_share_id: str
        """
        self._resource_share_id = resource_share_id

    @property
    def resource_share_name(self):
        """Gets the resource_share_name of this ResourceShareAssociation.

        资源共享实例的名称。

        :return: The resource_share_name of this ResourceShareAssociation.
        :rtype: str
        """
        return self._resource_share_name

    @resource_share_name.setter
    def resource_share_name(self, resource_share_name):
        """Sets the resource_share_name of this ResourceShareAssociation.

        资源共享实例的名称。

        :param resource_share_name: The resource_share_name of this ResourceShareAssociation.
        :type resource_share_name: str
        """
        self._resource_share_name = resource_share_name

    @property
    def status(self):
        """Gets the status of this ResourceShareAssociation.

        绑定的当前状态。

        :return: The status of this ResourceShareAssociation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResourceShareAssociation.

        绑定的当前状态。

        :param status: The status of this ResourceShareAssociation.
        :type status: str
        """
        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this ResourceShareAssociation.

        绑定的当前状态的描述。

        :return: The status_message of this ResourceShareAssociation.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this ResourceShareAssociation.

        绑定的当前状态的描述。

        :param status_message: The status_message of this ResourceShareAssociation.
        :type status_message: str
        """
        self._status_message = status_message

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
        if not isinstance(other, ResourceShareAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
