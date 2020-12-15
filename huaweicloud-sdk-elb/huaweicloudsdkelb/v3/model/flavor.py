# coding: utf-8

import pprint
import re

import six





class Flavor:


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
        'info': 'FlavorInfo',
        'name': 'str',
        'shared': 'bool',
        'project_id': 'str',
        'type': 'str',
        'availability_zone_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'info': 'info',
        'name': 'name',
        'shared': 'shared',
        'project_id': 'project_id',
        'type': 'type',
        'availability_zone_ids': 'availability_zone_ids'
    }

    def __init__(self, id=None, info=None, name=None, shared=None, project_id=None, type=None, availability_zone_ids=None):
        """Flavor - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._info = None
        self._name = None
        self._shared = None
        self._project_id = None
        self._type = None
        self._availability_zone_ids = None
        self.discriminator = None

        self.id = id
        self.info = info
        self.name = name
        self.shared = shared
        self.project_id = project_id
        self.type = type
        if availability_zone_ids is not None:
            self.availability_zone_ids = availability_zone_ids

    @property
    def id(self):
        """Gets the id of this Flavor.

        规格ID。

        :return: The id of this Flavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Flavor.

        规格ID。

        :param id: The id of this Flavor.
        :type: str
        """
        self._id = id

    @property
    def info(self):
        """Gets the info of this Flavor.


        :return: The info of this Flavor.
        :rtype: FlavorInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this Flavor.


        :param info: The info of this Flavor.
        :type: FlavorInfo
        """
        self._info = info

    @property
    def name(self):
        """Gets the name of this Flavor.

        规格名称。

        :return: The name of this Flavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Flavor.

        规格名称。

        :param name: The name of this Flavor.
        :type: str
        """
        self._name = name

    @property
    def shared(self):
        """Gets the shared of this Flavor.

        共享。

        :return: The shared of this Flavor.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this Flavor.

        共享。

        :param shared: The shared of this Flavor.
        :type: bool
        """
        self._shared = shared

    @property
    def project_id(self):
        """Gets the project_id of this Flavor.

        项目ID

        :return: The project_id of this Flavor.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Flavor.

        项目ID

        :param project_id: The project_id of this Flavor.
        :type: str
        """
        self._project_id = project_id

    @property
    def type(self):
        """Gets the type of this Flavor.

        L4和L7 分别表示四层和七层flavor。查询支持按type过滤

        :return: The type of this Flavor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Flavor.

        L4和L7 分别表示四层和七层flavor。查询支持按type过滤

        :param type: The type of this Flavor.
        :type: str
        """
        self._type = type

    @property
    def availability_zone_ids(self):
        """Gets the availability_zone_ids of this Flavor.

        availability_zone_ids字段，标志ELB对应L7-flavor在对应可用区是否可以售卖。 若该字段为[]代表该flavor不可售卖；若该字段为[\"ALL\"]，代表所有可用区可售卖；若仅部分可用区可售卖则返回[\"cn-north-1a\",\"cn-north-1b\"]。 可通过/v3/{project_id}/elb/availability-zones接口查询所有可售卖的可用区接口。

        :return: The availability_zone_ids of this Flavor.
        :rtype: list[str]
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        """Sets the availability_zone_ids of this Flavor.

        availability_zone_ids字段，标志ELB对应L7-flavor在对应可用区是否可以售卖。 若该字段为[]代表该flavor不可售卖；若该字段为[\"ALL\"]，代表所有可用区可售卖；若仅部分可用区可售卖则返回[\"cn-north-1a\",\"cn-north-1b\"]。 可通过/v3/{project_id}/elb/availability-zones接口查询所有可售卖的可用区接口。

        :param availability_zone_ids: The availability_zone_ids of this Flavor.
        :type: list[str]
        """
        self._availability_zone_ids = availability_zone_ids

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
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
