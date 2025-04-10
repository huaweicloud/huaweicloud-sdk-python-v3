# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DynamicMaskingPolicyCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_name': 'str',
        'column_type': 'str',
        'algorithm_type': 'str',
        'algorithm_detail': 'str',
        'algorithm_detail_dto': 'AlgorithmDetailDTO'
    }

    attribute_map = {
        'column_name': 'column_name',
        'column_type': 'column_type',
        'algorithm_type': 'algorithm_type',
        'algorithm_detail': 'algorithm_detail',
        'algorithm_detail_dto': 'algorithm_detail_dto'
    }

    def __init__(self, column_name=None, column_type=None, algorithm_type=None, algorithm_detail=None, algorithm_detail_dto=None):
        r"""DynamicMaskingPolicyCreate

        The model defined in huaweicloud sdk

        :param column_name: 数据表中的字段名称。
        :type column_name: str
        :param column_type: 数据表中字段的数据类型。
        :type column_type: str
        :param algorithm_type: 具体动态脱敏规则参数介绍请参见[动态脱敏规则介绍](dataartsstudio_01_1036.html)。 HIVE数据源动态脱敏算法 - MASK 掩盖英文字符和数字 - MASK_SHOW_LAST_4 保留后四位 - MASK_SHOW_FIRST_4 保留前四位 - MASK_HASH 哈希掩盖 - MASK_DATE_SHOW_YEAR 掩盖月份和日期 - MASK_NULL NULL掩盖  DWS数据源动态脱敏算法 - DWS_ALL_MASK 全掩码 - DWS_BACK_KEEP 保留后4位，其余脱敏为* - DWS_FRONT_KEEP 保留前2位，其余脱敏为* - DWS_SELF_CONFIG 需要输入开始位置、结束位置、脱敏字符传入detail结构体中，例如{\&quot;start\&quot;: 1, \&quot;end\&quot;: 2, \&quot;string_target\&quot;: \&quot;*\&quot;}  [DLI数据源动态脱敏算法](tag:nohcs) - [MASK 掩盖英文字符和数字](tag:nohcs) - [MASK_SHOW_LAST_4 保留后四位](tag:nohcs) - [MASK_SHOW_FIRST_4 保留前四位](tag:nohcs) - [MASK_HASH 哈希掩盖](tag:nohcs) - [MASK_DATE_SHOW_YEAR 掩盖月份和日期](tag:nohcs) - [MASK_NULL NULL掩盖](tag:nohcs)
        :type algorithm_type: str
        :param algorithm_detail: 动态脱敏策略算法详情。
        :type algorithm_detail: str
        :param algorithm_detail_dto: 
        :type algorithm_detail_dto: :class:`huaweicloudsdkdataartsstudio.v1.AlgorithmDetailDTO`
        """
        
        

        self._column_name = None
        self._column_type = None
        self._algorithm_type = None
        self._algorithm_detail = None
        self._algorithm_detail_dto = None
        self.discriminator = None

        self.column_name = column_name
        self.column_type = column_type
        if algorithm_type is not None:
            self.algorithm_type = algorithm_type
        if algorithm_detail is not None:
            self.algorithm_detail = algorithm_detail
        if algorithm_detail_dto is not None:
            self.algorithm_detail_dto = algorithm_detail_dto

    @property
    def column_name(self):
        r"""Gets the column_name of this DynamicMaskingPolicyCreate.

        数据表中的字段名称。

        :return: The column_name of this DynamicMaskingPolicyCreate.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this DynamicMaskingPolicyCreate.

        数据表中的字段名称。

        :param column_name: The column_name of this DynamicMaskingPolicyCreate.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_type(self):
        r"""Gets the column_type of this DynamicMaskingPolicyCreate.

        数据表中字段的数据类型。

        :return: The column_type of this DynamicMaskingPolicyCreate.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        r"""Sets the column_type of this DynamicMaskingPolicyCreate.

        数据表中字段的数据类型。

        :param column_type: The column_type of this DynamicMaskingPolicyCreate.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def algorithm_type(self):
        r"""Gets the algorithm_type of this DynamicMaskingPolicyCreate.

        具体动态脱敏规则参数介绍请参见[动态脱敏规则介绍](dataartsstudio_01_1036.html)。 HIVE数据源动态脱敏算法 - MASK 掩盖英文字符和数字 - MASK_SHOW_LAST_4 保留后四位 - MASK_SHOW_FIRST_4 保留前四位 - MASK_HASH 哈希掩盖 - MASK_DATE_SHOW_YEAR 掩盖月份和日期 - MASK_NULL NULL掩盖  DWS数据源动态脱敏算法 - DWS_ALL_MASK 全掩码 - DWS_BACK_KEEP 保留后4位，其余脱敏为* - DWS_FRONT_KEEP 保留前2位，其余脱敏为* - DWS_SELF_CONFIG 需要输入开始位置、结束位置、脱敏字符传入detail结构体中，例如{\"start\": 1, \"end\": 2, \"string_target\": \"*\"}  [DLI数据源动态脱敏算法](tag:nohcs) - [MASK 掩盖英文字符和数字](tag:nohcs) - [MASK_SHOW_LAST_4 保留后四位](tag:nohcs) - [MASK_SHOW_FIRST_4 保留前四位](tag:nohcs) - [MASK_HASH 哈希掩盖](tag:nohcs) - [MASK_DATE_SHOW_YEAR 掩盖月份和日期](tag:nohcs) - [MASK_NULL NULL掩盖](tag:nohcs)

        :return: The algorithm_type of this DynamicMaskingPolicyCreate.
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        r"""Sets the algorithm_type of this DynamicMaskingPolicyCreate.

        具体动态脱敏规则参数介绍请参见[动态脱敏规则介绍](dataartsstudio_01_1036.html)。 HIVE数据源动态脱敏算法 - MASK 掩盖英文字符和数字 - MASK_SHOW_LAST_4 保留后四位 - MASK_SHOW_FIRST_4 保留前四位 - MASK_HASH 哈希掩盖 - MASK_DATE_SHOW_YEAR 掩盖月份和日期 - MASK_NULL NULL掩盖  DWS数据源动态脱敏算法 - DWS_ALL_MASK 全掩码 - DWS_BACK_KEEP 保留后4位，其余脱敏为* - DWS_FRONT_KEEP 保留前2位，其余脱敏为* - DWS_SELF_CONFIG 需要输入开始位置、结束位置、脱敏字符传入detail结构体中，例如{\"start\": 1, \"end\": 2, \"string_target\": \"*\"}  [DLI数据源动态脱敏算法](tag:nohcs) - [MASK 掩盖英文字符和数字](tag:nohcs) - [MASK_SHOW_LAST_4 保留后四位](tag:nohcs) - [MASK_SHOW_FIRST_4 保留前四位](tag:nohcs) - [MASK_HASH 哈希掩盖](tag:nohcs) - [MASK_DATE_SHOW_YEAR 掩盖月份和日期](tag:nohcs) - [MASK_NULL NULL掩盖](tag:nohcs)

        :param algorithm_type: The algorithm_type of this DynamicMaskingPolicyCreate.
        :type algorithm_type: str
        """
        self._algorithm_type = algorithm_type

    @property
    def algorithm_detail(self):
        r"""Gets the algorithm_detail of this DynamicMaskingPolicyCreate.

        动态脱敏策略算法详情。

        :return: The algorithm_detail of this DynamicMaskingPolicyCreate.
        :rtype: str
        """
        return self._algorithm_detail

    @algorithm_detail.setter
    def algorithm_detail(self, algorithm_detail):
        r"""Sets the algorithm_detail of this DynamicMaskingPolicyCreate.

        动态脱敏策略算法详情。

        :param algorithm_detail: The algorithm_detail of this DynamicMaskingPolicyCreate.
        :type algorithm_detail: str
        """
        self._algorithm_detail = algorithm_detail

    @property
    def algorithm_detail_dto(self):
        r"""Gets the algorithm_detail_dto of this DynamicMaskingPolicyCreate.

        :return: The algorithm_detail_dto of this DynamicMaskingPolicyCreate.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AlgorithmDetailDTO`
        """
        return self._algorithm_detail_dto

    @algorithm_detail_dto.setter
    def algorithm_detail_dto(self, algorithm_detail_dto):
        r"""Sets the algorithm_detail_dto of this DynamicMaskingPolicyCreate.

        :param algorithm_detail_dto: The algorithm_detail_dto of this DynamicMaskingPolicyCreate.
        :type algorithm_detail_dto: :class:`huaweicloudsdkdataartsstudio.v1.AlgorithmDetailDTO`
        """
        self._algorithm_detail_dto = algorithm_detail_dto

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
        if not isinstance(other, DynamicMaskingPolicyCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
