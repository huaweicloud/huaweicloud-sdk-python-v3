# coding: utf-8

import pprint
import re

import six





class ListDatabaseRolesRequest:


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
        'role_name': 'str',
        'db_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'role_name': 'role_name',
        'db_name': 'db_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, role_name=None, db_name=None, offset=None, limit=None):
        """ListDatabaseRolesRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._role_name = None
        self._db_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if role_name is not None:
            self.role_name = role_name
        if db_name is not None:
            self.db_name = db_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDatabaseRolesRequest.


        :return: The instance_id of this ListDatabaseRolesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDatabaseRolesRequest.


        :param instance_id: The instance_id of this ListDatabaseRolesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def role_name(self):
        """Gets the role_name of this ListDatabaseRolesRequest.


        :return: The role_name of this ListDatabaseRolesRequest.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this ListDatabaseRolesRequest.


        :param role_name: The role_name of this ListDatabaseRolesRequest.
        :type: str
        """
        self._role_name = role_name

    @property
    def db_name(self):
        """Gets the db_name of this ListDatabaseRolesRequest.


        :return: The db_name of this ListDatabaseRolesRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this ListDatabaseRolesRequest.


        :param db_name: The db_name of this ListDatabaseRolesRequest.
        :type: str
        """
        self._db_name = db_name

    @property
    def offset(self):
        """Gets the offset of this ListDatabaseRolesRequest.


        :return: The offset of this ListDatabaseRolesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDatabaseRolesRequest.


        :param offset: The offset of this ListDatabaseRolesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDatabaseRolesRequest.


        :return: The limit of this ListDatabaseRolesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDatabaseRolesRequest.


        :param limit: The limit of this ListDatabaseRolesRequest.
        :type: int
        """
        self._limit = limit

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDatabaseRolesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
