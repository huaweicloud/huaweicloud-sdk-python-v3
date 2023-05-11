# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Trigger:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trigger_name': 'str',
        'trigger_type': 'str',
        'enabled': 'bool',
        'trigger_config': 'OBSTriggerConfig'
    }

    attribute_map = {
        'trigger_name': 'trigger_name',
        'trigger_type': 'trigger_type',
        'enabled': 'enabled',
        'trigger_config': 'trigger_config'
    }

    def __init__(self, trigger_name=None, trigger_type=None, enabled=None, trigger_config=None):
        """Trigger

        The model defined in huaweicloud sdk

        :param trigger_name: 触发器名称
        :type trigger_name: str
        :param trigger_type: 触发器类型 FLOWTIMER：定时触发器 SMN：SMN触发器 APIG：APIG触发器(共享版) APIG_DE：APIG触发器(专享版) OBS：OBS触发器
        :type trigger_type: str
        :param enabled: 是否启用触发器
        :type enabled: bool
        :param trigger_config: 
        :type trigger_config: :class:`huaweicloudsdkfunctiongraph.v2.OBSTriggerConfig`
        """
        
        

        self._trigger_name = None
        self._trigger_type = None
        self._enabled = None
        self._trigger_config = None
        self.discriminator = None

        self.trigger_name = trigger_name
        self.trigger_type = trigger_type
        if enabled is not None:
            self.enabled = enabled
        if trigger_config is not None:
            self.trigger_config = trigger_config

    @property
    def trigger_name(self):
        """Gets the trigger_name of this Trigger.

        触发器名称

        :return: The trigger_name of this Trigger.
        :rtype: str
        """
        return self._trigger_name

    @trigger_name.setter
    def trigger_name(self, trigger_name):
        """Sets the trigger_name of this Trigger.

        触发器名称

        :param trigger_name: The trigger_name of this Trigger.
        :type trigger_name: str
        """
        self._trigger_name = trigger_name

    @property
    def trigger_type(self):
        """Gets the trigger_type of this Trigger.

        触发器类型 FLOWTIMER：定时触发器 SMN：SMN触发器 APIG：APIG触发器(共享版) APIG_DE：APIG触发器(专享版) OBS：OBS触发器

        :return: The trigger_type of this Trigger.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this Trigger.

        触发器类型 FLOWTIMER：定时触发器 SMN：SMN触发器 APIG：APIG触发器(共享版) APIG_DE：APIG触发器(专享版) OBS：OBS触发器

        :param trigger_type: The trigger_type of this Trigger.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def enabled(self):
        """Gets the enabled of this Trigger.

        是否启用触发器

        :return: The enabled of this Trigger.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Trigger.

        是否启用触发器

        :param enabled: The enabled of this Trigger.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def trigger_config(self):
        """Gets the trigger_config of this Trigger.

        :return: The trigger_config of this Trigger.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.OBSTriggerConfig`
        """
        return self._trigger_config

    @trigger_config.setter
    def trigger_config(self, trigger_config):
        """Sets the trigger_config of this Trigger.

        :param trigger_config: The trigger_config of this Trigger.
        :type trigger_config: :class:`huaweicloudsdkfunctiongraph.v2.OBSTriggerConfig`
        """
        self._trigger_config = trigger_config

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
        if not isinstance(other, Trigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
