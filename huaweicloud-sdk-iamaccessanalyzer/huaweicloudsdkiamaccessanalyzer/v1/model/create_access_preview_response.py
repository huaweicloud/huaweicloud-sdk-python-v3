# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessPreviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_preview_id': 'str'
    }

    attribute_map = {
        'access_preview_id': 'access_preview_id'
    }

    def __init__(self, access_preview_id=None):
        r"""CreateAccessPreviewResponse

        The model defined in huaweicloud sdk

        :param access_preview_id: 访问预览的唯一标识符。
        :type access_preview_id: str
        """
        
        super(CreateAccessPreviewResponse, self).__init__()

        self._access_preview_id = None
        self.discriminator = None

        if access_preview_id is not None:
            self.access_preview_id = access_preview_id

    @property
    def access_preview_id(self):
        r"""Gets the access_preview_id of this CreateAccessPreviewResponse.

        访问预览的唯一标识符。

        :return: The access_preview_id of this CreateAccessPreviewResponse.
        :rtype: str
        """
        return self._access_preview_id

    @access_preview_id.setter
    def access_preview_id(self, access_preview_id):
        r"""Sets the access_preview_id of this CreateAccessPreviewResponse.

        访问预览的唯一标识符。

        :param access_preview_id: The access_preview_id of this CreateAccessPreviewResponse.
        :type access_preview_id: str
        """
        self._access_preview_id = access_preview_id

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
        if not isinstance(other, CreateAccessPreviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
