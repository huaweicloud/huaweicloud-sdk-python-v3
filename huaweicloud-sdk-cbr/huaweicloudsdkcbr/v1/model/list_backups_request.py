# coding: utf-8

import pprint
import re

import six





class ListBackupsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'checkpoint_id': 'str',
        'dec': 'bool',
        'end_time': 'str',
        'image_type': 'str',
        'limit': 'int',
        'marker': 'str',
        'name': 'str',
        'offset': 'int',
        'resource_az': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'sort': 'str',
        'start_time': 'str',
        'status': 'str',
        'vault_id': 'str',
        'enterprise_project_id': 'str',
        'own_type': 'str',
        'member_status': 'str',
        'parent_id': 'str',
        'used_percent': 'str'
    }

    attribute_map = {
        'checkpoint_id': 'checkpoint_id',
        'dec': 'dec',
        'end_time': 'end_time',
        'image_type': 'image_type',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'offset': 'offset',
        'resource_az': 'resource_az',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'sort': 'sort',
        'start_time': 'start_time',
        'status': 'status',
        'vault_id': 'vault_id',
        'enterprise_project_id': 'enterprise_project_id',
        'own_type': 'own_type',
        'member_status': 'member_status',
        'parent_id': 'parent_id',
        'used_percent': 'used_percent'
    }

    def __init__(self, checkpoint_id=None, dec=None, end_time=None, image_type=None, limit=None, marker=None, name=None, offset=None, resource_az=None, resource_id=None, resource_name=None, resource_type=None, sort=None, start_time=None, status=None, vault_id=None, enterprise_project_id=None, own_type='private', member_status=None, parent_id=None, used_percent=None):
        """ListBackupsRequest - a model defined in huaweicloud sdk"""
        
        

        self._checkpoint_id = None
        self._dec = None
        self._end_time = None
        self._image_type = None
        self._limit = None
        self._marker = None
        self._name = None
        self._offset = None
        self._resource_az = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._sort = None
        self._start_time = None
        self._status = None
        self._vault_id = None
        self._enterprise_project_id = None
        self._own_type = None
        self._member_status = None
        self._parent_id = None
        self._used_percent = None
        self.discriminator = None

        if checkpoint_id is not None:
            self.checkpoint_id = checkpoint_id
        if dec is not None:
            self.dec = dec
        if end_time is not None:
            self.end_time = end_time
        if image_type is not None:
            self.image_type = image_type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if resource_az is not None:
            self.resource_az = resource_az
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if sort is not None:
            self.sort = sort
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if vault_id is not None:
            self.vault_id = vault_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if own_type is not None:
            self.own_type = own_type
        if member_status is not None:
            self.member_status = member_status
        if parent_id is not None:
            self.parent_id = parent_id
        if used_percent is not None:
            self.used_percent = used_percent

    @property
    def checkpoint_id(self):
        """Gets the checkpoint_id of this ListBackupsRequest.


        :return: The checkpoint_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        """Sets the checkpoint_id of this ListBackupsRequest.


        :param checkpoint_id: The checkpoint_id of this ListBackupsRequest.
        :type: str
        """
        self._checkpoint_id = checkpoint_id

    @property
    def dec(self):
        """Gets the dec of this ListBackupsRequest.


        :return: The dec of this ListBackupsRequest.
        :rtype: bool
        """
        return self._dec

    @dec.setter
    def dec(self, dec):
        """Sets the dec of this ListBackupsRequest.


        :param dec: The dec of this ListBackupsRequest.
        :type: bool
        """
        self._dec = dec

    @property
    def end_time(self):
        """Gets the end_time of this ListBackupsRequest.


        :return: The end_time of this ListBackupsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListBackupsRequest.


        :param end_time: The end_time of this ListBackupsRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def image_type(self):
        """Gets the image_type of this ListBackupsRequest.


        :return: The image_type of this ListBackupsRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ListBackupsRequest.


        :param image_type: The image_type of this ListBackupsRequest.
        :type: str
        """
        self._image_type = image_type

    @property
    def limit(self):
        """Gets the limit of this ListBackupsRequest.


        :return: The limit of this ListBackupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBackupsRequest.


        :param limit: The limit of this ListBackupsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListBackupsRequest.


        :return: The marker of this ListBackupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListBackupsRequest.


        :param marker: The marker of this ListBackupsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListBackupsRequest.


        :return: The name of this ListBackupsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListBackupsRequest.


        :param name: The name of this ListBackupsRequest.
        :type: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListBackupsRequest.


        :return: The offset of this ListBackupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBackupsRequest.


        :param offset: The offset of this ListBackupsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def resource_az(self):
        """Gets the resource_az of this ListBackupsRequest.


        :return: The resource_az of this ListBackupsRequest.
        :rtype: str
        """
        return self._resource_az

    @resource_az.setter
    def resource_az(self, resource_az):
        """Sets the resource_az of this ListBackupsRequest.


        :param resource_az: The resource_az of this ListBackupsRequest.
        :type: str
        """
        self._resource_az = resource_az

    @property
    def resource_id(self):
        """Gets the resource_id of this ListBackupsRequest.


        :return: The resource_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListBackupsRequest.


        :param resource_id: The resource_id of this ListBackupsRequest.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ListBackupsRequest.


        :return: The resource_name of this ListBackupsRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListBackupsRequest.


        :param resource_name: The resource_name of this ListBackupsRequest.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this ListBackupsRequest.


        :return: The resource_type of this ListBackupsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListBackupsRequest.


        :param resource_type: The resource_type of this ListBackupsRequest.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def sort(self):
        """Gets the sort of this ListBackupsRequest.


        :return: The sort of this ListBackupsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListBackupsRequest.


        :param sort: The sort of this ListBackupsRequest.
        :type: str
        """
        self._sort = sort

    @property
    def start_time(self):
        """Gets the start_time of this ListBackupsRequest.


        :return: The start_time of this ListBackupsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListBackupsRequest.


        :param start_time: The start_time of this ListBackupsRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this ListBackupsRequest.


        :return: The status of this ListBackupsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListBackupsRequest.


        :param status: The status of this ListBackupsRequest.
        :type: str
        """
        self._status = status

    @property
    def vault_id(self):
        """Gets the vault_id of this ListBackupsRequest.


        :return: The vault_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this ListBackupsRequest.


        :param vault_id: The vault_id of this ListBackupsRequest.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListBackupsRequest.


        :return: The enterprise_project_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListBackupsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListBackupsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def own_type(self):
        """Gets the own_type of this ListBackupsRequest.


        :return: The own_type of this ListBackupsRequest.
        :rtype: str
        """
        return self._own_type

    @own_type.setter
    def own_type(self, own_type):
        """Sets the own_type of this ListBackupsRequest.


        :param own_type: The own_type of this ListBackupsRequest.
        :type: str
        """
        self._own_type = own_type

    @property
    def member_status(self):
        """Gets the member_status of this ListBackupsRequest.


        :return: The member_status of this ListBackupsRequest.
        :rtype: str
        """
        return self._member_status

    @member_status.setter
    def member_status(self, member_status):
        """Sets the member_status of this ListBackupsRequest.


        :param member_status: The member_status of this ListBackupsRequest.
        :type: str
        """
        self._member_status = member_status

    @property
    def parent_id(self):
        """Gets the parent_id of this ListBackupsRequest.


        :return: The parent_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ListBackupsRequest.


        :param parent_id: The parent_id of this ListBackupsRequest.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def used_percent(self):
        """Gets the used_percent of this ListBackupsRequest.


        :return: The used_percent of this ListBackupsRequest.
        :rtype: str
        """
        return self._used_percent

    @used_percent.setter
    def used_percent(self, used_percent):
        """Sets the used_percent of this ListBackupsRequest.


        :param used_percent: The used_percent of this ListBackupsRequest.
        :type: str
        """
        self._used_percent = used_percent

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
        if not isinstance(other, ListBackupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
