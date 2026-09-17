# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlanRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'key_word': 'str',
        'updated_time_interval': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'key_word': 'key_word',
        'updated_time_interval': 'updated_time_interval'
    }

    def __init__(self, project_id=None, key_word=None, updated_time_interval=None):
        r"""ListPlanRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param key_word: **参数解释：** 发布/迭代名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key_word: str
        :param updated_time_interval: **参数解释：** 更新发布/迭代时间，unix时间戳，单位：毫秒  样例：1576114296000,1576114396000 **约束限制：**  起止时间均为13位的时间戳字符串，使用英文逗号分割。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type updated_time_interval: str
        """
        
        

        self._project_id = None
        self._key_word = None
        self._updated_time_interval = None
        self.discriminator = None

        self.project_id = project_id
        if key_word is not None:
            self.key_word = key_word
        if updated_time_interval is not None:
            self.updated_time_interval = updated_time_interval

    @property
    def project_id(self):
        r"""Gets the project_id of this ListPlanRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this ListPlanRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListPlanRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this ListPlanRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def key_word(self):
        r"""Gets the key_word of this ListPlanRequest.

        **参数解释：** 发布/迭代名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key_word of this ListPlanRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this ListPlanRequest.

        **参数解释：** 发布/迭代名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key_word: The key_word of this ListPlanRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def updated_time_interval(self):
        r"""Gets the updated_time_interval of this ListPlanRequest.

        **参数解释：** 更新发布/迭代时间，unix时间戳，单位：毫秒  样例：1576114296000,1576114396000 **约束限制：**  起止时间均为13位的时间戳字符串，使用英文逗号分割。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The updated_time_interval of this ListPlanRequest.
        :rtype: str
        """
        return self._updated_time_interval

    @updated_time_interval.setter
    def updated_time_interval(self, updated_time_interval):
        r"""Sets the updated_time_interval of this ListPlanRequest.

        **参数解释：** 更新发布/迭代时间，unix时间戳，单位：毫秒  样例：1576114296000,1576114396000 **约束限制：**  起止时间均为13位的时间戳字符串，使用英文逗号分割。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param updated_time_interval: The updated_time_interval of this ListPlanRequest.
        :type updated_time_interval: str
        """
        self._updated_time_interval = updated_time_interval

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
        if not isinstance(other, ListPlanRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
