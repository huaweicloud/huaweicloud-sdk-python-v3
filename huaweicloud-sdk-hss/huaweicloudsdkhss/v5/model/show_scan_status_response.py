# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScanStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_status': 'str',
        'scaned_time': 'int'
    }

    attribute_map = {
        'scan_status': 'scan_status',
        'scaned_time': 'scaned_time'
    }

    def __init__(self, scan_status=None, scaned_time=None):
        r"""ShowScanStatusResponse

        The model defined in huaweicloud sdk

        :param scan_status: **参数解释**： 手动检测状态 **取值范围**： - neverscan：无扫描任务 - scanning：扫描中 - scaned：扫描完成 - failed：扫描失败 - over_time：扫描超时（扫描时间超过30分钟） - longscanning：扫描超时（扫描时间超过60分钟）
        :type scan_status: str
        :param scaned_time: **参数解释**： 检测完成时间 **取值范围**： 不涉及
        :type scaned_time: int
        """
        
        super().__init__()

        self._scan_status = None
        self._scaned_time = None
        self.discriminator = None

        if scan_status is not None:
            self.scan_status = scan_status
        if scaned_time is not None:
            self.scaned_time = scaned_time

    @property
    def scan_status(self):
        r"""Gets the scan_status of this ShowScanStatusResponse.

        **参数解释**： 手动检测状态 **取值范围**： - neverscan：无扫描任务 - scanning：扫描中 - scaned：扫描完成 - failed：扫描失败 - over_time：扫描超时（扫描时间超过30分钟） - longscanning：扫描超时（扫描时间超过60分钟）

        :return: The scan_status of this ShowScanStatusResponse.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this ShowScanStatusResponse.

        **参数解释**： 手动检测状态 **取值范围**： - neverscan：无扫描任务 - scanning：扫描中 - scaned：扫描完成 - failed：扫描失败 - over_time：扫描超时（扫描时间超过30分钟） - longscanning：扫描超时（扫描时间超过60分钟）

        :param scan_status: The scan_status of this ShowScanStatusResponse.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def scaned_time(self):
        r"""Gets the scaned_time of this ShowScanStatusResponse.

        **参数解释**： 检测完成时间 **取值范围**： 不涉及

        :return: The scaned_time of this ShowScanStatusResponse.
        :rtype: int
        """
        return self._scaned_time

    @scaned_time.setter
    def scaned_time(self, scaned_time):
        r"""Sets the scaned_time of this ShowScanStatusResponse.

        **参数解释**： 检测完成时间 **取值范围**： 不涉及

        :param scaned_time: The scaned_time of this ShowScanStatusResponse.
        :type scaned_time: int
        """
        self._scaned_time = scaned_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowScanStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowScanStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
