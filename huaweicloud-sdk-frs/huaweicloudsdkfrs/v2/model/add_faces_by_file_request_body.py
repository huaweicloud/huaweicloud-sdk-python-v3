# coding: utf-8

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
        'external_fields': 'str',
        'single': 'bool'
    }

    attribute_map = {
        'image_file': 'image_file',
        'external_image_id': 'external_image_id',
        'external_fields': 'external_fields',
        'single': 'single'
    }

    def __init__(self, image_file=None, external_image_id=None, external_fields=None, single=None):
        """AddFacesByFileRequestBody

        The model defined in huaweicloud sdk

        :param image_file: 本地图片文件，图片不能超过8MB，建议小于1MB。上传文件时，请求格式为multipart。
        :type image_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param external_image_id: 用户指定的图片外部ID，与当前图像绑定。用户没提供，系统会生成一个。 该ID长度范围为1～36位，可以包含字母、数字、中划线或者下划线，不包含其他的特殊字符。
        :type external_image_id: str
        :param external_fields: [根据用户自定义数据类型，填入相应的数值。创建faceset时定义该字段，Json字符串不校验重复性，参考[自定义字段](https://support.huaweicloud.com/api-face/face_02_0012.html)。](tag:hc) [根据用户自定义数据类型，填入相应的数值。创建faceset时定义该字段，Json字符串不校验重复性，参考[自定义字段](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0012.html)。](tag:hk)
        :type external_fields: str
        :param single: 是否将图片中的最大人脸添加至人脸库。可选值包括: • true: 传入的单张图片中如果包含多张人脸，则只将最大人脸添加到人脸库中。 • false: 默认为false。传入的单张图片中如果包含多张人脸，则将所有人脸添加至人脸库中。
        :type single: bool
        """
        
        

        self._image_file = None
        self._external_image_id = None
        self._external_fields = None
        self._single = None
        self.discriminator = None

        self.image_file = image_file
        if external_image_id is not None:
            self.external_image_id = external_image_id
        if external_fields is not None:
            self.external_fields = external_fields
        if single is not None:
            self.single = single

    @property
    def image_file(self):
        """Gets the image_file of this AddFacesByFileRequestBody.

        本地图片文件，图片不能超过8MB，建议小于1MB。上传文件时，请求格式为multipart。

        :return: The image_file of this AddFacesByFileRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._image_file

    @image_file.setter
    def image_file(self, image_file):
        """Sets the image_file of this AddFacesByFileRequestBody.

        本地图片文件，图片不能超过8MB，建议小于1MB。上传文件时，请求格式为multipart。

        :param image_file: The image_file of this AddFacesByFileRequestBody.
        :type image_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
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
        :type external_image_id: str
        """
        self._external_image_id = external_image_id

    @property
    def external_fields(self):
        """Gets the external_fields of this AddFacesByFileRequestBody.

        [根据用户自定义数据类型，填入相应的数值。创建faceset时定义该字段，Json字符串不校验重复性，参考[自定义字段](https://support.huaweicloud.com/api-face/face_02_0012.html)。](tag:hc) [根据用户自定义数据类型，填入相应的数值。创建faceset时定义该字段，Json字符串不校验重复性，参考[自定义字段](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0012.html)。](tag:hk)

        :return: The external_fields of this AddFacesByFileRequestBody.
        :rtype: str
        """
        return self._external_fields

    @external_fields.setter
    def external_fields(self, external_fields):
        """Sets the external_fields of this AddFacesByFileRequestBody.

        [根据用户自定义数据类型，填入相应的数值。创建faceset时定义该字段，Json字符串不校验重复性，参考[自定义字段](https://support.huaweicloud.com/api-face/face_02_0012.html)。](tag:hc) [根据用户自定义数据类型，填入相应的数值。创建faceset时定义该字段，Json字符串不校验重复性，参考[自定义字段](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0012.html)。](tag:hk)

        :param external_fields: The external_fields of this AddFacesByFileRequestBody.
        :type external_fields: str
        """
        self._external_fields = external_fields

    @property
    def single(self):
        """Gets the single of this AddFacesByFileRequestBody.

        是否将图片中的最大人脸添加至人脸库。可选值包括: • true: 传入的单张图片中如果包含多张人脸，则只将最大人脸添加到人脸库中。 • false: 默认为false。传入的单张图片中如果包含多张人脸，则将所有人脸添加至人脸库中。

        :return: The single of this AddFacesByFileRequestBody.
        :rtype: bool
        """
        return self._single

    @single.setter
    def single(self, single):
        """Sets the single of this AddFacesByFileRequestBody.

        是否将图片中的最大人脸添加至人脸库。可选值包括: • true: 传入的单张图片中如果包含多张人脸，则只将最大人脸添加到人脸库中。 • false: 默认为false。传入的单张图片中如果包含多张人脸，则将所有人脸添加至人脸库中。

        :param single: The single of this AddFacesByFileRequestBody.
        :type single: bool
        """
        self._single = single

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
