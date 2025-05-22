# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionSubItemVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'detail': 'str',
        'sub_item_name': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'estimated_time': 'int'
    }

    attribute_map = {
        'status': 'status',
        'detail': 'detail',
        'sub_item_name': 'sub_item_name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'estimated_time': 'estimated_time'
    }

    def __init__(self, status=None, detail=None, sub_item_name=None, begin_time=None, end_time=None, estimated_time=None):
        r"""ActionSubItemVo

        The model defined in huaweicloud sdk

        :param status: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type status: str
        :param detail: **参数解释**： 扩展信息。 **取值范围**： 不涉及。
        :type detail: str
        :param sub_item_name: **参数解释**： 子项名称，根据请求header中的x-language字段返回对应的中/英文名称。 **取值范围**： 不涉及。
        :type sub_item_name: str
        :param begin_time: **参数解释**： 开始时间。 **取值范围**： 时间格式，或null值。
        :type begin_time: str
        :param end_time: **参数解释**： 结束时间。 **取值范围**： 时间格式，或null值。
        :type end_time: str
        :param estimated_time: **参数解释**： 预估时间。 **取值范围**： 整数。
        :type estimated_time: int
        """
        
        

        self._status = None
        self._detail = None
        self._sub_item_name = None
        self._begin_time = None
        self._end_time = None
        self._estimated_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail
        if sub_item_name is not None:
            self.sub_item_name = sub_item_name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if estimated_time is not None:
            self.estimated_time = estimated_time

    @property
    def status(self):
        r"""Gets the status of this ActionSubItemVo.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The status of this ActionSubItemVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ActionSubItemVo.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param status: The status of this ActionSubItemVo.
        :type status: str
        """
        self._status = status

    @property
    def detail(self):
        r"""Gets the detail of this ActionSubItemVo.

        **参数解释**： 扩展信息。 **取值范围**： 不涉及。

        :return: The detail of this ActionSubItemVo.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this ActionSubItemVo.

        **参数解释**： 扩展信息。 **取值范围**： 不涉及。

        :param detail: The detail of this ActionSubItemVo.
        :type detail: str
        """
        self._detail = detail

    @property
    def sub_item_name(self):
        r"""Gets the sub_item_name of this ActionSubItemVo.

        **参数解释**： 子项名称，根据请求header中的x-language字段返回对应的中/英文名称。 **取值范围**： 不涉及。

        :return: The sub_item_name of this ActionSubItemVo.
        :rtype: str
        """
        return self._sub_item_name

    @sub_item_name.setter
    def sub_item_name(self, sub_item_name):
        r"""Sets the sub_item_name of this ActionSubItemVo.

        **参数解释**： 子项名称，根据请求header中的x-language字段返回对应的中/英文名称。 **取值范围**： 不涉及。

        :param sub_item_name: The sub_item_name of this ActionSubItemVo.
        :type sub_item_name: str
        """
        self._sub_item_name = sub_item_name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ActionSubItemVo.

        **参数解释**： 开始时间。 **取值范围**： 时间格式，或null值。

        :return: The begin_time of this ActionSubItemVo.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ActionSubItemVo.

        **参数解释**： 开始时间。 **取值范围**： 时间格式，或null值。

        :param begin_time: The begin_time of this ActionSubItemVo.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ActionSubItemVo.

        **参数解释**： 结束时间。 **取值范围**： 时间格式，或null值。

        :return: The end_time of this ActionSubItemVo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ActionSubItemVo.

        **参数解释**： 结束时间。 **取值范围**： 时间格式，或null值。

        :param end_time: The end_time of this ActionSubItemVo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def estimated_time(self):
        r"""Gets the estimated_time of this ActionSubItemVo.

        **参数解释**： 预估时间。 **取值范围**： 整数。

        :return: The estimated_time of this ActionSubItemVo.
        :rtype: int
        """
        return self._estimated_time

    @estimated_time.setter
    def estimated_time(self, estimated_time):
        r"""Sets the estimated_time of this ActionSubItemVo.

        **参数解释**： 预估时间。 **取值范围**： 整数。

        :param estimated_time: The estimated_time of this ActionSubItemVo.
        :type estimated_time: int
        """
        self._estimated_time = estimated_time

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
        if not isinstance(other, ActionSubItemVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
