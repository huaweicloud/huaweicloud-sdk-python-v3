# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIterationRequestV4:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'str',
        'description': 'str',
        'end_time': 'str',
        'name': 'str',
        'status': 'str',
        'over_type': 'str'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'description': 'description',
        'end_time': 'end_time',
        'name': 'name',
        'status': 'status',
        'over_type': 'over_type'
    }

    def __init__(self, begin_time=None, description=None, end_time=None, name=None, status=None, over_type=None):
        """UpdateIterationRequestV4

        The model defined in huaweicloud sdk

        :param begin_time: 开始时间，年-月-日
        :type begin_time: str
        :param description: 描述
        :type description: str
        :param end_time: 结束时间，年-月-日
        :type end_time: str
        :param name: 标题
        :type name: str
        :param status: 迭代的状态，0 未开始 &lt;--&gt; 1 进行中&lt;--&gt; 2 结束 &lt;--&gt; 1&lt;--&gt;0, 状态不能跨状态更改
        :type status: str
        :param over_type: 迭代结束时，工作项的处理（close 所有的工作项关闭，empty 没有关闭的工作项 放在block里面），status更新为2时需要填写over_type
        :type over_type: str
        """
        
        

        self._begin_time = None
        self._description = None
        self._end_time = None
        self._name = None
        self._status = None
        self._over_type = None
        self.discriminator = None

        self.begin_time = begin_time
        if description is not None:
            self.description = description
        self.end_time = end_time
        self.name = name
        if status is not None:
            self.status = status
        if over_type is not None:
            self.over_type = over_type

    @property
    def begin_time(self):
        """Gets the begin_time of this UpdateIterationRequestV4.

        开始时间，年-月-日

        :return: The begin_time of this UpdateIterationRequestV4.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this UpdateIterationRequestV4.

        开始时间，年-月-日

        :param begin_time: The begin_time of this UpdateIterationRequestV4.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def description(self):
        """Gets the description of this UpdateIterationRequestV4.

        描述

        :return: The description of this UpdateIterationRequestV4.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateIterationRequestV4.

        描述

        :param description: The description of this UpdateIterationRequestV4.
        :type description: str
        """
        self._description = description

    @property
    def end_time(self):
        """Gets the end_time of this UpdateIterationRequestV4.

        结束时间，年-月-日

        :return: The end_time of this UpdateIterationRequestV4.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this UpdateIterationRequestV4.

        结束时间，年-月-日

        :param end_time: The end_time of this UpdateIterationRequestV4.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def name(self):
        """Gets the name of this UpdateIterationRequestV4.

        标题

        :return: The name of this UpdateIterationRequestV4.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateIterationRequestV4.

        标题

        :param name: The name of this UpdateIterationRequestV4.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this UpdateIterationRequestV4.

        迭代的状态，0 未开始 <--> 1 进行中<--> 2 结束 <--> 1<-->0, 状态不能跨状态更改

        :return: The status of this UpdateIterationRequestV4.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateIterationRequestV4.

        迭代的状态，0 未开始 <--> 1 进行中<--> 2 结束 <--> 1<-->0, 状态不能跨状态更改

        :param status: The status of this UpdateIterationRequestV4.
        :type status: str
        """
        self._status = status

    @property
    def over_type(self):
        """Gets the over_type of this UpdateIterationRequestV4.

        迭代结束时，工作项的处理（close 所有的工作项关闭，empty 没有关闭的工作项 放在block里面），status更新为2时需要填写over_type

        :return: The over_type of this UpdateIterationRequestV4.
        :rtype: str
        """
        return self._over_type

    @over_type.setter
    def over_type(self, over_type):
        """Sets the over_type of this UpdateIterationRequestV4.

        迭代结束时，工作项的处理（close 所有的工作项关闭，empty 没有关闭的工作项 放在block里面），status更新为2时需要填写over_type

        :param over_type: The over_type of this UpdateIterationRequestV4.
        :type over_type: str
        """
        self._over_type = over_type

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
        if not isinstance(other, UpdateIterationRequestV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
