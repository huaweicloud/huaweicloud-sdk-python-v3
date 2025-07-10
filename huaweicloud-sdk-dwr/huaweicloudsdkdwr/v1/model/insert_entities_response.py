# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsertEntitiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'data': 'InsertEntitiesData'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'data': 'data'
    }

    def __init__(self, code=None, message=None, data=None):
        r"""InsertEntitiesResponse

        The model defined in huaweicloud sdk

        :param code: **参数解释：** 返回码。参见错误码章节。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type code: str
        :param message: **参数解释：** 描述信息 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type message: str
        :param data: 
        :type data: :class:`huaweicloudsdkdwr.v1.InsertEntitiesData`
        """
        
        super(InsertEntitiesResponse, self).__init__()

        self._code = None
        self._message = None
        self._data = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if data is not None:
            self.data = data

    @property
    def code(self):
        r"""Gets the code of this InsertEntitiesResponse.

        **参数解释：** 返回码。参见错误码章节。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The code of this InsertEntitiesResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this InsertEntitiesResponse.

        **参数解释：** 返回码。参见错误码章节。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param code: The code of this InsertEntitiesResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this InsertEntitiesResponse.

        **参数解释：** 描述信息 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The message of this InsertEntitiesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this InsertEntitiesResponse.

        **参数解释：** 描述信息 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param message: The message of this InsertEntitiesResponse.
        :type message: str
        """
        self._message = message

    @property
    def data(self):
        r"""Gets the data of this InsertEntitiesResponse.

        :return: The data of this InsertEntitiesResponse.
        :rtype: :class:`huaweicloudsdkdwr.v1.InsertEntitiesData`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this InsertEntitiesResponse.

        :param data: The data of this InsertEntitiesResponse.
        :type data: :class:`huaweicloudsdkdwr.v1.InsertEntitiesData`
        """
        self._data = data

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
        if not isinstance(other, InsertEntitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
