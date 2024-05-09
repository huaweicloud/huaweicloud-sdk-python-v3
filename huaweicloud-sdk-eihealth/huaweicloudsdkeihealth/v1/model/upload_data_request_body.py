# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadDataRequestBody:

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
        'target_folder': 'str',
        'part_number': 'str',
        'total_part': 'str',
        'multipart_id': 'str',
        'file_name': 'str',
        'md5': 'str'
    }

    attribute_map = {
        'file': 'file',
        'target_folder': 'target_folder',
        'part_number': 'part_number',
        'total_part': 'total_part',
        'multipart_id': 'multipart_id',
        'file_name': 'file_name',
        'md5': 'md5'
    }

    def __init__(self, file=None, target_folder=None, part_number=None, total_part=None, multipart_id=None, file_name=None, md5=None):
        """UploadDataRequestBody

        The model defined in huaweicloud sdk

        :param file: 文件流对象
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param target_folder: 目标文件夹
        :type target_folder: str
        :param part_number: 分段序号，表示第几个文件片段
        :type part_number: str
        :param total_part: 分段总数，上传的文件总共分成了几个片段
        :type total_part: str
        :param multipart_id: 分段上传任务id，除了第一个片段外，后续的片段都需要标识出任务id
        :type multipart_id: str
        :param file_name: 文件名称
        :type file_name: str
        :param md5: MD5
        :type md5: str
        """
        
        

        self._file = None
        self._target_folder = None
        self._part_number = None
        self._total_part = None
        self._multipart_id = None
        self._file_name = None
        self._md5 = None
        self.discriminator = None

        self.file = file
        if target_folder is not None:
            self.target_folder = target_folder
        if part_number is not None:
            self.part_number = part_number
        if total_part is not None:
            self.total_part = total_part
        if multipart_id is not None:
            self.multipart_id = multipart_id
        if file_name is not None:
            self.file_name = file_name
        if md5 is not None:
            self.md5 = md5

    @property
    def file(self):
        """Gets the file of this UploadDataRequestBody.

        文件流对象

        :return: The file of this UploadDataRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this UploadDataRequestBody.

        文件流对象

        :param file: The file of this UploadDataRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def target_folder(self):
        """Gets the target_folder of this UploadDataRequestBody.

        目标文件夹

        :return: The target_folder of this UploadDataRequestBody.
        :rtype: str
        """
        return self._target_folder

    @target_folder.setter
    def target_folder(self, target_folder):
        """Sets the target_folder of this UploadDataRequestBody.

        目标文件夹

        :param target_folder: The target_folder of this UploadDataRequestBody.
        :type target_folder: str
        """
        self._target_folder = target_folder

    @property
    def part_number(self):
        """Gets the part_number of this UploadDataRequestBody.

        分段序号，表示第几个文件片段

        :return: The part_number of this UploadDataRequestBody.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this UploadDataRequestBody.

        分段序号，表示第几个文件片段

        :param part_number: The part_number of this UploadDataRequestBody.
        :type part_number: str
        """
        self._part_number = part_number

    @property
    def total_part(self):
        """Gets the total_part of this UploadDataRequestBody.

        分段总数，上传的文件总共分成了几个片段

        :return: The total_part of this UploadDataRequestBody.
        :rtype: str
        """
        return self._total_part

    @total_part.setter
    def total_part(self, total_part):
        """Sets the total_part of this UploadDataRequestBody.

        分段总数，上传的文件总共分成了几个片段

        :param total_part: The total_part of this UploadDataRequestBody.
        :type total_part: str
        """
        self._total_part = total_part

    @property
    def multipart_id(self):
        """Gets the multipart_id of this UploadDataRequestBody.

        分段上传任务id，除了第一个片段外，后续的片段都需要标识出任务id

        :return: The multipart_id of this UploadDataRequestBody.
        :rtype: str
        """
        return self._multipart_id

    @multipart_id.setter
    def multipart_id(self, multipart_id):
        """Sets the multipart_id of this UploadDataRequestBody.

        分段上传任务id，除了第一个片段外，后续的片段都需要标识出任务id

        :param multipart_id: The multipart_id of this UploadDataRequestBody.
        :type multipart_id: str
        """
        self._multipart_id = multipart_id

    @property
    def file_name(self):
        """Gets the file_name of this UploadDataRequestBody.

        文件名称

        :return: The file_name of this UploadDataRequestBody.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this UploadDataRequestBody.

        文件名称

        :param file_name: The file_name of this UploadDataRequestBody.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def md5(self):
        """Gets the md5 of this UploadDataRequestBody.

        MD5

        :return: The md5 of this UploadDataRequestBody.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this UploadDataRequestBody.

        MD5

        :param md5: The md5 of this UploadDataRequestBody.
        :type md5: str
        """
        self._md5 = md5

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
        if not isinstance(other, UploadDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
