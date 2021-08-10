# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddFacesByFileRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'image_file': 'file',
        'external_image_id': 'str',
        'external_fields': 'str'
    }

    attribute_map = {
        'image_file': 'image_file',
        'external_image_id': 'external_image_id',
        'external_fields': 'external_fields'
    }

    def __init__(self, image_file=None, external_image_id=None, external_fields=None):
        """AddFacesByFileRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._image_file = None
        self._external_image_id = None
        self._external_fields = None
        self.discriminator = None

        if image_file is not None:
            self.image_file = image_file
        if external_image_id is not None:
            self.external_image_id = external_image_id
        if external_fields is not None:
            self.external_fields = external_fields

    @property
    def image_file(self):
        """Gets the image_file of this AddFacesByFileRequestBody.

        本地图片文件，图片不能超过8MB，建议小于1MB。上传文件时，请求格式为multipart。

        :return: The image_file of this AddFacesByFileRequestBody.
        :rtype: file
        """
        return self._image_file

    @image_file.setter
    def image_file(self, image_file):
        """Sets the image_file of this AddFacesByFileRequestBody.

        本地图片文件，图片不能超过8MB，建议小于1MB。上传文件时，请求格式为multipart。

        :param image_file: The image_file of this AddFacesByFileRequestBody.
        :type: file
        """
        self._image_file = image_file

    @property
    def external_image_id(self):
        """Gets the external_image_id of this AddFacesByFileRequestBody.

        用户指定的图片外部ID，与当前图像绑定。用户没提供，系统会生成一个。 该ID长度范围为1～36位，可以包含字母、数字、中划线或者下划线，不包含其他的特殊字符。

        :return: The external_image_id of this AddFacesByFileRequestBody.
        :rtype: str
        """
        return self._external_image_id

    @external_image_id.setter
    def external_image_id(self, external_image_id):
        """Sets the external_image_id of this AddFacesByFileRequestBody.

        用户指定的图片外部ID，与当前图像绑定。用户没提供，系统会生成一个。 该ID长度范围为1～36位，可以包含字母、数字、中划线或者下划线，不包含其他的特殊字符。

        :param external_image_id: The external_image_id of this AddFacesByFileRequestBody.
        :type: str
        """
        self._external_image_id = external_image_id

    @property
    def external_fields(self):
        """Gets the external_fields of this AddFacesByFileRequestBody.

        根据用户自定义数据类型，填入相应的数值。 创建faceset时定义该字段，Json字符串不校验重复性，参考[自定义字段](zh-cn_topic_0130807044.xml)。

        :return: The external_fields of this AddFacesByFileRequestBody.
        :rtype: str
        """
        return self._external_fields

    @external_fields.setter
    def external_fields(self, external_fields):
        """Sets the external_fields of this AddFacesByFileRequestBody.

        根据用户自定义数据类型，填入相应的数值。 创建faceset时定义该字段，Json字符串不校验重复性，参考[自定义字段](zh-cn_topic_0130807044.xml)。

        :param external_fields: The external_fields of this AddFacesByFileRequestBody.
        :type: str
        """
        self._external_fields = external_fields

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
        if not isinstance(other, AddFacesByFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
