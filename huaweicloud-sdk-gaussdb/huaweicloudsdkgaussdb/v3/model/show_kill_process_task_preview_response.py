# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKillProcessTaskPreviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'processes': 'list[ProcessDetail]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'processes': 'processes'
    }

    def __init__(self, total_count=None, processes=None):
        r"""ShowKillProcessTaskPreviewResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**：  会话总数，最多支持预览20条会话记录。  **取值范围**：  0-20。
        :type total_count: int
        :param processes: **参数解释**：  会话记录。
        :type processes: list[:class:`huaweicloudsdkgaussdb.v3.ProcessDetail`]
        """
        
        super().__init__()

        self._total_count = None
        self._processes = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if processes is not None:
            self.processes = processes

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowKillProcessTaskPreviewResponse.

        **参数解释**：  会话总数，最多支持预览20条会话记录。  **取值范围**：  0-20。

        :return: The total_count of this ShowKillProcessTaskPreviewResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowKillProcessTaskPreviewResponse.

        **参数解释**：  会话总数，最多支持预览20条会话记录。  **取值范围**：  0-20。

        :param total_count: The total_count of this ShowKillProcessTaskPreviewResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def processes(self):
        r"""Gets the processes of this ShowKillProcessTaskPreviewResponse.

        **参数解释**：  会话记录。

        :return: The processes of this ShowKillProcessTaskPreviewResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ProcessDetail`]
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        r"""Sets the processes of this ShowKillProcessTaskPreviewResponse.

        **参数解释**：  会话记录。

        :param processes: The processes of this ShowKillProcessTaskPreviewResponse.
        :type processes: list[:class:`huaweicloudsdkgaussdb.v3.ProcessDetail`]
        """
        self._processes = processes

    def to_dict(self):
        import warnings
        warnings.warn("ShowKillProcessTaskPreviewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowKillProcessTaskPreviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
