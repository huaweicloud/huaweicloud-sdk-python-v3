# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlertDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'data_object': 'ListAlertRsp',
        'dataclass_ref': 'AlertDetailDataclassRef',
        'format_version': 'int',
        'id': 'str',
        'type': 'str',
        'project_id': 'str',
        'update_time': 'str',
        'version': 'int',
        'workspace_id': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'data_object': 'data_object',
        'dataclass_ref': 'dataclass_ref',
        'format_version': 'format_version',
        'id': 'id',
        'type': 'type',
        'project_id': 'project_id',
        'update_time': 'update_time',
        'version': 'version',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, create_time=None, data_object=None, dataclass_ref=None, format_version=None, id=None, type=None, project_id=None, update_time=None, version=None, workspace_id=None):
        r"""ListAlertDetail

        The model defined in huaweicloud sdk

        :param create_time: 记录时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type create_time: str
        :param data_object: 
        :type data_object: :class:`huaweicloudsdksecmaster.v2.ListAlertRsp`
        :param dataclass_ref: 
        :type dataclass_ref: :class:`huaweicloudsdksecmaster.v2.AlertDetailDataclassRef`
        :param format_version: 格式版本
        :type format_version: int
        :param id: 告警唯一标识，UUID格式，最大36个字符
        :type id: str
        :param type: 数据类型
        :type type: str
        :param project_id: 当前项目的id
        :type project_id: str
        :param update_time: 更新时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type update_time: str
        :param version: 版本
        :type version: int
        :param workspace_id: 当前的工作空间id
        :type workspace_id: str
        """
        
        

        self._create_time = None
        self._data_object = None
        self._dataclass_ref = None
        self._format_version = None
        self._id = None
        self._type = None
        self._project_id = None
        self._update_time = None
        self._version = None
        self._workspace_id = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if data_object is not None:
            self.data_object = data_object
        if dataclass_ref is not None:
            self.dataclass_ref = dataclass_ref
        if format_version is not None:
            self.format_version = format_version
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if project_id is not None:
            self.project_id = project_id
        if update_time is not None:
            self.update_time = update_time
        if version is not None:
            self.version = version
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ListAlertDetail.

        记录时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The create_time of this ListAlertDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListAlertDetail.

        记录时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param create_time: The create_time of this ListAlertDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def data_object(self):
        r"""Gets the data_object of this ListAlertDetail.

        :return: The data_object of this ListAlertDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRsp`
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        r"""Sets the data_object of this ListAlertDetail.

        :param data_object: The data_object of this ListAlertDetail.
        :type data_object: :class:`huaweicloudsdksecmaster.v2.ListAlertRsp`
        """
        self._data_object = data_object

    @property
    def dataclass_ref(self):
        r"""Gets the dataclass_ref of this ListAlertDetail.

        :return: The dataclass_ref of this ListAlertDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AlertDetailDataclassRef`
        """
        return self._dataclass_ref

    @dataclass_ref.setter
    def dataclass_ref(self, dataclass_ref):
        r"""Sets the dataclass_ref of this ListAlertDetail.

        :param dataclass_ref: The dataclass_ref of this ListAlertDetail.
        :type dataclass_ref: :class:`huaweicloudsdksecmaster.v2.AlertDetailDataclassRef`
        """
        self._dataclass_ref = dataclass_ref

    @property
    def format_version(self):
        r"""Gets the format_version of this ListAlertDetail.

        格式版本

        :return: The format_version of this ListAlertDetail.
        :rtype: int
        """
        return self._format_version

    @format_version.setter
    def format_version(self, format_version):
        r"""Sets the format_version of this ListAlertDetail.

        格式版本

        :param format_version: The format_version of this ListAlertDetail.
        :type format_version: int
        """
        self._format_version = format_version

    @property
    def id(self):
        r"""Gets the id of this ListAlertDetail.

        告警唯一标识，UUID格式，最大36个字符

        :return: The id of this ListAlertDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAlertDetail.

        告警唯一标识，UUID格式，最大36个字符

        :param id: The id of this ListAlertDetail.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ListAlertDetail.

        数据类型

        :return: The type of this ListAlertDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAlertDetail.

        数据类型

        :param type: The type of this ListAlertDetail.
        :type type: str
        """
        self._type = type

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAlertDetail.

        当前项目的id

        :return: The project_id of this ListAlertDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAlertDetail.

        当前项目的id

        :param project_id: The project_id of this ListAlertDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def update_time(self):
        r"""Gets the update_time of this ListAlertDetail.

        更新时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The update_time of this ListAlertDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListAlertDetail.

        更新时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param update_time: The update_time of this ListAlertDetail.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def version(self):
        r"""Gets the version of this ListAlertDetail.

        版本

        :return: The version of this ListAlertDetail.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListAlertDetail.

        版本

        :param version: The version of this ListAlertDetail.
        :type version: int
        """
        self._version = version

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAlertDetail.

        当前的工作空间id

        :return: The workspace_id of this ListAlertDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAlertDetail.

        当前的工作空间id

        :param workspace_id: The workspace_id of this ListAlertDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, ListAlertDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
