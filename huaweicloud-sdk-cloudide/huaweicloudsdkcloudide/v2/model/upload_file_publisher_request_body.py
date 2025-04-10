# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadFilePublisherRequestBody:

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
        'publisher_id': 'str',
        'chunk_index': 'int',
        'merge': 'bool',
        'total_chunk_num': 'int',
        'parent_file_size': 'int',
        'parent_file_name': 'str',
        'override': 'bool',
        'chunk_md5': 'str',
        'parent_file_sha256': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'file': 'file',
        'publisher_id': 'publisher_id',
        'chunk_index': 'chunk_index',
        'merge': 'merge',
        'total_chunk_num': 'total_chunk_num',
        'parent_file_size': 'parent_file_size',
        'parent_file_name': 'parent_file_name',
        'override': 'override',
        'chunk_md5': 'chunk_md5',
        'parent_file_sha256': 'parent_file_sha256',
        'task_id': 'task_id'
    }

    def __init__(self, file=None, publisher_id=None, chunk_index=None, merge=None, total_chunk_num=None, parent_file_size=None, parent_file_name=None, override=None, chunk_md5=None, parent_file_sha256=None, task_id=None):
        r"""UploadFilePublisherRequestBody

        The model defined in huaweicloud sdk

        :param file: 文件
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param publisher_id: 传用户token时，此字段为必传项
        :type publisher_id: str
        :param chunk_index: 分片索引，第几个分片 取值范围：1-100
        :type chunk_index: int
        :param merge: 是否合并已上传的分片（包含本次分片内容）,true
        :type merge: bool
        :param total_chunk_num: 总分片数 0-100
        :type total_chunk_num: int
        :param parent_file_size: 父文件大小
        :type parent_file_size: int
        :param parent_file_name: 父文件名称
        :type parent_file_name: str
        :param override: 是否覆盖原有文件
        :type override: bool
        :param chunk_md5: 文件分片的md5,用于校验文件分片是否完整
        :type chunk_md5: str
        :param parent_file_sha256: 父文件hash，用于校验合并后的文件
        :type parent_file_sha256: str
        :param task_id: 上传任务的唯一标识，第一次上传分片时可不传
        :type task_id: str
        """
        
        

        self._file = None
        self._publisher_id = None
        self._chunk_index = None
        self._merge = None
        self._total_chunk_num = None
        self._parent_file_size = None
        self._parent_file_name = None
        self._override = None
        self._chunk_md5 = None
        self._parent_file_sha256 = None
        self._task_id = None
        self.discriminator = None

        self.file = file
        if publisher_id is not None:
            self.publisher_id = publisher_id
        self.chunk_index = chunk_index
        self.merge = merge
        self.total_chunk_num = total_chunk_num
        self.parent_file_size = parent_file_size
        self.parent_file_name = parent_file_name
        self.override = override
        self.chunk_md5 = chunk_md5
        if parent_file_sha256 is not None:
            self.parent_file_sha256 = parent_file_sha256
        if task_id is not None:
            self.task_id = task_id

    @property
    def file(self):
        r"""Gets the file of this UploadFilePublisherRequestBody.

        文件

        :return: The file of this UploadFilePublisherRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this UploadFilePublisherRequestBody.

        文件

        :param file: The file of this UploadFilePublisherRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def publisher_id(self):
        r"""Gets the publisher_id of this UploadFilePublisherRequestBody.

        传用户token时，此字段为必传项

        :return: The publisher_id of this UploadFilePublisherRequestBody.
        :rtype: str
        """
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, publisher_id):
        r"""Sets the publisher_id of this UploadFilePublisherRequestBody.

        传用户token时，此字段为必传项

        :param publisher_id: The publisher_id of this UploadFilePublisherRequestBody.
        :type publisher_id: str
        """
        self._publisher_id = publisher_id

    @property
    def chunk_index(self):
        r"""Gets the chunk_index of this UploadFilePublisherRequestBody.

        分片索引，第几个分片 取值范围：1-100

        :return: The chunk_index of this UploadFilePublisherRequestBody.
        :rtype: int
        """
        return self._chunk_index

    @chunk_index.setter
    def chunk_index(self, chunk_index):
        r"""Sets the chunk_index of this UploadFilePublisherRequestBody.

        分片索引，第几个分片 取值范围：1-100

        :param chunk_index: The chunk_index of this UploadFilePublisherRequestBody.
        :type chunk_index: int
        """
        self._chunk_index = chunk_index

    @property
    def merge(self):
        r"""Gets the merge of this UploadFilePublisherRequestBody.

        是否合并已上传的分片（包含本次分片内容）,true

        :return: The merge of this UploadFilePublisherRequestBody.
        :rtype: bool
        """
        return self._merge

    @merge.setter
    def merge(self, merge):
        r"""Sets the merge of this UploadFilePublisherRequestBody.

        是否合并已上传的分片（包含本次分片内容）,true

        :param merge: The merge of this UploadFilePublisherRequestBody.
        :type merge: bool
        """
        self._merge = merge

    @property
    def total_chunk_num(self):
        r"""Gets the total_chunk_num of this UploadFilePublisherRequestBody.

        总分片数 0-100

        :return: The total_chunk_num of this UploadFilePublisherRequestBody.
        :rtype: int
        """
        return self._total_chunk_num

    @total_chunk_num.setter
    def total_chunk_num(self, total_chunk_num):
        r"""Sets the total_chunk_num of this UploadFilePublisherRequestBody.

        总分片数 0-100

        :param total_chunk_num: The total_chunk_num of this UploadFilePublisherRequestBody.
        :type total_chunk_num: int
        """
        self._total_chunk_num = total_chunk_num

    @property
    def parent_file_size(self):
        r"""Gets the parent_file_size of this UploadFilePublisherRequestBody.

        父文件大小

        :return: The parent_file_size of this UploadFilePublisherRequestBody.
        :rtype: int
        """
        return self._parent_file_size

    @parent_file_size.setter
    def parent_file_size(self, parent_file_size):
        r"""Sets the parent_file_size of this UploadFilePublisherRequestBody.

        父文件大小

        :param parent_file_size: The parent_file_size of this UploadFilePublisherRequestBody.
        :type parent_file_size: int
        """
        self._parent_file_size = parent_file_size

    @property
    def parent_file_name(self):
        r"""Gets the parent_file_name of this UploadFilePublisherRequestBody.

        父文件名称

        :return: The parent_file_name of this UploadFilePublisherRequestBody.
        :rtype: str
        """
        return self._parent_file_name

    @parent_file_name.setter
    def parent_file_name(self, parent_file_name):
        r"""Sets the parent_file_name of this UploadFilePublisherRequestBody.

        父文件名称

        :param parent_file_name: The parent_file_name of this UploadFilePublisherRequestBody.
        :type parent_file_name: str
        """
        self._parent_file_name = parent_file_name

    @property
    def override(self):
        r"""Gets the override of this UploadFilePublisherRequestBody.

        是否覆盖原有文件

        :return: The override of this UploadFilePublisherRequestBody.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        r"""Sets the override of this UploadFilePublisherRequestBody.

        是否覆盖原有文件

        :param override: The override of this UploadFilePublisherRequestBody.
        :type override: bool
        """
        self._override = override

    @property
    def chunk_md5(self):
        r"""Gets the chunk_md5 of this UploadFilePublisherRequestBody.

        文件分片的md5,用于校验文件分片是否完整

        :return: The chunk_md5 of this UploadFilePublisherRequestBody.
        :rtype: str
        """
        return self._chunk_md5

    @chunk_md5.setter
    def chunk_md5(self, chunk_md5):
        r"""Sets the chunk_md5 of this UploadFilePublisherRequestBody.

        文件分片的md5,用于校验文件分片是否完整

        :param chunk_md5: The chunk_md5 of this UploadFilePublisherRequestBody.
        :type chunk_md5: str
        """
        self._chunk_md5 = chunk_md5

    @property
    def parent_file_sha256(self):
        r"""Gets the parent_file_sha256 of this UploadFilePublisherRequestBody.

        父文件hash，用于校验合并后的文件

        :return: The parent_file_sha256 of this UploadFilePublisherRequestBody.
        :rtype: str
        """
        return self._parent_file_sha256

    @parent_file_sha256.setter
    def parent_file_sha256(self, parent_file_sha256):
        r"""Sets the parent_file_sha256 of this UploadFilePublisherRequestBody.

        父文件hash，用于校验合并后的文件

        :param parent_file_sha256: The parent_file_sha256 of this UploadFilePublisherRequestBody.
        :type parent_file_sha256: str
        """
        self._parent_file_sha256 = parent_file_sha256

    @property
    def task_id(self):
        r"""Gets the task_id of this UploadFilePublisherRequestBody.

        上传任务的唯一标识，第一次上传分片时可不传

        :return: The task_id of this UploadFilePublisherRequestBody.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this UploadFilePublisherRequestBody.

        上传任务的唯一标识，第一次上传分片时可不传

        :param task_id: The task_id of this UploadFilePublisherRequestBody.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, UploadFilePublisherRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
