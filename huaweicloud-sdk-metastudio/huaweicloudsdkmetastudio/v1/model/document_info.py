# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'document_id': 'str',
        'knowledge_library_id': 'str',
        'file_name': 'str',
        'file_size': 'int',
        'file_type': 'str',
        'split_type': 'int',
        'chunk_size': 'int',
        'chunk_type': 'str',
        'separators': 'list[str]',
        'create_time': 'str',
        'update_time': 'str',
        'document_task_info': 'DocumentTaskInfo'
    }

    attribute_map = {
        'document_id': 'document_id',
        'knowledge_library_id': 'knowledge_library_id',
        'file_name': 'file_name',
        'file_size': 'file_size',
        'file_type': 'file_type',
        'split_type': 'split_type',
        'chunk_size': 'chunk_size',
        'chunk_type': 'chunk_type',
        'separators': 'separators',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'document_task_info': 'document_task_info'
    }

    def __init__(self, document_id=None, knowledge_library_id=None, file_name=None, file_size=None, file_type=None, split_type=None, chunk_size=None, chunk_type=None, separators=None, create_time=None, update_time=None, document_task_info=None):
        r"""DocumentInfo

        The model defined in huaweicloud sdk

        :param document_id: 文档ID。
        :type document_id: str
        :param knowledge_library_id: 知识库ID。
        :type knowledge_library_id: str
        :param file_name: 文档名称。
        :type file_name: str
        :param file_size: 文档大小，单位字节
        :type file_size: int
        :param file_type: 文档类型。
        :type file_type: str
        :param split_type: 分段类型 * 1: 自动分段 * 2: 手动分段
        :type split_type: int
        :param chunk_size: 分段长度。
        :type chunk_size: int
        :param chunk_type: 分段策略，多个策略之间用逗号分割。 &gt; title:标题分割；separator:分隔符分割
        :type chunk_type: str
        :param separators: 分隔符
        :type separators: list[str]
        :param create_time: 文档创建时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 文档更新时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param document_task_info: 
        :type document_task_info: :class:`huaweicloudsdkmetastudio.v1.DocumentTaskInfo`
        """
        
        

        self._document_id = None
        self._knowledge_library_id = None
        self._file_name = None
        self._file_size = None
        self._file_type = None
        self._split_type = None
        self._chunk_size = None
        self._chunk_type = None
        self._separators = None
        self._create_time = None
        self._update_time = None
        self._document_task_info = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if knowledge_library_id is not None:
            self.knowledge_library_id = knowledge_library_id
        if file_name is not None:
            self.file_name = file_name
        if file_size is not None:
            self.file_size = file_size
        if file_type is not None:
            self.file_type = file_type
        if split_type is not None:
            self.split_type = split_type
        if chunk_size is not None:
            self.chunk_size = chunk_size
        if chunk_type is not None:
            self.chunk_type = chunk_type
        if separators is not None:
            self.separators = separators
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if document_task_info is not None:
            self.document_task_info = document_task_info

    @property
    def document_id(self):
        r"""Gets the document_id of this DocumentInfo.

        文档ID。

        :return: The document_id of this DocumentInfo.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this DocumentInfo.

        文档ID。

        :param document_id: The document_id of this DocumentInfo.
        :type document_id: str
        """
        self._document_id = document_id

    @property
    def knowledge_library_id(self):
        r"""Gets the knowledge_library_id of this DocumentInfo.

        知识库ID。

        :return: The knowledge_library_id of this DocumentInfo.
        :rtype: str
        """
        return self._knowledge_library_id

    @knowledge_library_id.setter
    def knowledge_library_id(self, knowledge_library_id):
        r"""Sets the knowledge_library_id of this DocumentInfo.

        知识库ID。

        :param knowledge_library_id: The knowledge_library_id of this DocumentInfo.
        :type knowledge_library_id: str
        """
        self._knowledge_library_id = knowledge_library_id

    @property
    def file_name(self):
        r"""Gets the file_name of this DocumentInfo.

        文档名称。

        :return: The file_name of this DocumentInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this DocumentInfo.

        文档名称。

        :param file_name: The file_name of this DocumentInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_size(self):
        r"""Gets the file_size of this DocumentInfo.

        文档大小，单位字节

        :return: The file_size of this DocumentInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this DocumentInfo.

        文档大小，单位字节

        :param file_size: The file_size of this DocumentInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_type(self):
        r"""Gets the file_type of this DocumentInfo.

        文档类型。

        :return: The file_type of this DocumentInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this DocumentInfo.

        文档类型。

        :param file_type: The file_type of this DocumentInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def split_type(self):
        r"""Gets the split_type of this DocumentInfo.

        分段类型 * 1: 自动分段 * 2: 手动分段

        :return: The split_type of this DocumentInfo.
        :rtype: int
        """
        return self._split_type

    @split_type.setter
    def split_type(self, split_type):
        r"""Sets the split_type of this DocumentInfo.

        分段类型 * 1: 自动分段 * 2: 手动分段

        :param split_type: The split_type of this DocumentInfo.
        :type split_type: int
        """
        self._split_type = split_type

    @property
    def chunk_size(self):
        r"""Gets the chunk_size of this DocumentInfo.

        分段长度。

        :return: The chunk_size of this DocumentInfo.
        :rtype: int
        """
        return self._chunk_size

    @chunk_size.setter
    def chunk_size(self, chunk_size):
        r"""Sets the chunk_size of this DocumentInfo.

        分段长度。

        :param chunk_size: The chunk_size of this DocumentInfo.
        :type chunk_size: int
        """
        self._chunk_size = chunk_size

    @property
    def chunk_type(self):
        r"""Gets the chunk_type of this DocumentInfo.

        分段策略，多个策略之间用逗号分割。 > title:标题分割；separator:分隔符分割

        :return: The chunk_type of this DocumentInfo.
        :rtype: str
        """
        return self._chunk_type

    @chunk_type.setter
    def chunk_type(self, chunk_type):
        r"""Sets the chunk_type of this DocumentInfo.

        分段策略，多个策略之间用逗号分割。 > title:标题分割；separator:分隔符分割

        :param chunk_type: The chunk_type of this DocumentInfo.
        :type chunk_type: str
        """
        self._chunk_type = chunk_type

    @property
    def separators(self):
        r"""Gets the separators of this DocumentInfo.

        分隔符

        :return: The separators of this DocumentInfo.
        :rtype: list[str]
        """
        return self._separators

    @separators.setter
    def separators(self, separators):
        r"""Sets the separators of this DocumentInfo.

        分隔符

        :param separators: The separators of this DocumentInfo.
        :type separators: list[str]
        """
        self._separators = separators

    @property
    def create_time(self):
        r"""Gets the create_time of this DocumentInfo.

        文档创建时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this DocumentInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DocumentInfo.

        文档创建时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this DocumentInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this DocumentInfo.

        文档更新时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this DocumentInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DocumentInfo.

        文档更新时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this DocumentInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def document_task_info(self):
        r"""Gets the document_task_info of this DocumentInfo.

        :return: The document_task_info of this DocumentInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DocumentTaskInfo`
        """
        return self._document_task_info

    @document_task_info.setter
    def document_task_info(self, document_task_info):
        r"""Sets the document_task_info of this DocumentInfo.

        :param document_task_info: The document_task_info of this DocumentInfo.
        :type document_task_info: :class:`huaweicloudsdkmetastudio.v1.DocumentTaskInfo`
        """
        self._document_task_info = document_task_info

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
        if not isinstance(other, DocumentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
