# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceHangingInfos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lifecycle_hook_name': 'str',
        'lifecycle_action_key': 'str',
        'instance_id': 'str',
        'scaling_group_id': 'str',
        'lifecycle_hook_status': 'str',
        'timeout': 'str',
        'default_result': 'str'
    }

    attribute_map = {
        'lifecycle_hook_name': 'lifecycle_hook_name',
        'lifecycle_action_key': 'lifecycle_action_key',
        'instance_id': 'instance_id',
        'scaling_group_id': 'scaling_group_id',
        'lifecycle_hook_status': 'lifecycle_hook_status',
        'timeout': 'timeout',
        'default_result': 'default_result'
    }

    def __init__(self, lifecycle_hook_name=None, lifecycle_action_key=None, instance_id=None, scaling_group_id=None, lifecycle_hook_status=None, timeout=None, default_result=None):
        """InstanceHangingInfos

        The model defined in huaweicloud sdk

        :param lifecycle_hook_name: 生命周期挂钩名称。
        :type lifecycle_hook_name: str
        :param lifecycle_action_key: 生命周期操作令牌，用于指定生命周期回调对象。
        :type lifecycle_action_key: str
        :param instance_id: 伸缩实例ID。
        :type instance_id: str
        :param scaling_group_id: 伸缩组ID。
        :type scaling_group_id: str
        :param lifecycle_hook_status: 伸缩实例挂钩的挂起状态。HANGING：挂起。CONTINUE：继续。ABANDON：终止。
        :type lifecycle_hook_status: str
        :param timeout: 超时时间，遵循UTC时间，格式为：YYYY-MM-DDThh:mm:ssZZ。
        :type timeout: str
        :param default_result: 生命周期挂钩默认回调操作。
        :type default_result: str
        """
        
        

        self._lifecycle_hook_name = None
        self._lifecycle_action_key = None
        self._instance_id = None
        self._scaling_group_id = None
        self._lifecycle_hook_status = None
        self._timeout = None
        self._default_result = None
        self.discriminator = None

        if lifecycle_hook_name is not None:
            self.lifecycle_hook_name = lifecycle_hook_name
        if lifecycle_action_key is not None:
            self.lifecycle_action_key = lifecycle_action_key
        if instance_id is not None:
            self.instance_id = instance_id
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if lifecycle_hook_status is not None:
            self.lifecycle_hook_status = lifecycle_hook_status
        if timeout is not None:
            self.timeout = timeout
        if default_result is not None:
            self.default_result = default_result

    @property
    def lifecycle_hook_name(self):
        """Gets the lifecycle_hook_name of this InstanceHangingInfos.

        生命周期挂钩名称。

        :return: The lifecycle_hook_name of this InstanceHangingInfos.
        :rtype: str
        """
        return self._lifecycle_hook_name

    @lifecycle_hook_name.setter
    def lifecycle_hook_name(self, lifecycle_hook_name):
        """Sets the lifecycle_hook_name of this InstanceHangingInfos.

        生命周期挂钩名称。

        :param lifecycle_hook_name: The lifecycle_hook_name of this InstanceHangingInfos.
        :type lifecycle_hook_name: str
        """
        self._lifecycle_hook_name = lifecycle_hook_name

    @property
    def lifecycle_action_key(self):
        """Gets the lifecycle_action_key of this InstanceHangingInfos.

        生命周期操作令牌，用于指定生命周期回调对象。

        :return: The lifecycle_action_key of this InstanceHangingInfos.
        :rtype: str
        """
        return self._lifecycle_action_key

    @lifecycle_action_key.setter
    def lifecycle_action_key(self, lifecycle_action_key):
        """Sets the lifecycle_action_key of this InstanceHangingInfos.

        生命周期操作令牌，用于指定生命周期回调对象。

        :param lifecycle_action_key: The lifecycle_action_key of this InstanceHangingInfos.
        :type lifecycle_action_key: str
        """
        self._lifecycle_action_key = lifecycle_action_key

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceHangingInfos.

        伸缩实例ID。

        :return: The instance_id of this InstanceHangingInfos.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceHangingInfos.

        伸缩实例ID。

        :param instance_id: The instance_id of this InstanceHangingInfos.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this InstanceHangingInfos.

        伸缩组ID。

        :return: The scaling_group_id of this InstanceHangingInfos.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this InstanceHangingInfos.

        伸缩组ID。

        :param scaling_group_id: The scaling_group_id of this InstanceHangingInfos.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def lifecycle_hook_status(self):
        """Gets the lifecycle_hook_status of this InstanceHangingInfos.

        伸缩实例挂钩的挂起状态。HANGING：挂起。CONTINUE：继续。ABANDON：终止。

        :return: The lifecycle_hook_status of this InstanceHangingInfos.
        :rtype: str
        """
        return self._lifecycle_hook_status

    @lifecycle_hook_status.setter
    def lifecycle_hook_status(self, lifecycle_hook_status):
        """Sets the lifecycle_hook_status of this InstanceHangingInfos.

        伸缩实例挂钩的挂起状态。HANGING：挂起。CONTINUE：继续。ABANDON：终止。

        :param lifecycle_hook_status: The lifecycle_hook_status of this InstanceHangingInfos.
        :type lifecycle_hook_status: str
        """
        self._lifecycle_hook_status = lifecycle_hook_status

    @property
    def timeout(self):
        """Gets the timeout of this InstanceHangingInfos.

        超时时间，遵循UTC时间，格式为：YYYY-MM-DDThh:mm:ssZZ。

        :return: The timeout of this InstanceHangingInfos.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this InstanceHangingInfos.

        超时时间，遵循UTC时间，格式为：YYYY-MM-DDThh:mm:ssZZ。

        :param timeout: The timeout of this InstanceHangingInfos.
        :type timeout: str
        """
        self._timeout = timeout

    @property
    def default_result(self):
        """Gets the default_result of this InstanceHangingInfos.

        生命周期挂钩默认回调操作。

        :return: The default_result of this InstanceHangingInfos.
        :rtype: str
        """
        return self._default_result

    @default_result.setter
    def default_result(self, default_result):
        """Sets the default_result of this InstanceHangingInfos.

        生命周期挂钩默认回调操作。

        :param default_result: The default_result of this InstanceHangingInfos.
        :type default_result: str
        """
        self._default_result = default_result

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
        if not isinstance(other, InstanceHangingInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
