# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogtankDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'resource_type': 'LogtankResourceType',
        'resource_id': 'str',
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'status': 'ConfigStatus',
        'created_at': 'datetime',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, domain_id=None, project_id=None, resource_type=None, resource_id=None, log_group_id=None, log_stream_id=None, status=None, created_at=None, updated_at=None):
        r"""LogtankDetail

        The model defined in huaweicloud sdk

        :param id: 云日志ID。
        :type id: str
        :param domain_id: 租户ID。
        :type domain_id: str
        :param project_id: 项目ID。
        :type project_id: str
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkga.v1.LogtankResourceType`
        :param resource_id: 开启云日志的资源ID。
        :type resource_id: str
        :param log_group_id: 云日志组ID。
        :type log_group_id: str
        :param log_stream_id: 云日志流ID。
        :type log_stream_id: str
        :param status: 
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        :param created_at: 创建时间。
        :type created_at: datetime
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        

        self._id = None
        self._domain_id = None
        self._project_id = None
        self._resource_type = None
        self._resource_id = None
        self._log_group_id = None
        self._log_stream_id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this LogtankDetail.

        云日志ID。

        :return: The id of this LogtankDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LogtankDetail.

        云日志ID。

        :param id: The id of this LogtankDetail.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this LogtankDetail.

        租户ID。

        :return: The domain_id of this LogtankDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this LogtankDetail.

        租户ID。

        :param domain_id: The domain_id of this LogtankDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this LogtankDetail.

        项目ID。

        :return: The project_id of this LogtankDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this LogtankDetail.

        项目ID。

        :param project_id: The project_id of this LogtankDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this LogtankDetail.

        :return: The resource_type of this LogtankDetail.
        :rtype: :class:`huaweicloudsdkga.v1.LogtankResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this LogtankDetail.

        :param resource_type: The resource_type of this LogtankDetail.
        :type resource_type: :class:`huaweicloudsdkga.v1.LogtankResourceType`
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this LogtankDetail.

        开启云日志的资源ID。

        :return: The resource_id of this LogtankDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this LogtankDetail.

        开启云日志的资源ID。

        :param resource_id: The resource_id of this LogtankDetail.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this LogtankDetail.

        云日志组ID。

        :return: The log_group_id of this LogtankDetail.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this LogtankDetail.

        云日志组ID。

        :param log_group_id: The log_group_id of this LogtankDetail.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this LogtankDetail.

        云日志流ID。

        :return: The log_stream_id of this LogtankDetail.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this LogtankDetail.

        云日志流ID。

        :param log_stream_id: The log_stream_id of this LogtankDetail.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def status(self):
        r"""Gets the status of this LogtankDetail.

        :return: The status of this LogtankDetail.
        :rtype: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this LogtankDetail.

        :param status: The status of this LogtankDetail.
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this LogtankDetail.

        创建时间。

        :return: The created_at of this LogtankDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this LogtankDetail.

        创建时间。

        :param created_at: The created_at of this LogtankDetail.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this LogtankDetail.

        更新时间。

        :return: The updated_at of this LogtankDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this LogtankDetail.

        更新时间。

        :param updated_at: The updated_at of this LogtankDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, LogtankDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
