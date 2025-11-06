# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllRiskConfigCheckRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'pass_num': 'int',
        'failed_num': 'int',
        'processed_num': 'int',
        'data_list': 'list[CheckRulesResponseInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'pass_num': 'pass_num',
        'failed_num': 'failed_num',
        'processed_num': 'processed_num',
        'data_list': 'data_list'
    }

    def __init__(self, total_num=None, pass_num=None, failed_num=None, processed_num=None, data_list=None):
        r"""ListAllRiskConfigCheckRulesResponse

        The model defined in huaweicloud sdk

        :param total_num: **参数解释** 风险总数 **取值范围** 取值0-200000
        :type total_num: int
        :param pass_num: **参数解释** 已通过检查项数量 **取值范围** 取值0-200000
        :type pass_num: int
        :param failed_num: **参数解释** 未通过检查项数量 **取值范围** 取值0-200000
        :type failed_num: int
        :param processed_num: **参数解释** 已处理检查项数量 **取值范围** 取值0-200000
        :type processed_num: int
        :param data_list: **参数解释** 数据列表
        :type data_list: list[:class:`huaweicloudsdkhss.v5.CheckRulesResponseInfo`]
        """
        
        super().__init__()

        self._total_num = None
        self._pass_num = None
        self._failed_num = None
        self._processed_num = None
        self._data_list = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if pass_num is not None:
            self.pass_num = pass_num
        if failed_num is not None:
            self.failed_num = failed_num
        if processed_num is not None:
            self.processed_num = processed_num
        if data_list is not None:
            self.data_list = data_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListAllRiskConfigCheckRulesResponse.

        **参数解释** 风险总数 **取值范围** 取值0-200000

        :return: The total_num of this ListAllRiskConfigCheckRulesResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListAllRiskConfigCheckRulesResponse.

        **参数解释** 风险总数 **取值范围** 取值0-200000

        :param total_num: The total_num of this ListAllRiskConfigCheckRulesResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def pass_num(self):
        r"""Gets the pass_num of this ListAllRiskConfigCheckRulesResponse.

        **参数解释** 已通过检查项数量 **取值范围** 取值0-200000

        :return: The pass_num of this ListAllRiskConfigCheckRulesResponse.
        :rtype: int
        """
        return self._pass_num

    @pass_num.setter
    def pass_num(self, pass_num):
        r"""Sets the pass_num of this ListAllRiskConfigCheckRulesResponse.

        **参数解释** 已通过检查项数量 **取值范围** 取值0-200000

        :param pass_num: The pass_num of this ListAllRiskConfigCheckRulesResponse.
        :type pass_num: int
        """
        self._pass_num = pass_num

    @property
    def failed_num(self):
        r"""Gets the failed_num of this ListAllRiskConfigCheckRulesResponse.

        **参数解释** 未通过检查项数量 **取值范围** 取值0-200000

        :return: The failed_num of this ListAllRiskConfigCheckRulesResponse.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this ListAllRiskConfigCheckRulesResponse.

        **参数解释** 未通过检查项数量 **取值范围** 取值0-200000

        :param failed_num: The failed_num of this ListAllRiskConfigCheckRulesResponse.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def processed_num(self):
        r"""Gets the processed_num of this ListAllRiskConfigCheckRulesResponse.

        **参数解释** 已处理检查项数量 **取值范围** 取值0-200000

        :return: The processed_num of this ListAllRiskConfigCheckRulesResponse.
        :rtype: int
        """
        return self._processed_num

    @processed_num.setter
    def processed_num(self, processed_num):
        r"""Sets the processed_num of this ListAllRiskConfigCheckRulesResponse.

        **参数解释** 已处理检查项数量 **取值范围** 取值0-200000

        :param processed_num: The processed_num of this ListAllRiskConfigCheckRulesResponse.
        :type processed_num: int
        """
        self._processed_num = processed_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ListAllRiskConfigCheckRulesResponse.

        **参数解释** 数据列表

        :return: The data_list of this ListAllRiskConfigCheckRulesResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CheckRulesResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListAllRiskConfigCheckRulesResponse.

        **参数解释** 数据列表

        :param data_list: The data_list of this ListAllRiskConfigCheckRulesResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.CheckRulesResponseInfo`]
        """
        self._data_list = data_list

    def to_dict(self):
        import warnings
        warnings.warn("ListAllRiskConfigCheckRulesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAllRiskConfigCheckRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
