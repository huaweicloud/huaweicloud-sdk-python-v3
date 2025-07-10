# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FilesCreateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'file_md5': 'str',
        'file_size': 'int',
        'file_type': 'str',
        'asset_id': 'str',
        'asset_file_category': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_md5': 'file_md5',
        'file_size': 'file_size',
        'file_type': 'file_type',
        'asset_id': 'asset_id',
        'asset_file_category': 'asset_file_category'
    }

    def __init__(self, file_name=None, file_md5=None, file_size=None, file_type=None, asset_id=None, asset_file_category=None):
        r"""FilesCreateReq

        The model defined in huaweicloud sdk

        :param file_name: **参数解释**： 文件名。 **约束限制**： 不区分大小写。 **取值范围**： 字符长度1-256位。 **默认取值**： 不涉及
        :type file_name: str
        :param file_md5: **参数解释**： 文件内容MD5值。按照RFC 1864标准计算出消息体的MD5摘要字符串，即消息体128-bit MD5值经过base64编码后得到的字符串。 md5值获取详情请参考[使用Java代码生成文件内容的MD5值](metastudio_02_0052.xml)。 **约束限制**： 不涉及 **取值范围**： 字符长度24位。 **默认取值**： 不涉及
        :type file_md5: str
        :param file_size: **参数解释**： 文件总的大小。 **约束限制**： 最大支持5GB  **默认取值**： 不涉及
        :type file_size: int
        :param file_type: **参数解释**： 文件类型 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位。 **默认取值**： 默认提取文件后缀。
        :type file_type: str
        :param asset_id: **参数解释**： 本平台资产ID。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位。 **默认取值**： 不涉及
        :type asset_id: str
        :param asset_file_category: **参数解释**： 文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：PPT内容页图片文件 * SAMPLE：样例音频或样例动作文件 * OTHER：其他文件 * TEMPORARY：临时文件夹（用于文件替换时上传新文件） * PACKAGE：打包后的资产文件 &gt; * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER &gt; * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER &gt; * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER &gt; * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图) &gt; * 资产类型为IMAGE时，包含MAIN &gt; * 资产类型为VIDEO时，包含MAIN、COVER  **约束限制**： 一个资产中MAIN文件只有一个，且必须有一个 **取值范围**： 字符长度1-128位。 **默认取值**： 不涉及
        :type asset_file_category: str
        """
        
        

        self._file_name = None
        self._file_md5 = None
        self._file_size = None
        self._file_type = None
        self._asset_id = None
        self._asset_file_category = None
        self.discriminator = None

        self.file_name = file_name
        self.file_md5 = file_md5
        self.file_size = file_size
        self.file_type = file_type
        self.asset_id = asset_id
        self.asset_file_category = asset_file_category

    @property
    def file_name(self):
        r"""Gets the file_name of this FilesCreateReq.

        **参数解释**： 文件名。 **约束限制**： 不区分大小写。 **取值范围**： 字符长度1-256位。 **默认取值**： 不涉及

        :return: The file_name of this FilesCreateReq.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this FilesCreateReq.

        **参数解释**： 文件名。 **约束限制**： 不区分大小写。 **取值范围**： 字符长度1-256位。 **默认取值**： 不涉及

        :param file_name: The file_name of this FilesCreateReq.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_md5(self):
        r"""Gets the file_md5 of this FilesCreateReq.

        **参数解释**： 文件内容MD5值。按照RFC 1864标准计算出消息体的MD5摘要字符串，即消息体128-bit MD5值经过base64编码后得到的字符串。 md5值获取详情请参考[使用Java代码生成文件内容的MD5值](metastudio_02_0052.xml)。 **约束限制**： 不涉及 **取值范围**： 字符长度24位。 **默认取值**： 不涉及

        :return: The file_md5 of this FilesCreateReq.
        :rtype: str
        """
        return self._file_md5

    @file_md5.setter
    def file_md5(self, file_md5):
        r"""Sets the file_md5 of this FilesCreateReq.

        **参数解释**： 文件内容MD5值。按照RFC 1864标准计算出消息体的MD5摘要字符串，即消息体128-bit MD5值经过base64编码后得到的字符串。 md5值获取详情请参考[使用Java代码生成文件内容的MD5值](metastudio_02_0052.xml)。 **约束限制**： 不涉及 **取值范围**： 字符长度24位。 **默认取值**： 不涉及

        :param file_md5: The file_md5 of this FilesCreateReq.
        :type file_md5: str
        """
        self._file_md5 = file_md5

    @property
    def file_size(self):
        r"""Gets the file_size of this FilesCreateReq.

        **参数解释**： 文件总的大小。 **约束限制**： 最大支持5GB  **默认取值**： 不涉及

        :return: The file_size of this FilesCreateReq.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this FilesCreateReq.

        **参数解释**： 文件总的大小。 **约束限制**： 最大支持5GB  **默认取值**： 不涉及

        :param file_size: The file_size of this FilesCreateReq.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_type(self):
        r"""Gets the file_type of this FilesCreateReq.

        **参数解释**： 文件类型 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位。 **默认取值**： 默认提取文件后缀。

        :return: The file_type of this FilesCreateReq.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this FilesCreateReq.

        **参数解释**： 文件类型 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位。 **默认取值**： 默认提取文件后缀。

        :param file_type: The file_type of this FilesCreateReq.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def asset_id(self):
        r"""Gets the asset_id of this FilesCreateReq.

        **参数解释**： 本平台资产ID。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位。 **默认取值**： 不涉及

        :return: The asset_id of this FilesCreateReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this FilesCreateReq.

        **参数解释**： 本平台资产ID。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位。 **默认取值**： 不涉及

        :param asset_id: The asset_id of this FilesCreateReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_file_category(self):
        r"""Gets the asset_file_category of this FilesCreateReq.

        **参数解释**： 文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：PPT内容页图片文件 * SAMPLE：样例音频或样例动作文件 * OTHER：其他文件 * TEMPORARY：临时文件夹（用于文件替换时上传新文件） * PACKAGE：打包后的资产文件 > * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER > * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER > * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER > * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图) > * 资产类型为IMAGE时，包含MAIN > * 资产类型为VIDEO时，包含MAIN、COVER  **约束限制**： 一个资产中MAIN文件只有一个，且必须有一个 **取值范围**： 字符长度1-128位。 **默认取值**： 不涉及

        :return: The asset_file_category of this FilesCreateReq.
        :rtype: str
        """
        return self._asset_file_category

    @asset_file_category.setter
    def asset_file_category(self, asset_file_category):
        r"""Sets the asset_file_category of this FilesCreateReq.

        **参数解释**： 文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：PPT内容页图片文件 * SAMPLE：样例音频或样例动作文件 * OTHER：其他文件 * TEMPORARY：临时文件夹（用于文件替换时上传新文件） * PACKAGE：打包后的资产文件 > * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER > * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER > * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER > * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图) > * 资产类型为IMAGE时，包含MAIN > * 资产类型为VIDEO时，包含MAIN、COVER  **约束限制**： 一个资产中MAIN文件只有一个，且必须有一个 **取值范围**： 字符长度1-128位。 **默认取值**： 不涉及

        :param asset_file_category: The asset_file_category of this FilesCreateReq.
        :type asset_file_category: str
        """
        self._asset_file_category = asset_file_category

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
        if not isinstance(other, FilesCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
