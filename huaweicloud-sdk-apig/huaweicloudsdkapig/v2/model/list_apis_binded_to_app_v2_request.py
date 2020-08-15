# coding: utf-8

import pprint
import re

import six





class ListApisBindedToAppV2Request:


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
        'app_id': 'str',
        'api_id': 'str',
        'api_name': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'env_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'app_id': 'app_id',
        'api_id': 'api_id',
        'api_name': 'api_name',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'env_id': 'env_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, app_id=None, api_id=None, api_name=None, group_id=None, group_name=None, env_id=None, offset=0, limit=20):
        """ListApisBindedToAppV2Request - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._app_id = None
        self._api_id = None
        self._api_name = None
        self._group_id = None
        self._group_name = None
        self._env_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.app_id = app_id
        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if env_id is not None:
            self.env_id = env_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        """Gets the instance_id of this ListApisBindedToAppV2Request.


        :return: The instance_id of this ListApisBindedToAppV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListApisBindedToAppV2Request.


        :param instance_id: The instance_id of this ListApisBindedToAppV2Request.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        """Gets the app_id of this ListApisBindedToAppV2Request.


        :return: The app_id of this ListApisBindedToAppV2Request.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListApisBindedToAppV2Request.


        :param app_id: The app_id of this ListApisBindedToAppV2Request.
        :type: str
        """
        self._app_id = app_id

    @property
    def api_id(self):
        """Gets the api_id of this ListApisBindedToAppV2Request.


        :return: The api_id of this ListApisBindedToAppV2Request.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ListApisBindedToAppV2Request.


        :param api_id: The api_id of this ListApisBindedToAppV2Request.
        :type: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        """Gets the api_name of this ListApisBindedToAppV2Request.


        :return: The api_name of this ListApisBindedToAppV2Request.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this ListApisBindedToAppV2Request.


        :param api_name: The api_name of this ListApisBindedToAppV2Request.
        :type: str
        """
        self._api_name = api_name

    @property
    def group_id(self):
        """Gets the group_id of this ListApisBindedToAppV2Request.


        :return: The group_id of this ListApisBindedToAppV2Request.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListApisBindedToAppV2Request.


        :param group_id: The group_id of this ListApisBindedToAppV2Request.
        :type: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this ListApisBindedToAppV2Request.


        :return: The group_name of this ListApisBindedToAppV2Request.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListApisBindedToAppV2Request.


        :param group_name: The group_name of this ListApisBindedToAppV2Request.
        :type: str
        """
        self._group_name = group_name

    @property
    def env_id(self):
        """Gets the env_id of this ListApisBindedToAppV2Request.


        :return: The env_id of this ListApisBindedToAppV2Request.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ListApisBindedToAppV2Request.


        :param env_id: The env_id of this ListApisBindedToAppV2Request.
        :type: str
        """
        self._env_id = env_id

    @property
    def offset(self):
        """Gets the offset of this ListApisBindedToAppV2Request.


        :return: The offset of this ListApisBindedToAppV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListApisBindedToAppV2Request.


        :param offset: The offset of this ListApisBindedToAppV2Request.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListApisBindedToAppV2Request.


        :return: The limit of this ListApisBindedToAppV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApisBindedToAppV2Request.


        :param limit: The limit of this ListApisBindedToAppV2Request.
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
        if not isinstance(other, ListApisBindedToAppV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
