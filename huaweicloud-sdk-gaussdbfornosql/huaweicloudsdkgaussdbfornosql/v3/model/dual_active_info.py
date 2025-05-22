# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DualActiveInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'status': 'str',
        'destination_instance_id': 'str',
        'destination_region': 'str'
    }

    attribute_map = {
        'role': 'role',
        'status': 'status',
        'destination_instance_id': 'destination_instance_id',
        'destination_region': 'destination_region'
    }

    def __init__(self, role=None, status=None, destination_instance_id=None, destination_region=None):
        r"""DualActiveInfo

        The model defined in huaweicloud sdk

        :param role: 双活角色。
        :type role: str
        :param status: 双活状态。
        :type status: str
        :param destination_instance_id: 双活对端实例id。
        :type destination_instance_id: str
        :param destination_region: 双活对端region。
        :type destination_region: str
        """
        
        

        self._role = None
        self._status = None
        self._destination_instance_id = None
        self._destination_region = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if status is not None:
            self.status = status
        if destination_instance_id is not None:
            self.destination_instance_id = destination_instance_id
        if destination_region is not None:
            self.destination_region = destination_region

    @property
    def role(self):
        r"""Gets the role of this DualActiveInfo.

        双活角色。

        :return: The role of this DualActiveInfo.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this DualActiveInfo.

        双活角色。

        :param role: The role of this DualActiveInfo.
        :type role: str
        """
        self._role = role

    @property
    def status(self):
        r"""Gets the status of this DualActiveInfo.

        双活状态。

        :return: The status of this DualActiveInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DualActiveInfo.

        双活状态。

        :param status: The status of this DualActiveInfo.
        :type status: str
        """
        self._status = status

    @property
    def destination_instance_id(self):
        r"""Gets the destination_instance_id of this DualActiveInfo.

        双活对端实例id。

        :return: The destination_instance_id of this DualActiveInfo.
        :rtype: str
        """
        return self._destination_instance_id

    @destination_instance_id.setter
    def destination_instance_id(self, destination_instance_id):
        r"""Sets the destination_instance_id of this DualActiveInfo.

        双活对端实例id。

        :param destination_instance_id: The destination_instance_id of this DualActiveInfo.
        :type destination_instance_id: str
        """
        self._destination_instance_id = destination_instance_id

    @property
    def destination_region(self):
        r"""Gets the destination_region of this DualActiveInfo.

        双活对端region。

        :return: The destination_region of this DualActiveInfo.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        r"""Sets the destination_region of this DualActiveInfo.

        双活对端region。

        :param destination_region: The destination_region of this DualActiveInfo.
        :type destination_region: str
        """
        self._destination_region = destination_region

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
        if not isinstance(other, DualActiveInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
