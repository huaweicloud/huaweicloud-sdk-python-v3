# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportImageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'body': 'ExportImageRequestBody'
    }

    attribute_map = {
        'image_id': 'image_id',
        'body': 'body'
    }

    def __init__(self, image_id=None, body=None):
        """ExportImageRequest

        The model defined in huaweicloud sdk

        :param image_id: 镜像ID。
        :type image_id: str
        :param body: Body of the ExportImageRequest
        :type body: :class:`huaweicloudsdkims.v2.ExportImageRequestBody`
        """
        
        

        self._image_id = None
        self._body = None
        self.discriminator = None

        self.image_id = image_id
        if body is not None:
            self.body = body

    @property
    def image_id(self):
        """Gets the image_id of this ExportImageRequest.

        镜像ID。

        :return: The image_id of this ExportImageRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ExportImageRequest.

        镜像ID。

        :param image_id: The image_id of this ExportImageRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def body(self):
        """Gets the body of this ExportImageRequest.

        :return: The body of this ExportImageRequest.
        :rtype: :class:`huaweicloudsdkims.v2.ExportImageRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ExportImageRequest.

        :param body: The body of this ExportImageRequest.
        :type body: :class:`huaweicloudsdkims.v2.ExportImageRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ExportImageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
