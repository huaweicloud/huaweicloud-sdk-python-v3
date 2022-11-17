# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunNerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'named_entities': 'list[NamedEntity]',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'named_entities': 'named_entities',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, named_entities=None, error_code=None, error_msg=None):
        """RunNerResponse

        The model defined in huaweicloud sdk

        :param named_entities: 命名实体识别结果。调用失败时无此字段。
        :type named_entities: list[:class:`huaweicloudsdknlp.v2.NamedEntity`]
        :param error_code: 调用失败时的错误码，具体请参见错误码。调用成功时无此字段。
        :type error_code: str
        :param error_msg: 调用失败时的错误信息。调用成功时无此字段。
        :type error_msg: str
        """
        
        super(RunNerResponse, self).__init__()

        self._named_entities = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if named_entities is not None:
            self.named_entities = named_entities
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def named_entities(self):
        """Gets the named_entities of this RunNerResponse.

        命名实体识别结果。调用失败时无此字段。

        :return: The named_entities of this RunNerResponse.
        :rtype: list[:class:`huaweicloudsdknlp.v2.NamedEntity`]
        """
        return self._named_entities

    @named_entities.setter
    def named_entities(self, named_entities):
        """Sets the named_entities of this RunNerResponse.

        命名实体识别结果。调用失败时无此字段。

        :param named_entities: The named_entities of this RunNerResponse.
        :type named_entities: list[:class:`huaweicloudsdknlp.v2.NamedEntity`]
        """
        self._named_entities = named_entities

    @property
    def error_code(self):
        """Gets the error_code of this RunNerResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :return: The error_code of this RunNerResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this RunNerResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :param error_code: The error_code of this RunNerResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this RunNerResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :return: The error_msg of this RunNerResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this RunNerResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :param error_msg: The error_msg of this RunNerResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, RunNerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
