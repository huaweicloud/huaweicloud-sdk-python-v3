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
        'download_url': 'str',
        'state': 'str',
        'block_reason_code': 'str',
        'reason': 'str',
        'file_extra_meta': 'FileExtraMeta'
    }

    attribute_map = {
        'file_id': 'file_id',
        'file_name': 'file_name',
        'file_md5': 'file_md5',
        'file_size': 'file_size',
        'file_type': 'file_type',
        'asset_file_category': 'asset_file_category',
        'download_url': 'download_url',
        'state': 'state',
        'block_reason_code': 'block_reason_code',
        'reason': 'reason',
        'file_extra_meta': 'file_extra_meta'
    }

    def __init__(self, file_id=None, file_name=None, file_md5=None, file_size=None, file_type=None, asset_file_category=None, download_url=None, state=None, block_reason_code=None, reason=None, file_extra_meta=None):
        r"""AssetFileInfo

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
        :param asset_file_category: 文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：内容页图片 * SAMPLE：样例音频 * OTHER：其他文件 * TEMPORARY：临时文件夹（用于文件替换时上传新文件） * PACKAGE：打包后的资产文件 &gt; * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER &gt; * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER &gt; * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER(遮罩文件) &gt; * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图)
        :type asset_file_category: str
        :param download_url: 文件下载URL，有效期为24小时。
        :type download_url: str
        :param state: 文件状态枚举: * CREATING：文件上传中 * CREATED：文件已上传（自动审核通过） * FAILED：文件上传失败 * CANCELLED：文件上传已取消 * DELETING：文件删除中 * DELETED：文件已删除 * UPLOADED：文件已上传（尚未审核） * REVIEW：人工审核（文件已上传） * BLOCK：冻结
        :type state: str
        :param block_reason_code: 冻结原因编号。
        :type block_reason_code: str
        :param reason: 审核失败原因
        :type reason: str
        :param file_extra_meta: 
        :type file_extra_meta: :class:`huaweicloudsdkmetastudio.v1.FileExtraMeta`
        """
        
        

        self._file_id = None
        self._file_name = None
        self._file_md5 = None
        self._file_size = None
        self._file_type = None
        self._asset_file_category = None
        self._download_url = None
        self._state = None
        self._block_reason_code = None
        self._reason = None
        self._file_extra_meta = None
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
        if state is not None:
            self.state = state
        if block_reason_code is not None:
            self.block_reason_code = block_reason_code
        if reason is not None:
            self.reason = reason
        if file_extra_meta is not None:
            self.file_extra_meta = file_extra_meta

    @property
    def file_id(self):
        r"""Gets the file_id of this AssetFileInfo.

        文件ID。

        :return: The file_id of this AssetFileInfo.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this AssetFileInfo.

        文件ID。

        :param file_id: The file_id of this AssetFileInfo.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def file_name(self):
        r"""Gets the file_name of this AssetFileInfo.

        文件名创建文件时候不区分大小写，最大长度256，最小长度1。

        :return: The file_name of this AssetFileInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this AssetFileInfo.

        文件名创建文件时候不区分大小写，最大长度256，最小长度1。

        :param file_name: The file_name of this AssetFileInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_md5(self):
        r"""Gets the file_md5 of this AssetFileInfo.

        文件内容MD5值，固定24位。

        :return: The file_md5 of this AssetFileInfo.
        :rtype: str
        """
        return self._file_md5

    @file_md5.setter
    def file_md5(self, file_md5):
        r"""Sets the file_md5 of this AssetFileInfo.

        文件内容MD5值，固定24位。

        :param file_md5: The file_md5 of this AssetFileInfo.
        :type file_md5: str
        """
        self._file_md5 = file_md5

    @property
    def file_size(self):
        r"""Gets the file_size of this AssetFileInfo.

        文件总的大小，最小1，最大5368709120。

        :return: The file_size of this AssetFileInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this AssetFileInfo.

        文件总的大小，最小1，最大5368709120。

        :param file_size: The file_size of this AssetFileInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_type(self):
        r"""Gets the file_type of this AssetFileInfo.

        文件类型（默认提取文件后缀）。

        :return: The file_type of this AssetFileInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this AssetFileInfo.

        文件类型（默认提取文件后缀）。

        :param file_type: The file_type of this AssetFileInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def asset_file_category(self):
        r"""Gets the asset_file_category of this AssetFileInfo.

        文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：内容页图片 * SAMPLE：样例音频 * OTHER：其他文件 * TEMPORARY：临时文件夹（用于文件替换时上传新文件） * PACKAGE：打包后的资产文件 > * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER > * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER > * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER(遮罩文件) > * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图)

        :return: The asset_file_category of this AssetFileInfo.
        :rtype: str
        """
        return self._asset_file_category

    @asset_file_category.setter
    def asset_file_category(self, asset_file_category):
        r"""Sets the asset_file_category of this AssetFileInfo.

        文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * COVER：封面文件 * PAGE：内容页图片 * SAMPLE：样例音频 * OTHER：其他文件 * TEMPORARY：临时文件夹（用于文件替换时上传新文件） * PACKAGE：打包后的资产文件 > * 资产类型为PPT时，包含MAIN、COVER、PAGE和OTHER > * 资产类型为VOICE_MODEL时，包含MAIN、SAMPLE(样例音频文件)和OTHER > * 资产类型为HUMAN_MODEL_2D时，包含MAIN、COVER、SAMPLE(动作样例)和OTHER(遮罩文件) > * 资产类型为BUSINESS_CARD_TEMPLET时，包含MAIN和COVER(名片效果图)

        :param asset_file_category: The asset_file_category of this AssetFileInfo.
        :type asset_file_category: str
        """
        self._asset_file_category = asset_file_category

    @property
    def download_url(self):
        r"""Gets the download_url of this AssetFileInfo.

        文件下载URL，有效期为24小时。

        :return: The download_url of this AssetFileInfo.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this AssetFileInfo.

        文件下载URL，有效期为24小时。

        :param download_url: The download_url of this AssetFileInfo.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def state(self):
        r"""Gets the state of this AssetFileInfo.

        文件状态枚举: * CREATING：文件上传中 * CREATED：文件已上传（自动审核通过） * FAILED：文件上传失败 * CANCELLED：文件上传已取消 * DELETING：文件删除中 * DELETED：文件已删除 * UPLOADED：文件已上传（尚未审核） * REVIEW：人工审核（文件已上传） * BLOCK：冻结

        :return: The state of this AssetFileInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this AssetFileInfo.

        文件状态枚举: * CREATING：文件上传中 * CREATED：文件已上传（自动审核通过） * FAILED：文件上传失败 * CANCELLED：文件上传已取消 * DELETING：文件删除中 * DELETED：文件已删除 * UPLOADED：文件已上传（尚未审核） * REVIEW：人工审核（文件已上传） * BLOCK：冻结

        :param state: The state of this AssetFileInfo.
        :type state: str
        """
        self._state = state

    @property
    def block_reason_code(self):
        r"""Gets the block_reason_code of this AssetFileInfo.

        冻结原因编号。

        :return: The block_reason_code of this AssetFileInfo.
        :rtype: str
        """
        return self._block_reason_code

    @block_reason_code.setter
    def block_reason_code(self, block_reason_code):
        r"""Sets the block_reason_code of this AssetFileInfo.

        冻结原因编号。

        :param block_reason_code: The block_reason_code of this AssetFileInfo.
        :type block_reason_code: str
        """
        self._block_reason_code = block_reason_code

    @property
    def reason(self):
        r"""Gets the reason of this AssetFileInfo.

        审核失败原因

        :return: The reason of this AssetFileInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this AssetFileInfo.

        审核失败原因

        :param reason: The reason of this AssetFileInfo.
        :type reason: str
        """
        self._reason = reason

    @property
    def file_extra_meta(self):
        r"""Gets the file_extra_meta of this AssetFileInfo.

        :return: The file_extra_meta of this AssetFileInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.FileExtraMeta`
        """
        return self._file_extra_meta

    @file_extra_meta.setter
    def file_extra_meta(self, file_extra_meta):
        r"""Sets the file_extra_meta of this AssetFileInfo.

        :param file_extra_meta: The file_extra_meta of this AssetFileInfo.
        :type file_extra_meta: :class:`huaweicloudsdkmetastudio.v1.FileExtraMeta`
        """
        self._file_extra_meta = file_extra_meta

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
