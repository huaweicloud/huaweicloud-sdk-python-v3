# coding: utf-8

import pprint
import re

import six





class OpExtendInfoReplication:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'destination_backup_id': 'str',
        'destination_checkpoint_id': 'str',
        'destination_project_id': 'str',
        'destination_region': 'str',
        'source_backup_id': 'str',
        'source_checkpoint_id': 'str',
        'source_project_id': 'str',
        'source_region': 'str',
        'source_backup_name': 'str',
        'destination_backup_name': 'str'
    }

    attribute_map = {
        'destination_backup_id': 'destination_backup_id',
        'destination_checkpoint_id': 'destination_checkpoint_id',
        'destination_project_id': 'destination_project_id',
        'destination_region': 'destination_region',
        'source_backup_id': 'source_backup_id',
        'source_checkpoint_id': 'source_checkpoint_id',
        'source_project_id': 'source_project_id',
        'source_region': 'source_region',
        'source_backup_name': 'source_backup_name',
        'destination_backup_name': 'destination_backup_name'
    }

    def __init__(self, destination_backup_id=None, destination_checkpoint_id=None, destination_project_id=None, destination_region=None, source_backup_id=None, source_checkpoint_id=None, source_project_id=None, source_region=None, source_backup_name=None, destination_backup_name=None):
        """OpExtendInfoReplication - a model defined in huaweicloud sdk"""
        
        

        self._destination_backup_id = None
        self._destination_checkpoint_id = None
        self._destination_project_id = None
        self._destination_region = None
        self._source_backup_id = None
        self._source_checkpoint_id = None
        self._source_project_id = None
        self._source_region = None
        self._source_backup_name = None
        self._destination_backup_name = None
        self.discriminator = None

        if destination_backup_id is not None:
            self.destination_backup_id = destination_backup_id
        if destination_checkpoint_id is not None:
            self.destination_checkpoint_id = destination_checkpoint_id
        self.destination_project_id = destination_project_id
        self.destination_region = destination_region
        self.source_backup_id = source_backup_id
        if source_checkpoint_id is not None:
            self.source_checkpoint_id = source_checkpoint_id
        self.source_project_id = source_project_id
        self.source_region = source_region
        if source_backup_name is not None:
            self.source_backup_name = source_backup_name
        if destination_backup_name is not None:
            self.destination_backup_name = destination_backup_name

    @property
    def destination_backup_id(self):
        """Gets the destination_backup_id of this OpExtendInfoReplication.

        目标副本ID

        :return: The destination_backup_id of this OpExtendInfoReplication.
        :rtype: str
        """
        return self._destination_backup_id

    @destination_backup_id.setter
    def destination_backup_id(self, destination_backup_id):
        """Sets the destination_backup_id of this OpExtendInfoReplication.

        目标副本ID

        :param destination_backup_id: The destination_backup_id of this OpExtendInfoReplication.
        :type: str
        """
        self._destination_backup_id = destination_backup_id

    @property
    def destination_checkpoint_id(self):
        """Gets the destination_checkpoint_id of this OpExtendInfoReplication.

        目标还原点ID

        :return: The destination_checkpoint_id of this OpExtendInfoReplication.
        :rtype: str
        """
        return self._destination_checkpoint_id

    @destination_checkpoint_id.setter
    def destination_checkpoint_id(self, destination_checkpoint_id):
        """Sets the destination_checkpoint_id of this OpExtendInfoReplication.

        目标还原点ID

        :param destination_checkpoint_id: The destination_checkpoint_id of this OpExtendInfoReplication.
        :type: str
        """
        self._destination_checkpoint_id = destination_checkpoint_id

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this OpExtendInfoReplication.

        目标project_id

        :return: The destination_project_id of this OpExtendInfoReplication.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this OpExtendInfoReplication.

        目标project_id

        :param destination_project_id: The destination_project_id of this OpExtendInfoReplication.
        :type: str
        """
        self._destination_project_id = destination_project_id

    @property
    def destination_region(self):
        """Gets the destination_region of this OpExtendInfoReplication.

        目标区域

        :return: The destination_region of this OpExtendInfoReplication.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this OpExtendInfoReplication.

        目标区域

        :param destination_region: The destination_region of this OpExtendInfoReplication.
        :type: str
        """
        self._destination_region = destination_region

    @property
    def source_backup_id(self):
        """Gets the source_backup_id of this OpExtendInfoReplication.

        源副本ID

        :return: The source_backup_id of this OpExtendInfoReplication.
        :rtype: str
        """
        return self._source_backup_id

    @source_backup_id.setter
    def source_backup_id(self, source_backup_id):
        """Sets the source_backup_id of this OpExtendInfoReplication.

        源副本ID

        :param source_backup_id: The source_backup_id of this OpExtendInfoReplication.
        :type: str
        """
        self._source_backup_id = source_backup_id

    @property
    def source_checkpoint_id(self):
        """Gets the source_checkpoint_id of this OpExtendInfoReplication.

        源还原点ID

        :return: The source_checkpoint_id of this OpExtendInfoReplication.
        :rtype: str
        """
        return self._source_checkpoint_id

    @source_checkpoint_id.setter
    def source_checkpoint_id(self, source_checkpoint_id):
        """Sets the source_checkpoint_id of this OpExtendInfoReplication.

        源还原点ID

        :param source_checkpoint_id: The source_checkpoint_id of this OpExtendInfoReplication.
        :type: str
        """
        self._source_checkpoint_id = source_checkpoint_id

    @property
    def source_project_id(self):
        """Gets the source_project_id of this OpExtendInfoReplication.

        源project_id

        :return: The source_project_id of this OpExtendInfoReplication.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this OpExtendInfoReplication.

        源project_id

        :param source_project_id: The source_project_id of this OpExtendInfoReplication.
        :type: str
        """
        self._source_project_id = source_project_id

    @property
    def source_region(self):
        """Gets the source_region of this OpExtendInfoReplication.

        源区域

        :return: The source_region of this OpExtendInfoReplication.
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        """Sets the source_region of this OpExtendInfoReplication.

        源区域

        :param source_region: The source_region of this OpExtendInfoReplication.
        :type: str
        """
        self._source_region = source_region

    @property
    def source_backup_name(self):
        """Gets the source_backup_name of this OpExtendInfoReplication.

        源备份名称

        :return: The source_backup_name of this OpExtendInfoReplication.
        :rtype: str
        """
        return self._source_backup_name

    @source_backup_name.setter
    def source_backup_name(self, source_backup_name):
        """Sets the source_backup_name of this OpExtendInfoReplication.

        源备份名称

        :param source_backup_name: The source_backup_name of this OpExtendInfoReplication.
        :type: str
        """
        self._source_backup_name = source_backup_name

    @property
    def destination_backup_name(self):
        """Gets the destination_backup_name of this OpExtendInfoReplication.

        目标备份名称

        :return: The destination_backup_name of this OpExtendInfoReplication.
        :rtype: str
        """
        return self._destination_backup_name

    @destination_backup_name.setter
    def destination_backup_name(self, destination_backup_name):
        """Sets the destination_backup_name of this OpExtendInfoReplication.

        目标备份名称

        :param destination_backup_name: The destination_backup_name of this OpExtendInfoReplication.
        :type: str
        """
        self._destination_backup_name = destination_backup_name

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
        if not isinstance(other, OpExtendInfoReplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
