# coding: utf-8

import pprint
import re

import six





class ListTagsRequest:


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
        'page': 'int',
        'imagetype': 'str',
        'id': 'str',
        'status': 'str',
        'name': 'str',
        'min_disk': 'int',
        'platform': 'str',
        'os_type': 'str',
        'member_status': 'str',
        'virtual_env_type': 'str',
        'enterprise_project_id': 'str',
        'architecture': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'page': 'page',
        'imagetype': '__imagetype',
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'min_disk': 'min_disk',
        'platform': '__platform',
        'os_type': '__os_type',
        'member_status': 'member_status',
        'virtual_env_type': 'virtual_env_type',
        'enterprise_project_id': 'enterprise_project_id',
        'architecture': 'architecture',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, limit=None, page=1, imagetype=None, id=None, status=None, name=None, min_disk=None, platform=None, os_type=None, member_status=None, virtual_env_type=None, enterprise_project_id=None, architecture=None, created_at=None, updated_at=None):
        """ListTagsRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._page = None
        self._imagetype = None
        self._id = None
        self._status = None
        self._name = None
        self._min_disk = None
        self._platform = None
        self._os_type = None
        self._member_status = None
        self._virtual_env_type = None
        self._enterprise_project_id = None
        self._architecture = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if page is not None:
            self.page = page
        if imagetype is not None:
            self.imagetype = imagetype
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if min_disk is not None:
            self.min_disk = min_disk
        if platform is not None:
            self.platform = platform
        if os_type is not None:
            self.os_type = os_type
        if member_status is not None:
            self.member_status = member_status
        if virtual_env_type is not None:
            self.virtual_env_type = virtual_env_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if architecture is not None:
            self.architecture = architecture
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def limit(self):
        """Gets the limit of this ListTagsRequest.


        :return: The limit of this ListTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTagsRequest.


        :param limit: The limit of this ListTagsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def page(self):
        """Gets the page of this ListTagsRequest.


        :return: The page of this ListTagsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListTagsRequest.


        :param page: The page of this ListTagsRequest.
        :type: int
        """
        self._page = page

    @property
    def imagetype(self):
        """Gets the imagetype of this ListTagsRequest.


        :return: The imagetype of this ListTagsRequest.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        """Sets the imagetype of this ListTagsRequest.


        :param imagetype: The imagetype of this ListTagsRequest.
        :type: str
        """
        self._imagetype = imagetype

    @property
    def id(self):
        """Gets the id of this ListTagsRequest.


        :return: The id of this ListTagsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListTagsRequest.


        :param id: The id of this ListTagsRequest.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ListTagsRequest.


        :return: The status of this ListTagsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListTagsRequest.


        :param status: The status of this ListTagsRequest.
        :type: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this ListTagsRequest.


        :return: The name of this ListTagsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTagsRequest.


        :param name: The name of this ListTagsRequest.
        :type: str
        """
        self._name = name

    @property
    def min_disk(self):
        """Gets the min_disk of this ListTagsRequest.


        :return: The min_disk of this ListTagsRequest.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this ListTagsRequest.


        :param min_disk: The min_disk of this ListTagsRequest.
        :type: int
        """
        self._min_disk = min_disk

    @property
    def platform(self):
        """Gets the platform of this ListTagsRequest.


        :return: The platform of this ListTagsRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ListTagsRequest.


        :param platform: The platform of this ListTagsRequest.
        :type: str
        """
        self._platform = platform

    @property
    def os_type(self):
        """Gets the os_type of this ListTagsRequest.


        :return: The os_type of this ListTagsRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListTagsRequest.


        :param os_type: The os_type of this ListTagsRequest.
        :type: str
        """
        self._os_type = os_type

    @property
    def member_status(self):
        """Gets the member_status of this ListTagsRequest.


        :return: The member_status of this ListTagsRequest.
        :rtype: str
        """
        return self._member_status

    @member_status.setter
    def member_status(self, member_status):
        """Sets the member_status of this ListTagsRequest.


        :param member_status: The member_status of this ListTagsRequest.
        :type: str
        """
        self._member_status = member_status

    @property
    def virtual_env_type(self):
        """Gets the virtual_env_type of this ListTagsRequest.


        :return: The virtual_env_type of this ListTagsRequest.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        """Sets the virtual_env_type of this ListTagsRequest.


        :param virtual_env_type: The virtual_env_type of this ListTagsRequest.
        :type: str
        """
        self._virtual_env_type = virtual_env_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListTagsRequest.


        :return: The enterprise_project_id of this ListTagsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListTagsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListTagsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def architecture(self):
        """Gets the architecture of this ListTagsRequest.


        :return: The architecture of this ListTagsRequest.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ListTagsRequest.


        :param architecture: The architecture of this ListTagsRequest.
        :type: str
        """
        self._architecture = architecture

    @property
    def created_at(self):
        """Gets the created_at of this ListTagsRequest.


        :return: The created_at of this ListTagsRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListTagsRequest.


        :param created_at: The created_at of this ListTagsRequest.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ListTagsRequest.


        :return: The updated_at of this ListTagsRequest.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListTagsRequest.


        :param updated_at: The updated_at of this ListTagsRequest.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
