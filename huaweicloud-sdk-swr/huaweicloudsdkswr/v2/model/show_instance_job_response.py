# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceJobResponse(SdkResponse):

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
        'instance_id': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'type': 'str',
        'status': 'str',
        'reason': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'type': 'type',
        'status': 'status',
        'reason': 'reason',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, instance_id=None, resource_id=None, resource_name=None, type=None, status=None, reason=None, created_at=None, updated_at=None):
        r"""ShowInstanceJobResponse

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param instance_id: 相关实例ID
        :type instance_id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param type: 类型
        :type type: str
        :param status: 状态
        :type status: str
        :param reason: 失败原因
        :type reason: str
        :param created_at: 实例创建时间
        :type created_at: str
        :param updated_at: 实例更新时间
        :type updated_at: str
        """
        
        super(ShowInstanceJobResponse, self).__init__()

        self._id = None
        self._instance_id = None
        self._resource_id = None
        self._resource_name = None
        self._type = None
        self._status = None
        self._reason = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ShowInstanceJobResponse.

        任务ID

        :return: The id of this ShowInstanceJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowInstanceJobResponse.

        任务ID

        :param id: The id of this ShowInstanceJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceJobResponse.

        相关实例ID

        :return: The instance_id of this ShowInstanceJobResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceJobResponse.

        相关实例ID

        :param instance_id: The instance_id of this ShowInstanceJobResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ShowInstanceJobResponse.

        资源ID

        :return: The resource_id of this ShowInstanceJobResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ShowInstanceJobResponse.

        资源ID

        :param resource_id: The resource_id of this ShowInstanceJobResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ShowInstanceJobResponse.

        资源名称

        :return: The resource_name of this ShowInstanceJobResponse.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ShowInstanceJobResponse.

        资源名称

        :param resource_name: The resource_name of this ShowInstanceJobResponse.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def type(self):
        r"""Gets the type of this ShowInstanceJobResponse.

        类型

        :return: The type of this ShowInstanceJobResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowInstanceJobResponse.

        类型

        :param type: The type of this ShowInstanceJobResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ShowInstanceJobResponse.

        状态

        :return: The status of this ShowInstanceJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInstanceJobResponse.

        状态

        :param status: The status of this ShowInstanceJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this ShowInstanceJobResponse.

        失败原因

        :return: The reason of this ShowInstanceJobResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ShowInstanceJobResponse.

        失败原因

        :param reason: The reason of this ShowInstanceJobResponse.
        :type reason: str
        """
        self._reason = reason

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowInstanceJobResponse.

        实例创建时间

        :return: The created_at of this ShowInstanceJobResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowInstanceJobResponse.

        实例创建时间

        :param created_at: The created_at of this ShowInstanceJobResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowInstanceJobResponse.

        实例更新时间

        :return: The updated_at of this ShowInstanceJobResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowInstanceJobResponse.

        实例更新时间

        :param updated_at: The updated_at of this ShowInstanceJobResponse.
        :type updated_at: str
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
        if not isinstance(other, ShowInstanceJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
