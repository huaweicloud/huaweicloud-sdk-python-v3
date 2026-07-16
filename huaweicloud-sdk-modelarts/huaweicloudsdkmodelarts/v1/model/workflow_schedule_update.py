# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowScheduleUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'dict(str, object)',
        'enable': 'bool'
    }

    attribute_map = {
        'content': 'content',
        'enable': 'enable'
    }

    def __init__(self, content=None, enable=None):
        r"""WorkflowScheduleUpdate

        The model defined in huaweicloud sdk

        :param content: 内容。
        :type content: dict(str, object)
        :param enable: 使能标志。
        :type enable: bool
        """
        
        

        self._content = None
        self._enable = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if enable is not None:
            self.enable = enable

    @property
    def content(self):
        r"""Gets the content of this WorkflowScheduleUpdate.

        内容。

        :return: The content of this WorkflowScheduleUpdate.
        :rtype: dict(str, object)
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this WorkflowScheduleUpdate.

        内容。

        :param content: The content of this WorkflowScheduleUpdate.
        :type content: dict(str, object)
        """
        self._content = content

    @property
    def enable(self):
        r"""Gets the enable of this WorkflowScheduleUpdate.

        使能标志。

        :return: The enable of this WorkflowScheduleUpdate.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this WorkflowScheduleUpdate.

        使能标志。

        :param enable: The enable of this WorkflowScheduleUpdate.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, WorkflowScheduleUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
