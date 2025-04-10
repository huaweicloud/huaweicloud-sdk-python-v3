# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmClusterAvailabilityZone:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'available_zone_id': 'str',
        'available_zone_name': 'str',
        'available_zone_code': 'str',
        'az_status': 'str',
        'type': 'str',
        'tags': 'object'
    }

    attribute_map = {
        'available_zone_id': 'availableZoneId',
        'available_zone_name': 'availableZoneName',
        'available_zone_code': 'availableZoneCode',
        'az_status': 'azStatus',
        'type': 'type',
        'tags': 'tags'
    }

    def __init__(self, available_zone_id=None, available_zone_name=None, available_zone_code=None, az_status=None, type=None, tags=None):
        r"""CdmClusterAvailabilityZone

        The model defined in huaweicloud sdk

        :param available_zone_id: 可用区ID。
        :type available_zone_id: str
        :param available_zone_name: 可用区名称。
        :type available_zone_name: str
        :param available_zone_code: 可用区码。
        :type available_zone_code: str
        :param az_status: 可用区状态。
        :type az_status: str
        :param type: 可用区类型。
        :type type: str
        :param tags: 可用区tag。
        :type tags: object
        """
        
        

        self._available_zone_id = None
        self._available_zone_name = None
        self._available_zone_code = None
        self._az_status = None
        self._type = None
        self._tags = None
        self.discriminator = None

        if available_zone_id is not None:
            self.available_zone_id = available_zone_id
        if available_zone_name is not None:
            self.available_zone_name = available_zone_name
        if available_zone_code is not None:
            self.available_zone_code = available_zone_code
        if az_status is not None:
            self.az_status = az_status
        if type is not None:
            self.type = type
        if tags is not None:
            self.tags = tags

    @property
    def available_zone_id(self):
        r"""Gets the available_zone_id of this CdmClusterAvailabilityZone.

        可用区ID。

        :return: The available_zone_id of this CdmClusterAvailabilityZone.
        :rtype: str
        """
        return self._available_zone_id

    @available_zone_id.setter
    def available_zone_id(self, available_zone_id):
        r"""Sets the available_zone_id of this CdmClusterAvailabilityZone.

        可用区ID。

        :param available_zone_id: The available_zone_id of this CdmClusterAvailabilityZone.
        :type available_zone_id: str
        """
        self._available_zone_id = available_zone_id

    @property
    def available_zone_name(self):
        r"""Gets the available_zone_name of this CdmClusterAvailabilityZone.

        可用区名称。

        :return: The available_zone_name of this CdmClusterAvailabilityZone.
        :rtype: str
        """
        return self._available_zone_name

    @available_zone_name.setter
    def available_zone_name(self, available_zone_name):
        r"""Sets the available_zone_name of this CdmClusterAvailabilityZone.

        可用区名称。

        :param available_zone_name: The available_zone_name of this CdmClusterAvailabilityZone.
        :type available_zone_name: str
        """
        self._available_zone_name = available_zone_name

    @property
    def available_zone_code(self):
        r"""Gets the available_zone_code of this CdmClusterAvailabilityZone.

        可用区码。

        :return: The available_zone_code of this CdmClusterAvailabilityZone.
        :rtype: str
        """
        return self._available_zone_code

    @available_zone_code.setter
    def available_zone_code(self, available_zone_code):
        r"""Sets the available_zone_code of this CdmClusterAvailabilityZone.

        可用区码。

        :param available_zone_code: The available_zone_code of this CdmClusterAvailabilityZone.
        :type available_zone_code: str
        """
        self._available_zone_code = available_zone_code

    @property
    def az_status(self):
        r"""Gets the az_status of this CdmClusterAvailabilityZone.

        可用区状态。

        :return: The az_status of this CdmClusterAvailabilityZone.
        :rtype: str
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        r"""Sets the az_status of this CdmClusterAvailabilityZone.

        可用区状态。

        :param az_status: The az_status of this CdmClusterAvailabilityZone.
        :type az_status: str
        """
        self._az_status = az_status

    @property
    def type(self):
        r"""Gets the type of this CdmClusterAvailabilityZone.

        可用区类型。

        :return: The type of this CdmClusterAvailabilityZone.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CdmClusterAvailabilityZone.

        可用区类型。

        :param type: The type of this CdmClusterAvailabilityZone.
        :type type: str
        """
        self._type = type

    @property
    def tags(self):
        r"""Gets the tags of this CdmClusterAvailabilityZone.

        可用区tag。

        :return: The tags of this CdmClusterAvailabilityZone.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CdmClusterAvailabilityZone.

        可用区tag。

        :param tags: The tags of this CdmClusterAvailabilityZone.
        :type tags: object
        """
        self._tags = tags

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
        if not isinstance(other, CdmClusterAvailabilityZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
