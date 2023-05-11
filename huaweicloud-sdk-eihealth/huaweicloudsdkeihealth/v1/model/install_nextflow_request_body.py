# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstallNextflowRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'file',
        'part_number': 'int',
        'total_part': 'int',
        'multipart_id': 'str',
        'file_name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'file': 'file',
        'part_number': 'part_number',
        'total_part': 'total_part',
        'multipart_id': 'multipart_id',
        'file_name': 'file_name',
        'version': 'version'
    }

    def __init__(self, file=None, part_number=None, total_part=None, multipart_id=None, file_name=None, version=None):
        """InstallNextflowRequestBody

        The model defined in huaweicloud sdk

        :param file: 文件流对象
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param part_number: 分段序号，表示第几个文件片段
        :type part_number: int
        :param total_part: 分段总数，上传的文件总共分成了几个片段
        :type total_part: int
        :param multipart_id: 分段上传任务id，除了第一个片段外，后续的片段都需要标识出任务id
        :type multipart_id: str
        :param file_name: 文件名称
        :type file_name: str
        :param version: 版本号
        :type version: str
        """
        
        

        self._file = None
        self._part_number = None
        self._total_part = None
        self._multipart_id = None
        self._file_name = None
        self._version = None
        self.discriminator = None

        if file is not None:
            self.file = file
        if part_number is not None:
            self.part_number = part_number
        if total_part is not None:
            self.total_part = total_part
        if multipart_id is not None:
            self.multipart_id = multipart_id
        if file_name is not None:
            self.file_name = file_name
        if version is not None:
            self.version = version

    @property
    def file(self):
        """Gets the file of this InstallNextflowRequestBody.

        文件流对象

        :return: The file of this InstallNextflowRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this InstallNextflowRequestBody.

        文件流对象

        :param file: The file of this InstallNextflowRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def part_number(self):
        """Gets the part_number of this InstallNextflowRequestBody.

        分段序号，表示第几个文件片段

        :return: The part_number of this InstallNextflowRequestBody.
        :rtype: int
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this InstallNextflowRequestBody.

        分段序号，表示第几个文件片段

        :param part_number: The part_number of this InstallNextflowRequestBody.
        :type part_number: int
        """
        self._part_number = part_number

    @property
    def total_part(self):
        """Gets the total_part of this InstallNextflowRequestBody.

        分段总数，上传的文件总共分成了几个片段

        :return: The total_part of this InstallNextflowRequestBody.
        :rtype: int
        """
        return self._total_part

    @total_part.setter
    def total_part(self, total_part):
        """Sets the total_part of this InstallNextflowRequestBody.

        分段总数，上传的文件总共分成了几个片段

        :param total_part: The total_part of this InstallNextflowRequestBody.
        :type total_part: int
        """
        self._total_part = total_part

    @property
    def multipart_id(self):
        """Gets the multipart_id of this InstallNextflowRequestBody.

        分段上传任务id，除了第一个片段外，后续的片段都需要标识出任务id

        :return: The multipart_id of this InstallNextflowRequestBody.
        :rtype: str
        """
        return self._multipart_id

    @multipart_id.setter
    def multipart_id(self, multipart_id):
        """Sets the multipart_id of this InstallNextflowRequestBody.

        分段上传任务id，除了第一个片段外，后续的片段都需要标识出任务id

        :param multipart_id: The multipart_id of this InstallNextflowRequestBody.
        :type multipart_id: str
        """
        self._multipart_id = multipart_id

    @property
    def file_name(self):
        """Gets the file_name of this InstallNextflowRequestBody.

        文件名称

        :return: The file_name of this InstallNextflowRequestBody.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this InstallNextflowRequestBody.

        文件名称

        :param file_name: The file_name of this InstallNextflowRequestBody.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def version(self):
        """Gets the version of this InstallNextflowRequestBody.

        版本号

        :return: The version of this InstallNextflowRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstallNextflowRequestBody.

        版本号

        :param version: The version of this InstallNextflowRequestBody.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, InstallNextflowRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
