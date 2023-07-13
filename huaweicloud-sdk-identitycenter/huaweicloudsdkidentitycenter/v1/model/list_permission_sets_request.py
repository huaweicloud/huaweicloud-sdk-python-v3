# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionSetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'permission_set_id': 'str',
        'permission_urn': 'str',
        'name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'marker': 'marker',
        'permission_set_id': 'permission_set_id',
        'permission_urn': 'permission_urn',
        'name': 'name'
    }

    def __init__(self, instance_id=None, limit=None, marker=None, permission_set_id=None, permission_urn=None, name=None):
        """ListPermissionSetsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 
        :type instance_id: str
        :param limit: 
        :type limit: int
        :param marker: 
        :type marker: str
        :param permission_set_id: 权限集的全局唯一标识符（ID）
        :type permission_set_id: str
        :param permission_urn: 权限集urn
        :type permission_urn: str
        :param name: 权限集名称
        :type name: str
        """
        
        

        self._instance_id = None
        self._limit = None
        self._marker = None
        self._permission_set_id = None
        self._permission_urn = None
        self._name = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if permission_urn is not None:
            self.permission_urn = permission_urn
        if name is not None:
            self.name = name

    @property
    def instance_id(self):
        """Gets the instance_id of this ListPermissionSetsRequest.

        :return: The instance_id of this ListPermissionSetsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListPermissionSetsRequest.

        :param instance_id: The instance_id of this ListPermissionSetsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListPermissionSetsRequest.

        :return: The limit of this ListPermissionSetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPermissionSetsRequest.

        :param limit: The limit of this ListPermissionSetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPermissionSetsRequest.

        :return: The marker of this ListPermissionSetsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPermissionSetsRequest.

        :param marker: The marker of this ListPermissionSetsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def permission_set_id(self):
        """Gets the permission_set_id of this ListPermissionSetsRequest.

        权限集的全局唯一标识符（ID）

        :return: The permission_set_id of this ListPermissionSetsRequest.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        """Sets the permission_set_id of this ListPermissionSetsRequest.

        权限集的全局唯一标识符（ID）

        :param permission_set_id: The permission_set_id of this ListPermissionSetsRequest.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def permission_urn(self):
        """Gets the permission_urn of this ListPermissionSetsRequest.

        权限集urn

        :return: The permission_urn of this ListPermissionSetsRequest.
        :rtype: str
        """
        return self._permission_urn

    @permission_urn.setter
    def permission_urn(self, permission_urn):
        """Sets the permission_urn of this ListPermissionSetsRequest.

        权限集urn

        :param permission_urn: The permission_urn of this ListPermissionSetsRequest.
        :type permission_urn: str
        """
        self._permission_urn = permission_urn

    @property
    def name(self):
        """Gets the name of this ListPermissionSetsRequest.

        权限集名称

        :return: The name of this ListPermissionSetsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPermissionSetsRequest.

        权限集名称

        :param name: The name of this ListPermissionSetsRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListPermissionSetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
