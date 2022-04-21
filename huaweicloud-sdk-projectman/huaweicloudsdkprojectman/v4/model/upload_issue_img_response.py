# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadIssueImgResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'img_id': 'str',
        'img_url': 'str'
    }

    attribute_map = {
        'img_id': 'img_id',
        'img_url': 'img_url'
    }

    def __init__(self, img_id=None, img_url=None):
        """UploadIssueImgResponse

        The model defined in huaweicloud sdk

        :param img_id: 图片id
        :type img_id: str
        :param img_url: 图片url v1改成v3作为下载图片请求
        :type img_url: str
        """
        
        super(UploadIssueImgResponse, self).__init__()

        self._img_id = None
        self._img_url = None
        self.discriminator = None

        if img_id is not None:
            self.img_id = img_id
        if img_url is not None:
            self.img_url = img_url

    @property
    def img_id(self):
        """Gets the img_id of this UploadIssueImgResponse.

        图片id

        :return: The img_id of this UploadIssueImgResponse.
        :rtype: str
        """
        return self._img_id

    @img_id.setter
    def img_id(self, img_id):
        """Sets the img_id of this UploadIssueImgResponse.

        图片id

        :param img_id: The img_id of this UploadIssueImgResponse.
        :type img_id: str
        """
        self._img_id = img_id

    @property
    def img_url(self):
        """Gets the img_url of this UploadIssueImgResponse.

        图片url v1改成v3作为下载图片请求

        :return: The img_url of this UploadIssueImgResponse.
        :rtype: str
        """
        return self._img_url

    @img_url.setter
    def img_url(self, img_url):
        """Sets the img_url of this UploadIssueImgResponse.

        图片url v1改成v3作为下载图片请求

        :param img_url: The img_url of this UploadIssueImgResponse.
        :type img_url: str
        """
        self._img_url = img_url

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
        if not isinstance(other, UploadIssueImgResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
