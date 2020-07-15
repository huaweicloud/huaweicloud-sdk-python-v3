# coding: utf-8

import pprint
import re

import six





class QueryOrgVmrResultDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'vmr_id': 'str',
        'vmr_name': 'str',
        'vmr_pkg_name': 'str',
        'vmr_pkg_parties': 'int',
        'member': 'IdMarkDTO',
        'device': 'IdMarkDTO',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'vmr_id': 'vmrId',
        'vmr_name': 'vmrName',
        'vmr_pkg_name': 'vmrPkgName',
        'vmr_pkg_parties': 'vmrPkgParties',
        'member': 'member',
        'device': 'device',
        'status': 'status'
    }

    def __init__(self, id=None, vmr_id=None, vmr_name=None, vmr_pkg_name=None, vmr_pkg_parties=None, member=None, device=None, status=None):
        """QueryOrgVmrResultDTO - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._vmr_id = None
        self._vmr_name = None
        self._vmr_pkg_name = None
        self._vmr_pkg_parties = None
        self._member = None
        self._device = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vmr_id is not None:
            self.vmr_id = vmr_id
        if vmr_name is not None:
            self.vmr_name = vmr_name
        if vmr_pkg_name is not None:
            self.vmr_pkg_name = vmr_pkg_name
        if vmr_pkg_parties is not None:
            self.vmr_pkg_parties = vmr_pkg_parties
        if member is not None:
            self.member = member
        if device is not None:
            self.device = device
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this QueryOrgVmrResultDTO.

        唯一标识

        :return: The id of this QueryOrgVmrResultDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryOrgVmrResultDTO.

        唯一标识

        :param id: The id of this QueryOrgVmrResultDTO.
        :type: str
        """
        self._id = id

    @property
    def vmr_id(self):
        """Gets the vmr_id of this QueryOrgVmrResultDTO.

        云会议室ID。

        :return: The vmr_id of this QueryOrgVmrResultDTO.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this QueryOrgVmrResultDTO.

        云会议室ID。

        :param vmr_id: The vmr_id of this QueryOrgVmrResultDTO.
        :type: str
        """
        self._vmr_id = vmr_id

    @property
    def vmr_name(self):
        """Gets the vmr_name of this QueryOrgVmrResultDTO.

        云会议室名称。

        :return: The vmr_name of this QueryOrgVmrResultDTO.
        :rtype: str
        """
        return self._vmr_name

    @vmr_name.setter
    def vmr_name(self, vmr_name):
        """Sets the vmr_name of this QueryOrgVmrResultDTO.

        云会议室名称。

        :param vmr_name: The vmr_name of this QueryOrgVmrResultDTO.
        :type: str
        """
        self._vmr_name = vmr_name

    @property
    def vmr_pkg_name(self):
        """Gets the vmr_pkg_name of this QueryOrgVmrResultDTO.

        云会议室套餐名称。

        :return: The vmr_pkg_name of this QueryOrgVmrResultDTO.
        :rtype: str
        """
        return self._vmr_pkg_name

    @vmr_pkg_name.setter
    def vmr_pkg_name(self, vmr_pkg_name):
        """Sets the vmr_pkg_name of this QueryOrgVmrResultDTO.

        云会议室套餐名称。

        :param vmr_pkg_name: The vmr_pkg_name of this QueryOrgVmrResultDTO.
        :type: str
        """
        self._vmr_pkg_name = vmr_pkg_name

    @property
    def vmr_pkg_parties(self):
        """Gets the vmr_pkg_parties of this QueryOrgVmrResultDTO.

        云会议室套餐会议并发方数。

        :return: The vmr_pkg_parties of this QueryOrgVmrResultDTO.
        :rtype: int
        """
        return self._vmr_pkg_parties

    @vmr_pkg_parties.setter
    def vmr_pkg_parties(self, vmr_pkg_parties):
        """Sets the vmr_pkg_parties of this QueryOrgVmrResultDTO.

        云会议室套餐会议并发方数。

        :param vmr_pkg_parties: The vmr_pkg_parties of this QueryOrgVmrResultDTO.
        :type: int
        """
        self._vmr_pkg_parties = vmr_pkg_parties

    @property
    def member(self):
        """Gets the member of this QueryOrgVmrResultDTO.


        :return: The member of this QueryOrgVmrResultDTO.
        :rtype: IdMarkDTO
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this QueryOrgVmrResultDTO.


        :param member: The member of this QueryOrgVmrResultDTO.
        :type: IdMarkDTO
        """
        self._member = member

    @property
    def device(self):
        """Gets the device of this QueryOrgVmrResultDTO.


        :return: The device of this QueryOrgVmrResultDTO.
        :rtype: IdMarkDTO
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this QueryOrgVmrResultDTO.


        :param device: The device of this QueryOrgVmrResultDTO.
        :type: IdMarkDTO
        """
        self._device = device

    @property
    def status(self):
        """Gets the status of this QueryOrgVmrResultDTO.

        云会议室状态。 * 0：正常 * 1：冻结 * 2：未分配 

        :return: The status of this QueryOrgVmrResultDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryOrgVmrResultDTO.

        云会议室状态。 * 0：正常 * 1：冻结 * 2：未分配 

        :param status: The status of this QueryOrgVmrResultDTO.
        :type: int
        """
        self._status = status

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
        if not isinstance(other, QueryOrgVmrResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
