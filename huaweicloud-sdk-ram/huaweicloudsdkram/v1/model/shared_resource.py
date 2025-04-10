# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SharedResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_urn': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'resource_type': 'str',
        'resource_share_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'resource_urn': 'resource_urn',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'resource_type': 'resource_type',
        'resource_share_id': 'resource_share_id',
        'status': 'status'
    }

    def __init__(self, resource_urn=None, created_at=None, updated_at=None, resource_type=None, resource_share_id=None, status=None):
        r"""SharedResource

        The model defined in huaweicloud sdk

        :param resource_urn: 资源的统一资源名称。
        :type resource_urn: str
        :param created_at: 资源与资源共享实例关联的时间。
        :type created_at: datetime
        :param updated_at: 最后一次更新资源共享实例的时间。
        :type updated_at: datetime
        :param resource_type: 资源的类型。
        :type resource_type: str
        :param resource_share_id: 资源绑定的资源共享实例的ID。
        :type resource_share_id: str
        :param status: 资源绑定的当前状态。
        :type status: str
        """
        
        

        self._resource_urn = None
        self._created_at = None
        self._updated_at = None
        self._resource_type = None
        self._resource_share_id = None
        self._status = None
        self.discriminator = None

        if resource_urn is not None:
            self.resource_urn = resource_urn
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_share_id is not None:
            self.resource_share_id = resource_share_id
        if status is not None:
            self.status = status

    @property
    def resource_urn(self):
        r"""Gets the resource_urn of this SharedResource.

        资源的统一资源名称。

        :return: The resource_urn of this SharedResource.
        :rtype: str
        """
        return self._resource_urn

    @resource_urn.setter
    def resource_urn(self, resource_urn):
        r"""Sets the resource_urn of this SharedResource.

        资源的统一资源名称。

        :param resource_urn: The resource_urn of this SharedResource.
        :type resource_urn: str
        """
        self._resource_urn = resource_urn

    @property
    def created_at(self):
        r"""Gets the created_at of this SharedResource.

        资源与资源共享实例关联的时间。

        :return: The created_at of this SharedResource.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SharedResource.

        资源与资源共享实例关联的时间。

        :param created_at: The created_at of this SharedResource.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SharedResource.

        最后一次更新资源共享实例的时间。

        :return: The updated_at of this SharedResource.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SharedResource.

        最后一次更新资源共享实例的时间。

        :param updated_at: The updated_at of this SharedResource.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def resource_type(self):
        r"""Gets the resource_type of this SharedResource.

        资源的类型。

        :return: The resource_type of this SharedResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this SharedResource.

        资源的类型。

        :param resource_type: The resource_type of this SharedResource.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_share_id(self):
        r"""Gets the resource_share_id of this SharedResource.

        资源绑定的资源共享实例的ID。

        :return: The resource_share_id of this SharedResource.
        :rtype: str
        """
        return self._resource_share_id

    @resource_share_id.setter
    def resource_share_id(self, resource_share_id):
        r"""Sets the resource_share_id of this SharedResource.

        资源绑定的资源共享实例的ID。

        :param resource_share_id: The resource_share_id of this SharedResource.
        :type resource_share_id: str
        """
        self._resource_share_id = resource_share_id

    @property
    def status(self):
        r"""Gets the status of this SharedResource.

        资源绑定的当前状态。

        :return: The status of this SharedResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SharedResource.

        资源绑定的当前状态。

        :param status: The status of this SharedResource.
        :type status: str
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
        if not isinstance(other, SharedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
