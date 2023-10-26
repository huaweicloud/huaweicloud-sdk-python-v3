# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHpcShareRequestBody:

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
        'gc_time': 'int'
    }

    attribute_map = {
        'action': 'action',
        'gc_time': 'gc_time'
    }

    def __init__(self, action=None, gc_time=None):
        """UpdateHpcShareRequestBody

        The model defined in huaweicloud sdk

        :param action: 更新 HPC 型文件系统的操作类型。当前仅支持取值 config_gc_time
        :type action: str
        :param gc_time: 文件系统冷数据淘汰时间，单位为小时，取值范围 [1, 100000000]。新建立的 OBS 绑定关系冷数据淘汰时间默认为 60 小时
        :type gc_time: int
        """
        
        

        self._action = None
        self._gc_time = None
        self.discriminator = None

        self.action = action
        self.gc_time = gc_time

    @property
    def action(self):
        """Gets the action of this UpdateHpcShareRequestBody.

        更新 HPC 型文件系统的操作类型。当前仅支持取值 config_gc_time

        :return: The action of this UpdateHpcShareRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateHpcShareRequestBody.

        更新 HPC 型文件系统的操作类型。当前仅支持取值 config_gc_time

        :param action: The action of this UpdateHpcShareRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def gc_time(self):
        """Gets the gc_time of this UpdateHpcShareRequestBody.

        文件系统冷数据淘汰时间，单位为小时，取值范围 [1, 100000000]。新建立的 OBS 绑定关系冷数据淘汰时间默认为 60 小时

        :return: The gc_time of this UpdateHpcShareRequestBody.
        :rtype: int
        """
        return self._gc_time

    @gc_time.setter
    def gc_time(self, gc_time):
        """Sets the gc_time of this UpdateHpcShareRequestBody.

        文件系统冷数据淘汰时间，单位为小时，取值范围 [1, 100000000]。新建立的 OBS 绑定关系冷数据淘汰时间默认为 60 小时

        :param gc_time: The gc_time of this UpdateHpcShareRequestBody.
        :type gc_time: int
        """
        self._gc_time = gc_time

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
        if not isinstance(other, UpdateHpcShareRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
