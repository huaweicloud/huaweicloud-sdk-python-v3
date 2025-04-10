# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAimTemplateMaterialRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'material_id': 'str',
        'file_type': 'str',
        'file_url': 'str',
        'file_stream': 'str',
        'image_rate': 'str',
        'file_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'material_id': 'material_id',
        'file_type': 'file_type',
        'file_url': 'file_url',
        'file_stream': 'file_stream',
        'image_rate': 'image_rate',
        'file_name': 'file_name',
        'description': 'description'
    }

    def __init__(self, resource_type=None, material_id=None, file_type=None, file_url=None, file_stream=None, image_rate=None, file_name=None, description=None):
        r"""UploadAimTemplateMaterialRequestBody

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型。  - image：图片 - video：视频 - thumbnail：缩略图  &gt; 图片支持png、jpeg、jpg格式，最大2M; &gt; 视频支持格式mp4，大小不超过7M，建议时长不超过33S; &gt; 缩略图支持png、jpeg、jpg格式，大小不超过100K。 
        :type resource_type: str
        :param material_id: 素材ID。 &gt; resource_type&#x3D;thumbnail时，material_id必填，填写内容为上传视频资源返回的material_id字段的值。 
        :type material_id: str
        :param file_type: 文件类型。 - url：资源为URL链接地址 - stream：资源为多媒体资源文件流的BASE64编码，需要带资源类型前缀，样例：\&quot;data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gIoSUNDX1BST0ZJTEUAAQEAAAIYAAAAAAQwAABtbnRyUkdCIFhZWiAAAAAAAAAAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQ...\&quot;，样例过长，未显示全部 
        :type file_type: str
        :param file_url: 文件URL。  &gt; file_type&#x3D;url时，file_url为必填。URL地址必须包含文件格式的后缀，例如：jpg、jpeg，大小写后缀都支持。 
        :type file_url: str
        :param file_stream: 文件资源码流。  &gt; file_type&#x3D;stream时，file_stream为必填。 
        :type file_stream: str
        :param image_rate: 图像比例。 - oneToOne：指1:1比例 - sixteenToNine：指16:9比例 - threeToOne：指3:1比例 - fortyEightToSixtyFive：指48:65比例 - twentyOneToNine：指21:9比例 - threeToFour：指3:4比例  &gt; resource type&#x3D;image时，image_rate必填。 
        :type image_rate: str
        :param file_name: 文件名称。  &gt; file_type&#x3D;stream时，file_name必填。 
        :type file_name: str
        :param description: 描述。
        :type description: str
        """
        
        

        self._resource_type = None
        self._material_id = None
        self._file_type = None
        self._file_url = None
        self._file_stream = None
        self._image_rate = None
        self._file_name = None
        self._description = None
        self.discriminator = None

        self.resource_type = resource_type
        if material_id is not None:
            self.material_id = material_id
        self.file_type = file_type
        if file_url is not None:
            self.file_url = file_url
        if file_stream is not None:
            self.file_stream = file_stream
        if image_rate is not None:
            self.image_rate = image_rate
        if file_name is not None:
            self.file_name = file_name
        if description is not None:
            self.description = description

    @property
    def resource_type(self):
        r"""Gets the resource_type of this UploadAimTemplateMaterialRequestBody.

        资源类型。  - image：图片 - video：视频 - thumbnail：缩略图  > 图片支持png、jpeg、jpg格式，最大2M; > 视频支持格式mp4，大小不超过7M，建议时长不超过33S; > 缩略图支持png、jpeg、jpg格式，大小不超过100K。 

        :return: The resource_type of this UploadAimTemplateMaterialRequestBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this UploadAimTemplateMaterialRequestBody.

        资源类型。  - image：图片 - video：视频 - thumbnail：缩略图  > 图片支持png、jpeg、jpg格式，最大2M; > 视频支持格式mp4，大小不超过7M，建议时长不超过33S; > 缩略图支持png、jpeg、jpg格式，大小不超过100K。 

        :param resource_type: The resource_type of this UploadAimTemplateMaterialRequestBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def material_id(self):
        r"""Gets the material_id of this UploadAimTemplateMaterialRequestBody.

        素材ID。 > resource_type=thumbnail时，material_id必填，填写内容为上传视频资源返回的material_id字段的值。 

        :return: The material_id of this UploadAimTemplateMaterialRequestBody.
        :rtype: str
        """
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        r"""Sets the material_id of this UploadAimTemplateMaterialRequestBody.

        素材ID。 > resource_type=thumbnail时，material_id必填，填写内容为上传视频资源返回的material_id字段的值。 

        :param material_id: The material_id of this UploadAimTemplateMaterialRequestBody.
        :type material_id: str
        """
        self._material_id = material_id

    @property
    def file_type(self):
        r"""Gets the file_type of this UploadAimTemplateMaterialRequestBody.

        文件类型。 - url：资源为URL链接地址 - stream：资源为多媒体资源文件流的BASE64编码，需要带资源类型前缀，样例：\"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gIoSUNDX1BST0ZJTEUAAQEAAAIYAAAAAAQwAABtbnRyUkdCIFhZWiAAAAAAAAAAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQ...\"，样例过长，未显示全部 

        :return: The file_type of this UploadAimTemplateMaterialRequestBody.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this UploadAimTemplateMaterialRequestBody.

        文件类型。 - url：资源为URL链接地址 - stream：资源为多媒体资源文件流的BASE64编码，需要带资源类型前缀，样例：\"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gIoSUNDX1BST0ZJTEUAAQEAAAIYAAAAAAQwAABtbnRyUkdCIFhZWiAAAAAAAAAAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQ...\"，样例过长，未显示全部 

        :param file_type: The file_type of this UploadAimTemplateMaterialRequestBody.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def file_url(self):
        r"""Gets the file_url of this UploadAimTemplateMaterialRequestBody.

        文件URL。  > file_type=url时，file_url为必填。URL地址必须包含文件格式的后缀，例如：jpg、jpeg，大小写后缀都支持。 

        :return: The file_url of this UploadAimTemplateMaterialRequestBody.
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        r"""Sets the file_url of this UploadAimTemplateMaterialRequestBody.

        文件URL。  > file_type=url时，file_url为必填。URL地址必须包含文件格式的后缀，例如：jpg、jpeg，大小写后缀都支持。 

        :param file_url: The file_url of this UploadAimTemplateMaterialRequestBody.
        :type file_url: str
        """
        self._file_url = file_url

    @property
    def file_stream(self):
        r"""Gets the file_stream of this UploadAimTemplateMaterialRequestBody.

        文件资源码流。  > file_type=stream时，file_stream为必填。 

        :return: The file_stream of this UploadAimTemplateMaterialRequestBody.
        :rtype: str
        """
        return self._file_stream

    @file_stream.setter
    def file_stream(self, file_stream):
        r"""Sets the file_stream of this UploadAimTemplateMaterialRequestBody.

        文件资源码流。  > file_type=stream时，file_stream为必填。 

        :param file_stream: The file_stream of this UploadAimTemplateMaterialRequestBody.
        :type file_stream: str
        """
        self._file_stream = file_stream

    @property
    def image_rate(self):
        r"""Gets the image_rate of this UploadAimTemplateMaterialRequestBody.

        图像比例。 - oneToOne：指1:1比例 - sixteenToNine：指16:9比例 - threeToOne：指3:1比例 - fortyEightToSixtyFive：指48:65比例 - twentyOneToNine：指21:9比例 - threeToFour：指3:4比例  > resource type=image时，image_rate必填。 

        :return: The image_rate of this UploadAimTemplateMaterialRequestBody.
        :rtype: str
        """
        return self._image_rate

    @image_rate.setter
    def image_rate(self, image_rate):
        r"""Sets the image_rate of this UploadAimTemplateMaterialRequestBody.

        图像比例。 - oneToOne：指1:1比例 - sixteenToNine：指16:9比例 - threeToOne：指3:1比例 - fortyEightToSixtyFive：指48:65比例 - twentyOneToNine：指21:9比例 - threeToFour：指3:4比例  > resource type=image时，image_rate必填。 

        :param image_rate: The image_rate of this UploadAimTemplateMaterialRequestBody.
        :type image_rate: str
        """
        self._image_rate = image_rate

    @property
    def file_name(self):
        r"""Gets the file_name of this UploadAimTemplateMaterialRequestBody.

        文件名称。  > file_type=stream时，file_name必填。 

        :return: The file_name of this UploadAimTemplateMaterialRequestBody.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this UploadAimTemplateMaterialRequestBody.

        文件名称。  > file_type=stream时，file_name必填。 

        :param file_name: The file_name of this UploadAimTemplateMaterialRequestBody.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def description(self):
        r"""Gets the description of this UploadAimTemplateMaterialRequestBody.

        描述。

        :return: The description of this UploadAimTemplateMaterialRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UploadAimTemplateMaterialRequestBody.

        描述。

        :param description: The description of this UploadAimTemplateMaterialRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UploadAimTemplateMaterialRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
