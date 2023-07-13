# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfirmImageUploadResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'image_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'image_url': 'image_url'
    }

    def __init__(self, id=None, image_url=None):
        """ConfirmImageUploadResponse

        The model defined in huaweicloud sdk

        :param id: 水印配置模板id&lt;br/&gt; 
        :type id: str
        :param image_url: 水印图片的下载url&lt;br/&gt; 
        :type image_url: str
        """
        
        super(ConfirmImageUploadResponse, self).__init__()

        self._id = None
        self._image_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if image_url is not None:
            self.image_url = image_url

    @property
    def id(self):
        """Gets the id of this ConfirmImageUploadResponse.

        水印配置模板id<br/> 

        :return: The id of this ConfirmImageUploadResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfirmImageUploadResponse.

        水印配置模板id<br/> 

        :param id: The id of this ConfirmImageUploadResponse.
        :type id: str
        """
        self._id = id

    @property
    def image_url(self):
        """Gets the image_url of this ConfirmImageUploadResponse.

        水印图片的下载url<br/> 

        :return: The image_url of this ConfirmImageUploadResponse.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ConfirmImageUploadResponse.

        水印图片的下载url<br/> 

        :param image_url: The image_url of this ConfirmImageUploadResponse.
        :type image_url: str
        """
        self._image_url = image_url

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
        if not isinstance(other, ConfirmImageUploadResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
