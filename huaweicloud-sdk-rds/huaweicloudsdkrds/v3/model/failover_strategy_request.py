# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailoverStrategyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repair_strategy': 'str'
    }

    attribute_map = {
        'repair_strategy': 'repairStrategy'
    }

    def __init__(self, repair_strategy=None):
        r"""FailoverStrategyRequest

        The model defined in huaweicloud sdk

        :param repair_strategy: 可用性策略，可选择如下方式： - reliability：可靠性优先，数据库应该尽可能保障数据的可靠性，即数据丢失量最少。对于数据一致性要求较高的业务，建议选择该策略。 - availability：可用性优先，数据库应该可快恢复服务，即可用时间最长。对于数据库在线时间要求较高的业务，建议选择该策略。
        :type repair_strategy: str
        """
        
        

        self._repair_strategy = None
        self.discriminator = None

        self.repair_strategy = repair_strategy

    @property
    def repair_strategy(self):
        r"""Gets the repair_strategy of this FailoverStrategyRequest.

        可用性策略，可选择如下方式： - reliability：可靠性优先，数据库应该尽可能保障数据的可靠性，即数据丢失量最少。对于数据一致性要求较高的业务，建议选择该策略。 - availability：可用性优先，数据库应该可快恢复服务，即可用时间最长。对于数据库在线时间要求较高的业务，建议选择该策略。

        :return: The repair_strategy of this FailoverStrategyRequest.
        :rtype: str
        """
        return self._repair_strategy

    @repair_strategy.setter
    def repair_strategy(self, repair_strategy):
        r"""Sets the repair_strategy of this FailoverStrategyRequest.

        可用性策略，可选择如下方式： - reliability：可靠性优先，数据库应该尽可能保障数据的可靠性，即数据丢失量最少。对于数据一致性要求较高的业务，建议选择该策略。 - availability：可用性优先，数据库应该可快恢复服务，即可用时间最长。对于数据库在线时间要求较高的业务，建议选择该策略。

        :param repair_strategy: The repair_strategy of this FailoverStrategyRequest.
        :type repair_strategy: str
        """
        self._repair_strategy = repair_strategy

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
        if not isinstance(other, FailoverStrategyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
