# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainMigrateProjectStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'region_id': 'str',
        'progress': 'int',
        'fail_code': 'int',
        'fail_reason': 'str'
    }

    attribute_map = {
        'status': 'status',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'region_id': 'region_id',
        'progress': 'progress',
        'fail_code': 'fail_code',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, status=None, project_id=None, project_name=None, region_id=None, progress=None, fail_code=None, fail_reason=None):
        """DomainMigrateProjectStatus

        The model defined in huaweicloud sdk

        :param status: 迁移状态
        :type status: str
        :param project_id: 项目ID
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param region_id: 区域ID
        :type region_id: str
        :param progress: 迁移进度
        :type progress: int
        :param fail_code: 失败错误码（仅当项目状态为失败时才有该参数）。
        :type fail_code: int
        :param fail_reason: 失败原因（仅当项目状态为失败时才有该参数）。
        :type fail_reason: str
        """
        
        

        self._status = None
        self._project_id = None
        self._project_name = None
        self._region_id = None
        self._progress = None
        self._fail_code = None
        self._fail_reason = None
        self.discriminator = None

        self.status = status
        self.project_id = project_id
        self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        if progress is not None:
            self.progress = progress
        if fail_code is not None:
            self.fail_code = fail_code
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def status(self):
        """Gets the status of this DomainMigrateProjectStatus.

        迁移状态

        :return: The status of this DomainMigrateProjectStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DomainMigrateProjectStatus.

        迁移状态

        :param status: The status of this DomainMigrateProjectStatus.
        :type status: str
        """
        self._status = status

    @property
    def project_id(self):
        """Gets the project_id of this DomainMigrateProjectStatus.

        项目ID

        :return: The project_id of this DomainMigrateProjectStatus.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DomainMigrateProjectStatus.

        项目ID

        :param project_id: The project_id of this DomainMigrateProjectStatus.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this DomainMigrateProjectStatus.

        项目名称

        :return: The project_name of this DomainMigrateProjectStatus.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DomainMigrateProjectStatus.

        项目名称

        :param project_name: The project_name of this DomainMigrateProjectStatus.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this DomainMigrateProjectStatus.

        区域ID

        :return: The region_id of this DomainMigrateProjectStatus.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this DomainMigrateProjectStatus.

        区域ID

        :param region_id: The region_id of this DomainMigrateProjectStatus.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def progress(self):
        """Gets the progress of this DomainMigrateProjectStatus.

        迁移进度

        :return: The progress of this DomainMigrateProjectStatus.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DomainMigrateProjectStatus.

        迁移进度

        :param progress: The progress of this DomainMigrateProjectStatus.
        :type progress: int
        """
        self._progress = progress

    @property
    def fail_code(self):
        """Gets the fail_code of this DomainMigrateProjectStatus.

        失败错误码（仅当项目状态为失败时才有该参数）。

        :return: The fail_code of this DomainMigrateProjectStatus.
        :rtype: int
        """
        return self._fail_code

    @fail_code.setter
    def fail_code(self, fail_code):
        """Sets the fail_code of this DomainMigrateProjectStatus.

        失败错误码（仅当项目状态为失败时才有该参数）。

        :param fail_code: The fail_code of this DomainMigrateProjectStatus.
        :type fail_code: int
        """
        self._fail_code = fail_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this DomainMigrateProjectStatus.

        失败原因（仅当项目状态为失败时才有该参数）。

        :return: The fail_reason of this DomainMigrateProjectStatus.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this DomainMigrateProjectStatus.

        失败原因（仅当项目状态为失败时才有该参数）。

        :param fail_reason: The fail_reason of this DomainMigrateProjectStatus.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, DomainMigrateProjectStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
