# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrchestrationBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'orchestration_name': 'str',
        'orchestration_strategy': 'str',
        'orchestration_mapped_param': 'OrchestrationMappedParam',
        'is_preprocessing': 'bool'
    }

    attribute_map = {
        'orchestration_name': 'orchestration_name',
        'orchestration_strategy': 'orchestration_strategy',
        'orchestration_mapped_param': 'orchestration_mapped_param',
        'is_preprocessing': 'is_preprocessing'
    }

    def __init__(self, orchestration_name=None, orchestration_strategy=None, orchestration_mapped_param=None, is_preprocessing=None):
        r"""OrchestrationBaseInfo

        The model defined in huaweicloud sdk

        :param orchestration_name: 编排映射规则名称。  支持英文，数字，下划线，且只能以英文开头，3-64个字符，同一实例下不允许重名。
        :type orchestration_name: str
        :param orchestration_strategy: 编排策略，有以下几种策略类型： - list：列表； - hash：哈希； - range：区间； - hash_range: 哈希+区间； - none_value: 空值映射； - default: 默认值映射； - head_n: 截取前n项； - tail_n: 截取后n项； 当编排策略为list时，orchestration_map列表长度*map_param_list长度不超过3000。
        :type orchestration_strategy: str
        :param orchestration_mapped_param: 
        :type orchestration_mapped_param: :class:`huaweicloudsdkapig.v2.OrchestrationMappedParam`
        :param is_preprocessing: 是否为预处理策略，预处理策略只会生成临时参数作为后面参数编排规则的入参标记。当为预处理策略时，该编排规则不能作为除default之外的最后一个编排规则。
        :type is_preprocessing: bool
        """
        
        

        self._orchestration_name = None
        self._orchestration_strategy = None
        self._orchestration_mapped_param = None
        self._is_preprocessing = None
        self.discriminator = None

        self.orchestration_name = orchestration_name
        self.orchestration_strategy = orchestration_strategy
        if orchestration_mapped_param is not None:
            self.orchestration_mapped_param = orchestration_mapped_param
        if is_preprocessing is not None:
            self.is_preprocessing = is_preprocessing

    @property
    def orchestration_name(self):
        r"""Gets the orchestration_name of this OrchestrationBaseInfo.

        编排映射规则名称。  支持英文，数字，下划线，且只能以英文开头，3-64个字符，同一实例下不允许重名。

        :return: The orchestration_name of this OrchestrationBaseInfo.
        :rtype: str
        """
        return self._orchestration_name

    @orchestration_name.setter
    def orchestration_name(self, orchestration_name):
        r"""Sets the orchestration_name of this OrchestrationBaseInfo.

        编排映射规则名称。  支持英文，数字，下划线，且只能以英文开头，3-64个字符，同一实例下不允许重名。

        :param orchestration_name: The orchestration_name of this OrchestrationBaseInfo.
        :type orchestration_name: str
        """
        self._orchestration_name = orchestration_name

    @property
    def orchestration_strategy(self):
        r"""Gets the orchestration_strategy of this OrchestrationBaseInfo.

        编排策略，有以下几种策略类型： - list：列表； - hash：哈希； - range：区间； - hash_range: 哈希+区间； - none_value: 空值映射； - default: 默认值映射； - head_n: 截取前n项； - tail_n: 截取后n项； 当编排策略为list时，orchestration_map列表长度*map_param_list长度不超过3000。

        :return: The orchestration_strategy of this OrchestrationBaseInfo.
        :rtype: str
        """
        return self._orchestration_strategy

    @orchestration_strategy.setter
    def orchestration_strategy(self, orchestration_strategy):
        r"""Sets the orchestration_strategy of this OrchestrationBaseInfo.

        编排策略，有以下几种策略类型： - list：列表； - hash：哈希； - range：区间； - hash_range: 哈希+区间； - none_value: 空值映射； - default: 默认值映射； - head_n: 截取前n项； - tail_n: 截取后n项； 当编排策略为list时，orchestration_map列表长度*map_param_list长度不超过3000。

        :param orchestration_strategy: The orchestration_strategy of this OrchestrationBaseInfo.
        :type orchestration_strategy: str
        """
        self._orchestration_strategy = orchestration_strategy

    @property
    def orchestration_mapped_param(self):
        r"""Gets the orchestration_mapped_param of this OrchestrationBaseInfo.

        :return: The orchestration_mapped_param of this OrchestrationBaseInfo.
        :rtype: :class:`huaweicloudsdkapig.v2.OrchestrationMappedParam`
        """
        return self._orchestration_mapped_param

    @orchestration_mapped_param.setter
    def orchestration_mapped_param(self, orchestration_mapped_param):
        r"""Sets the orchestration_mapped_param of this OrchestrationBaseInfo.

        :param orchestration_mapped_param: The orchestration_mapped_param of this OrchestrationBaseInfo.
        :type orchestration_mapped_param: :class:`huaweicloudsdkapig.v2.OrchestrationMappedParam`
        """
        self._orchestration_mapped_param = orchestration_mapped_param

    @property
    def is_preprocessing(self):
        r"""Gets the is_preprocessing of this OrchestrationBaseInfo.

        是否为预处理策略，预处理策略只会生成临时参数作为后面参数编排规则的入参标记。当为预处理策略时，该编排规则不能作为除default之外的最后一个编排规则。

        :return: The is_preprocessing of this OrchestrationBaseInfo.
        :rtype: bool
        """
        return self._is_preprocessing

    @is_preprocessing.setter
    def is_preprocessing(self, is_preprocessing):
        r"""Sets the is_preprocessing of this OrchestrationBaseInfo.

        是否为预处理策略，预处理策略只会生成临时参数作为后面参数编排规则的入参标记。当为预处理策略时，该编排规则不能作为除default之外的最后一个编排规则。

        :param is_preprocessing: The is_preprocessing of this OrchestrationBaseInfo.
        :type is_preprocessing: bool
        """
        self._is_preprocessing = is_preprocessing

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
        if not isinstance(other, OrchestrationBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
