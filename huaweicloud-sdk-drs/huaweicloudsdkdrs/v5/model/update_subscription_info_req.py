# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubscriptionInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'consume_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'consume_time': 'consume_time'
    }

    def __init__(self, name=None, description=None, consume_time=None):
        r"""UpdateSubscriptionInfoReq

        The model defined in huaweicloud sdk

        :param name: 任务名称 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50
        :type name: str
        :param description: 描述
        :type description: str
        :param consume_time: 消费时间点，在修改完消费时间点后，拉取到的增量数据从修改后的消费时间点开始。 约束：修改的时间点必须在订阅任务的时间范围内（从任务创建到当前时间之间），取值为时间戳，例如：1769393264000。
        :type consume_time: int
        """
        
        

        self._name = None
        self._description = None
        self._consume_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if consume_time is not None:
            self.consume_time = consume_time

    @property
    def name(self):
        r"""Gets the name of this UpdateSubscriptionInfoReq.

        任务名称 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50

        :return: The name of this UpdateSubscriptionInfoReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateSubscriptionInfoReq.

        任务名称 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50

        :param name: The name of this UpdateSubscriptionInfoReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateSubscriptionInfoReq.

        描述

        :return: The description of this UpdateSubscriptionInfoReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateSubscriptionInfoReq.

        描述

        :param description: The description of this UpdateSubscriptionInfoReq.
        :type description: str
        """
        self._description = description

    @property
    def consume_time(self):
        r"""Gets the consume_time of this UpdateSubscriptionInfoReq.

        消费时间点，在修改完消费时间点后，拉取到的增量数据从修改后的消费时间点开始。 约束：修改的时间点必须在订阅任务的时间范围内（从任务创建到当前时间之间），取值为时间戳，例如：1769393264000。

        :return: The consume_time of this UpdateSubscriptionInfoReq.
        :rtype: int
        """
        return self._consume_time

    @consume_time.setter
    def consume_time(self, consume_time):
        r"""Sets the consume_time of this UpdateSubscriptionInfoReq.

        消费时间点，在修改完消费时间点后，拉取到的增量数据从修改后的消费时间点开始。 约束：修改的时间点必须在订阅任务的时间范围内（从任务创建到当前时间之间），取值为时间戳，例如：1769393264000。

        :param consume_time: The consume_time of this UpdateSubscriptionInfoReq.
        :type consume_time: int
        """
        self._consume_time = consume_time

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
        if not isinstance(other, UpdateSubscriptionInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
