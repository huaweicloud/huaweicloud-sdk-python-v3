# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetFileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id': 'str',
        'file_name': 'str',
        'file_md5': 'str',
        'file_size': 'int',
        'file_type': 'str',
        'asset_file_category': 'str',
        'download_url': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'file_name': 'file_name',
        'file_md5': 'file_md5',
        'file_size': 'file_size',
        'file_type': 'file_type',
        'asset_file_category': 'asset_file_category',
        'download_url': 'download_url'
    }

    def __init__(self, file_id=None, file_name=None, file_md5=None, file_size=None, file_type=None, asset_file_category=None, download_url=None):
        """AssetFileInfo

        The model defined in huaweicloud sdk

        :param file_id: 文件ID。
        :type file_id: str
        :param file_name: 文件名创建文件时候不区分大小写，最大长度256，最小长度1。
        :type file_name: str
        :param file_md5: 文件内容MD5值，固定24位。
        :type file_md5: str
        :param file_size: 文件总的大小，最小1，最大5368709120。
        :type file_size: int
        :param file_type: 文件类型（默认提取文件后缀）。
        :type file_type: str
        :param asset_file_category: 文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：内容页图片 * SAMPLE：样例音频 * OTHER：其他文件 * WHOLE_MODEL：全模型 * USER_MODIFIED_MODEL：用户上传模型 &gt; * 资产类型为SCENE、ANIMATION、VIDEO、IMAGE、MATERIAL时，包含MAIN、COVER和OTHER &gt; * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER &gt; * 资产类型为HUMAN_MODEL时，包含MAIN、COVER和OTHER &gt; * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER &gt; * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER(遮罩文件) &gt; * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图)
        :type asset_file_category: str
        :param download_url: 文件下载URL，有效期为24小时。
        :type download_url: str
        """
        
        

        self._file_id = None
        self._file_name = None
        self._file_md5 = None
        self._file_size = None
        self._file_type = None
        self._asset_file_category = None
        self._download_url = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name
        if file_md5 is not None:
            self.file_md5 = file_md5
        if file_size is not None:
            self.file_size = file_size
        if file_type is not None:
            self.file_type = file_type
        if asset_file_category is not None:
            self.asset_file_category = asset_file_category
        if download_url is not None:
            self.download_url = download_url

    @property
    def file_id(self):
        """Gets the file_id of this AssetFileInfo.

        文件ID。

        :return: The file_id of this AssetFileInfo.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this AssetFileInfo.

        文件ID。

        :param file_id: The file_id of this AssetFileInfo.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def file_name(self):
        """Gets the file_name of this AssetFileInfo.

        文件名创建文件时候不区分大小写，最大长度256，最小长度1。

        :return: The file_name of this AssetFileInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this AssetFileInfo.

        文件名创建文件时候不区分大小写，最大长度256，最小长度1。

        :param file_name: The file_name of this AssetFileInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_md5(self):
        """Gets the file_md5 of this AssetFileInfo.

        文件内容MD5值，固定24位。

        :return: The file_md5 of this AssetFileInfo.
        :rtype: str
        """
        return self._file_md5

    @file_md5.setter
    def file_md5(self, file_md5):
        """Sets the file_md5 of this AssetFileInfo.

        文件内容MD5值，固定24位。

        :param file_md5: The file_md5 of this AssetFileInfo.
        :type file_md5: str
        """
        self._file_md5 = file_md5

    @property
    def file_size(self):
        """Gets the file_size of this AssetFileInfo.

        文件总的大小，最小1，最大5368709120。

        :return: The file_size of this AssetFileInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this AssetFileInfo.

        文件总的大小，最小1，最大5368709120。

        :param file_size: The file_size of this AssetFileInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_type(self):
        """Gets the file_type of this AssetFileInfo.

        文件类型（默认提取文件后缀）。

        :return: The file_type of this AssetFileInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this AssetFileInfo.

        文件类型（默认提取文件后缀）。

        :param file_type: The file_type of this AssetFileInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def asset_file_category(self):
        """Gets the asset_file_category of this AssetFileInfo.

        文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：内容页图片 * SAMPLE：样例音频 * OTHER：其他文件 * WHOLE_MODEL：全模型 * USER_MODIFIED_MODEL：用户上传模型 > * 资产类型为SCENE、ANIMATION、VIDEO、IMAGE、MATERIAL时，包含MAIN、COVER和OTHER > * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER > * 资产类型为HUMAN_MODEL时，包含MAIN、COVER和OTHER > * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER > * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER(遮罩文件) > * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图)

        :return: The asset_file_category of this AssetFileInfo.
        :rtype: str
        """
        return self._asset_file_category

    @asset_file_category.setter
    def asset_file_category(self, asset_file_category):
        """Sets the asset_file_category of this AssetFileInfo.

        文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：内容页图片 * SAMPLE：样例音频 * OTHER：其他文件 * WHOLE_MODEL：全模型 * USER_MODIFIED_MODEL：用户上传模型 > * 资产类型为SCENE、ANIMATION、VIDEO、IMAGE、MATERIAL时，包含MAIN、COVER和OTHER > * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER > * 资产类型为HUMAN_MODEL时，包含MAIN、COVER和OTHER > * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER > * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER(遮罩文件) > * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图)

        :param asset_file_category: The asset_file_category of this AssetFileInfo.
        :type asset_file_category: str
        """
        self._asset_file_category = asset_file_category

    @property
    def download_url(self):
        """Gets the download_url of this AssetFileInfo.

        文件下载URL，有效期为24小时。

        :return: The download_url of this AssetFileInfo.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this AssetFileInfo.

        文件下载URL，有效期为24小时。

        :param download_url: The download_url of this AssetFileInfo.
        :type download_url: str
        """
        self._download_url = download_url

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
        if not isinstance(other, AssetFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
