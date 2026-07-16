# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerTaskLimit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_task': 'int'
    }

    attribute_map = {
        'max_task': 'max_task'
    }

    def __init__(self, max_task=None):
        r"""ServerTaskLimit

        The model defined in huaweicloud sdk

        :param max_task: **参数解释：** 单个服务任务限制总数。 **取值范围：** [0, 10000]。
        :type max_task: int
        """
        
        

        self._max_task = None
        self.discriminator = None

        if max_task is not None:
            self.max_task = max_task

    @property
    def max_task(self):
        r"""Gets the max_task of this ServerTaskLimit.

        **参数解释：** 单个服务任务限制总数。 **取值范围：** [0, 10000]。

        :return: The max_task of this ServerTaskLimit.
        :rtype: int
        """
        return self._max_task

    @max_task.setter
    def max_task(self, max_task):
        r"""Sets the max_task of this ServerTaskLimit.

        **参数解释：** 单个服务任务限制总数。 **取值范围：** [0, 10000]。

        :param max_task: The max_task of this ServerTaskLimit.
        :type max_task: int
        """
        self._max_task = max_task

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerTaskLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
