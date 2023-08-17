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
        """FilesCreateReq

        The model defined in huaweicloud sdk

        :param file_name: 文件名，不区分大小写，最大长度256，最小长度1。
        :type file_name: str
        :param file_md5: 文件内容MD5值，MD5值需要进行Base64编码。
        :type file_md5: str
        :param file_size: 文件总的大小，最小1，最大5368709120。
        :type file_size: int
        :param file_type: 文件类型（默认提取文件后缀）。
        :type file_type: str
        :param asset_id: 资产ID。
        :type asset_id: str
        :param asset_file_category: 文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：内容页图片 * SAMPLE：样例音频 * OTHER：其他文件 * WHOLE_MODEL：全模型 * USER_MODIFIED_MODEL：用户上传模型 &gt; * 资产类型为SCENE、ANIMATION、VIDEO、IMAGE、MATERIAL时，包含MAIN、COVER和OTHER &gt; * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER &gt; * 资产类型为HUMAN_MODEL时，包含MAIN、COVER、WHOLE_MODEL、USER_MODIFIED_MODEL和OTHER &gt; * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER &gt; * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER(遮罩文件) &gt; * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图)
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
        """Gets the file_name of this FilesCreateReq.

        文件名，不区分大小写，最大长度256，最小长度1。

        :return: The file_name of this FilesCreateReq.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FilesCreateReq.

        文件名，不区分大小写，最大长度256，最小长度1。

        :param file_name: The file_name of this FilesCreateReq.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_md5(self):
        """Gets the file_md5 of this FilesCreateReq.

        文件内容MD5值，MD5值需要进行Base64编码。

        :return: The file_md5 of this FilesCreateReq.
        :rtype: str
        """
        return self._file_md5

    @file_md5.setter
    def file_md5(self, file_md5):
        """Sets the file_md5 of this FilesCreateReq.

        文件内容MD5值，MD5值需要进行Base64编码。

        :param file_md5: The file_md5 of this FilesCreateReq.
        :type file_md5: str
        """
        self._file_md5 = file_md5

    @property
    def file_size(self):
        """Gets the file_size of this FilesCreateReq.

        文件总的大小，最小1，最大5368709120。

        :return: The file_size of this FilesCreateReq.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this FilesCreateReq.

        文件总的大小，最小1，最大5368709120。

        :param file_size: The file_size of this FilesCreateReq.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_type(self):
        """Gets the file_type of this FilesCreateReq.

        文件类型（默认提取文件后缀）。

        :return: The file_type of this FilesCreateReq.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this FilesCreateReq.

        文件类型（默认提取文件后缀）。

        :param file_type: The file_type of this FilesCreateReq.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def asset_id(self):
        """Gets the asset_id of this FilesCreateReq.

        资产ID。

        :return: The asset_id of this FilesCreateReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this FilesCreateReq.

        资产ID。

        :param asset_id: The asset_id of this FilesCreateReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_file_category(self):
        """Gets the asset_file_category of this FilesCreateReq.

        文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：内容页图片 * SAMPLE：样例音频 * OTHER：其他文件 * WHOLE_MODEL：全模型 * USER_MODIFIED_MODEL：用户上传模型 > * 资产类型为SCENE、ANIMATION、VIDEO、IMAGE、MATERIAL时，包含MAIN、COVER和OTHER > * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER > * 资产类型为HUMAN_MODEL时，包含MAIN、COVER、WHOLE_MODEL、USER_MODIFIED_MODEL和OTHER > * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER > * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER(遮罩文件) > * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图)

        :return: The asset_file_category of this FilesCreateReq.
        :rtype: str
        """
        return self._asset_file_category

    @asset_file_category.setter
    def asset_file_category(self, asset_file_category):
        """Sets the asset_file_category of this FilesCreateReq.

        文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：内容页图片 * SAMPLE：样例音频 * OTHER：其他文件 * WHOLE_MODEL：全模型 * USER_MODIFIED_MODEL：用户上传模型 > * 资产类型为SCENE、ANIMATION、VIDEO、IMAGE、MATERIAL时，包含MAIN、COVER和OTHER > * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER > * 资产类型为HUMAN_MODEL时，包含MAIN、COVER、WHOLE_MODEL、USER_MODIFIED_MODEL和OTHER > * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER > * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER(遮罩文件) > * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图)

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
