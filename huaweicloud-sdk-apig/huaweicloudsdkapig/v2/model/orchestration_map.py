# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrchestrationMap:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'map_param_list': 'list[str]',
        'map_param_range': 'OrchestrationMapParamRange',
        'mapped_param_value': 'str',
        'intercept_length': 'int'
    }

    attribute_map = {
        'map_param_list': 'map_param_list',
        'map_param_range': 'map_param_range',
        'mapped_param_value': 'mapped_param_value',
        'intercept_length': 'intercept_length'
    }

    def __init__(self, map_param_list=None, map_param_range=None, mapped_param_value=None, intercept_length=None):
        r"""OrchestrationMap

        The model defined in huaweicloud sdk

        :param map_param_list: 用于映射编排后参数的列表配置，当orchestration_strategy&#x3D;list时必填，列表长度范围为0-3000。  列表的取值只支持英文，数字，中划线和下划线，1-128个字符。
        :type map_param_list: list[str]
        :param map_param_range: 
        :type map_param_range: :class:`huaweicloudsdkapig.v2.OrchestrationMapParamRange`
        :param mapped_param_value: 编排后的参数取值，只支持英文和数字，1-128个字符。 当orchestration_strategy为hash、head_n、tail_n，或者is_preprocessing为false时，非必填，其他情况必填。
        :type mapped_param_value: str
        :param intercept_length: 截取长度，取值范围为1-100，当策略类型为head_n和tail_n时必填，当截取长度大于参数长度时，截取参数的结果为完整参数。
        :type intercept_length: int
        """
        
        

        self._map_param_list = None
        self._map_param_range = None
        self._mapped_param_value = None
        self._intercept_length = None
        self.discriminator = None

        if map_param_list is not None:
            self.map_param_list = map_param_list
        if map_param_range is not None:
            self.map_param_range = map_param_range
        if mapped_param_value is not None:
            self.mapped_param_value = mapped_param_value
        if intercept_length is not None:
            self.intercept_length = intercept_length

    @property
    def map_param_list(self):
        r"""Gets the map_param_list of this OrchestrationMap.

        用于映射编排后参数的列表配置，当orchestration_strategy=list时必填，列表长度范围为0-3000。  列表的取值只支持英文，数字，中划线和下划线，1-128个字符。

        :return: The map_param_list of this OrchestrationMap.
        :rtype: list[str]
        """
        return self._map_param_list

    @map_param_list.setter
    def map_param_list(self, map_param_list):
        r"""Sets the map_param_list of this OrchestrationMap.

        用于映射编排后参数的列表配置，当orchestration_strategy=list时必填，列表长度范围为0-3000。  列表的取值只支持英文，数字，中划线和下划线，1-128个字符。

        :param map_param_list: The map_param_list of this OrchestrationMap.
        :type map_param_list: list[str]
        """
        self._map_param_list = map_param_list

    @property
    def map_param_range(self):
        r"""Gets the map_param_range of this OrchestrationMap.

        :return: The map_param_range of this OrchestrationMap.
        :rtype: :class:`huaweicloudsdkapig.v2.OrchestrationMapParamRange`
        """
        return self._map_param_range

    @map_param_range.setter
    def map_param_range(self, map_param_range):
        r"""Sets the map_param_range of this OrchestrationMap.

        :param map_param_range: The map_param_range of this OrchestrationMap.
        :type map_param_range: :class:`huaweicloudsdkapig.v2.OrchestrationMapParamRange`
        """
        self._map_param_range = map_param_range

    @property
    def mapped_param_value(self):
        r"""Gets the mapped_param_value of this OrchestrationMap.

        编排后的参数取值，只支持英文和数字，1-128个字符。 当orchestration_strategy为hash、head_n、tail_n，或者is_preprocessing为false时，非必填，其他情况必填。

        :return: The mapped_param_value of this OrchestrationMap.
        :rtype: str
        """
        return self._mapped_param_value

    @mapped_param_value.setter
    def mapped_param_value(self, mapped_param_value):
        r"""Sets the mapped_param_value of this OrchestrationMap.

        编排后的参数取值，只支持英文和数字，1-128个字符。 当orchestration_strategy为hash、head_n、tail_n，或者is_preprocessing为false时，非必填，其他情况必填。

        :param mapped_param_value: The mapped_param_value of this OrchestrationMap.
        :type mapped_param_value: str
        """
        self._mapped_param_value = mapped_param_value

    @property
    def intercept_length(self):
        r"""Gets the intercept_length of this OrchestrationMap.

        截取长度，取值范围为1-100，当策略类型为head_n和tail_n时必填，当截取长度大于参数长度时，截取参数的结果为完整参数。

        :return: The intercept_length of this OrchestrationMap.
        :rtype: int
        """
        return self._intercept_length

    @intercept_length.setter
    def intercept_length(self, intercept_length):
        r"""Sets the intercept_length of this OrchestrationMap.

        截取长度，取值范围为1-100，当策略类型为head_n和tail_n时必填，当截取长度大于参数长度时，截取参数的结果为完整参数。

        :param intercept_length: The intercept_length of this OrchestrationMap.
        :type intercept_length: int
        """
        self._intercept_length = intercept_length

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
        if not isinstance(other, OrchestrationMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
