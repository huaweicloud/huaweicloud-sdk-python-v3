# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTrainingJobLogsPreviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'current_size': 'int',
        'full_size': 'int'
    }

    attribute_map = {
        'content': 'content',
        'current_size': 'current_size',
        'full_size': 'full_size'
    }

    def __init__(self, content=None, current_size=None, full_size=None):
        r"""ShowTrainingJobLogsPreviewResponse

        The model defined in huaweicloud sdk

        :param content: 日志内容。如果日志大小没有超过上限（n兆）则返回全部内容，如果日志超过了上限（n兆）则返回最新的n兆的日志。2022/03/01 00:00:00 (GMT+08:00)后，此参数名称由“context”改为“content”。
        :type content: str
        :param current_size: 当前返回的日志大小（单位：字节）。最大为5兆。
        :type current_size: int
        :param full_size: 完整的日志大小（单位：字节）。
        :type full_size: int
        """
        
        super().__init__()

        self._content = None
        self._current_size = None
        self._full_size = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if current_size is not None:
            self.current_size = current_size
        if full_size is not None:
            self.full_size = full_size

    @property
    def content(self):
        r"""Gets the content of this ShowTrainingJobLogsPreviewResponse.

        日志内容。如果日志大小没有超过上限（n兆）则返回全部内容，如果日志超过了上限（n兆）则返回最新的n兆的日志。2022/03/01 00:00:00 (GMT+08:00)后，此参数名称由“context”改为“content”。

        :return: The content of this ShowTrainingJobLogsPreviewResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowTrainingJobLogsPreviewResponse.

        日志内容。如果日志大小没有超过上限（n兆）则返回全部内容，如果日志超过了上限（n兆）则返回最新的n兆的日志。2022/03/01 00:00:00 (GMT+08:00)后，此参数名称由“context”改为“content”。

        :param content: The content of this ShowTrainingJobLogsPreviewResponse.
        :type content: str
        """
        self._content = content

    @property
    def current_size(self):
        r"""Gets the current_size of this ShowTrainingJobLogsPreviewResponse.

        当前返回的日志大小（单位：字节）。最大为5兆。

        :return: The current_size of this ShowTrainingJobLogsPreviewResponse.
        :rtype: int
        """
        return self._current_size

    @current_size.setter
    def current_size(self, current_size):
        r"""Sets the current_size of this ShowTrainingJobLogsPreviewResponse.

        当前返回的日志大小（单位：字节）。最大为5兆。

        :param current_size: The current_size of this ShowTrainingJobLogsPreviewResponse.
        :type current_size: int
        """
        self._current_size = current_size

    @property
    def full_size(self):
        r"""Gets the full_size of this ShowTrainingJobLogsPreviewResponse.

        完整的日志大小（单位：字节）。

        :return: The full_size of this ShowTrainingJobLogsPreviewResponse.
        :rtype: int
        """
        return self._full_size

    @full_size.setter
    def full_size(self, full_size):
        r"""Sets the full_size of this ShowTrainingJobLogsPreviewResponse.

        完整的日志大小（单位：字节）。

        :param full_size: The full_size of this ShowTrainingJobLogsPreviewResponse.
        :type full_size: int
        """
        self._full_size = full_size

    def to_dict(self):
        import warnings
        warnings.warn("ShowTrainingJobLogsPreviewResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowTrainingJobLogsPreviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
