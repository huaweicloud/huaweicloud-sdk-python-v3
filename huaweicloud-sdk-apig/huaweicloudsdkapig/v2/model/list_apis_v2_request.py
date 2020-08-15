# coding: utf-8

import pprint
import re

import six





class ListApisV2Request:


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
        'id': 'str',
        'name': 'str',
        'group_id': 'str',
        'req_protocol': 'str',
        'req_method': 'str',
        'req_uri': 'str',
        'auth_type': 'str',
        'env_id': 'str',
        'type': 'int',
        'offset': 'int',
        'limit': 'int',
        'precise_search': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'id': 'id',
        'name': 'name',
        'group_id': 'group_id',
        'req_protocol': 'req_protocol',
        'req_method': 'req_method',
        'req_uri': 'req_uri',
        'auth_type': 'auth_type',
        'env_id': 'env_id',
        'type': 'type',
        'offset': 'offset',
        'limit': 'limit',
        'precise_search': 'precise_search'
    }

    def __init__(self, instance_id=None, id=None, name=None, group_id=None, req_protocol=None, req_method=None, req_uri=None, auth_type=None, env_id=None, type=None, offset=0, limit=20, precise_search=None):
        """ListApisV2Request - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._id = None
        self._name = None
        self._group_id = None
        self._req_protocol = None
        self._req_method = None
        self._req_uri = None
        self._auth_type = None
        self._env_id = None
        self._type = None
        self._offset = None
        self._limit = None
        self._precise_search = None
        self.discriminator = None

        self.instance_id = instance_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if group_id is not None:
            self.group_id = group_id
        if req_protocol is not None:
            self.req_protocol = req_protocol
        if req_method is not None:
            self.req_method = req_method
        if req_uri is not None:
            self.req_uri = req_uri
        if auth_type is not None:
            self.auth_type = auth_type
        if env_id is not None:
            self.env_id = env_id
        if type is not None:
            self.type = type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if precise_search is not None:
            self.precise_search = precise_search

    @property
    def instance_id(self):
        """Gets the instance_id of this ListApisV2Request.


        :return: The instance_id of this ListApisV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListApisV2Request.


        :param instance_id: The instance_id of this ListApisV2Request.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def id(self):
        """Gets the id of this ListApisV2Request.


        :return: The id of this ListApisV2Request.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListApisV2Request.


        :param id: The id of this ListApisV2Request.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListApisV2Request.


        :return: The name of this ListApisV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListApisV2Request.


        :param name: The name of this ListApisV2Request.
        :type: str
        """
        self._name = name

    @property
    def group_id(self):
        """Gets the group_id of this ListApisV2Request.


        :return: The group_id of this ListApisV2Request.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListApisV2Request.


        :param group_id: The group_id of this ListApisV2Request.
        :type: str
        """
        self._group_id = group_id

    @property
    def req_protocol(self):
        """Gets the req_protocol of this ListApisV2Request.


        :return: The req_protocol of this ListApisV2Request.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        """Sets the req_protocol of this ListApisV2Request.


        :param req_protocol: The req_protocol of this ListApisV2Request.
        :type: str
        """
        self._req_protocol = req_protocol

    @property
    def req_method(self):
        """Gets the req_method of this ListApisV2Request.


        :return: The req_method of this ListApisV2Request.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this ListApisV2Request.


        :param req_method: The req_method of this ListApisV2Request.
        :type: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        """Gets the req_uri of this ListApisV2Request.


        :return: The req_uri of this ListApisV2Request.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this ListApisV2Request.


        :param req_uri: The req_uri of this ListApisV2Request.
        :type: str
        """
        self._req_uri = req_uri

    @property
    def auth_type(self):
        """Gets the auth_type of this ListApisV2Request.


        :return: The auth_type of this ListApisV2Request.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ListApisV2Request.


        :param auth_type: The auth_type of this ListApisV2Request.
        :type: str
        """
        self._auth_type = auth_type

    @property
    def env_id(self):
        """Gets the env_id of this ListApisV2Request.


        :return: The env_id of this ListApisV2Request.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ListApisV2Request.


        :param env_id: The env_id of this ListApisV2Request.
        :type: str
        """
        self._env_id = env_id

    @property
    def type(self):
        """Gets the type of this ListApisV2Request.


        :return: The type of this ListApisV2Request.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListApisV2Request.


        :param type: The type of this ListApisV2Request.
        :type: int
        """
        self._type = type

    @property
    def offset(self):
        """Gets the offset of this ListApisV2Request.


        :return: The offset of this ListApisV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListApisV2Request.


        :param offset: The offset of this ListApisV2Request.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListApisV2Request.


        :return: The limit of this ListApisV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApisV2Request.


        :param limit: The limit of this ListApisV2Request.
        :type: int
        """
        self._limit = limit

    @property
    def precise_search(self):
        """Gets the precise_search of this ListApisV2Request.


        :return: The precise_search of this ListApisV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        """Sets the precise_search of this ListApisV2Request.


        :param precise_search: The precise_search of this ListApisV2Request.
        :type: str
        """
        self._precise_search = precise_search

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
        if not isinstance(other, ListApisV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
