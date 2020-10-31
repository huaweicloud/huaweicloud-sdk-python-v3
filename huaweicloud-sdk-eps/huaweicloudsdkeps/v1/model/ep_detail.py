# coding: utf-8

import pprint
import re

import six





class EpDetail:


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
        'name': 'str',
        'description': 'str',
        'status': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, description=None, status=None, created_at=None, updated_at=None, type=None):
        """EpDetail - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.type = type

    @property
    def id(self):
        """Gets the id of this EpDetail.

        企业项目ID

        :return: The id of this EpDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EpDetail.

        企业项目ID

        :param id: The id of this EpDetail.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EpDetail.

        企业项目名称

        :return: The name of this EpDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EpDetail.

        企业项目名称

        :param name: The name of this EpDetail.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EpDetail.

        企业项目描述

        :return: The description of this EpDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EpDetail.

        企业项目描述

        :param description: The description of this EpDetail.
        :type: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this EpDetail.

        企业项目状态。1启用，2停用

        :return: The status of this EpDetail.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EpDetail.

        企业项目状态。1启用，2停用

        :param status: The status of this EpDetail.
        :type: int
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this EpDetail.

        创建时间，格式为UTC格式。如：2018-05-18T06:49:06Z。

        :return: The created_at of this EpDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EpDetail.

        创建时间，格式为UTC格式。如：2018-05-18T06:49:06Z。

        :param created_at: The created_at of this EpDetail.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EpDetail.

        修改时间，格式为UTC格式。如：2018-05-28T02:21:36Z。

        :return: The updated_at of this EpDetail.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EpDetail.

        修改时间，格式为UTC格式。如：2018-05-28T02:21:36Z。

        :param updated_at: The updated_at of this EpDetail.
        :type: datetime
        """
        self._updated_at = updated_at

    @property
    def type(self):
        """Gets the type of this EpDetail.

        项目类型。prod-商用项目；poc-测试项目

        :return: The type of this EpDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EpDetail.

        项目类型。prod-商用项目；poc-测试项目

        :param type: The type of this EpDetail.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, EpDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
