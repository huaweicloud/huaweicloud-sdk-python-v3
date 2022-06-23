# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunQueueActionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'force': 'bool',
        'cu_count': 'int'
    }

    attribute_map = {
        'action': 'action',
        'force': 'force',
        'cu_count': 'cu_count'
    }

    def __init__(self, action=None, force=None, cu_count=None):
        """RunQueueActionReq

        The model defined in huaweicloud sdk

        :param action: 执行动作：restart：重启scale_out：扩容scale_in：缩容，目前只支持restart、scale_out、scale_in。
        :type action: str
        :param force: 是否强制重启，action为restart时可选择配置，默认为false。
        :type force: bool
        :param cu_count: 扩容或者缩容的cu数。“action”为“scale_out”或者“scale_in”时可选择配置
        :type cu_count: int
        """
        
        

        self._action = None
        self._force = None
        self._cu_count = None
        self.discriminator = None

        self.action = action
        if force is not None:
            self.force = force
        if cu_count is not None:
            self.cu_count = cu_count

    @property
    def action(self):
        """Gets the action of this RunQueueActionReq.

        执行动作：restart：重启scale_out：扩容scale_in：缩容，目前只支持restart、scale_out、scale_in。

        :return: The action of this RunQueueActionReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this RunQueueActionReq.

        执行动作：restart：重启scale_out：扩容scale_in：缩容，目前只支持restart、scale_out、scale_in。

        :param action: The action of this RunQueueActionReq.
        :type action: str
        """
        self._action = action

    @property
    def force(self):
        """Gets the force of this RunQueueActionReq.

        是否强制重启，action为restart时可选择配置，默认为false。

        :return: The force of this RunQueueActionReq.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this RunQueueActionReq.

        是否强制重启，action为restart时可选择配置，默认为false。

        :param force: The force of this RunQueueActionReq.
        :type force: bool
        """
        self._force = force

    @property
    def cu_count(self):
        """Gets the cu_count of this RunQueueActionReq.

        扩容或者缩容的cu数。“action”为“scale_out”或者“scale_in”时可选择配置

        :return: The cu_count of this RunQueueActionReq.
        :rtype: int
        """
        return self._cu_count

    @cu_count.setter
    def cu_count(self, cu_count):
        """Sets the cu_count of this RunQueueActionReq.

        扩容或者缩容的cu数。“action”为“scale_out”或者“scale_in”时可选择配置

        :param cu_count: The cu_count of this RunQueueActionReq.
        :type cu_count: int
        """
        self._cu_count = cu_count

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
        if not isinstance(other, RunQueueActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
