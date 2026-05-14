# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadResourceQueue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'short_query_optimize': 'str',
        'short_query_concurrency_num': 'str'
    }

    attribute_map = {
        'short_query_optimize': 'short_query_optimize',
        'short_query_concurrency_num': 'short_query_concurrency_num'
    }

    def __init__(self, short_query_optimize=None, short_query_concurrency_num=None):
        r"""WorkloadResourceQueue

        The model defined in huaweicloud sdk

        :param short_query_optimize: **参数解释**： 工作负载队列短查询加速开关。 **约束限制**： 不涉及。 **取值范围**： - on：开启 - off：关闭 **默认取值**： on
        :type short_query_optimize: str
        :param short_query_concurrency_num: **参数解释**： 工作负载队列短查询并发数。 **约束限制**： 不涉及。 **取值范围**： -1以上，-1表示不限制。 **默认取值**： -1
        :type short_query_concurrency_num: str
        """
        
        

        self._short_query_optimize = None
        self._short_query_concurrency_num = None
        self.discriminator = None

        if short_query_optimize is not None:
            self.short_query_optimize = short_query_optimize
        if short_query_concurrency_num is not None:
            self.short_query_concurrency_num = short_query_concurrency_num

    @property
    def short_query_optimize(self):
        r"""Gets the short_query_optimize of this WorkloadResourceQueue.

        **参数解释**： 工作负载队列短查询加速开关。 **约束限制**： 不涉及。 **取值范围**： - on：开启 - off：关闭 **默认取值**： on

        :return: The short_query_optimize of this WorkloadResourceQueue.
        :rtype: str
        """
        return self._short_query_optimize

    @short_query_optimize.setter
    def short_query_optimize(self, short_query_optimize):
        r"""Sets the short_query_optimize of this WorkloadResourceQueue.

        **参数解释**： 工作负载队列短查询加速开关。 **约束限制**： 不涉及。 **取值范围**： - on：开启 - off：关闭 **默认取值**： on

        :param short_query_optimize: The short_query_optimize of this WorkloadResourceQueue.
        :type short_query_optimize: str
        """
        self._short_query_optimize = short_query_optimize

    @property
    def short_query_concurrency_num(self):
        r"""Gets the short_query_concurrency_num of this WorkloadResourceQueue.

        **参数解释**： 工作负载队列短查询并发数。 **约束限制**： 不涉及。 **取值范围**： -1以上，-1表示不限制。 **默认取值**： -1

        :return: The short_query_concurrency_num of this WorkloadResourceQueue.
        :rtype: str
        """
        return self._short_query_concurrency_num

    @short_query_concurrency_num.setter
    def short_query_concurrency_num(self, short_query_concurrency_num):
        r"""Sets the short_query_concurrency_num of this WorkloadResourceQueue.

        **参数解释**： 工作负载队列短查询并发数。 **约束限制**： 不涉及。 **取值范围**： -1以上，-1表示不限制。 **默认取值**： -1

        :param short_query_concurrency_num: The short_query_concurrency_num of this WorkloadResourceQueue.
        :type short_query_concurrency_num: str
        """
        self._short_query_concurrency_num = short_query_concurrency_num

    def to_dict(self):
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
        if not isinstance(other, WorkloadResourceQueue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
