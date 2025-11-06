# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDisasterRecordRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str'
    }

    attribute_map = {
        'id': 'id'
    }

    def __init__(self, id=None):
        r"""DeleteDisasterRecordRequestBody

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 容灾任务ID。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、中划线、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type id: str
        """
        
        

        self._id = None
        self.discriminator = None

        self.id = id

    @property
    def id(self):
        r"""Gets the id of this DeleteDisasterRecordRequestBody.

        **参数解释**: 容灾任务ID。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、中划线、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The id of this DeleteDisasterRecordRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteDisasterRecordRequestBody.

        **参数解释**: 容灾任务ID。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、中划线、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param id: The id of this DeleteDisasterRecordRequestBody.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, DeleteDisasterRecordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
