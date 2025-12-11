# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBaselineScanStatusResponse(SdkResponse):

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
        'scanned_time': 'int'
    }

    attribute_map = {
        'scan_status': 'scan_status',
        'scanned_time': 'scanned_time'
    }

    def __init__(self, scan_status=None, scanned_time=None):
        r"""ShowBaselineScanStatusResponse

        The model defined in huaweicloud sdk

        :param scan_status: **参数解释**: 扫描状态 **约束限制**: 不涉及 **取值范围**: - neverscan: 未扫描 - scanning: 扫描中 - scanned: 扫描完成 - failed: 扫描失败  **默认取值**: 不涉及 
        :type scan_status: str
        :param scanned_time: **参数解释**: 扫描结束时间，单位毫秒 **约束限制**: 不涉及 **取值范围**: 大小0-4070880000000 **默认取值**: 不涉及 
        :type scanned_time: int
        """
        
        super().__init__()

        self._scan_status = None
        self._scanned_time = None
        self.discriminator = None

        if scan_status is not None:
            self.scan_status = scan_status
        if scanned_time is not None:
            self.scanned_time = scanned_time

    @property
    def scan_status(self):
        r"""Gets the scan_status of this ShowBaselineScanStatusResponse.

        **参数解释**: 扫描状态 **约束限制**: 不涉及 **取值范围**: - neverscan: 未扫描 - scanning: 扫描中 - scanned: 扫描完成 - failed: 扫描失败  **默认取值**: 不涉及 

        :return: The scan_status of this ShowBaselineScanStatusResponse.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this ShowBaselineScanStatusResponse.

        **参数解释**: 扫描状态 **约束限制**: 不涉及 **取值范围**: - neverscan: 未扫描 - scanning: 扫描中 - scanned: 扫描完成 - failed: 扫描失败  **默认取值**: 不涉及 

        :param scan_status: The scan_status of this ShowBaselineScanStatusResponse.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def scanned_time(self):
        r"""Gets the scanned_time of this ShowBaselineScanStatusResponse.

        **参数解释**: 扫描结束时间，单位毫秒 **约束限制**: 不涉及 **取值范围**: 大小0-4070880000000 **默认取值**: 不涉及 

        :return: The scanned_time of this ShowBaselineScanStatusResponse.
        :rtype: int
        """
        return self._scanned_time

    @scanned_time.setter
    def scanned_time(self, scanned_time):
        r"""Sets the scanned_time of this ShowBaselineScanStatusResponse.

        **参数解释**: 扫描结束时间，单位毫秒 **约束限制**: 不涉及 **取值范围**: 大小0-4070880000000 **默认取值**: 不涉及 

        :param scanned_time: The scanned_time of this ShowBaselineScanStatusResponse.
        :type scanned_time: int
        """
        self._scanned_time = scanned_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowBaselineScanStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowBaselineScanStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
