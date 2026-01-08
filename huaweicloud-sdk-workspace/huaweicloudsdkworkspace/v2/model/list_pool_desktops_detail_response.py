# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoolDesktopsDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_desktops': 'list[PoolDesktopsDetailInfo]',
        'total_count': 'int',
        'on_demand_desktops_num': 'int',
        'period_desktops_num': 'int',
        'inconsistent_type': 'str'
    }

    attribute_map = {
        'pool_desktops': 'pool_desktops',
        'total_count': 'total_count',
        'on_demand_desktops_num': 'on_demand_desktops_num',
        'period_desktops_num': 'period_desktops_num',
        'inconsistent_type': 'inconsistent_type'
    }

    def __init__(self, pool_desktops=None, total_count=None, on_demand_desktops_num=None, period_desktops_num=None, inconsistent_type=None):
        r"""ListPoolDesktopsDetailResponse

        The model defined in huaweicloud sdk

        :param pool_desktops: 池桌面详情。
        :type pool_desktops: list[:class:`huaweicloudsdkworkspace.v2.PoolDesktopsDetailInfo`]
        :param total_count: 桌面总数。
        :type total_count: int
        :param on_demand_desktops_num: 按需桌面总数。
        :type on_demand_desktops_num: int
        :param period_desktops_num: 包周期桌面总数。
        :type period_desktops_num: int
        :param inconsistent_type: 通过该类型过滤出与桌面池规格类型不一致的桌面 - product_id: 查找productID与桌面池套餐ID不一致的桌面 - image_id: 查找imageID与桌面池镜像ID不一致的桌面 - disk_num: 查找数据盘数量与桌面池配置不一致的桌面 - disk_size: 查找磁盘累加容量与桌面池配置不一致的桌面
        :type inconsistent_type: str
        """
        
        super().__init__()

        self._pool_desktops = None
        self._total_count = None
        self._on_demand_desktops_num = None
        self._period_desktops_num = None
        self._inconsistent_type = None
        self.discriminator = None

        if pool_desktops is not None:
            self.pool_desktops = pool_desktops
        if total_count is not None:
            self.total_count = total_count
        if on_demand_desktops_num is not None:
            self.on_demand_desktops_num = on_demand_desktops_num
        if period_desktops_num is not None:
            self.period_desktops_num = period_desktops_num
        if inconsistent_type is not None:
            self.inconsistent_type = inconsistent_type

    @property
    def pool_desktops(self):
        r"""Gets the pool_desktops of this ListPoolDesktopsDetailResponse.

        池桌面详情。

        :return: The pool_desktops of this ListPoolDesktopsDetailResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.PoolDesktopsDetailInfo`]
        """
        return self._pool_desktops

    @pool_desktops.setter
    def pool_desktops(self, pool_desktops):
        r"""Sets the pool_desktops of this ListPoolDesktopsDetailResponse.

        池桌面详情。

        :param pool_desktops: The pool_desktops of this ListPoolDesktopsDetailResponse.
        :type pool_desktops: list[:class:`huaweicloudsdkworkspace.v2.PoolDesktopsDetailInfo`]
        """
        self._pool_desktops = pool_desktops

    @property
    def total_count(self):
        r"""Gets the total_count of this ListPoolDesktopsDetailResponse.

        桌面总数。

        :return: The total_count of this ListPoolDesktopsDetailResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListPoolDesktopsDetailResponse.

        桌面总数。

        :param total_count: The total_count of this ListPoolDesktopsDetailResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def on_demand_desktops_num(self):
        r"""Gets the on_demand_desktops_num of this ListPoolDesktopsDetailResponse.

        按需桌面总数。

        :return: The on_demand_desktops_num of this ListPoolDesktopsDetailResponse.
        :rtype: int
        """
        return self._on_demand_desktops_num

    @on_demand_desktops_num.setter
    def on_demand_desktops_num(self, on_demand_desktops_num):
        r"""Sets the on_demand_desktops_num of this ListPoolDesktopsDetailResponse.

        按需桌面总数。

        :param on_demand_desktops_num: The on_demand_desktops_num of this ListPoolDesktopsDetailResponse.
        :type on_demand_desktops_num: int
        """
        self._on_demand_desktops_num = on_demand_desktops_num

    @property
    def period_desktops_num(self):
        r"""Gets the period_desktops_num of this ListPoolDesktopsDetailResponse.

        包周期桌面总数。

        :return: The period_desktops_num of this ListPoolDesktopsDetailResponse.
        :rtype: int
        """
        return self._period_desktops_num

    @period_desktops_num.setter
    def period_desktops_num(self, period_desktops_num):
        r"""Sets the period_desktops_num of this ListPoolDesktopsDetailResponse.

        包周期桌面总数。

        :param period_desktops_num: The period_desktops_num of this ListPoolDesktopsDetailResponse.
        :type period_desktops_num: int
        """
        self._period_desktops_num = period_desktops_num

    @property
    def inconsistent_type(self):
        r"""Gets the inconsistent_type of this ListPoolDesktopsDetailResponse.

        通过该类型过滤出与桌面池规格类型不一致的桌面 - product_id: 查找productID与桌面池套餐ID不一致的桌面 - image_id: 查找imageID与桌面池镜像ID不一致的桌面 - disk_num: 查找数据盘数量与桌面池配置不一致的桌面 - disk_size: 查找磁盘累加容量与桌面池配置不一致的桌面

        :return: The inconsistent_type of this ListPoolDesktopsDetailResponse.
        :rtype: str
        """
        return self._inconsistent_type

    @inconsistent_type.setter
    def inconsistent_type(self, inconsistent_type):
        r"""Sets the inconsistent_type of this ListPoolDesktopsDetailResponse.

        通过该类型过滤出与桌面池规格类型不一致的桌面 - product_id: 查找productID与桌面池套餐ID不一致的桌面 - image_id: 查找imageID与桌面池镜像ID不一致的桌面 - disk_num: 查找数据盘数量与桌面池配置不一致的桌面 - disk_size: 查找磁盘累加容量与桌面池配置不一致的桌面

        :param inconsistent_type: The inconsistent_type of this ListPoolDesktopsDetailResponse.
        :type inconsistent_type: str
        """
        self._inconsistent_type = inconsistent_type

    def to_dict(self):
        import warnings
        warnings.warn("ListPoolDesktopsDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListPoolDesktopsDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
