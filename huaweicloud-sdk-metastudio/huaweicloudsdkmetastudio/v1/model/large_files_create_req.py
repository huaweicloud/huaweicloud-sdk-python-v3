# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LargeFilesCreateReq:

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
        'file_size': 'int',
        'file_type': 'str',
        'asset_id': 'str',
        'asset_file_category': 'str',
        'file_multipart_count': 'int'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_size': 'file_size',
        'file_type': 'file_type',
        'asset_id': 'asset_id',
        'asset_file_category': 'asset_file_category',
        'file_multipart_count': 'file_multipart_count'
    }

    def __init__(self, file_name=None, file_size=None, file_type=None, asset_id=None, asset_file_category=None, file_multipart_count=None):
        r"""LargeFilesCreateReq

        The model defined in huaweicloud sdk

        :param file_name: 文件名，不区分大小写，最大长度256，最小长度1。
        :type file_name: str
        :param file_size: 文件总的大小，最小1，最大536870912000。
        :type file_size: int
        :param file_type: 文件类型（默认提取文件后缀）。
        :type file_type: str
        :param asset_id: 资产ID。
        :type asset_id: str
        :param asset_file_category: 文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * OTHER：其他文件 * PACKAGE：打包后的资产文件
        :type asset_file_category: str
        :param file_multipart_count: ORI4K文件分段上传数量，默认值为1
        :type file_multipart_count: int
        """
        
        

        self._file_name = None
        self._file_size = None
        self._file_type = None
        self._asset_id = None
        self._asset_file_category = None
        self._file_multipart_count = None
        self.discriminator = None

        self.file_name = file_name
        if file_size is not None:
            self.file_size = file_size
        self.file_type = file_type
        self.asset_id = asset_id
        self.asset_file_category = asset_file_category
        if file_multipart_count is not None:
            self.file_multipart_count = file_multipart_count

    @property
    def file_name(self):
        r"""Gets the file_name of this LargeFilesCreateReq.

        文件名，不区分大小写，最大长度256，最小长度1。

        :return: The file_name of this LargeFilesCreateReq.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this LargeFilesCreateReq.

        文件名，不区分大小写，最大长度256，最小长度1。

        :param file_name: The file_name of this LargeFilesCreateReq.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_size(self):
        r"""Gets the file_size of this LargeFilesCreateReq.

        文件总的大小，最小1，最大536870912000。

        :return: The file_size of this LargeFilesCreateReq.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this LargeFilesCreateReq.

        文件总的大小，最小1，最大536870912000。

        :param file_size: The file_size of this LargeFilesCreateReq.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_type(self):
        r"""Gets the file_type of this LargeFilesCreateReq.

        文件类型（默认提取文件后缀）。

        :return: The file_type of this LargeFilesCreateReq.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this LargeFilesCreateReq.

        文件类型（默认提取文件后缀）。

        :param file_type: The file_type of this LargeFilesCreateReq.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def asset_id(self):
        r"""Gets the asset_id of this LargeFilesCreateReq.

        资产ID。

        :return: The asset_id of this LargeFilesCreateReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this LargeFilesCreateReq.

        资产ID。

        :param asset_id: The asset_id of this LargeFilesCreateReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_file_category(self):
        r"""Gets the asset_file_category of this LargeFilesCreateReq.

        文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * OTHER：其他文件 * PACKAGE：打包后的资产文件

        :return: The asset_file_category of this LargeFilesCreateReq.
        :rtype: str
        """
        return self._asset_file_category

    @asset_file_category.setter
    def asset_file_category(self, asset_file_category):
        r"""Sets the asset_file_category of this LargeFilesCreateReq.

        文件在资产中的分类。每种资产类型包含的文件分类不同。 * MAIN：主文件 * OTHER：其他文件 * PACKAGE：打包后的资产文件

        :param asset_file_category: The asset_file_category of this LargeFilesCreateReq.
        :type asset_file_category: str
        """
        self._asset_file_category = asset_file_category

    @property
    def file_multipart_count(self):
        r"""Gets the file_multipart_count of this LargeFilesCreateReq.

        ORI4K文件分段上传数量，默认值为1

        :return: The file_multipart_count of this LargeFilesCreateReq.
        :rtype: int
        """
        return self._file_multipart_count

    @file_multipart_count.setter
    def file_multipart_count(self, file_multipart_count):
        r"""Sets the file_multipart_count of this LargeFilesCreateReq.

        ORI4K文件分段上传数量，默认值为1

        :param file_multipart_count: The file_multipart_count of this LargeFilesCreateReq.
        :type file_multipart_count: int
        """
        self._file_multipart_count = file_multipart_count

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
        if not isinstance(other, LargeFilesCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
