# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddFacesUrlReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'image_url': 'str',
        'external_fields': 'object',
        'external_image_id': 'str'
    }

    attribute_map = {
        'image_url': 'image_url',
        'external_fields': 'external_fields',
        'external_image_id': 'external_image_id'
    }

    def __init__(self, image_url=None, external_fields=None, external_image_id=None):
        """AddFacesUrlReq - a model defined in huaweicloud sdk"""
        
        

        self._image_url = None
        self._external_fields = None
        self._external_image_id = None
        self.discriminator = None

        self.image_url = image_url
        if external_fields is not None:
            self.external_fields = external_fields
        if external_image_id is not None:
            self.external_image_id = external_image_id

    @property
    def image_url(self):
        """Gets the image_url of this AddFacesUrlReq.

        图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。 开通读取权限的操作请参见服务授权。

        :return: The image_url of this AddFacesUrlReq.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this AddFacesUrlReq.

        图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。 开通读取权限的操作请参见服务授权。

        :param image_url: The image_url of this AddFacesUrlReq.
        :type: str
        """
        self._image_url = image_url

    @property
    def external_fields(self):
        """Gets the external_fields of this AddFacesUrlReq.

        根据用户自定义数据类型，填入相应的数值。 创建faceset时定义该字段，Json字符串不校验重复性，参考自定义字段。

        :return: The external_fields of this AddFacesUrlReq.
        :rtype: object
        """
        return self._external_fields

    @external_fields.setter
    def external_fields(self, external_fields):
        """Sets the external_fields of this AddFacesUrlReq.

        根据用户自定义数据类型，填入相应的数值。 创建faceset时定义该字段，Json字符串不校验重复性，参考自定义字段。

        :param external_fields: The external_fields of this AddFacesUrlReq.
        :type: object
        """
        self._external_fields = external_fields

    @property
    def external_image_id(self):
        """Gets the external_image_id of this AddFacesUrlReq.

        用户指定的图片外部ID，与当前图像绑定。用户没提供，系统会生成一个。 该ID长度范围为1～36位，可以包含字母、数字、中划线或者下划线，不包含其他的特殊字符。

        :return: The external_image_id of this AddFacesUrlReq.
        :rtype: str
        """
        return self._external_image_id

    @external_image_id.setter
    def external_image_id(self, external_image_id):
        """Sets the external_image_id of this AddFacesUrlReq.

        用户指定的图片外部ID，与当前图像绑定。用户没提供，系统会生成一个。 该ID长度范围为1～36位，可以包含字母、数字、中划线或者下划线，不包含其他的特殊字符。

        :param external_image_id: The external_image_id of this AddFacesUrlReq.
        :type: str
        """
        self._external_image_id = external_image_id

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
        if not isinstance(other, AddFacesUrlReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
