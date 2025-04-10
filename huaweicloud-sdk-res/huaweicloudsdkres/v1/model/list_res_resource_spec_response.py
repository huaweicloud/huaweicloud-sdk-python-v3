# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResResourceSpecResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offline_spec': 'list[str]',
        'nearline_spec': 'list[str]',
        'deep_learning_spec': 'list[str]',
        'is_success': 'bool',
        'message': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'offline_spec': 'offline_spec',
        'nearline_spec': 'nearline_spec',
        'deep_learning_spec': 'deep_learning_spec',
        'is_success': 'is_success',
        'message': 'message',
        'error_code': 'error_code'
    }

    def __init__(self, offline_spec=None, nearline_spec=None, deep_learning_spec=None, is_success=None, message=None, error_code=None):
        r"""ListResResourceSpecResponse

        The model defined in huaweicloud sdk

        :param offline_spec: 离线计算规格。
        :type offline_spec: list[str]
        :param nearline_spec: 实时计算规格。
        :type nearline_spec: list[str]
        :param deep_learning_spec: 排序模型计算规格。
        :type deep_learning_spec: list[str]
        :param is_success: 请求是否成功。
        :type is_success: bool
        :param message: 返回消息（请求成功时，不返回此字段）。
        :type message: str
        :param error_code: 错误码（请求成功时，不返回此字段）。
        :type error_code: str
        """
        
        super(ListResResourceSpecResponse, self).__init__()

        self._offline_spec = None
        self._nearline_spec = None
        self._deep_learning_spec = None
        self._is_success = None
        self._message = None
        self._error_code = None
        self.discriminator = None

        if offline_spec is not None:
            self.offline_spec = offline_spec
        if nearline_spec is not None:
            self.nearline_spec = nearline_spec
        if deep_learning_spec is not None:
            self.deep_learning_spec = deep_learning_spec
        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if error_code is not None:
            self.error_code = error_code

    @property
    def offline_spec(self):
        r"""Gets the offline_spec of this ListResResourceSpecResponse.

        离线计算规格。

        :return: The offline_spec of this ListResResourceSpecResponse.
        :rtype: list[str]
        """
        return self._offline_spec

    @offline_spec.setter
    def offline_spec(self, offline_spec):
        r"""Sets the offline_spec of this ListResResourceSpecResponse.

        离线计算规格。

        :param offline_spec: The offline_spec of this ListResResourceSpecResponse.
        :type offline_spec: list[str]
        """
        self._offline_spec = offline_spec

    @property
    def nearline_spec(self):
        r"""Gets the nearline_spec of this ListResResourceSpecResponse.

        实时计算规格。

        :return: The nearline_spec of this ListResResourceSpecResponse.
        :rtype: list[str]
        """
        return self._nearline_spec

    @nearline_spec.setter
    def nearline_spec(self, nearline_spec):
        r"""Sets the nearline_spec of this ListResResourceSpecResponse.

        实时计算规格。

        :param nearline_spec: The nearline_spec of this ListResResourceSpecResponse.
        :type nearline_spec: list[str]
        """
        self._nearline_spec = nearline_spec

    @property
    def deep_learning_spec(self):
        r"""Gets the deep_learning_spec of this ListResResourceSpecResponse.

        排序模型计算规格。

        :return: The deep_learning_spec of this ListResResourceSpecResponse.
        :rtype: list[str]
        """
        return self._deep_learning_spec

    @deep_learning_spec.setter
    def deep_learning_spec(self, deep_learning_spec):
        r"""Sets the deep_learning_spec of this ListResResourceSpecResponse.

        排序模型计算规格。

        :param deep_learning_spec: The deep_learning_spec of this ListResResourceSpecResponse.
        :type deep_learning_spec: list[str]
        """
        self._deep_learning_spec = deep_learning_spec

    @property
    def is_success(self):
        r"""Gets the is_success of this ListResResourceSpecResponse.

        请求是否成功。

        :return: The is_success of this ListResResourceSpecResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ListResResourceSpecResponse.

        请求是否成功。

        :param is_success: The is_success of this ListResResourceSpecResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ListResResourceSpecResponse.

        返回消息（请求成功时，不返回此字段）。

        :return: The message of this ListResResourceSpecResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListResResourceSpecResponse.

        返回消息（请求成功时，不返回此字段）。

        :param message: The message of this ListResResourceSpecResponse.
        :type message: str
        """
        self._message = message

    @property
    def error_code(self):
        r"""Gets the error_code of this ListResResourceSpecResponse.

        错误码（请求成功时，不返回此字段）。

        :return: The error_code of this ListResResourceSpecResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ListResResourceSpecResponse.

        错误码（请求成功时，不返回此字段）。

        :param error_code: The error_code of this ListResResourceSpecResponse.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, ListResResourceSpecResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
