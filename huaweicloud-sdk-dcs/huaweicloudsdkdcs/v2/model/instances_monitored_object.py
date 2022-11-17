# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstancesMonitoredObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dcs_instance_id': 'str',
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'dcs_instance_id': 'dcs_instance_id',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, dcs_instance_id=None, name=None, status=None):
        """InstancesMonitoredObject

        The model defined in huaweicloud sdk

        :param dcs_instance_id: 测量对象ID，即实例的ID。
        :type dcs_instance_id: str
        :param name: 测量对象名称，即实例名称。
        :type name: str
        :param status: 测量对象状态，即实例状态。
        :type status: str
        """
        
        

        self._dcs_instance_id = None
        self._name = None
        self._status = None
        self.discriminator = None

        if dcs_instance_id is not None:
            self.dcs_instance_id = dcs_instance_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def dcs_instance_id(self):
        """Gets the dcs_instance_id of this InstancesMonitoredObject.

        测量对象ID，即实例的ID。

        :return: The dcs_instance_id of this InstancesMonitoredObject.
        :rtype: str
        """
        return self._dcs_instance_id

    @dcs_instance_id.setter
    def dcs_instance_id(self, dcs_instance_id):
        """Sets the dcs_instance_id of this InstancesMonitoredObject.

        测量对象ID，即实例的ID。

        :param dcs_instance_id: The dcs_instance_id of this InstancesMonitoredObject.
        :type dcs_instance_id: str
        """
        self._dcs_instance_id = dcs_instance_id

    @property
    def name(self):
        """Gets the name of this InstancesMonitoredObject.

        测量对象名称，即实例名称。

        :return: The name of this InstancesMonitoredObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstancesMonitoredObject.

        测量对象名称，即实例名称。

        :param name: The name of this InstancesMonitoredObject.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this InstancesMonitoredObject.

        测量对象状态，即实例状态。

        :return: The status of this InstancesMonitoredObject.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstancesMonitoredObject.

        测量对象状态，即实例状态。

        :param status: The status of this InstancesMonitoredObject.
        :type status: str
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
        if not isinstance(other, InstancesMonitoredObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
