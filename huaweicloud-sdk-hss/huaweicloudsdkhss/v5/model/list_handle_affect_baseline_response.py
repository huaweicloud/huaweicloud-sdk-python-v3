# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHandleAffectBaselineResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_rule_num': 'int',
        'rule_num': 'int',
        'host_num': 'int',
        'data_list': 'list[HandleAffectBaselineInfo]'
    }

    attribute_map = {
        'total_rule_num': 'total_rule_num',
        'rule_num': 'rule_num',
        'host_num': 'host_num',
        'data_list': 'data_list'
    }

    def __init__(self, total_rule_num=None, rule_num=None, host_num=None, data_list=None):
        r"""ListHandleAffectBaselineResponse

        The model defined in huaweicloud sdk

        :param total_rule_num: **参数解释** 该操作影响的范围的总数 **取值范围**   取值0-5000
        :type total_rule_num: int
        :param rule_num: **参数解释** 该操作影响的检查项数 **取值范围**   取值0-5000
        :type rule_num: int
        :param host_num: **参数解释** 该操作影响的主机数 **取值范围**   取值0-5000
        :type host_num: int
        :param data_list: **参数解释** 该操作影响范围的详细信息的列表
        :type data_list: list[:class:`huaweicloudsdkhss.v5.HandleAffectBaselineInfo`]
        """
        
        super(ListHandleAffectBaselineResponse, self).__init__()

        self._total_rule_num = None
        self._rule_num = None
        self._host_num = None
        self._data_list = None
        self.discriminator = None

        if total_rule_num is not None:
            self.total_rule_num = total_rule_num
        if rule_num is not None:
            self.rule_num = rule_num
        if host_num is not None:
            self.host_num = host_num
        if data_list is not None:
            self.data_list = data_list

    @property
    def total_rule_num(self):
        r"""Gets the total_rule_num of this ListHandleAffectBaselineResponse.

        **参数解释** 该操作影响的范围的总数 **取值范围**   取值0-5000

        :return: The total_rule_num of this ListHandleAffectBaselineResponse.
        :rtype: int
        """
        return self._total_rule_num

    @total_rule_num.setter
    def total_rule_num(self, total_rule_num):
        r"""Sets the total_rule_num of this ListHandleAffectBaselineResponse.

        **参数解释** 该操作影响的范围的总数 **取值范围**   取值0-5000

        :param total_rule_num: The total_rule_num of this ListHandleAffectBaselineResponse.
        :type total_rule_num: int
        """
        self._total_rule_num = total_rule_num

    @property
    def rule_num(self):
        r"""Gets the rule_num of this ListHandleAffectBaselineResponse.

        **参数解释** 该操作影响的检查项数 **取值范围**   取值0-5000

        :return: The rule_num of this ListHandleAffectBaselineResponse.
        :rtype: int
        """
        return self._rule_num

    @rule_num.setter
    def rule_num(self, rule_num):
        r"""Sets the rule_num of this ListHandleAffectBaselineResponse.

        **参数解释** 该操作影响的检查项数 **取值范围**   取值0-5000

        :param rule_num: The rule_num of this ListHandleAffectBaselineResponse.
        :type rule_num: int
        """
        self._rule_num = rule_num

    @property
    def host_num(self):
        r"""Gets the host_num of this ListHandleAffectBaselineResponse.

        **参数解释** 该操作影响的主机数 **取值范围**   取值0-5000

        :return: The host_num of this ListHandleAffectBaselineResponse.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ListHandleAffectBaselineResponse.

        **参数解释** 该操作影响的主机数 **取值范围**   取值0-5000

        :param host_num: The host_num of this ListHandleAffectBaselineResponse.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ListHandleAffectBaselineResponse.

        **参数解释** 该操作影响范围的详细信息的列表

        :return: The data_list of this ListHandleAffectBaselineResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HandleAffectBaselineInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListHandleAffectBaselineResponse.

        **参数解释** 该操作影响范围的详细信息的列表

        :param data_list: The data_list of this ListHandleAffectBaselineResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.HandleAffectBaselineInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ListHandleAffectBaselineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
