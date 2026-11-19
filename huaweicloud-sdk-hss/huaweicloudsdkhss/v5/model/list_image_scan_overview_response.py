# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageScanOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_image_num': 'int',
        'risky_image_num': 'int',
        'vuls_num': 'int',
        'risky_config_num': 'int',
        'malwares_num': 'int',
        'unscanned_num': 'int',
        'scanning_task_num': 'int',
        'finished_task_num': 'int',
        'latest_scan_time': 'int',
        'local_scanning_task_num': 'int',
        'local_finished_task_num': 'int'
    }

    attribute_map = {
        'total_image_num': 'total_image_num',
        'risky_image_num': 'risky_image_num',
        'vuls_num': 'vuls_num',
        'risky_config_num': 'risky_config_num',
        'malwares_num': 'malwares_num',
        'unscanned_num': 'unscanned_num',
        'scanning_task_num': 'scanning_task_num',
        'finished_task_num': 'finished_task_num',
        'latest_scan_time': 'latest_scan_time',
        'local_scanning_task_num': 'local_scanning_task_num',
        'local_finished_task_num': 'local_finished_task_num'
    }

    def __init__(self, total_image_num=None, risky_image_num=None, vuls_num=None, risky_config_num=None, malwares_num=None, unscanned_num=None, scanning_task_num=None, finished_task_num=None, latest_scan_time=None, local_scanning_task_num=None, local_finished_task_num=None):
        r"""ListImageScanOverviewResponse

        The model defined in huaweicloud sdk

        :param total_image_num: **参数解释**: 镜像总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_image_num: int
        :param risky_image_num: **参数解释**: 存在风险的镜像数 **取值范围**: 最小值0，最大值2147483647 
        :type risky_image_num: int
        :param vuls_num: **参数解释**: 漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type vuls_num: int
        :param risky_config_num: **参数解释**: 风险配置数 **取值范围**: 最小值0，最大值2147483647 
        :type risky_config_num: int
        :param malwares_num: **参数解释**: 恶意文件数 **取值范围**: 最小值0，最大值2147483647 
        :type malwares_num: int
        :param unscanned_num: **参数解释**: 未扫描数 **取值范围**: 最小值0，最大值2147483647 
        :type unscanned_num: int
        :param scanning_task_num: **参数解释**: 扫描中任务数 **取值范围**: 最小值0，最大值2147483647 
        :type scanning_task_num: int
        :param finished_task_num: **参数解释**: 已完成任务数 **取值范围**: 最小值0，最大值2147483647 
        :type finished_task_num: int
        :param latest_scan_time: **参数解释**: 最近扫描时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 
        :type latest_scan_time: int
        :param local_scanning_task_num: **参数解释**: 本地扫描中任务数 **取值范围**: 最小值0，最大值2147483647 
        :type local_scanning_task_num: int
        :param local_finished_task_num: **参数解释**: 本地已完成任务数 **取值范围**: 最小值0，最大值2147483647 
        :type local_finished_task_num: int
        """
        
        super().__init__()

        self._total_image_num = None
        self._risky_image_num = None
        self._vuls_num = None
        self._risky_config_num = None
        self._malwares_num = None
        self._unscanned_num = None
        self._scanning_task_num = None
        self._finished_task_num = None
        self._latest_scan_time = None
        self._local_scanning_task_num = None
        self._local_finished_task_num = None
        self.discriminator = None

        if total_image_num is not None:
            self.total_image_num = total_image_num
        if risky_image_num is not None:
            self.risky_image_num = risky_image_num
        if vuls_num is not None:
            self.vuls_num = vuls_num
        if risky_config_num is not None:
            self.risky_config_num = risky_config_num
        if malwares_num is not None:
            self.malwares_num = malwares_num
        if unscanned_num is not None:
            self.unscanned_num = unscanned_num
        if scanning_task_num is not None:
            self.scanning_task_num = scanning_task_num
        if finished_task_num is not None:
            self.finished_task_num = finished_task_num
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if local_scanning_task_num is not None:
            self.local_scanning_task_num = local_scanning_task_num
        if local_finished_task_num is not None:
            self.local_finished_task_num = local_finished_task_num

    @property
    def total_image_num(self):
        r"""Gets the total_image_num of this ListImageScanOverviewResponse.

        **参数解释**: 镜像总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_image_num of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._total_image_num

    @total_image_num.setter
    def total_image_num(self, total_image_num):
        r"""Sets the total_image_num of this ListImageScanOverviewResponse.

        **参数解释**: 镜像总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_image_num: The total_image_num of this ListImageScanOverviewResponse.
        :type total_image_num: int
        """
        self._total_image_num = total_image_num

    @property
    def risky_image_num(self):
        r"""Gets the risky_image_num of this ListImageScanOverviewResponse.

        **参数解释**: 存在风险的镜像数 **取值范围**: 最小值0，最大值2147483647 

        :return: The risky_image_num of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._risky_image_num

    @risky_image_num.setter
    def risky_image_num(self, risky_image_num):
        r"""Sets the risky_image_num of this ListImageScanOverviewResponse.

        **参数解释**: 存在风险的镜像数 **取值范围**: 最小值0，最大值2147483647 

        :param risky_image_num: The risky_image_num of this ListImageScanOverviewResponse.
        :type risky_image_num: int
        """
        self._risky_image_num = risky_image_num

    @property
    def vuls_num(self):
        r"""Gets the vuls_num of this ListImageScanOverviewResponse.

        **参数解释**: 漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The vuls_num of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._vuls_num

    @vuls_num.setter
    def vuls_num(self, vuls_num):
        r"""Sets the vuls_num of this ListImageScanOverviewResponse.

        **参数解释**: 漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param vuls_num: The vuls_num of this ListImageScanOverviewResponse.
        :type vuls_num: int
        """
        self._vuls_num = vuls_num

    @property
    def risky_config_num(self):
        r"""Gets the risky_config_num of this ListImageScanOverviewResponse.

        **参数解释**: 风险配置数 **取值范围**: 最小值0，最大值2147483647 

        :return: The risky_config_num of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._risky_config_num

    @risky_config_num.setter
    def risky_config_num(self, risky_config_num):
        r"""Sets the risky_config_num of this ListImageScanOverviewResponse.

        **参数解释**: 风险配置数 **取值范围**: 最小值0，最大值2147483647 

        :param risky_config_num: The risky_config_num of this ListImageScanOverviewResponse.
        :type risky_config_num: int
        """
        self._risky_config_num = risky_config_num

    @property
    def malwares_num(self):
        r"""Gets the malwares_num of this ListImageScanOverviewResponse.

        **参数解释**: 恶意文件数 **取值范围**: 最小值0，最大值2147483647 

        :return: The malwares_num of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._malwares_num

    @malwares_num.setter
    def malwares_num(self, malwares_num):
        r"""Sets the malwares_num of this ListImageScanOverviewResponse.

        **参数解释**: 恶意文件数 **取值范围**: 最小值0，最大值2147483647 

        :param malwares_num: The malwares_num of this ListImageScanOverviewResponse.
        :type malwares_num: int
        """
        self._malwares_num = malwares_num

    @property
    def unscanned_num(self):
        r"""Gets the unscanned_num of this ListImageScanOverviewResponse.

        **参数解释**: 未扫描数 **取值范围**: 最小值0，最大值2147483647 

        :return: The unscanned_num of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._unscanned_num

    @unscanned_num.setter
    def unscanned_num(self, unscanned_num):
        r"""Sets the unscanned_num of this ListImageScanOverviewResponse.

        **参数解释**: 未扫描数 **取值范围**: 最小值0，最大值2147483647 

        :param unscanned_num: The unscanned_num of this ListImageScanOverviewResponse.
        :type unscanned_num: int
        """
        self._unscanned_num = unscanned_num

    @property
    def scanning_task_num(self):
        r"""Gets the scanning_task_num of this ListImageScanOverviewResponse.

        **参数解释**: 扫描中任务数 **取值范围**: 最小值0，最大值2147483647 

        :return: The scanning_task_num of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._scanning_task_num

    @scanning_task_num.setter
    def scanning_task_num(self, scanning_task_num):
        r"""Sets the scanning_task_num of this ListImageScanOverviewResponse.

        **参数解释**: 扫描中任务数 **取值范围**: 最小值0，最大值2147483647 

        :param scanning_task_num: The scanning_task_num of this ListImageScanOverviewResponse.
        :type scanning_task_num: int
        """
        self._scanning_task_num = scanning_task_num

    @property
    def finished_task_num(self):
        r"""Gets the finished_task_num of this ListImageScanOverviewResponse.

        **参数解释**: 已完成任务数 **取值范围**: 最小值0，最大值2147483647 

        :return: The finished_task_num of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._finished_task_num

    @finished_task_num.setter
    def finished_task_num(self, finished_task_num):
        r"""Sets the finished_task_num of this ListImageScanOverviewResponse.

        **参数解释**: 已完成任务数 **取值范围**: 最小值0，最大值2147483647 

        :param finished_task_num: The finished_task_num of this ListImageScanOverviewResponse.
        :type finished_task_num: int
        """
        self._finished_task_num = finished_task_num

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this ListImageScanOverviewResponse.

        **参数解释**: 最近扫描时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The latest_scan_time of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this ListImageScanOverviewResponse.

        **参数解释**: 最近扫描时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :param latest_scan_time: The latest_scan_time of this ListImageScanOverviewResponse.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def local_scanning_task_num(self):
        r"""Gets the local_scanning_task_num of this ListImageScanOverviewResponse.

        **参数解释**: 本地扫描中任务数 **取值范围**: 最小值0，最大值2147483647 

        :return: The local_scanning_task_num of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._local_scanning_task_num

    @local_scanning_task_num.setter
    def local_scanning_task_num(self, local_scanning_task_num):
        r"""Sets the local_scanning_task_num of this ListImageScanOverviewResponse.

        **参数解释**: 本地扫描中任务数 **取值范围**: 最小值0，最大值2147483647 

        :param local_scanning_task_num: The local_scanning_task_num of this ListImageScanOverviewResponse.
        :type local_scanning_task_num: int
        """
        self._local_scanning_task_num = local_scanning_task_num

    @property
    def local_finished_task_num(self):
        r"""Gets the local_finished_task_num of this ListImageScanOverviewResponse.

        **参数解释**: 本地已完成任务数 **取值范围**: 最小值0，最大值2147483647 

        :return: The local_finished_task_num of this ListImageScanOverviewResponse.
        :rtype: int
        """
        return self._local_finished_task_num

    @local_finished_task_num.setter
    def local_finished_task_num(self, local_finished_task_num):
        r"""Sets the local_finished_task_num of this ListImageScanOverviewResponse.

        **参数解释**: 本地已完成任务数 **取值范围**: 最小值0，最大值2147483647 

        :param local_finished_task_num: The local_finished_task_num of this ListImageScanOverviewResponse.
        :type local_finished_task_num: int
        """
        self._local_finished_task_num = local_finished_task_num

    def to_dict(self):
        import warnings
        warnings.warn("ListImageScanOverviewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListImageScanOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
