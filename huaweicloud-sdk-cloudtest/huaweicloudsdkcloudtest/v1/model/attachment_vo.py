# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'creator': 'str',
        'updator': 'str',
        'region': 'str',
        'doc_id': 'str',
        'parent_uri': 'str',
        'parent_type': 'str',
        'file_name': 'str',
        'store_file_name': 'str',
        'file_path': 'str',
        'file_size': 'int',
        'file_type': 'str',
        'system_type': 'str',
        'create_time': 'datetime',
        'create_time_timestamp': 'int',
        'update_time': 'datetime',
        'update_time_timestamp': 'int',
        'project_uuid': 'str',
        'related_type': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'creator': 'creator',
        'updator': 'updator',
        'region': 'region',
        'doc_id': 'doc_id',
        'parent_uri': 'parent_uri',
        'parent_type': 'parent_type',
        'file_name': 'file_name',
        'store_file_name': 'store_file_name',
        'file_path': 'file_path',
        'file_size': 'file_size',
        'file_type': 'file_type',
        'system_type': 'system_type',
        'create_time': 'create_time',
        'create_time_timestamp': 'create_time_timestamp',
        'update_time': 'update_time',
        'update_time_timestamp': 'update_time_timestamp',
        'project_uuid': 'project_uuid',
        'related_type': 'related_type'
    }

    def __init__(self, uri=None, creator=None, updator=None, region=None, doc_id=None, parent_uri=None, parent_type=None, file_name=None, store_file_name=None, file_path=None, file_size=None, file_type=None, system_type=None, create_time=None, create_time_timestamp=None, update_time=None, update_time_timestamp=None, project_uuid=None, related_type=None):
        """AttachmentVo

        The model defined in huaweicloud sdk

        :param uri: 附件Uri
        :type uri: str
        :param creator: 创建人
        :type creator: str
        :param updator: 更新人
        :type updator: str
        :param region: 逻辑region
        :type region: str
        :param doc_id: 文档id
        :type doc_id: str
        :param parent_uri: 父节点Uri
        :type parent_uri: str
        :param parent_type: 父节点类型
        :type parent_type: str
        :param file_name: 文件名
        :type file_name: str
        :param store_file_name: 保存文件名
        :type store_file_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param file_size: 文件大小
        :type file_size: int
        :param file_type: 文件类型
        :type file_type: str
        :param system_type: 系统区分：docman或testman
        :type system_type: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param create_time_timestamp: 创建时间时间戳
        :type create_time_timestamp: int
        :param update_time: 更新时间
        :type update_time: datetime
        :param update_time_timestamp: 更新时间时间戳
        :type update_time_timestamp: int
        :param project_uuid: 项目id
        :type project_uuid: str
        :param related_type: 附件类型 0 本地上传  other 关联文档
        :type related_type: str
        """
        
        

        self._uri = None
        self._creator = None
        self._updator = None
        self._region = None
        self._doc_id = None
        self._parent_uri = None
        self._parent_type = None
        self._file_name = None
        self._store_file_name = None
        self._file_path = None
        self._file_size = None
        self._file_type = None
        self._system_type = None
        self._create_time = None
        self._create_time_timestamp = None
        self._update_time = None
        self._update_time_timestamp = None
        self._project_uuid = None
        self._related_type = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if creator is not None:
            self.creator = creator
        if updator is not None:
            self.updator = updator
        if region is not None:
            self.region = region
        if doc_id is not None:
            self.doc_id = doc_id
        if parent_uri is not None:
            self.parent_uri = parent_uri
        if parent_type is not None:
            self.parent_type = parent_type
        if file_name is not None:
            self.file_name = file_name
        if store_file_name is not None:
            self.store_file_name = store_file_name
        if file_path is not None:
            self.file_path = file_path
        if file_size is not None:
            self.file_size = file_size
        if file_type is not None:
            self.file_type = file_type
        if system_type is not None:
            self.system_type = system_type
        if create_time is not None:
            self.create_time = create_time
        if create_time_timestamp is not None:
            self.create_time_timestamp = create_time_timestamp
        if update_time is not None:
            self.update_time = update_time
        if update_time_timestamp is not None:
            self.update_time_timestamp = update_time_timestamp
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if related_type is not None:
            self.related_type = related_type

    @property
    def uri(self):
        """Gets the uri of this AttachmentVo.

        附件Uri

        :return: The uri of this AttachmentVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this AttachmentVo.

        附件Uri

        :param uri: The uri of this AttachmentVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def creator(self):
        """Gets the creator of this AttachmentVo.

        创建人

        :return: The creator of this AttachmentVo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this AttachmentVo.

        创建人

        :param creator: The creator of this AttachmentVo.
        :type creator: str
        """
        self._creator = creator

    @property
    def updator(self):
        """Gets the updator of this AttachmentVo.

        更新人

        :return: The updator of this AttachmentVo.
        :rtype: str
        """
        return self._updator

    @updator.setter
    def updator(self, updator):
        """Sets the updator of this AttachmentVo.

        更新人

        :param updator: The updator of this AttachmentVo.
        :type updator: str
        """
        self._updator = updator

    @property
    def region(self):
        """Gets the region of this AttachmentVo.

        逻辑region

        :return: The region of this AttachmentVo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AttachmentVo.

        逻辑region

        :param region: The region of this AttachmentVo.
        :type region: str
        """
        self._region = region

    @property
    def doc_id(self):
        """Gets the doc_id of this AttachmentVo.

        文档id

        :return: The doc_id of this AttachmentVo.
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """Sets the doc_id of this AttachmentVo.

        文档id

        :param doc_id: The doc_id of this AttachmentVo.
        :type doc_id: str
        """
        self._doc_id = doc_id

    @property
    def parent_uri(self):
        """Gets the parent_uri of this AttachmentVo.

        父节点Uri

        :return: The parent_uri of this AttachmentVo.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        """Sets the parent_uri of this AttachmentVo.

        父节点Uri

        :param parent_uri: The parent_uri of this AttachmentVo.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def parent_type(self):
        """Gets the parent_type of this AttachmentVo.

        父节点类型

        :return: The parent_type of this AttachmentVo.
        :rtype: str
        """
        return self._parent_type

    @parent_type.setter
    def parent_type(self, parent_type):
        """Sets the parent_type of this AttachmentVo.

        父节点类型

        :param parent_type: The parent_type of this AttachmentVo.
        :type parent_type: str
        """
        self._parent_type = parent_type

    @property
    def file_name(self):
        """Gets the file_name of this AttachmentVo.

        文件名

        :return: The file_name of this AttachmentVo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this AttachmentVo.

        文件名

        :param file_name: The file_name of this AttachmentVo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def store_file_name(self):
        """Gets the store_file_name of this AttachmentVo.

        保存文件名

        :return: The store_file_name of this AttachmentVo.
        :rtype: str
        """
        return self._store_file_name

    @store_file_name.setter
    def store_file_name(self, store_file_name):
        """Sets the store_file_name of this AttachmentVo.

        保存文件名

        :param store_file_name: The store_file_name of this AttachmentVo.
        :type store_file_name: str
        """
        self._store_file_name = store_file_name

    @property
    def file_path(self):
        """Gets the file_path of this AttachmentVo.

        文件路径

        :return: The file_path of this AttachmentVo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this AttachmentVo.

        文件路径

        :param file_path: The file_path of this AttachmentVo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_size(self):
        """Gets the file_size of this AttachmentVo.

        文件大小

        :return: The file_size of this AttachmentVo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this AttachmentVo.

        文件大小

        :param file_size: The file_size of this AttachmentVo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_type(self):
        """Gets the file_type of this AttachmentVo.

        文件类型

        :return: The file_type of this AttachmentVo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this AttachmentVo.

        文件类型

        :param file_type: The file_type of this AttachmentVo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def system_type(self):
        """Gets the system_type of this AttachmentVo.

        系统区分：docman或testman

        :return: The system_type of this AttachmentVo.
        :rtype: str
        """
        return self._system_type

    @system_type.setter
    def system_type(self, system_type):
        """Sets the system_type of this AttachmentVo.

        系统区分：docman或testman

        :param system_type: The system_type of this AttachmentVo.
        :type system_type: str
        """
        self._system_type = system_type

    @property
    def create_time(self):
        """Gets the create_time of this AttachmentVo.

        创建时间

        :return: The create_time of this AttachmentVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AttachmentVo.

        创建时间

        :param create_time: The create_time of this AttachmentVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_time_timestamp(self):
        """Gets the create_time_timestamp of this AttachmentVo.

        创建时间时间戳

        :return: The create_time_timestamp of this AttachmentVo.
        :rtype: int
        """
        return self._create_time_timestamp

    @create_time_timestamp.setter
    def create_time_timestamp(self, create_time_timestamp):
        """Sets the create_time_timestamp of this AttachmentVo.

        创建时间时间戳

        :param create_time_timestamp: The create_time_timestamp of this AttachmentVo.
        :type create_time_timestamp: int
        """
        self._create_time_timestamp = create_time_timestamp

    @property
    def update_time(self):
        """Gets the update_time of this AttachmentVo.

        更新时间

        :return: The update_time of this AttachmentVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AttachmentVo.

        更新时间

        :param update_time: The update_time of this AttachmentVo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_time_timestamp(self):
        """Gets the update_time_timestamp of this AttachmentVo.

        更新时间时间戳

        :return: The update_time_timestamp of this AttachmentVo.
        :rtype: int
        """
        return self._update_time_timestamp

    @update_time_timestamp.setter
    def update_time_timestamp(self, update_time_timestamp):
        """Sets the update_time_timestamp of this AttachmentVo.

        更新时间时间戳

        :param update_time_timestamp: The update_time_timestamp of this AttachmentVo.
        :type update_time_timestamp: int
        """
        self._update_time_timestamp = update_time_timestamp

    @property
    def project_uuid(self):
        """Gets the project_uuid of this AttachmentVo.

        项目id

        :return: The project_uuid of this AttachmentVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this AttachmentVo.

        项目id

        :param project_uuid: The project_uuid of this AttachmentVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def related_type(self):
        """Gets the related_type of this AttachmentVo.

        附件类型 0 本地上传  other 关联文档

        :return: The related_type of this AttachmentVo.
        :rtype: str
        """
        return self._related_type

    @related_type.setter
    def related_type(self, related_type):
        """Sets the related_type of this AttachmentVo.

        附件类型 0 本地上传  other 关联文档

        :param related_type: The related_type of this AttachmentVo.
        :type related_type: str
        """
        self._related_type = related_type

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
        if not isinstance(other, AttachmentVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
