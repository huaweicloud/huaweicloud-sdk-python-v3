# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulAffectedStaticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_num': 'int',
        'host_num': 'int',
        'image_num': 'int',
        'container_num': 'int',
        'data_list': 'list[VulAffectedStatisticsResponseInfoDataList]',
        'total_vul_num': 'int',
        'extend_tips': 'list[str]',
        'extend_text_tips': 'list[str]',
        'disabled_operate_types': 'VulAffectedStatisticsResponseInfoDisabledOperateTypes',
        'cce_vul_num': 'int',
        'basic_host_num': 'int',
        'cce_disabled_vul_list': 'list[VulAffectedStatisticsResponseInfoCceDisabledVulList]'
    }

    attribute_map = {
        'vul_num': 'vul_num',
        'host_num': 'host_num',
        'image_num': 'image_num',
        'container_num': 'container_num',
        'data_list': 'data_list',
        'total_vul_num': 'total_vul_num',
        'extend_tips': 'extend_tips',
        'extend_text_tips': 'extend_text_tips',
        'disabled_operate_types': 'disabled_operate_types',
        'cce_vul_num': 'cce_vul_num',
        'basic_host_num': 'basic_host_num',
        'cce_disabled_vul_list': 'cce_disabled_vul_list'
    }

    def __init__(self, vul_num=None, host_num=None, image_num=None, container_num=None, data_list=None, total_vul_num=None, extend_tips=None, extend_text_tips=None, disabled_operate_types=None, cce_vul_num=None, basic_host_num=None, cce_disabled_vul_list=None):
        r"""ShowVulAffectedStaticsResponse

        The model defined in huaweicloud sdk

        :param vul_num: **参数解释**: 影响的漏洞数量(按漏洞编号计算) **取值范围**: 最小值0，最大值2147483647 
        :type vul_num: int
        :param host_num: **参数解释**: 影响主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type host_num: int
        :param image_num: **参数解释**: 影响镜像数量 **取值范围**: 最小值0，最大值2147483647 
        :type image_num: int
        :param container_num: **参数解释**: 影响容器数量 **取值范围**: 最小值0，最大值2147483647 
        :type container_num: int
        :param data_list: **参数解释**: 按漏洞类型的统计值，当select_type为all_host或空时，有该字段 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulAffectedStatisticsResponseInfoDataList`]
        :param total_vul_num: **参数解释**: 影响的总漏洞条数(主机+漏洞 以此维度计算) **取值范围**: 最小值0，最大值2147483647 
        :type total_vul_num: int
        :param extend_tips: **参数解释**: 提示 
        :type extend_tips: list[str]
        :param extend_text_tips: **参数解释**: 漏洞修复提示 **取值范围**: 最小值1，最大值500 
        :type extend_text_tips: list[str]
        :param disabled_operate_types: 
        :type disabled_operate_types: :class:`huaweicloudsdkhss.v5.VulAffectedStatisticsResponseInfoDisabledOperateTypes`
        :param cce_vul_num: **参数解释**: CCE漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type cce_vul_num: int
        :param basic_host_num: **参数解释**: 基础版主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type basic_host_num: int
        :param cce_disabled_vul_list: **参数解释**: CCE主机漏洞禁止修复列表 
        :type cce_disabled_vul_list: list[:class:`huaweicloudsdkhss.v5.VulAffectedStatisticsResponseInfoCceDisabledVulList`]
        """
        
        super().__init__()

        self._vul_num = None
        self._host_num = None
        self._image_num = None
        self._container_num = None
        self._data_list = None
        self._total_vul_num = None
        self._extend_tips = None
        self._extend_text_tips = None
        self._disabled_operate_types = None
        self._cce_vul_num = None
        self._basic_host_num = None
        self._cce_disabled_vul_list = None
        self.discriminator = None

        if vul_num is not None:
            self.vul_num = vul_num
        if host_num is not None:
            self.host_num = host_num
        if image_num is not None:
            self.image_num = image_num
        if container_num is not None:
            self.container_num = container_num
        if data_list is not None:
            self.data_list = data_list
        if total_vul_num is not None:
            self.total_vul_num = total_vul_num
        if extend_tips is not None:
            self.extend_tips = extend_tips
        if extend_text_tips is not None:
            self.extend_text_tips = extend_text_tips
        if disabled_operate_types is not None:
            self.disabled_operate_types = disabled_operate_types
        if cce_vul_num is not None:
            self.cce_vul_num = cce_vul_num
        if basic_host_num is not None:
            self.basic_host_num = basic_host_num
        if cce_disabled_vul_list is not None:
            self.cce_disabled_vul_list = cce_disabled_vul_list

    @property
    def vul_num(self):
        r"""Gets the vul_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 影响的漏洞数量(按漏洞编号计算) **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_num of this ShowVulAffectedStaticsResponse.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 影响的漏洞数量(按漏洞编号计算) **取值范围**: 最小值0，最大值2147483647 

        :param vul_num: The vul_num of this ShowVulAffectedStaticsResponse.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def host_num(self):
        r"""Gets the host_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 影响主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The host_num of this ShowVulAffectedStaticsResponse.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 影响主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param host_num: The host_num of this ShowVulAffectedStaticsResponse.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def image_num(self):
        r"""Gets the image_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 影响镜像数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The image_num of this ShowVulAffectedStaticsResponse.
        :rtype: int
        """
        return self._image_num

    @image_num.setter
    def image_num(self, image_num):
        r"""Sets the image_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 影响镜像数量 **取值范围**: 最小值0，最大值2147483647 

        :param image_num: The image_num of this ShowVulAffectedStaticsResponse.
        :type image_num: int
        """
        self._image_num = image_num

    @property
    def container_num(self):
        r"""Gets the container_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 影响容器数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The container_num of this ShowVulAffectedStaticsResponse.
        :rtype: int
        """
        return self._container_num

    @container_num.setter
    def container_num(self, container_num):
        r"""Sets the container_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 影响容器数量 **取值范围**: 最小值0，最大值2147483647 

        :param container_num: The container_num of this ShowVulAffectedStaticsResponse.
        :type container_num: int
        """
        self._container_num = container_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ShowVulAffectedStaticsResponse.

        **参数解释**: 按漏洞类型的统计值，当select_type为all_host或空时，有该字段 

        :return: The data_list of this ShowVulAffectedStaticsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulAffectedStatisticsResponseInfoDataList`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ShowVulAffectedStaticsResponse.

        **参数解释**: 按漏洞类型的统计值，当select_type为all_host或空时，有该字段 

        :param data_list: The data_list of this ShowVulAffectedStaticsResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulAffectedStatisticsResponseInfoDataList`]
        """
        self._data_list = data_list

    @property
    def total_vul_num(self):
        r"""Gets the total_vul_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 影响的总漏洞条数(主机+漏洞 以此维度计算) **取值范围**: 最小值0，最大值2147483647 

        :return: The total_vul_num of this ShowVulAffectedStaticsResponse.
        :rtype: int
        """
        return self._total_vul_num

    @total_vul_num.setter
    def total_vul_num(self, total_vul_num):
        r"""Sets the total_vul_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 影响的总漏洞条数(主机+漏洞 以此维度计算) **取值范围**: 最小值0，最大值2147483647 

        :param total_vul_num: The total_vul_num of this ShowVulAffectedStaticsResponse.
        :type total_vul_num: int
        """
        self._total_vul_num = total_vul_num

    @property
    def extend_tips(self):
        r"""Gets the extend_tips of this ShowVulAffectedStaticsResponse.

        **参数解释**: 提示 

        :return: The extend_tips of this ShowVulAffectedStaticsResponse.
        :rtype: list[str]
        """
        return self._extend_tips

    @extend_tips.setter
    def extend_tips(self, extend_tips):
        r"""Sets the extend_tips of this ShowVulAffectedStaticsResponse.

        **参数解释**: 提示 

        :param extend_tips: The extend_tips of this ShowVulAffectedStaticsResponse.
        :type extend_tips: list[str]
        """
        self._extend_tips = extend_tips

    @property
    def extend_text_tips(self):
        r"""Gets the extend_text_tips of this ShowVulAffectedStaticsResponse.

        **参数解释**: 漏洞修复提示 **取值范围**: 最小值1，最大值500 

        :return: The extend_text_tips of this ShowVulAffectedStaticsResponse.
        :rtype: list[str]
        """
        return self._extend_text_tips

    @extend_text_tips.setter
    def extend_text_tips(self, extend_text_tips):
        r"""Sets the extend_text_tips of this ShowVulAffectedStaticsResponse.

        **参数解释**: 漏洞修复提示 **取值范围**: 最小值1，最大值500 

        :param extend_text_tips: The extend_text_tips of this ShowVulAffectedStaticsResponse.
        :type extend_text_tips: list[str]
        """
        self._extend_text_tips = extend_text_tips

    @property
    def disabled_operate_types(self):
        r"""Gets the disabled_operate_types of this ShowVulAffectedStaticsResponse.

        :return: The disabled_operate_types of this ShowVulAffectedStaticsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.VulAffectedStatisticsResponseInfoDisabledOperateTypes`
        """
        return self._disabled_operate_types

    @disabled_operate_types.setter
    def disabled_operate_types(self, disabled_operate_types):
        r"""Sets the disabled_operate_types of this ShowVulAffectedStaticsResponse.

        :param disabled_operate_types: The disabled_operate_types of this ShowVulAffectedStaticsResponse.
        :type disabled_operate_types: :class:`huaweicloudsdkhss.v5.VulAffectedStatisticsResponseInfoDisabledOperateTypes`
        """
        self._disabled_operate_types = disabled_operate_types

    @property
    def cce_vul_num(self):
        r"""Gets the cce_vul_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: CCE漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The cce_vul_num of this ShowVulAffectedStaticsResponse.
        :rtype: int
        """
        return self._cce_vul_num

    @cce_vul_num.setter
    def cce_vul_num(self, cce_vul_num):
        r"""Sets the cce_vul_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: CCE漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param cce_vul_num: The cce_vul_num of this ShowVulAffectedStaticsResponse.
        :type cce_vul_num: int
        """
        self._cce_vul_num = cce_vul_num

    @property
    def basic_host_num(self):
        r"""Gets the basic_host_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 基础版主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The basic_host_num of this ShowVulAffectedStaticsResponse.
        :rtype: int
        """
        return self._basic_host_num

    @basic_host_num.setter
    def basic_host_num(self, basic_host_num):
        r"""Sets the basic_host_num of this ShowVulAffectedStaticsResponse.

        **参数解释**: 基础版主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param basic_host_num: The basic_host_num of this ShowVulAffectedStaticsResponse.
        :type basic_host_num: int
        """
        self._basic_host_num = basic_host_num

    @property
    def cce_disabled_vul_list(self):
        r"""Gets the cce_disabled_vul_list of this ShowVulAffectedStaticsResponse.

        **参数解释**: CCE主机漏洞禁止修复列表 

        :return: The cce_disabled_vul_list of this ShowVulAffectedStaticsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulAffectedStatisticsResponseInfoCceDisabledVulList`]
        """
        return self._cce_disabled_vul_list

    @cce_disabled_vul_list.setter
    def cce_disabled_vul_list(self, cce_disabled_vul_list):
        r"""Sets the cce_disabled_vul_list of this ShowVulAffectedStaticsResponse.

        **参数解释**: CCE主机漏洞禁止修复列表 

        :param cce_disabled_vul_list: The cce_disabled_vul_list of this ShowVulAffectedStaticsResponse.
        :type cce_disabled_vul_list: list[:class:`huaweicloudsdkhss.v5.VulAffectedStatisticsResponseInfoCceDisabledVulList`]
        """
        self._cce_disabled_vul_list = cce_disabled_vul_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowVulAffectedStaticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVulAffectedStaticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
