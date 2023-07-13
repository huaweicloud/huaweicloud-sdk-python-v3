# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountAssignmentsRequest:

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
        'account_id': 'str',
        'permission_set_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'marker': 'marker',
        'account_id': 'account_id',
        'permission_set_id': 'permission_set_id'
    }

    def __init__(self, instance_id=None, limit=None, marker=None, account_id=None, permission_set_id=None):
        """ListAccountAssignmentsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 
        :type instance_id: str
        :param limit: 
        :type limit: int
        :param marker: 
        :type marker: str
        :param account_id: 指定账户的唯一身份标识.
        :type account_id: str
        :param permission_set_id: 指定权限集的唯一身份标识.
        :type permission_set_id: str
        """
        
        

        self._instance_id = None
        self._limit = None
        self._marker = None
        self._account_id = None
        self._permission_set_id = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        self.account_id = account_id
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListAccountAssignmentsRequest.

        :return: The instance_id of this ListAccountAssignmentsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListAccountAssignmentsRequest.

        :param instance_id: The instance_id of this ListAccountAssignmentsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListAccountAssignmentsRequest.

        :return: The limit of this ListAccountAssignmentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAccountAssignmentsRequest.

        :param limit: The limit of this ListAccountAssignmentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListAccountAssignmentsRequest.

        :return: The marker of this ListAccountAssignmentsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAccountAssignmentsRequest.

        :param marker: The marker of this ListAccountAssignmentsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def account_id(self):
        """Gets the account_id of this ListAccountAssignmentsRequest.

        指定账户的唯一身份标识.

        :return: The account_id of this ListAccountAssignmentsRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ListAccountAssignmentsRequest.

        指定账户的唯一身份标识.

        :param account_id: The account_id of this ListAccountAssignmentsRequest.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def permission_set_id(self):
        """Gets the permission_set_id of this ListAccountAssignmentsRequest.

        指定权限集的唯一身份标识.

        :return: The permission_set_id of this ListAccountAssignmentsRequest.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        """Sets the permission_set_id of this ListAccountAssignmentsRequest.

        指定权限集的唯一身份标识.

        :param permission_set_id: The permission_set_id of this ListAccountAssignmentsRequest.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

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
        if not isinstance(other, ListAccountAssignmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
