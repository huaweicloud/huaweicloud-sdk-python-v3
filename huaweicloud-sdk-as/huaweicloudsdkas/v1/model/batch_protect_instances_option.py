# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchProtectInstancesOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instances_id': 'list[str]',
        'instance_delete': 'str',
        'action': 'str',
        'instance_append': 'str'
    }

    attribute_map = {
        'instances_id': 'instances_id',
        'instance_delete': 'instance_delete',
        'action': 'action',
        'instance_append': 'instance_append'
    }

    def __init__(self, instances_id=None, instance_delete=None, action=None, instance_append=None):
        """BatchProtectInstancesOption

        The model defined in huaweicloud sdk

        :param instances_id: 云服务器ID。
        :type instances_id: list[str]
        :param instance_delete: 从伸缩组中移出实例时，是否删除云服务器。默认为no；可选值为yes或no。只有action为REMOVE时，这个字段才生效。
        :type instance_delete: str
        :param action: 批量操作实例action标识：添加：ADD  移除： REMOVE  设置实例保护： PROTECT  取消实例保护： UNPROTECT；转入备用状态：ENTER_STANDBY 移出备用状态:EXIT_STANDBY
        :type action: str
        :param instance_append: 将实例移入备用状态时，是否补充新的云服务器。取值如下：no：不补充新的实例，默认情况为no。yes：补充新的实例。只有action为ENTER_STANDBY时，这个字段才生效。
        :type instance_append: str
        """
        
        

        self._instances_id = None
        self._instance_delete = None
        self._action = None
        self._instance_append = None
        self.discriminator = None

        self.instances_id = instances_id
        if instance_delete is not None:
            self.instance_delete = instance_delete
        self.action = action
        if instance_append is not None:
            self.instance_append = instance_append

    @property
    def instances_id(self):
        """Gets the instances_id of this BatchProtectInstancesOption.

        云服务器ID。

        :return: The instances_id of this BatchProtectInstancesOption.
        :rtype: list[str]
        """
        return self._instances_id

    @instances_id.setter
    def instances_id(self, instances_id):
        """Sets the instances_id of this BatchProtectInstancesOption.

        云服务器ID。

        :param instances_id: The instances_id of this BatchProtectInstancesOption.
        :type instances_id: list[str]
        """
        self._instances_id = instances_id

    @property
    def instance_delete(self):
        """Gets the instance_delete of this BatchProtectInstancesOption.

        从伸缩组中移出实例时，是否删除云服务器。默认为no；可选值为yes或no。只有action为REMOVE时，这个字段才生效。

        :return: The instance_delete of this BatchProtectInstancesOption.
        :rtype: str
        """
        return self._instance_delete

    @instance_delete.setter
    def instance_delete(self, instance_delete):
        """Sets the instance_delete of this BatchProtectInstancesOption.

        从伸缩组中移出实例时，是否删除云服务器。默认为no；可选值为yes或no。只有action为REMOVE时，这个字段才生效。

        :param instance_delete: The instance_delete of this BatchProtectInstancesOption.
        :type instance_delete: str
        """
        self._instance_delete = instance_delete

    @property
    def action(self):
        """Gets the action of this BatchProtectInstancesOption.

        批量操作实例action标识：添加：ADD  移除： REMOVE  设置实例保护： PROTECT  取消实例保护： UNPROTECT；转入备用状态：ENTER_STANDBY 移出备用状态:EXIT_STANDBY

        :return: The action of this BatchProtectInstancesOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BatchProtectInstancesOption.

        批量操作实例action标识：添加：ADD  移除： REMOVE  设置实例保护： PROTECT  取消实例保护： UNPROTECT；转入备用状态：ENTER_STANDBY 移出备用状态:EXIT_STANDBY

        :param action: The action of this BatchProtectInstancesOption.
        :type action: str
        """
        self._action = action

    @property
    def instance_append(self):
        """Gets the instance_append of this BatchProtectInstancesOption.

        将实例移入备用状态时，是否补充新的云服务器。取值如下：no：不补充新的实例，默认情况为no。yes：补充新的实例。只有action为ENTER_STANDBY时，这个字段才生效。

        :return: The instance_append of this BatchProtectInstancesOption.
        :rtype: str
        """
        return self._instance_append

    @instance_append.setter
    def instance_append(self, instance_append):
        """Sets the instance_append of this BatchProtectInstancesOption.

        将实例移入备用状态时，是否补充新的云服务器。取值如下：no：不补充新的实例，默认情况为no。yes：补充新的实例。只有action为ENTER_STANDBY时，这个字段才生效。

        :param instance_append: The instance_append of this BatchProtectInstancesOption.
        :type instance_append: str
        """
        self._instance_append = instance_append

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
        if not isinstance(other, BatchProtectInstancesOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
