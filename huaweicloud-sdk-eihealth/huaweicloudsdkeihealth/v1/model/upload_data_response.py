# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'multipart_id': 'str'
    }

    attribute_map = {
        'multipart_id': 'multipart_id'
    }

    def __init__(self, multipart_id=None):
        r"""UploadDataResponse

        The model defined in huaweicloud sdk

        :param multipart_id: 分段上传任务id
        :type multipart_id: str
        """
        
        super(UploadDataResponse, self).__init__()

        self._multipart_id = None
        self.discriminator = None

        if multipart_id is not None:
            self.multipart_id = multipart_id

    @property
    def multipart_id(self):
        r"""Gets the multipart_id of this UploadDataResponse.

        分段上传任务id

        :return: The multipart_id of this UploadDataResponse.
        :rtype: str
        """
        return self._multipart_id

    @multipart_id.setter
    def multipart_id(self, multipart_id):
        r"""Sets the multipart_id of this UploadDataResponse.

        分段上传任务id

        :param multipart_id: The multipart_id of this UploadDataResponse.
        :type multipart_id: str
        """
        self._multipart_id = multipart_id

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
        if not isinstance(other, UploadDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
