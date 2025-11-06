# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogsTreeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'list[LogTreeDto]'
    }

    attribute_map = {
        'body': 'body'
    }

    def __init__(self, body=None):
        r"""ListLogsTreeResponse

        The model defined in huaweicloud sdk

        :param body: 文件树列表
        :type body: list[:class:`huaweicloudsdkcodeartsrepo.v4.LogTreeDto`]
        """
        
        super().__init__()

        self._body = None
        self.discriminator = None

        if body is not None:
            self.body = body

    @property
    def body(self):
        r"""Gets the body of this ListLogsTreeResponse.

        文件树列表

        :return: The body of this ListLogsTreeResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.LogTreeDto`]
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListLogsTreeResponse.

        文件树列表

        :param body: The body of this ListLogsTreeResponse.
        :type body: list[:class:`huaweicloudsdkcodeartsrepo.v4.LogTreeDto`]
        """
        self._body = body

    def to_dict(self):
        import warnings
        warnings.warn("ListLogsTreeResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListLogsTreeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
