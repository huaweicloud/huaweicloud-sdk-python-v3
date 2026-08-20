# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWdrSnapshotAvailableGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, x_language=None, instance_id=None, begin_time=None, end_time=None):
        r"""ListWdrSnapshotAvailableGroupsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn - en-us  **默认取值**: en-us
        :type x_language: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param begin_time: **参数解释**: 开始时间。 **约束限制**: 不涉及。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。注意，对于时区的+号，需要进行编码，替换为%2B。 **默认取值**: 不涉及。
        :type begin_time: str
        :param end_time: **参数解释**: 结束时间。 **约束限制**: 不涉及。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。对于时区的+号，需要进行编码，替换为%2B。 **默认取值**: 不涉及。
        :type end_time: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.begin_time = begin_time
        self.end_time = end_time

    @property
    def x_language(self):
        r"""Gets the x_language of this ListWdrSnapshotAvailableGroupsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn - en-us  **默认取值**: en-us

        :return: The x_language of this ListWdrSnapshotAvailableGroupsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListWdrSnapshotAvailableGroupsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListWdrSnapshotAvailableGroupsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListWdrSnapshotAvailableGroupsRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ListWdrSnapshotAvailableGroupsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListWdrSnapshotAvailableGroupsRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListWdrSnapshotAvailableGroupsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListWdrSnapshotAvailableGroupsRequest.

        **参数解释**: 开始时间。 **约束限制**: 不涉及。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。注意，对于时区的+号，需要进行编码，替换为%2B。 **默认取值**: 不涉及。

        :return: The begin_time of this ListWdrSnapshotAvailableGroupsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListWdrSnapshotAvailableGroupsRequest.

        **参数解释**: 开始时间。 **约束限制**: 不涉及。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。注意，对于时区的+号，需要进行编码，替换为%2B。 **默认取值**: 不涉及。

        :param begin_time: The begin_time of this ListWdrSnapshotAvailableGroupsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListWdrSnapshotAvailableGroupsRequest.

        **参数解释**: 结束时间。 **约束限制**: 不涉及。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。对于时区的+号，需要进行编码，替换为%2B。 **默认取值**: 不涉及。

        :return: The end_time of this ListWdrSnapshotAvailableGroupsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListWdrSnapshotAvailableGroupsRequest.

        **参数解释**: 结束时间。 **约束限制**: 不涉及。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。对于时区的+号，需要进行编码，替换为%2B。 **默认取值**: 不涉及。

        :param end_time: The end_time of this ListWdrSnapshotAvailableGroupsRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListWdrSnapshotAvailableGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
