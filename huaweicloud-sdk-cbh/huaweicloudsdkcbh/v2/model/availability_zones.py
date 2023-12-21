# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailabilityZones:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'id': 'str',
        'display_name': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'id': 'id',
        'display_name': 'display_name',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, region_id=None, id=None, display_name=None, status=None, type=None):
        """AvailabilityZones

        The model defined in huaweicloud sdk

        :param region_id: 可用区ID。
        :type region_id: str
        :param id: 可用分区ID。
        :type id: str
        :param display_name: 可用分区显示名称。
        :type display_name: str
        :param status: 可用分区状态。 - Running：运行中
        :type status: str
        :param type: 可用分区类型。 - Core：核心可用区 - Dedicated：专属可用区，只对内部客户开放
        :type type: str
        """
        
        

        self._region_id = None
        self._id = None
        self._display_name = None
        self._status = None
        self._type = None
        self.discriminator = None

        self.region_id = region_id
        self.id = id
        self.display_name = display_name
        self.status = status
        if type is not None:
            self.type = type

    @property
    def region_id(self):
        """Gets the region_id of this AvailabilityZones.

        可用区ID。

        :return: The region_id of this AvailabilityZones.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this AvailabilityZones.

        可用区ID。

        :param region_id: The region_id of this AvailabilityZones.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def id(self):
        """Gets the id of this AvailabilityZones.

        可用分区ID。

        :return: The id of this AvailabilityZones.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AvailabilityZones.

        可用分区ID。

        :param id: The id of this AvailabilityZones.
        :type id: str
        """
        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this AvailabilityZones.

        可用分区显示名称。

        :return: The display_name of this AvailabilityZones.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AvailabilityZones.

        可用分区显示名称。

        :param display_name: The display_name of this AvailabilityZones.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def status(self):
        """Gets the status of this AvailabilityZones.

        可用分区状态。 - Running：运行中

        :return: The status of this AvailabilityZones.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AvailabilityZones.

        可用分区状态。 - Running：运行中

        :param status: The status of this AvailabilityZones.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this AvailabilityZones.

        可用分区类型。 - Core：核心可用区 - Dedicated：专属可用区，只对内部客户开放

        :return: The type of this AvailabilityZones.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AvailabilityZones.

        可用分区类型。 - Core：核心可用区 - Dedicated：专属可用区，只对内部客户开放

        :param type: The type of this AvailabilityZones.
        :type type: str
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AvailabilityZones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
