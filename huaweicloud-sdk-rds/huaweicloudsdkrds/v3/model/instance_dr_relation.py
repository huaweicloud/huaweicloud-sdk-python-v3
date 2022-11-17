# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDrRelation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'master_instance': 'MasterInstance',
        'slave_instances': 'list[SlaveInstance]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'master_instance': 'master_instance',
        'slave_instances': 'slave_instances'
    }

    def __init__(self, instance_id=None, master_instance=None, slave_instances=None):
        """InstanceDrRelation

        The model defined in huaweicloud sdk

        :param instance_id: 当前区域实例ID。
        :type instance_id: str
        :param master_instance: 
        :type master_instance: :class:`huaweicloudsdkrds.v3.MasterInstance`
        :param slave_instances: 容灾实例信息列表。
        :type slave_instances: list[:class:`huaweicloudsdkrds.v3.SlaveInstance`]
        """
        
        

        self._instance_id = None
        self._master_instance = None
        self._slave_instances = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if master_instance is not None:
            self.master_instance = master_instance
        if slave_instances is not None:
            self.slave_instances = slave_instances

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceDrRelation.

        当前区域实例ID。

        :return: The instance_id of this InstanceDrRelation.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceDrRelation.

        当前区域实例ID。

        :param instance_id: The instance_id of this InstanceDrRelation.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def master_instance(self):
        """Gets the master_instance of this InstanceDrRelation.

        :return: The master_instance of this InstanceDrRelation.
        :rtype: :class:`huaweicloudsdkrds.v3.MasterInstance`
        """
        return self._master_instance

    @master_instance.setter
    def master_instance(self, master_instance):
        """Sets the master_instance of this InstanceDrRelation.

        :param master_instance: The master_instance of this InstanceDrRelation.
        :type master_instance: :class:`huaweicloudsdkrds.v3.MasterInstance`
        """
        self._master_instance = master_instance

    @property
    def slave_instances(self):
        """Gets the slave_instances of this InstanceDrRelation.

        容灾实例信息列表。

        :return: The slave_instances of this InstanceDrRelation.
        :rtype: list[:class:`huaweicloudsdkrds.v3.SlaveInstance`]
        """
        return self._slave_instances

    @slave_instances.setter
    def slave_instances(self, slave_instances):
        """Sets the slave_instances of this InstanceDrRelation.

        容灾实例信息列表。

        :param slave_instances: The slave_instances of this InstanceDrRelation.
        :type slave_instances: list[:class:`huaweicloudsdkrds.v3.SlaveInstance`]
        """
        self._slave_instances = slave_instances

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
        if not isinstance(other, InstanceDrRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
