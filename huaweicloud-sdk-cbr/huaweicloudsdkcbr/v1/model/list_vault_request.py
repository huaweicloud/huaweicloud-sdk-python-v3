# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVaultRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'cloud_type': 'str',
        'protect_type': 'str',
        'object_type': 'str',
        'enterprise_project_id': 'str',
        'id': 'str',
        'policy_id': 'str',
        'status': 'str',
        'resource_ids': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'cloud_type': 'cloud_type',
        'protect_type': 'protect_type',
        'object_type': 'object_type',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'policy_id': 'policy_id',
        'status': 'status',
        'resource_ids': 'resource_ids'
    }

    def __init__(self, limit=None, name=None, offset=None, cloud_type=None, protect_type=None, object_type=None, enterprise_project_id=None, id=None, policy_id=None, status=None, resource_ids=None):
        """ListVaultRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._name = None
        self._offset = None
        self._cloud_type = None
        self._protect_type = None
        self._object_type = None
        self._enterprise_project_id = None
        self._id = None
        self._policy_id = None
        self._status = None
        self._resource_ids = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if cloud_type is not None:
            self.cloud_type = cloud_type
        if protect_type is not None:
            self.protect_type = protect_type
        if object_type is not None:
            self.object_type = object_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if policy_id is not None:
            self.policy_id = policy_id
        if status is not None:
            self.status = status
        if resource_ids is not None:
            self.resource_ids = resource_ids

    @property
    def limit(self):
        """Gets the limit of this ListVaultRequest.

        每页显示条目数，正整数

        :return: The limit of this ListVaultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVaultRequest.

        每页显示条目数，正整数

        :param limit: The limit of this ListVaultRequest.
        :type: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListVaultRequest.

        存储库名称

        :return: The name of this ListVaultRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListVaultRequest.

        存储库名称

        :param name: The name of this ListVaultRequest.
        :type: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListVaultRequest.

        偏移值,正整数

        :return: The offset of this ListVaultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVaultRequest.

        偏移值,正整数

        :param offset: The offset of this ListVaultRequest.
        :type: int
        """
        self._offset = offset

    @property
    def cloud_type(self):
        """Gets the cloud_type of this ListVaultRequest.

        云类型

        :return: The cloud_type of this ListVaultRequest.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this ListVaultRequest.

        云类型

        :param cloud_type: The cloud_type of this ListVaultRequest.
        :type: str
        """
        self._cloud_type = cloud_type

    @property
    def protect_type(self):
        """Gets the protect_type of this ListVaultRequest.

        保护类型

        :return: The protect_type of this ListVaultRequest.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        """Sets the protect_type of this ListVaultRequest.

        保护类型

        :param protect_type: The protect_type of this ListVaultRequest.
        :type: str
        """
        self._protect_type = protect_type

    @property
    def object_type(self):
        """Gets the object_type of this ListVaultRequest.

        资源类型

        :return: The object_type of this ListVaultRequest.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ListVaultRequest.

        资源类型

        :param object_type: The object_type of this ListVaultRequest.
        :type: str
        """
        self._object_type = object_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListVaultRequest.

        企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id

        :return: The enterprise_project_id of this ListVaultRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListVaultRequest.

        企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListVaultRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this ListVaultRequest.

        存储库ID

        :return: The id of this ListVaultRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListVaultRequest.

        存储库ID

        :param id: The id of this ListVaultRequest.
        :type: str
        """
        self._id = id

    @property
    def policy_id(self):
        """Gets the policy_id of this ListVaultRequest.

        策略ID

        :return: The policy_id of this ListVaultRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ListVaultRequest.

        策略ID

        :param policy_id: The policy_id of this ListVaultRequest.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def status(self):
        """Gets the status of this ListVaultRequest.

        状态

        :return: The status of this ListVaultRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListVaultRequest.

        状态

        :param status: The status of this ListVaultRequest.
        :type: str
        """
        self._status = status

    @property
    def resource_ids(self):
        """Gets the resource_ids of this ListVaultRequest.

        资源id

        :return: The resource_ids of this ListVaultRequest.
        :rtype: str
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this ListVaultRequest.

        资源id

        :param resource_ids: The resource_ids of this ListVaultRequest.
        :type: str
        """
        self._resource_ids = resource_ids

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListVaultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
