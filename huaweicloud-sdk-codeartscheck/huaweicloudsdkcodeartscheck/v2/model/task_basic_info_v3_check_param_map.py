# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskBasicInfoV3CheckParamMap:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'param1': 'str',
        'param2': 'str'
    }

    attribute_map = {
        'param1': 'param1',
        'param2': 'param2'
    }

    def __init__(self, param1=None, param2=None):
        r"""TaskBasicInfoV3CheckParamMap

        The model defined in huaweicloud sdk

        :param param1: **参数解释：** 字段的name为自定义参数的Key，字段的值为自定义参数的Value。 **取值范围：** 长度为[1~8192]个字符。
        :type param1: str
        :param param2: **参数解释：** 字段的name为自定义参数的Key，字段的值为自定义参数的Value。 **取值范围：** 长度为[1~8192]个字符。
        :type param2: str
        """
        
        

        self._param1 = None
        self._param2 = None
        self.discriminator = None

        if param1 is not None:
            self.param1 = param1
        if param2 is not None:
            self.param2 = param2

    @property
    def param1(self):
        r"""Gets the param1 of this TaskBasicInfoV3CheckParamMap.

        **参数解释：** 字段的name为自定义参数的Key，字段的值为自定义参数的Value。 **取值范围：** 长度为[1~8192]个字符。

        :return: The param1 of this TaskBasicInfoV3CheckParamMap.
        :rtype: str
        """
        return self._param1

    @param1.setter
    def param1(self, param1):
        r"""Sets the param1 of this TaskBasicInfoV3CheckParamMap.

        **参数解释：** 字段的name为自定义参数的Key，字段的值为自定义参数的Value。 **取值范围：** 长度为[1~8192]个字符。

        :param param1: The param1 of this TaskBasicInfoV3CheckParamMap.
        :type param1: str
        """
        self._param1 = param1

    @property
    def param2(self):
        r"""Gets the param2 of this TaskBasicInfoV3CheckParamMap.

        **参数解释：** 字段的name为自定义参数的Key，字段的值为自定义参数的Value。 **取值范围：** 长度为[1~8192]个字符。

        :return: The param2 of this TaskBasicInfoV3CheckParamMap.
        :rtype: str
        """
        return self._param2

    @param2.setter
    def param2(self, param2):
        r"""Sets the param2 of this TaskBasicInfoV3CheckParamMap.

        **参数解释：** 字段的name为自定义参数的Key，字段的值为自定义参数的Value。 **取值范围：** 长度为[1~8192]个字符。

        :param param2: The param2 of this TaskBasicInfoV3CheckParamMap.
        :type param2: str
        """
        self._param2 = param2

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
        if not isinstance(other, TaskBasicInfoV3CheckParamMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
