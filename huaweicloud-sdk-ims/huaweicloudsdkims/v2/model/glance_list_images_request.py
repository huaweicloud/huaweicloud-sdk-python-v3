# coding: utf-8

import pprint
import re

import six





class GlanceListImagesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'imagetype': 'str',
        'isregistered': 'bool',
        'os_bit': 'str',
        'os_type': 'str',
        'platform': 'str',
        'support_diskintensive': 'str',
        'support_highperformance': 'str',
        'support_kvm': 'str',
        'support_kvm_gpu_type': 'str',
        'support_kvm_infiniband': 'str',
        'support_largememory': 'str',
        'support_xen': 'str',
        'support_xen_gpu_type': 'str',
        'support_xen_hana': 'str',
        'container_format': 'str',
        'disk_format': 'str',
        'id': 'str',
        'limit': 'int',
        'marker': 'str',
        'member_status': 'str',
        'min_disk': 'int',
        'min_ram': 'int',
        'name': 'str',
        'owner': 'str',
        'protected': 'bool',
        'sort_dir': 'str',
        'sort_key': 'str',
        'status': 'str',
        'tag': 'str',
        'visibility': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'imagetype': '__imagetype',
        'isregistered': '__isregistered',
        'os_bit': '__os_bit',
        'os_type': '__os_type',
        'platform': '__platform',
        'support_diskintensive': '__support_diskintensive',
        'support_highperformance': '__support_highperformance',
        'support_kvm': '__support_kvm',
        'support_kvm_gpu_type': '__support_kvm_gpu_type',
        'support_kvm_infiniband': '__support_kvm_infiniband',
        'support_largememory': '__support_largememory',
        'support_xen': '__support_xen',
        'support_xen_gpu_type': '__support_xen_gpu_type',
        'support_xen_hana': '__support_xen_hana',
        'container_format': 'container_format',
        'disk_format': 'disk_format',
        'id': 'id',
        'limit': 'limit',
        'marker': 'marker',
        'member_status': 'member_status',
        'min_disk': 'min_disk',
        'min_ram': 'min_ram',
        'name': 'name',
        'owner': 'owner',
        'protected': 'protected',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'status': 'status',
        'tag': 'tag',
        'visibility': 'visibility',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, imagetype=None, isregistered=True, os_bit=None, os_type=None, platform=None, support_diskintensive=None, support_highperformance=None, support_kvm=None, support_kvm_gpu_type=None, support_kvm_infiniband=None, support_largememory=None, support_xen=None, support_xen_gpu_type=None, support_xen_hana=None, container_format='bare', disk_format='vhd', id=None, limit=25, marker=None, member_status=None, min_disk=None, min_ram=None, name=None, owner=None, protected=None, sort_dir=None, sort_key=None, status=None, tag=None, visibility=None, created_at=None, updated_at=None):
        """GlanceListImagesRequest - a model defined in huaweicloud sdk"""
        
        

        self._imagetype = None
        self._isregistered = None
        self._os_bit = None
        self._os_type = None
        self._platform = None
        self._support_diskintensive = None
        self._support_highperformance = None
        self._support_kvm = None
        self._support_kvm_gpu_type = None
        self._support_kvm_infiniband = None
        self._support_largememory = None
        self._support_xen = None
        self._support_xen_gpu_type = None
        self._support_xen_hana = None
        self._container_format = None
        self._disk_format = None
        self._id = None
        self._limit = None
        self._marker = None
        self._member_status = None
        self._min_disk = None
        self._min_ram = None
        self._name = None
        self._owner = None
        self._protected = None
        self._sort_dir = None
        self._sort_key = None
        self._status = None
        self._tag = None
        self._visibility = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if imagetype is not None:
            self.imagetype = imagetype
        if isregistered is not None:
            self.isregistered = isregistered
        if os_bit is not None:
            self.os_bit = os_bit
        if os_type is not None:
            self.os_type = os_type
        if platform is not None:
            self.platform = platform
        if support_diskintensive is not None:
            self.support_diskintensive = support_diskintensive
        if support_highperformance is not None:
            self.support_highperformance = support_highperformance
        if support_kvm is not None:
            self.support_kvm = support_kvm
        if support_kvm_gpu_type is not None:
            self.support_kvm_gpu_type = support_kvm_gpu_type
        if support_kvm_infiniband is not None:
            self.support_kvm_infiniband = support_kvm_infiniband
        if support_largememory is not None:
            self.support_largememory = support_largememory
        if support_xen is not None:
            self.support_xen = support_xen
        if support_xen_gpu_type is not None:
            self.support_xen_gpu_type = support_xen_gpu_type
        if support_xen_hana is not None:
            self.support_xen_hana = support_xen_hana
        if container_format is not None:
            self.container_format = container_format
        if disk_format is not None:
            self.disk_format = disk_format
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if member_status is not None:
            self.member_status = member_status
        if min_disk is not None:
            self.min_disk = min_disk
        if min_ram is not None:
            self.min_ram = min_ram
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if protected is not None:
            self.protected = protected
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status
        if tag is not None:
            self.tag = tag
        if visibility is not None:
            self.visibility = visibility
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def imagetype(self):
        """Gets the imagetype of this GlanceListImagesRequest.


        :return: The imagetype of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        """Sets the imagetype of this GlanceListImagesRequest.


        :param imagetype: The imagetype of this GlanceListImagesRequest.
        :type: str
        """
        self._imagetype = imagetype

    @property
    def isregistered(self):
        """Gets the isregistered of this GlanceListImagesRequest.


        :return: The isregistered of this GlanceListImagesRequest.
        :rtype: bool
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        """Sets the isregistered of this GlanceListImagesRequest.


        :param isregistered: The isregistered of this GlanceListImagesRequest.
        :type: bool
        """
        self._isregistered = isregistered

    @property
    def os_bit(self):
        """Gets the os_bit of this GlanceListImagesRequest.


        :return: The os_bit of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        """Sets the os_bit of this GlanceListImagesRequest.


        :param os_bit: The os_bit of this GlanceListImagesRequest.
        :type: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        """Gets the os_type of this GlanceListImagesRequest.


        :return: The os_type of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this GlanceListImagesRequest.


        :param os_type: The os_type of this GlanceListImagesRequest.
        :type: str
        """
        self._os_type = os_type

    @property
    def platform(self):
        """Gets the platform of this GlanceListImagesRequest.


        :return: The platform of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this GlanceListImagesRequest.


        :param platform: The platform of this GlanceListImagesRequest.
        :type: str
        """
        self._platform = platform

    @property
    def support_diskintensive(self):
        """Gets the support_diskintensive of this GlanceListImagesRequest.


        :return: The support_diskintensive of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._support_diskintensive

    @support_diskintensive.setter
    def support_diskintensive(self, support_diskintensive):
        """Sets the support_diskintensive of this GlanceListImagesRequest.


        :param support_diskintensive: The support_diskintensive of this GlanceListImagesRequest.
        :type: str
        """
        self._support_diskintensive = support_diskintensive

    @property
    def support_highperformance(self):
        """Gets the support_highperformance of this GlanceListImagesRequest.


        :return: The support_highperformance of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._support_highperformance

    @support_highperformance.setter
    def support_highperformance(self, support_highperformance):
        """Sets the support_highperformance of this GlanceListImagesRequest.


        :param support_highperformance: The support_highperformance of this GlanceListImagesRequest.
        :type: str
        """
        self._support_highperformance = support_highperformance

    @property
    def support_kvm(self):
        """Gets the support_kvm of this GlanceListImagesRequest.


        :return: The support_kvm of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._support_kvm

    @support_kvm.setter
    def support_kvm(self, support_kvm):
        """Sets the support_kvm of this GlanceListImagesRequest.


        :param support_kvm: The support_kvm of this GlanceListImagesRequest.
        :type: str
        """
        self._support_kvm = support_kvm

    @property
    def support_kvm_gpu_type(self):
        """Gets the support_kvm_gpu_type of this GlanceListImagesRequest.


        :return: The support_kvm_gpu_type of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._support_kvm_gpu_type

    @support_kvm_gpu_type.setter
    def support_kvm_gpu_type(self, support_kvm_gpu_type):
        """Sets the support_kvm_gpu_type of this GlanceListImagesRequest.


        :param support_kvm_gpu_type: The support_kvm_gpu_type of this GlanceListImagesRequest.
        :type: str
        """
        self._support_kvm_gpu_type = support_kvm_gpu_type

    @property
    def support_kvm_infiniband(self):
        """Gets the support_kvm_infiniband of this GlanceListImagesRequest.


        :return: The support_kvm_infiniband of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._support_kvm_infiniband

    @support_kvm_infiniband.setter
    def support_kvm_infiniband(self, support_kvm_infiniband):
        """Sets the support_kvm_infiniband of this GlanceListImagesRequest.


        :param support_kvm_infiniband: The support_kvm_infiniband of this GlanceListImagesRequest.
        :type: str
        """
        self._support_kvm_infiniband = support_kvm_infiniband

    @property
    def support_largememory(self):
        """Gets the support_largememory of this GlanceListImagesRequest.


        :return: The support_largememory of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._support_largememory

    @support_largememory.setter
    def support_largememory(self, support_largememory):
        """Sets the support_largememory of this GlanceListImagesRequest.


        :param support_largememory: The support_largememory of this GlanceListImagesRequest.
        :type: str
        """
        self._support_largememory = support_largememory

    @property
    def support_xen(self):
        """Gets the support_xen of this GlanceListImagesRequest.


        :return: The support_xen of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._support_xen

    @support_xen.setter
    def support_xen(self, support_xen):
        """Sets the support_xen of this GlanceListImagesRequest.


        :param support_xen: The support_xen of this GlanceListImagesRequest.
        :type: str
        """
        self._support_xen = support_xen

    @property
    def support_xen_gpu_type(self):
        """Gets the support_xen_gpu_type of this GlanceListImagesRequest.


        :return: The support_xen_gpu_type of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._support_xen_gpu_type

    @support_xen_gpu_type.setter
    def support_xen_gpu_type(self, support_xen_gpu_type):
        """Sets the support_xen_gpu_type of this GlanceListImagesRequest.


        :param support_xen_gpu_type: The support_xen_gpu_type of this GlanceListImagesRequest.
        :type: str
        """
        self._support_xen_gpu_type = support_xen_gpu_type

    @property
    def support_xen_hana(self):
        """Gets the support_xen_hana of this GlanceListImagesRequest.


        :return: The support_xen_hana of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._support_xen_hana

    @support_xen_hana.setter
    def support_xen_hana(self, support_xen_hana):
        """Sets the support_xen_hana of this GlanceListImagesRequest.


        :param support_xen_hana: The support_xen_hana of this GlanceListImagesRequest.
        :type: str
        """
        self._support_xen_hana = support_xen_hana

    @property
    def container_format(self):
        """Gets the container_format of this GlanceListImagesRequest.


        :return: The container_format of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        """Sets the container_format of this GlanceListImagesRequest.


        :param container_format: The container_format of this GlanceListImagesRequest.
        :type: str
        """
        self._container_format = container_format

    @property
    def disk_format(self):
        """Gets the disk_format of this GlanceListImagesRequest.


        :return: The disk_format of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        """Sets the disk_format of this GlanceListImagesRequest.


        :param disk_format: The disk_format of this GlanceListImagesRequest.
        :type: str
        """
        self._disk_format = disk_format

    @property
    def id(self):
        """Gets the id of this GlanceListImagesRequest.


        :return: The id of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlanceListImagesRequest.


        :param id: The id of this GlanceListImagesRequest.
        :type: str
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this GlanceListImagesRequest.


        :return: The limit of this GlanceListImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GlanceListImagesRequest.


        :param limit: The limit of this GlanceListImagesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this GlanceListImagesRequest.


        :return: The marker of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this GlanceListImagesRequest.


        :param marker: The marker of this GlanceListImagesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def member_status(self):
        """Gets the member_status of this GlanceListImagesRequest.


        :return: The member_status of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._member_status

    @member_status.setter
    def member_status(self, member_status):
        """Sets the member_status of this GlanceListImagesRequest.


        :param member_status: The member_status of this GlanceListImagesRequest.
        :type: str
        """
        self._member_status = member_status

    @property
    def min_disk(self):
        """Gets the min_disk of this GlanceListImagesRequest.


        :return: The min_disk of this GlanceListImagesRequest.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this GlanceListImagesRequest.


        :param min_disk: The min_disk of this GlanceListImagesRequest.
        :type: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        """Gets the min_ram of this GlanceListImagesRequest.


        :return: The min_ram of this GlanceListImagesRequest.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this GlanceListImagesRequest.


        :param min_ram: The min_ram of this GlanceListImagesRequest.
        :type: int
        """
        self._min_ram = min_ram

    @property
    def name(self):
        """Gets the name of this GlanceListImagesRequest.


        :return: The name of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlanceListImagesRequest.


        :param name: The name of this GlanceListImagesRequest.
        :type: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this GlanceListImagesRequest.


        :return: The owner of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this GlanceListImagesRequest.


        :param owner: The owner of this GlanceListImagesRequest.
        :type: str
        """
        self._owner = owner

    @property
    def protected(self):
        """Gets the protected of this GlanceListImagesRequest.


        :return: The protected of this GlanceListImagesRequest.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this GlanceListImagesRequest.


        :param protected: The protected of this GlanceListImagesRequest.
        :type: bool
        """
        self._protected = protected

    @property
    def sort_dir(self):
        """Gets the sort_dir of this GlanceListImagesRequest.


        :return: The sort_dir of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this GlanceListImagesRequest.


        :param sort_dir: The sort_dir of this GlanceListImagesRequest.
        :type: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this GlanceListImagesRequest.


        :return: The sort_key of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this GlanceListImagesRequest.


        :param sort_key: The sort_key of this GlanceListImagesRequest.
        :type: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        """Gets the status of this GlanceListImagesRequest.


        :return: The status of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GlanceListImagesRequest.


        :param status: The status of this GlanceListImagesRequest.
        :type: str
        """
        self._status = status

    @property
    def tag(self):
        """Gets the tag of this GlanceListImagesRequest.


        :return: The tag of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this GlanceListImagesRequest.


        :param tag: The tag of this GlanceListImagesRequest.
        :type: str
        """
        self._tag = tag

    @property
    def visibility(self):
        """Gets the visibility of this GlanceListImagesRequest.


        :return: The visibility of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this GlanceListImagesRequest.


        :param visibility: The visibility of this GlanceListImagesRequest.
        :type: str
        """
        self._visibility = visibility

    @property
    def created_at(self):
        """Gets the created_at of this GlanceListImagesRequest.


        :return: The created_at of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GlanceListImagesRequest.


        :param created_at: The created_at of this GlanceListImagesRequest.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GlanceListImagesRequest.


        :return: The updated_at of this GlanceListImagesRequest.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GlanceListImagesRequest.


        :param updated_at: The updated_at of this GlanceListImagesRequest.
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
        if not isinstance(other, GlanceListImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
