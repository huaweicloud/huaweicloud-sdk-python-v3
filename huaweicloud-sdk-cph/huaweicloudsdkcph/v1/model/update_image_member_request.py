# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateImageMemberRequest:

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
        'body': 'UpdateImageMemberRequestBody'
    }

    attribute_map = {
        'image_id': 'image_id',
        'body': 'body'
    }

    def __init__(self, image_id=None, body=None):
        r"""UpdateImageMemberRequest

        The model defined in huaweicloud sdk

        :param image_id: 镜像id。
        :type image_id: str
        :param body: Body of the UpdateImageMemberRequest
        :type body: :class:`huaweicloudsdkcph.v1.UpdateImageMemberRequestBody`
        """
        
        

        self._image_id = None
        self._body = None
        self.discriminator = None

        self.image_id = image_id
        if body is not None:
            self.body = body

    @property
    def image_id(self):
        r"""Gets the image_id of this UpdateImageMemberRequest.

        镜像id。

        :return: The image_id of this UpdateImageMemberRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this UpdateImageMemberRequest.

        镜像id。

        :param image_id: The image_id of this UpdateImageMemberRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def body(self):
        r"""Gets the body of this UpdateImageMemberRequest.

        :return: The body of this UpdateImageMemberRequest.
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateImageMemberRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateImageMemberRequest.

        :param body: The body of this UpdateImageMemberRequest.
        :type body: :class:`huaweicloudsdkcph.v1.UpdateImageMemberRequestBody`
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
        if not isinstance(other, UpdateImageMemberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
