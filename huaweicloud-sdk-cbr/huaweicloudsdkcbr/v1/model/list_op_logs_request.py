# coding: utf-8

import pprint
import re

import six





class ListOpLogsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'operation_type': 'str',
        'provider_id': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'start_time': 'str',
        'status': 'str',
        'vault_id': 'str',
        'vault_name': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'operation_type': 'operation_type',
        'provider_id': 'provider_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'start_time': 'start_time',
        'status': 'status',
        'vault_id': 'vault_id',
        'vault_name': 'vault_name',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, end_time=None, limit=None, offset=None, operation_type=None, provider_id=None, resource_id=None, resource_name=None, start_time=None, status=None, vault_id=None, vault_name=None, enterprise_project_id=None):
        """ListOpLogsRequest - a model defined in huaweicloud sdk"""
        
        

        self._end_time = None
        self._limit = None
        self._offset = None
        self._operation_type = None
        self._provider_id = None
        self._resource_id = None
        self._resource_name = None
        self._start_time = None
        self._status = None
        self._vault_id = None
        self._vault_name = None
        self._enterprise_project_id = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if operation_type is not None:
            self.operation_type = operation_type
        if provider_id is not None:
            self.provider_id = provider_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if vault_id is not None:
            self.vault_id = vault_id
        if vault_name is not None:
            self.vault_name = vault_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def end_time(self):
        """Gets the end_time of this ListOpLogsRequest.


        :return: The end_time of this ListOpLogsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListOpLogsRequest.


        :param end_time: The end_time of this ListOpLogsRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListOpLogsRequest.


        :return: The limit of this ListOpLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListOpLogsRequest.


        :param limit: The limit of this ListOpLogsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListOpLogsRequest.


        :return: The offset of this ListOpLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListOpLogsRequest.


        :param offset: The offset of this ListOpLogsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def operation_type(self):
        """Gets the operation_type of this ListOpLogsRequest.


        :return: The operation_type of this ListOpLogsRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this ListOpLogsRequest.


        :param operation_type: The operation_type of this ListOpLogsRequest.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def provider_id(self):
        """Gets the provider_id of this ListOpLogsRequest.


        :return: The provider_id of this ListOpLogsRequest.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this ListOpLogsRequest.


        :param provider_id: The provider_id of this ListOpLogsRequest.
        :type: str
        """
        self._provider_id = provider_id

    @property
    def resource_id(self):
        """Gets the resource_id of this ListOpLogsRequest.


        :return: The resource_id of this ListOpLogsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListOpLogsRequest.


        :param resource_id: The resource_id of this ListOpLogsRequest.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ListOpLogsRequest.


        :return: The resource_name of this ListOpLogsRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListOpLogsRequest.


        :param resource_name: The resource_name of this ListOpLogsRequest.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def start_time(self):
        """Gets the start_time of this ListOpLogsRequest.


        :return: The start_time of this ListOpLogsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListOpLogsRequest.


        :param start_time: The start_time of this ListOpLogsRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this ListOpLogsRequest.


        :return: The status of this ListOpLogsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListOpLogsRequest.


        :param status: The status of this ListOpLogsRequest.
        :type: str
        """
        self._status = status

    @property
    def vault_id(self):
        """Gets the vault_id of this ListOpLogsRequest.


        :return: The vault_id of this ListOpLogsRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this ListOpLogsRequest.


        :param vault_id: The vault_id of this ListOpLogsRequest.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def vault_name(self):
        """Gets the vault_name of this ListOpLogsRequest.


        :return: The vault_name of this ListOpLogsRequest.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        """Sets the vault_name of this ListOpLogsRequest.


        :param vault_name: The vault_name of this ListOpLogsRequest.
        :type: str
        """
        self._vault_name = vault_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListOpLogsRequest.


        :return: The enterprise_project_id of this ListOpLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListOpLogsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListOpLogsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListOpLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
