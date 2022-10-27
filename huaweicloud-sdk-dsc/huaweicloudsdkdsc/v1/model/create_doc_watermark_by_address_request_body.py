# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDocWatermarkByAddressRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'src_file': 'str',
        'doc_type': 'str',
        'dst_file': 'str',
        'blind_watermark': 'str',
        'visible_watermark': 'str',
        'image_mark': 'str',
        'visible_type': 'str',
        'file_password': 'str',
        'marked_file_password': 'str',
        'readonly_password': 'str',
        'front': 'int',
        'rotation': 'int',
        'opacity': 'float'
    }

    attribute_map = {
        'region_id': 'region_id',
        'src_file': 'src_file',
        'doc_type': 'doc_type',
        'dst_file': 'dst_file',
        'blind_watermark': 'blind_watermark',
        'visible_watermark': 'visible_watermark',
        'image_mark': 'image_mark',
        'visible_type': 'visible_type',
        'file_password': 'file_password',
        'marked_file_password': 'marked_file_password',
        'readonly_password': 'readonly_password',
        'front': 'front',
        'rotation': 'rotation',
        'opacity': 'opacity'
    }

    def __init__(self, region_id=None, src_file=None, doc_type=None, dst_file=None, blind_watermark=None, visible_watermark=None, image_mark=None, visible_type=None, file_password=None, marked_file_password=None, readonly_password=None, front=None, rotation=None, opacity=None):
        """CreateDocWatermarkByAddressRequestBody

        The model defined in huaweicloud sdk

        :param region_id: 项目所在region的id，如：xx-xx-1。
        :type region_id: str
        :param src_file: 待添加水印的文档地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。
        :type src_file: str
        :param doc_type: 待嵌入水印的文档类型。
        :type doc_type: str
        :param dst_file: 添加水印后的文档存放地址，格式和要求同src_file字段，不设置时，默认取src_file的值，即添加水印后覆盖原文件。
        :type dst_file: str
        :param blind_watermark: 暗文字水印内容，与“visible_watermark”字段至少有一个不为空
        :type blind_watermark: str
        :param visible_watermark: 明文字水印内容，与暗水印“blind_watermark”字段至少有一个不为空。
        :type visible_watermark: str
        :param image_mark: 待嵌入的图形明水印文件的地址,  字段格式要求同src_file字段，图形文件的格式必须为“png”或“jpg”，否则返回参数错误；图像文件大小不超过1MB
        :type image_mark: str
        :param visible_type: 该字段控制明水印嵌入文字还是图片。默认为**TEXT**类型，需填写visible_watermark字段设置明文字水印； 当该字段为**IMAGE**时，需填写image_watermark字段设置水印图片地址此时 ，“visible_watermark”，“font_size”，“rotation”和“opacity”字段无效。
        :type visible_type: str
        :param file_password: 待加水印文件有密码时，读取文件的密码， 最大支持长度256。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。
        :type file_password: str
        :param marked_file_password: 添加水印后给文件设置密码， 最大支持长度256。默认不加文档密码。
        :type marked_file_password: str
        :param readonly_password: 添加水印后给文件设置只读密码， 最大支持长度256。默认不加只读密码。
        :type readonly_password: str
        :param front: 明水印字体大小，取值为[1,100]，默认值50
        :type front: int
        :param rotation: 明水印旋转角度，逆时针方向，取值为[0,90]，默认值45。
        :type rotation: int
        :param opacity: 明水印的透明度，取值[0,1]，默认值为0.3；
        :type opacity: float
        """
        
        

        self._region_id = None
        self._src_file = None
        self._doc_type = None
        self._dst_file = None
        self._blind_watermark = None
        self._visible_watermark = None
        self._image_mark = None
        self._visible_type = None
        self._file_password = None
        self._marked_file_password = None
        self._readonly_password = None
        self._front = None
        self._rotation = None
        self._opacity = None
        self.discriminator = None

        self.region_id = region_id
        self.src_file = src_file
        self.doc_type = doc_type
        if dst_file is not None:
            self.dst_file = dst_file
        if blind_watermark is not None:
            self.blind_watermark = blind_watermark
        if visible_watermark is not None:
            self.visible_watermark = visible_watermark
        if image_mark is not None:
            self.image_mark = image_mark
        if visible_type is not None:
            self.visible_type = visible_type
        if file_password is not None:
            self.file_password = file_password
        if marked_file_password is not None:
            self.marked_file_password = marked_file_password
        if readonly_password is not None:
            self.readonly_password = readonly_password
        if front is not None:
            self.front = front
        if rotation is not None:
            self.rotation = rotation
        if opacity is not None:
            self.opacity = opacity

    @property
    def region_id(self):
        """Gets the region_id of this CreateDocWatermarkByAddressRequestBody.

        项目所在region的id，如：xx-xx-1。

        :return: The region_id of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateDocWatermarkByAddressRequestBody.

        项目所在region的id，如：xx-xx-1。

        :param region_id: The region_id of this CreateDocWatermarkByAddressRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def src_file(self):
        """Gets the src_file of this CreateDocWatermarkByAddressRequestBody.

        待添加水印的文档地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。

        :return: The src_file of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._src_file

    @src_file.setter
    def src_file(self, src_file):
        """Sets the src_file of this CreateDocWatermarkByAddressRequestBody.

        待添加水印的文档地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。

        :param src_file: The src_file of this CreateDocWatermarkByAddressRequestBody.
        :type src_file: str
        """
        self._src_file = src_file

    @property
    def doc_type(self):
        """Gets the doc_type of this CreateDocWatermarkByAddressRequestBody.

        待嵌入水印的文档类型。

        :return: The doc_type of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """Sets the doc_type of this CreateDocWatermarkByAddressRequestBody.

        待嵌入水印的文档类型。

        :param doc_type: The doc_type of this CreateDocWatermarkByAddressRequestBody.
        :type doc_type: str
        """
        self._doc_type = doc_type

    @property
    def dst_file(self):
        """Gets the dst_file of this CreateDocWatermarkByAddressRequestBody.

        添加水印后的文档存放地址，格式和要求同src_file字段，不设置时，默认取src_file的值，即添加水印后覆盖原文件。

        :return: The dst_file of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._dst_file

    @dst_file.setter
    def dst_file(self, dst_file):
        """Sets the dst_file of this CreateDocWatermarkByAddressRequestBody.

        添加水印后的文档存放地址，格式和要求同src_file字段，不设置时，默认取src_file的值，即添加水印后覆盖原文件。

        :param dst_file: The dst_file of this CreateDocWatermarkByAddressRequestBody.
        :type dst_file: str
        """
        self._dst_file = dst_file

    @property
    def blind_watermark(self):
        """Gets the blind_watermark of this CreateDocWatermarkByAddressRequestBody.

        暗文字水印内容，与“visible_watermark”字段至少有一个不为空

        :return: The blind_watermark of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._blind_watermark

    @blind_watermark.setter
    def blind_watermark(self, blind_watermark):
        """Sets the blind_watermark of this CreateDocWatermarkByAddressRequestBody.

        暗文字水印内容，与“visible_watermark”字段至少有一个不为空

        :param blind_watermark: The blind_watermark of this CreateDocWatermarkByAddressRequestBody.
        :type blind_watermark: str
        """
        self._blind_watermark = blind_watermark

    @property
    def visible_watermark(self):
        """Gets the visible_watermark of this CreateDocWatermarkByAddressRequestBody.

        明文字水印内容，与暗水印“blind_watermark”字段至少有一个不为空。

        :return: The visible_watermark of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._visible_watermark

    @visible_watermark.setter
    def visible_watermark(self, visible_watermark):
        """Sets the visible_watermark of this CreateDocWatermarkByAddressRequestBody.

        明文字水印内容，与暗水印“blind_watermark”字段至少有一个不为空。

        :param visible_watermark: The visible_watermark of this CreateDocWatermarkByAddressRequestBody.
        :type visible_watermark: str
        """
        self._visible_watermark = visible_watermark

    @property
    def image_mark(self):
        """Gets the image_mark of this CreateDocWatermarkByAddressRequestBody.

        待嵌入的图形明水印文件的地址,  字段格式要求同src_file字段，图形文件的格式必须为“png”或“jpg”，否则返回参数错误；图像文件大小不超过1MB

        :return: The image_mark of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._image_mark

    @image_mark.setter
    def image_mark(self, image_mark):
        """Sets the image_mark of this CreateDocWatermarkByAddressRequestBody.

        待嵌入的图形明水印文件的地址,  字段格式要求同src_file字段，图形文件的格式必须为“png”或“jpg”，否则返回参数错误；图像文件大小不超过1MB

        :param image_mark: The image_mark of this CreateDocWatermarkByAddressRequestBody.
        :type image_mark: str
        """
        self._image_mark = image_mark

    @property
    def visible_type(self):
        """Gets the visible_type of this CreateDocWatermarkByAddressRequestBody.

        该字段控制明水印嵌入文字还是图片。默认为**TEXT**类型，需填写visible_watermark字段设置明文字水印； 当该字段为**IMAGE**时，需填写image_watermark字段设置水印图片地址此时 ，“visible_watermark”，“font_size”，“rotation”和“opacity”字段无效。

        :return: The visible_type of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._visible_type

    @visible_type.setter
    def visible_type(self, visible_type):
        """Sets the visible_type of this CreateDocWatermarkByAddressRequestBody.

        该字段控制明水印嵌入文字还是图片。默认为**TEXT**类型，需填写visible_watermark字段设置明文字水印； 当该字段为**IMAGE**时，需填写image_watermark字段设置水印图片地址此时 ，“visible_watermark”，“font_size”，“rotation”和“opacity”字段无效。

        :param visible_type: The visible_type of this CreateDocWatermarkByAddressRequestBody.
        :type visible_type: str
        """
        self._visible_type = visible_type

    @property
    def file_password(self):
        """Gets the file_password of this CreateDocWatermarkByAddressRequestBody.

        待加水印文件有密码时，读取文件的密码， 最大支持长度256。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。

        :return: The file_password of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._file_password

    @file_password.setter
    def file_password(self, file_password):
        """Sets the file_password of this CreateDocWatermarkByAddressRequestBody.

        待加水印文件有密码时，读取文件的密码， 最大支持长度256。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。

        :param file_password: The file_password of this CreateDocWatermarkByAddressRequestBody.
        :type file_password: str
        """
        self._file_password = file_password

    @property
    def marked_file_password(self):
        """Gets the marked_file_password of this CreateDocWatermarkByAddressRequestBody.

        添加水印后给文件设置密码， 最大支持长度256。默认不加文档密码。

        :return: The marked_file_password of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._marked_file_password

    @marked_file_password.setter
    def marked_file_password(self, marked_file_password):
        """Sets the marked_file_password of this CreateDocWatermarkByAddressRequestBody.

        添加水印后给文件设置密码， 最大支持长度256。默认不加文档密码。

        :param marked_file_password: The marked_file_password of this CreateDocWatermarkByAddressRequestBody.
        :type marked_file_password: str
        """
        self._marked_file_password = marked_file_password

    @property
    def readonly_password(self):
        """Gets the readonly_password of this CreateDocWatermarkByAddressRequestBody.

        添加水印后给文件设置只读密码， 最大支持长度256。默认不加只读密码。

        :return: The readonly_password of this CreateDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._readonly_password

    @readonly_password.setter
    def readonly_password(self, readonly_password):
        """Sets the readonly_password of this CreateDocWatermarkByAddressRequestBody.

        添加水印后给文件设置只读密码， 最大支持长度256。默认不加只读密码。

        :param readonly_password: The readonly_password of this CreateDocWatermarkByAddressRequestBody.
        :type readonly_password: str
        """
        self._readonly_password = readonly_password

    @property
    def front(self):
        """Gets the front of this CreateDocWatermarkByAddressRequestBody.

        明水印字体大小，取值为[1,100]，默认值50

        :return: The front of this CreateDocWatermarkByAddressRequestBody.
        :rtype: int
        """
        return self._front

    @front.setter
    def front(self, front):
        """Sets the front of this CreateDocWatermarkByAddressRequestBody.

        明水印字体大小，取值为[1,100]，默认值50

        :param front: The front of this CreateDocWatermarkByAddressRequestBody.
        :type front: int
        """
        self._front = front

    @property
    def rotation(self):
        """Gets the rotation of this CreateDocWatermarkByAddressRequestBody.

        明水印旋转角度，逆时针方向，取值为[0,90]，默认值45。

        :return: The rotation of this CreateDocWatermarkByAddressRequestBody.
        :rtype: int
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this CreateDocWatermarkByAddressRequestBody.

        明水印旋转角度，逆时针方向，取值为[0,90]，默认值45。

        :param rotation: The rotation of this CreateDocWatermarkByAddressRequestBody.
        :type rotation: int
        """
        self._rotation = rotation

    @property
    def opacity(self):
        """Gets the opacity of this CreateDocWatermarkByAddressRequestBody.

        明水印的透明度，取值[0,1]，默认值为0.3；

        :return: The opacity of this CreateDocWatermarkByAddressRequestBody.
        :rtype: float
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Sets the opacity of this CreateDocWatermarkByAddressRequestBody.

        明水印的透明度，取值[0,1]，默认值为0.3；

        :param opacity: The opacity of this CreateDocWatermarkByAddressRequestBody.
        :type opacity: float
        """
        self._opacity = opacity

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
        if not isinstance(other, CreateDocWatermarkByAddressRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
