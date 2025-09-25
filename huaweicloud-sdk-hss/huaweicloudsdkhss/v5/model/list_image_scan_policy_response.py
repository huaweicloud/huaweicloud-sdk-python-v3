# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageScanPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_all': 'bool',
        'enabled': 'bool',
        'scan_cycle': 'int',
        'scan_scope': 'int',
        'rate_limit': 'int',
        'time_scope': 'int',
        'total_registry_num': 'int',
        'registry_list': 'list[ImageScanPolicyRespInfoRegistryList]'
    }

    attribute_map = {
        'is_all': 'is_all',
        'enabled': 'enabled',
        'scan_cycle': 'scan_cycle',
        'scan_scope': 'scan_scope',
        'rate_limit': 'rate_limit',
        'time_scope': 'time_scope',
        'total_registry_num': 'total_registry_num',
        'registry_list': 'registry_list'
    }

    def __init__(self, is_all=None, enabled=None, scan_cycle=None, scan_scope=None, rate_limit=None, time_scope=None, total_registry_num=None, registry_list=None):
        r"""ListImageScanPolicyResponse

        The model defined in huaweicloud sdk

        :param is_all: 扫描全部镜像 | true:扫描全部镜像 false:指定镜像扫描
        :type is_all: bool
        :param enabled: 定时扫描策略开关
        :type enabled: bool
        :param scan_cycle: 定时扫描周期 | 3 每三天 7 每一周 14 每两周
        :type scan_cycle: int
        :param scan_scope: 扫描风险类型 | 0:无 0x0fffff:全部 0x0f0000:漏洞 0x00f000:基线检查 0x000f00:恶意文件 0x0000f0:敏感信息 0x00000f:软件合规
        :type scan_scope: int
        :param rate_limit: 扫描限速 单位：个/h | 0 不限制
        :type rate_limit: int
        :param time_scope: 时间范围 单位：天 | 0 全部镜像 1 3 7
        :type time_scope: int
        :param total_registry_num: 镜像仓库列表总数
        :type total_registry_num: int
        :param registry_list: 镜像列表
        :type registry_list: list[:class:`huaweicloudsdkhss.v5.ImageScanPolicyRespInfoRegistryList`]
        """
        
        super(ListImageScanPolicyResponse, self).__init__()

        self._is_all = None
        self._enabled = None
        self._scan_cycle = None
        self._scan_scope = None
        self._rate_limit = None
        self._time_scope = None
        self._total_registry_num = None
        self._registry_list = None
        self.discriminator = None

        if is_all is not None:
            self.is_all = is_all
        if enabled is not None:
            self.enabled = enabled
        if scan_cycle is not None:
            self.scan_cycle = scan_cycle
        if scan_scope is not None:
            self.scan_scope = scan_scope
        if rate_limit is not None:
            self.rate_limit = rate_limit
        if time_scope is not None:
            self.time_scope = time_scope
        if total_registry_num is not None:
            self.total_registry_num = total_registry_num
        if registry_list is not None:
            self.registry_list = registry_list

    @property
    def is_all(self):
        r"""Gets the is_all of this ListImageScanPolicyResponse.

        扫描全部镜像 | true:扫描全部镜像 false:指定镜像扫描

        :return: The is_all of this ListImageScanPolicyResponse.
        :rtype: bool
        """
        return self._is_all

    @is_all.setter
    def is_all(self, is_all):
        r"""Sets the is_all of this ListImageScanPolicyResponse.

        扫描全部镜像 | true:扫描全部镜像 false:指定镜像扫描

        :param is_all: The is_all of this ListImageScanPolicyResponse.
        :type is_all: bool
        """
        self._is_all = is_all

    @property
    def enabled(self):
        r"""Gets the enabled of this ListImageScanPolicyResponse.

        定时扫描策略开关

        :return: The enabled of this ListImageScanPolicyResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListImageScanPolicyResponse.

        定时扫描策略开关

        :param enabled: The enabled of this ListImageScanPolicyResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def scan_cycle(self):
        r"""Gets the scan_cycle of this ListImageScanPolicyResponse.

        定时扫描周期 | 3 每三天 7 每一周 14 每两周

        :return: The scan_cycle of this ListImageScanPolicyResponse.
        :rtype: int
        """
        return self._scan_cycle

    @scan_cycle.setter
    def scan_cycle(self, scan_cycle):
        r"""Sets the scan_cycle of this ListImageScanPolicyResponse.

        定时扫描周期 | 3 每三天 7 每一周 14 每两周

        :param scan_cycle: The scan_cycle of this ListImageScanPolicyResponse.
        :type scan_cycle: int
        """
        self._scan_cycle = scan_cycle

    @property
    def scan_scope(self):
        r"""Gets the scan_scope of this ListImageScanPolicyResponse.

        扫描风险类型 | 0:无 0x0fffff:全部 0x0f0000:漏洞 0x00f000:基线检查 0x000f00:恶意文件 0x0000f0:敏感信息 0x00000f:软件合规

        :return: The scan_scope of this ListImageScanPolicyResponse.
        :rtype: int
        """
        return self._scan_scope

    @scan_scope.setter
    def scan_scope(self, scan_scope):
        r"""Sets the scan_scope of this ListImageScanPolicyResponse.

        扫描风险类型 | 0:无 0x0fffff:全部 0x0f0000:漏洞 0x00f000:基线检查 0x000f00:恶意文件 0x0000f0:敏感信息 0x00000f:软件合规

        :param scan_scope: The scan_scope of this ListImageScanPolicyResponse.
        :type scan_scope: int
        """
        self._scan_scope = scan_scope

    @property
    def rate_limit(self):
        r"""Gets the rate_limit of this ListImageScanPolicyResponse.

        扫描限速 单位：个/h | 0 不限制

        :return: The rate_limit of this ListImageScanPolicyResponse.
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        r"""Sets the rate_limit of this ListImageScanPolicyResponse.

        扫描限速 单位：个/h | 0 不限制

        :param rate_limit: The rate_limit of this ListImageScanPolicyResponse.
        :type rate_limit: int
        """
        self._rate_limit = rate_limit

    @property
    def time_scope(self):
        r"""Gets the time_scope of this ListImageScanPolicyResponse.

        时间范围 单位：天 | 0 全部镜像 1 3 7

        :return: The time_scope of this ListImageScanPolicyResponse.
        :rtype: int
        """
        return self._time_scope

    @time_scope.setter
    def time_scope(self, time_scope):
        r"""Sets the time_scope of this ListImageScanPolicyResponse.

        时间范围 单位：天 | 0 全部镜像 1 3 7

        :param time_scope: The time_scope of this ListImageScanPolicyResponse.
        :type time_scope: int
        """
        self._time_scope = time_scope

    @property
    def total_registry_num(self):
        r"""Gets the total_registry_num of this ListImageScanPolicyResponse.

        镜像仓库列表总数

        :return: The total_registry_num of this ListImageScanPolicyResponse.
        :rtype: int
        """
        return self._total_registry_num

    @total_registry_num.setter
    def total_registry_num(self, total_registry_num):
        r"""Sets the total_registry_num of this ListImageScanPolicyResponse.

        镜像仓库列表总数

        :param total_registry_num: The total_registry_num of this ListImageScanPolicyResponse.
        :type total_registry_num: int
        """
        self._total_registry_num = total_registry_num

    @property
    def registry_list(self):
        r"""Gets the registry_list of this ListImageScanPolicyResponse.

        镜像列表

        :return: The registry_list of this ListImageScanPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ImageScanPolicyRespInfoRegistryList`]
        """
        return self._registry_list

    @registry_list.setter
    def registry_list(self, registry_list):
        r"""Sets the registry_list of this ListImageScanPolicyResponse.

        镜像列表

        :param registry_list: The registry_list of this ListImageScanPolicyResponse.
        :type registry_list: list[:class:`huaweicloudsdkhss.v5.ImageScanPolicyRespInfoRegistryList`]
        """
        self._registry_list = registry_list

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
        if not isinstance(other, ListImageScanPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
