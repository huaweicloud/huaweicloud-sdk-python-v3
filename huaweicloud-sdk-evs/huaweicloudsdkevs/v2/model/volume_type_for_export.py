# coding: utf-8

import pprint
import re

import six


class VolumeTypeForExport(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'is_public': 'bool',
        'extra_specs': 'VolumeTypeExtraSpecs',
        'description': 'str',
        'qos_specs_id': 'str',
        'deleted': 'bool',
        'deleted_at': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_public': 'is_public',
        'extra_specs': 'extra_specs',
        'description': 'description',
        'qos_specs_id': 'qos_specs_id',
        'deleted': 'deleted',
        'deleted_at': 'deleted_at',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, is_public=None, extra_specs=None, description=None, qos_specs_id=None, deleted=None, deleted_at=None, created_at=None, updated_at=None):  # noqa: E501
        """VolumeTypeForExport - a model defined in huaweicloud sdk"""

        self._id = None
        self._name = None
        self._is_public = None
        self._extra_specs = None
        self._description = None
        self._qos_specs_id = None
        self._deleted = None
        self._deleted_at = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        if is_public is not None:
            self.is_public = is_public
        if extra_specs is not None:
            self.extra_specs = extra_specs
        if description is not None:
            self.description = description
        if qos_specs_id is not None:
            self.qos_specs_id = qos_specs_id
        if deleted is not None:
            self.deleted = deleted
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this VolumeTypeForExport.

        云硬盘类型的ID。

        :return: The id of this VolumeTypeForExport.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeTypeForExport.

        云硬盘类型的ID。

        :param id: The id of this VolumeTypeForExport.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VolumeTypeForExport.

        云硬盘类型名称。

        :return: The name of this VolumeTypeForExport.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeTypeForExport.

        云硬盘类型名称。

        :param name: The name of this VolumeTypeForExport.
        :type: str
        """
        self._name = name

    @property
    def is_public(self):
        """Gets the is_public of this VolumeTypeForExport.

        预留属性。

        :return: The is_public of this VolumeTypeForExport.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this VolumeTypeForExport.

        预留属性。

        :param is_public: The is_public of this VolumeTypeForExport.
        :type: bool
        """
        self._is_public = is_public

    @property
    def extra_specs(self):
        """Gets the extra_specs of this VolumeTypeForExport.


        :return: The extra_specs of this VolumeTypeForExport.
        :rtype: VolumeTypeExtraSpecs
        """
        return self._extra_specs

    @extra_specs.setter
    def extra_specs(self, extra_specs):
        """Sets the extra_specs of this VolumeTypeForExport.


        :param extra_specs: The extra_specs of this VolumeTypeForExport.
        :type: VolumeTypeExtraSpecs
        """
        self._extra_specs = extra_specs

    @property
    def description(self):
        """Gets the description of this VolumeTypeForExport.

        云硬盘类型的描述信息。

        :return: The description of this VolumeTypeForExport.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VolumeTypeForExport.

        云硬盘类型的描述信息。

        :param description: The description of this VolumeTypeForExport.
        :type: str
        """
        self._description = description

    @property
    def qos_specs_id(self):
        """Gets the qos_specs_id of this VolumeTypeForExport.

        预留属性。

        :return: The qos_specs_id of this VolumeTypeForExport.
        :rtype: str
        """
        return self._qos_specs_id

    @qos_specs_id.setter
    def qos_specs_id(self, qos_specs_id):
        """Sets the qos_specs_id of this VolumeTypeForExport.

        预留属性。

        :param qos_specs_id: The qos_specs_id of this VolumeTypeForExport.
        :type: str
        """
        self._qos_specs_id = qos_specs_id

    @property
    def deleted(self):
        """Gets the deleted of this VolumeTypeForExport.

        云硬盘类型是否被删除标识。

        :return: The deleted of this VolumeTypeForExport.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this VolumeTypeForExport.

        云硬盘类型是否被删除标识。

        :param deleted: The deleted of this VolumeTypeForExport.
        :type: bool
        """
        self._deleted = deleted

    @property
    def deleted_at(self):
        """Gets the deleted_at of this VolumeTypeForExport.

        云硬盘类型的删除时间。

        :return: The deleted_at of this VolumeTypeForExport.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this VolumeTypeForExport.

        云硬盘类型的删除时间。

        :param deleted_at: The deleted_at of this VolumeTypeForExport.
        :type: str
        """
        self._deleted_at = deleted_at

    @property
    def created_at(self):
        """Gets the created_at of this VolumeTypeForExport.

        云硬盘类型的创建时间。

        :return: The created_at of this VolumeTypeForExport.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VolumeTypeForExport.

        云硬盘类型的创建时间。

        :param created_at: The created_at of this VolumeTypeForExport.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this VolumeTypeForExport.

        云硬盘类型的更新时间。

        :return: The updated_at of this VolumeTypeForExport.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VolumeTypeForExport.

        云硬盘类型的更新时间。

        :param updated_at: The updated_at of this VolumeTypeForExport.
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
        if not isinstance(other, VolumeTypeForExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
