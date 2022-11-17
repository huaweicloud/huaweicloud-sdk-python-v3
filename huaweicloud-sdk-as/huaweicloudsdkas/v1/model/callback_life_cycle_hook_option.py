# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CallbackLifeCycleHookOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lifecycle_action_key': 'str',
        'instance_id': 'str',
        'lifecycle_hook_name': 'str',
        'lifecycle_action_result': 'str'
    }

    attribute_map = {
        'lifecycle_action_key': 'lifecycle_action_key',
        'instance_id': 'instance_id',
        'lifecycle_hook_name': 'lifecycle_hook_name',
        'lifecycle_action_result': 'lifecycle_action_result'
    }

    def __init__(self, lifecycle_action_key=None, instance_id=None, lifecycle_hook_name=None, lifecycle_action_result=None):
        """CallbackLifeCycleHookOption

        The model defined in huaweicloud sdk

        :param lifecycle_action_key: 生命周期操作令牌，通过查询伸缩实例挂起信息接口获取。指定生命周期回调对象，当不传入instance_id字段时，该字段为必选。当该字段与instance_id字段都传入，优先使用该字段进行回调。
        :type lifecycle_action_key: str
        :param instance_id: 实例ID。指定生命周期回调对象，当不传入lifecycle_action_key字段时，该字段为必选。
        :type instance_id: str
        :param lifecycle_hook_name: 生命周期挂钩名称。指定生命周期回调对象，当不传入lifecycle_action_key字段时，该字段为必选。
        :type lifecycle_hook_name: str
        :param lifecycle_action_result: 生命周期回调操作。ABANDON：终止。CONTINUE：继续。EXTEND：延长超时时间，每次延长1小时。
        :type lifecycle_action_result: str
        """
        
        

        self._lifecycle_action_key = None
        self._instance_id = None
        self._lifecycle_hook_name = None
        self._lifecycle_action_result = None
        self.discriminator = None

        if lifecycle_action_key is not None:
            self.lifecycle_action_key = lifecycle_action_key
        if instance_id is not None:
            self.instance_id = instance_id
        if lifecycle_hook_name is not None:
            self.lifecycle_hook_name = lifecycle_hook_name
        self.lifecycle_action_result = lifecycle_action_result

    @property
    def lifecycle_action_key(self):
        """Gets the lifecycle_action_key of this CallbackLifeCycleHookOption.

        生命周期操作令牌，通过查询伸缩实例挂起信息接口获取。指定生命周期回调对象，当不传入instance_id字段时，该字段为必选。当该字段与instance_id字段都传入，优先使用该字段进行回调。

        :return: The lifecycle_action_key of this CallbackLifeCycleHookOption.
        :rtype: str
        """
        return self._lifecycle_action_key

    @lifecycle_action_key.setter
    def lifecycle_action_key(self, lifecycle_action_key):
        """Sets the lifecycle_action_key of this CallbackLifeCycleHookOption.

        生命周期操作令牌，通过查询伸缩实例挂起信息接口获取。指定生命周期回调对象，当不传入instance_id字段时，该字段为必选。当该字段与instance_id字段都传入，优先使用该字段进行回调。

        :param lifecycle_action_key: The lifecycle_action_key of this CallbackLifeCycleHookOption.
        :type lifecycle_action_key: str
        """
        self._lifecycle_action_key = lifecycle_action_key

    @property
    def instance_id(self):
        """Gets the instance_id of this CallbackLifeCycleHookOption.

        实例ID。指定生命周期回调对象，当不传入lifecycle_action_key字段时，该字段为必选。

        :return: The instance_id of this CallbackLifeCycleHookOption.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CallbackLifeCycleHookOption.

        实例ID。指定生命周期回调对象，当不传入lifecycle_action_key字段时，该字段为必选。

        :param instance_id: The instance_id of this CallbackLifeCycleHookOption.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def lifecycle_hook_name(self):
        """Gets the lifecycle_hook_name of this CallbackLifeCycleHookOption.

        生命周期挂钩名称。指定生命周期回调对象，当不传入lifecycle_action_key字段时，该字段为必选。

        :return: The lifecycle_hook_name of this CallbackLifeCycleHookOption.
        :rtype: str
        """
        return self._lifecycle_hook_name

    @lifecycle_hook_name.setter
    def lifecycle_hook_name(self, lifecycle_hook_name):
        """Sets the lifecycle_hook_name of this CallbackLifeCycleHookOption.

        生命周期挂钩名称。指定生命周期回调对象，当不传入lifecycle_action_key字段时，该字段为必选。

        :param lifecycle_hook_name: The lifecycle_hook_name of this CallbackLifeCycleHookOption.
        :type lifecycle_hook_name: str
        """
        self._lifecycle_hook_name = lifecycle_hook_name

    @property
    def lifecycle_action_result(self):
        """Gets the lifecycle_action_result of this CallbackLifeCycleHookOption.

        生命周期回调操作。ABANDON：终止。CONTINUE：继续。EXTEND：延长超时时间，每次延长1小时。

        :return: The lifecycle_action_result of this CallbackLifeCycleHookOption.
        :rtype: str
        """
        return self._lifecycle_action_result

    @lifecycle_action_result.setter
    def lifecycle_action_result(self, lifecycle_action_result):
        """Sets the lifecycle_action_result of this CallbackLifeCycleHookOption.

        生命周期回调操作。ABANDON：终止。CONTINUE：继续。EXTEND：延长超时时间，每次延长1小时。

        :param lifecycle_action_result: The lifecycle_action_result of this CallbackLifeCycleHookOption.
        :type lifecycle_action_result: str
        """
        self._lifecycle_action_result = lifecycle_action_result

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
        if not isinstance(other, CallbackLifeCycleHookOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
