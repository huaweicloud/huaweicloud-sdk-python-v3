# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SharedPrincipal:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_share_id': 'str',
        'id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'resource_share_id': 'resource_share_id',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, resource_share_id=None, id=None, created_at=None, updated_at=None):
        r"""SharedPrincipal

        The model defined in huaweicloud sdk

        :param resource_share_id: 资源使用者绑定的资源共享实例的ID。
        :type resource_share_id: str
        :param id: 资源使用者的账号ID或URN。
        :type id: str
        :param created_at: 资源使用者与资源共享实例关联的时间。
        :type created_at: datetime
        :param updated_at: 最后一次更新资源共享实例的时间。
        :type updated_at: datetime
        """
        
        

        self._resource_share_id = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if resource_share_id is not None:
            self.resource_share_id = resource_share_id
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def resource_share_id(self):
        r"""Gets the resource_share_id of this SharedPrincipal.

        资源使用者绑定的资源共享实例的ID。

        :return: The resource_share_id of this SharedPrincipal.
        :rtype: str
        """
        return self._resource_share_id

    @resource_share_id.setter
    def resource_share_id(self, resource_share_id):
        r"""Sets the resource_share_id of this SharedPrincipal.

        资源使用者绑定的资源共享实例的ID。

        :param resource_share_id: The resource_share_id of this SharedPrincipal.
        :type resource_share_id: str
        """
        self._resource_share_id = resource_share_id

    @property
    def id(self):
        r"""Gets the id of this SharedPrincipal.

        资源使用者的账号ID或URN。

        :return: The id of this SharedPrincipal.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SharedPrincipal.

        资源使用者的账号ID或URN。

        :param id: The id of this SharedPrincipal.
        :type id: str
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this SharedPrincipal.

        资源使用者与资源共享实例关联的时间。

        :return: The created_at of this SharedPrincipal.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SharedPrincipal.

        资源使用者与资源共享实例关联的时间。

        :param created_at: The created_at of this SharedPrincipal.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SharedPrincipal.

        最后一次更新资源共享实例的时间。

        :return: The updated_at of this SharedPrincipal.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SharedPrincipal.

        最后一次更新资源共享实例的时间。

        :param updated_at: The updated_at of this SharedPrincipal.
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
        if not isinstance(other, SharedPrincipal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
