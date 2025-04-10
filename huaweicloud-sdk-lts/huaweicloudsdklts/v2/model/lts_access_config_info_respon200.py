# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LTSAccessConfigInfoRespon200:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_config_id': 'str',
        'project_id': 'str',
        'access_config_name': 'str',
        'access_config_type': 'object',
        'group_id': 'str',
        'log_group_name': 'str',
        'log_stream_id': 'str',
        'log_stream_name': 'str',
        'create_time': 'int',
        'agency_log_access': 'PreviewAgencyLogAccessReqBody'
    }

    attribute_map = {
        'access_config_id': 'access_config_id',
        'project_id': 'project_id',
        'access_config_name': 'access_config_name',
        'access_config_type': 'access_config_type',
        'group_id': 'group_id',
        'log_group_name': 'log_group_name',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'create_time': 'create_time',
        'agency_log_access': 'agency_log_access'
    }

    def __init__(self, access_config_id=None, project_id=None, access_config_name=None, access_config_type=None, group_id=None, log_group_name=None, log_stream_id=None, log_stream_name=None, create_time=None, agency_log_access=None):
        r"""LTSAccessConfigInfoRespon200

        The model defined in huaweicloud sdk

        :param access_config_id: 跨账号日志接入id
        :type access_config_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param access_config_name: 跨账号日志接入名称
        :type access_config_name: str
        :param access_config_type: 跨账号日志接入类型
        :type access_config_type: object
        :param group_id: 日志组ID
        :type group_id: str
        :param log_group_name: 日志组名称
        :type log_group_name: str
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param create_time: 创建时间
        :type create_time: int
        :param agency_log_access: 
        :type agency_log_access: :class:`huaweicloudsdklts.v2.PreviewAgencyLogAccessReqBody`
        """
        
        

        self._access_config_id = None
        self._project_id = None
        self._access_config_name = None
        self._access_config_type = None
        self._group_id = None
        self._log_group_name = None
        self._log_stream_id = None
        self._log_stream_name = None
        self._create_time = None
        self._agency_log_access = None
        self.discriminator = None

        if access_config_id is not None:
            self.access_config_id = access_config_id
        if project_id is not None:
            self.project_id = project_id
        if access_config_name is not None:
            self.access_config_name = access_config_name
        if access_config_type is not None:
            self.access_config_type = access_config_type
        if group_id is not None:
            self.group_id = group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        if create_time is not None:
            self.create_time = create_time
        if agency_log_access is not None:
            self.agency_log_access = agency_log_access

    @property
    def access_config_id(self):
        r"""Gets the access_config_id of this LTSAccessConfigInfoRespon200.

        跨账号日志接入id

        :return: The access_config_id of this LTSAccessConfigInfoRespon200.
        :rtype: str
        """
        return self._access_config_id

    @access_config_id.setter
    def access_config_id(self, access_config_id):
        r"""Sets the access_config_id of this LTSAccessConfigInfoRespon200.

        跨账号日志接入id

        :param access_config_id: The access_config_id of this LTSAccessConfigInfoRespon200.
        :type access_config_id: str
        """
        self._access_config_id = access_config_id

    @property
    def project_id(self):
        r"""Gets the project_id of this LTSAccessConfigInfoRespon200.

        项目ID

        :return: The project_id of this LTSAccessConfigInfoRespon200.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this LTSAccessConfigInfoRespon200.

        项目ID

        :param project_id: The project_id of this LTSAccessConfigInfoRespon200.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def access_config_name(self):
        r"""Gets the access_config_name of this LTSAccessConfigInfoRespon200.

        跨账号日志接入名称

        :return: The access_config_name of this LTSAccessConfigInfoRespon200.
        :rtype: str
        """
        return self._access_config_name

    @access_config_name.setter
    def access_config_name(self, access_config_name):
        r"""Sets the access_config_name of this LTSAccessConfigInfoRespon200.

        跨账号日志接入名称

        :param access_config_name: The access_config_name of this LTSAccessConfigInfoRespon200.
        :type access_config_name: str
        """
        self._access_config_name = access_config_name

    @property
    def access_config_type(self):
        r"""Gets the access_config_type of this LTSAccessConfigInfoRespon200.

        跨账号日志接入类型

        :return: The access_config_type of this LTSAccessConfigInfoRespon200.
        :rtype: object
        """
        return self._access_config_type

    @access_config_type.setter
    def access_config_type(self, access_config_type):
        r"""Sets the access_config_type of this LTSAccessConfigInfoRespon200.

        跨账号日志接入类型

        :param access_config_type: The access_config_type of this LTSAccessConfigInfoRespon200.
        :type access_config_type: object
        """
        self._access_config_type = access_config_type

    @property
    def group_id(self):
        r"""Gets the group_id of this LTSAccessConfigInfoRespon200.

        日志组ID

        :return: The group_id of this LTSAccessConfigInfoRespon200.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this LTSAccessConfigInfoRespon200.

        日志组ID

        :param group_id: The group_id of this LTSAccessConfigInfoRespon200.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this LTSAccessConfigInfoRespon200.

        日志组名称

        :return: The log_group_name of this LTSAccessConfigInfoRespon200.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this LTSAccessConfigInfoRespon200.

        日志组名称

        :param log_group_name: The log_group_name of this LTSAccessConfigInfoRespon200.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this LTSAccessConfigInfoRespon200.

        日志流ID

        :return: The log_stream_id of this LTSAccessConfigInfoRespon200.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this LTSAccessConfigInfoRespon200.

        日志流ID

        :param log_stream_id: The log_stream_id of this LTSAccessConfigInfoRespon200.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        r"""Gets the log_stream_name of this LTSAccessConfigInfoRespon200.

        日志流名称

        :return: The log_stream_name of this LTSAccessConfigInfoRespon200.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        r"""Sets the log_stream_name of this LTSAccessConfigInfoRespon200.

        日志流名称

        :param log_stream_name: The log_stream_name of this LTSAccessConfigInfoRespon200.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def create_time(self):
        r"""Gets the create_time of this LTSAccessConfigInfoRespon200.

        创建时间

        :return: The create_time of this LTSAccessConfigInfoRespon200.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this LTSAccessConfigInfoRespon200.

        创建时间

        :param create_time: The create_time of this LTSAccessConfigInfoRespon200.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def agency_log_access(self):
        r"""Gets the agency_log_access of this LTSAccessConfigInfoRespon200.

        :return: The agency_log_access of this LTSAccessConfigInfoRespon200.
        :rtype: :class:`huaweicloudsdklts.v2.PreviewAgencyLogAccessReqBody`
        """
        return self._agency_log_access

    @agency_log_access.setter
    def agency_log_access(self, agency_log_access):
        r"""Sets the agency_log_access of this LTSAccessConfigInfoRespon200.

        :param agency_log_access: The agency_log_access of this LTSAccessConfigInfoRespon200.
        :type agency_log_access: :class:`huaweicloudsdklts.v2.PreviewAgencyLogAccessReqBody`
        """
        self._agency_log_access = agency_log_access

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
        if not isinstance(other, LTSAccessConfigInfoRespon200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
