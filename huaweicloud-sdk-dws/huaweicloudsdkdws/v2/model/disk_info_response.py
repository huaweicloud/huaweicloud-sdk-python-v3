# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskInfoResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'percentage': 'str',
        'id': 'str',
        'name': 'str',
        'disk_capacity': 'str',
        'disk_used': 'str'
    }

    attribute_map = {
        'percentage': 'percentage',
        'id': 'id',
        'name': 'name',
        'disk_capacity': 'disk_capacity',
        'disk_used': 'disk_used'
    }

    def __init__(self, percentage=None, id=None, name=None, disk_capacity=None, disk_used=None):
        r"""DiskInfoResponse

        The model defined in huaweicloud sdk

        :param percentage: **参数解释**： 已使用百分比。 **取值范围**： 不涉及。
        :type percentage: str
        :param id: **参数解释**： 节点ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 节点名。 **取值范围**： 不涉及。
        :type name: str
        :param disk_capacity: **参数解释**： 磁盘规格。 **取值范围**： 不涉及。
        :type disk_capacity: str
        :param disk_used: **参数解释**： 已使用量。 **取值范围**： 不涉及。
        :type disk_used: str
        """
        
        

        self._percentage = None
        self._id = None
        self._name = None
        self._disk_capacity = None
        self._disk_used = None
        self.discriminator = None

        if percentage is not None:
            self.percentage = percentage
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if disk_capacity is not None:
            self.disk_capacity = disk_capacity
        if disk_used is not None:
            self.disk_used = disk_used

    @property
    def percentage(self):
        r"""Gets the percentage of this DiskInfoResponse.

        **参数解释**： 已使用百分比。 **取值范围**： 不涉及。

        :return: The percentage of this DiskInfoResponse.
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        r"""Sets the percentage of this DiskInfoResponse.

        **参数解释**： 已使用百分比。 **取值范围**： 不涉及。

        :param percentage: The percentage of this DiskInfoResponse.
        :type percentage: str
        """
        self._percentage = percentage

    @property
    def id(self):
        r"""Gets the id of this DiskInfoResponse.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。

        :return: The id of this DiskInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DiskInfoResponse.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。

        :param id: The id of this DiskInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DiskInfoResponse.

        **参数解释**： 节点名。 **取值范围**： 不涉及。

        :return: The name of this DiskInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DiskInfoResponse.

        **参数解释**： 节点名。 **取值范围**： 不涉及。

        :param name: The name of this DiskInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def disk_capacity(self):
        r"""Gets the disk_capacity of this DiskInfoResponse.

        **参数解释**： 磁盘规格。 **取值范围**： 不涉及。

        :return: The disk_capacity of this DiskInfoResponse.
        :rtype: str
        """
        return self._disk_capacity

    @disk_capacity.setter
    def disk_capacity(self, disk_capacity):
        r"""Sets the disk_capacity of this DiskInfoResponse.

        **参数解释**： 磁盘规格。 **取值范围**： 不涉及。

        :param disk_capacity: The disk_capacity of this DiskInfoResponse.
        :type disk_capacity: str
        """
        self._disk_capacity = disk_capacity

    @property
    def disk_used(self):
        r"""Gets the disk_used of this DiskInfoResponse.

        **参数解释**： 已使用量。 **取值范围**： 不涉及。

        :return: The disk_used of this DiskInfoResponse.
        :rtype: str
        """
        return self._disk_used

    @disk_used.setter
    def disk_used(self, disk_used):
        r"""Sets the disk_used of this DiskInfoResponse.

        **参数解释**： 已使用量。 **取值范围**： 不涉及。

        :param disk_used: The disk_used of this DiskInfoResponse.
        :type disk_used: str
        """
        self._disk_used = disk_used

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
        if not isinstance(other, DiskInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
