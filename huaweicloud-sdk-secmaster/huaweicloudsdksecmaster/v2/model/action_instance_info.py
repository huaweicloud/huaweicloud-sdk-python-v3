# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionInstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'ActionInfo',
        'instance_log': 'AuditLogInfo'
    }

    attribute_map = {
        'action': 'action',
        'instance_log': 'instance_log'
    }

    def __init__(self, action=None, instance_log=None):
        r"""ActionInstanceInfo

        The model defined in huaweicloud sdk

        :param action: 
        :type action: :class:`huaweicloudsdksecmaster.v2.ActionInfo`
        :param instance_log: 
        :type instance_log: :class:`huaweicloudsdksecmaster.v2.AuditLogInfo`
        """
        
        

        self._action = None
        self._instance_log = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if instance_log is not None:
            self.instance_log = instance_log

    @property
    def action(self):
        r"""Gets the action of this ActionInstanceInfo.

        :return: The action of this ActionInstanceInfo.
        :rtype: :class:`huaweicloudsdksecmaster.v2.ActionInfo`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ActionInstanceInfo.

        :param action: The action of this ActionInstanceInfo.
        :type action: :class:`huaweicloudsdksecmaster.v2.ActionInfo`
        """
        self._action = action

    @property
    def instance_log(self):
        r"""Gets the instance_log of this ActionInstanceInfo.

        :return: The instance_log of this ActionInstanceInfo.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AuditLogInfo`
        """
        return self._instance_log

    @instance_log.setter
    def instance_log(self, instance_log):
        r"""Sets the instance_log of this ActionInstanceInfo.

        :param instance_log: The instance_log of this ActionInstanceInfo.
        :type instance_log: :class:`huaweicloudsdksecmaster.v2.AuditLogInfo`
        """
        self._instance_log = instance_log

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
        if not isinstance(other, ActionInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
