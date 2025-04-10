# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectLiveFaceByBase64Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'LiveDetectFaceRespResult',
        'warning_list': 'list[WarningList]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'result': 'result',
        'warning_list': 'warning-list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, result=None, warning_list=None, x_request_id=None):
        r"""DetectLiveFaceByBase64Response

        The model defined in huaweicloud sdk

        :param result: 
        :type result: :class:`huaweicloudsdkfrs.v2.LiveDetectFaceRespResult`
        :param warning_list: 警告信息列表。 调用失败时无此字段。
        :type warning_list: list[:class:`huaweicloudsdkfrs.v2.WarningList`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DetectLiveFaceByBase64Response, self).__init__()

        self._result = None
        self._warning_list = None
        self._x_request_id = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if warning_list is not None:
            self.warning_list = warning_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def result(self):
        r"""Gets the result of this DetectLiveFaceByBase64Response.

        :return: The result of this DetectLiveFaceByBase64Response.
        :rtype: :class:`huaweicloudsdkfrs.v2.LiveDetectFaceRespResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this DetectLiveFaceByBase64Response.

        :param result: The result of this DetectLiveFaceByBase64Response.
        :type result: :class:`huaweicloudsdkfrs.v2.LiveDetectFaceRespResult`
        """
        self._result = result

    @property
    def warning_list(self):
        r"""Gets the warning_list of this DetectLiveFaceByBase64Response.

        警告信息列表。 调用失败时无此字段。

        :return: The warning_list of this DetectLiveFaceByBase64Response.
        :rtype: list[:class:`huaweicloudsdkfrs.v2.WarningList`]
        """
        return self._warning_list

    @warning_list.setter
    def warning_list(self, warning_list):
        r"""Sets the warning_list of this DetectLiveFaceByBase64Response.

        警告信息列表。 调用失败时无此字段。

        :param warning_list: The warning_list of this DetectLiveFaceByBase64Response.
        :type warning_list: list[:class:`huaweicloudsdkfrs.v2.WarningList`]
        """
        self._warning_list = warning_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this DetectLiveFaceByBase64Response.

        :return: The x_request_id of this DetectLiveFaceByBase64Response.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this DetectLiveFaceByBase64Response.

        :param x_request_id: The x_request_id of this DetectLiveFaceByBase64Response.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, DetectLiveFaceByBase64Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
