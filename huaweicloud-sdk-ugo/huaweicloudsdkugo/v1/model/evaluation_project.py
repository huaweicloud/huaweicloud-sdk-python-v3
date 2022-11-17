# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationProject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluation_project_id': 'int',
        'evaluation_project_name': 'str',
        'evaluation_project_status': 'str',
        'project_status_detail': 'ProjectStatusDetail',
        'source_db_type': 'str',
        'source_db_version': 'str',
        'target_db_type': 'str',
        'target_db_version': 'str',
        'collect_size': 'int',
        'resource_id': 'str',
        'created_time': 'str',
        'updated_time': 'str',
        'error_reason': 'str'
    }

    attribute_map = {
        'evaluation_project_id': 'evaluation_project_id',
        'evaluation_project_name': 'evaluation_project_name',
        'evaluation_project_status': 'evaluation_project_status',
        'project_status_detail': 'project_status_detail',
        'source_db_type': 'source_db_type',
        'source_db_version': 'source_db_version',
        'target_db_type': 'target_db_type',
        'target_db_version': 'target_db_version',
        'collect_size': 'collect_size',
        'resource_id': 'resource_id',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'error_reason': 'error_reason'
    }

    def __init__(self, evaluation_project_id=None, evaluation_project_name=None, evaluation_project_status=None, project_status_detail=None, source_db_type=None, source_db_version=None, target_db_type=None, target_db_version=None, collect_size=None, resource_id=None, created_time=None, updated_time=None, error_reason=None):
        """EvaluationProject

        The model defined in huaweicloud sdk

        :param evaluation_project_id: 评估项目ID。
        :type evaluation_project_id: int
        :param evaluation_project_name: 评估项目名称。
        :type evaluation_project_name: str
        :param evaluation_project_status: 评估项目状态。
        :type evaluation_project_status: str
        :param project_status_detail: 
        :type project_status_detail: :class:`huaweicloudsdkugo.v1.ProjectStatusDetail`
        :param source_db_type: 源数据库类型。
        :type source_db_type: str
        :param source_db_version: 源数据库版本。
        :type source_db_version: str
        :param target_db_type: 目标数据库类型。
        :type target_db_type: str
        :param target_db_version: 目标数据库版本。
        :type target_db_version: str
        :param collect_size: 已收集的SQL大小，单位：B。
        :type collect_size: int
        :param resource_id: 资源ID。
        :type resource_id: str
        :param created_time: 创建时间。
        :type created_time: str
        :param updated_time: 更新时间。
        :type updated_time: str
        :param error_reason: 失败原因。
        :type error_reason: str
        """
        
        

        self._evaluation_project_id = None
        self._evaluation_project_name = None
        self._evaluation_project_status = None
        self._project_status_detail = None
        self._source_db_type = None
        self._source_db_version = None
        self._target_db_type = None
        self._target_db_version = None
        self._collect_size = None
        self._resource_id = None
        self._created_time = None
        self._updated_time = None
        self._error_reason = None
        self.discriminator = None

        self.evaluation_project_id = evaluation_project_id
        self.evaluation_project_name = evaluation_project_name
        self.evaluation_project_status = evaluation_project_status
        if project_status_detail is not None:
            self.project_status_detail = project_status_detail
        self.source_db_type = source_db_type
        self.source_db_version = source_db_version
        if target_db_type is not None:
            self.target_db_type = target_db_type
        if target_db_version is not None:
            self.target_db_version = target_db_version
        if collect_size is not None:
            self.collect_size = collect_size
        self.resource_id = resource_id
        self.created_time = created_time
        self.updated_time = updated_time
        if error_reason is not None:
            self.error_reason = error_reason

    @property
    def evaluation_project_id(self):
        """Gets the evaluation_project_id of this EvaluationProject.

        评估项目ID。

        :return: The evaluation_project_id of this EvaluationProject.
        :rtype: int
        """
        return self._evaluation_project_id

    @evaluation_project_id.setter
    def evaluation_project_id(self, evaluation_project_id):
        """Sets the evaluation_project_id of this EvaluationProject.

        评估项目ID。

        :param evaluation_project_id: The evaluation_project_id of this EvaluationProject.
        :type evaluation_project_id: int
        """
        self._evaluation_project_id = evaluation_project_id

    @property
    def evaluation_project_name(self):
        """Gets the evaluation_project_name of this EvaluationProject.

        评估项目名称。

        :return: The evaluation_project_name of this EvaluationProject.
        :rtype: str
        """
        return self._evaluation_project_name

    @evaluation_project_name.setter
    def evaluation_project_name(self, evaluation_project_name):
        """Sets the evaluation_project_name of this EvaluationProject.

        评估项目名称。

        :param evaluation_project_name: The evaluation_project_name of this EvaluationProject.
        :type evaluation_project_name: str
        """
        self._evaluation_project_name = evaluation_project_name

    @property
    def evaluation_project_status(self):
        """Gets the evaluation_project_status of this EvaluationProject.

        评估项目状态。

        :return: The evaluation_project_status of this EvaluationProject.
        :rtype: str
        """
        return self._evaluation_project_status

    @evaluation_project_status.setter
    def evaluation_project_status(self, evaluation_project_status):
        """Sets the evaluation_project_status of this EvaluationProject.

        评估项目状态。

        :param evaluation_project_status: The evaluation_project_status of this EvaluationProject.
        :type evaluation_project_status: str
        """
        self._evaluation_project_status = evaluation_project_status

    @property
    def project_status_detail(self):
        """Gets the project_status_detail of this EvaluationProject.

        :return: The project_status_detail of this EvaluationProject.
        :rtype: :class:`huaweicloudsdkugo.v1.ProjectStatusDetail`
        """
        return self._project_status_detail

    @project_status_detail.setter
    def project_status_detail(self, project_status_detail):
        """Sets the project_status_detail of this EvaluationProject.

        :param project_status_detail: The project_status_detail of this EvaluationProject.
        :type project_status_detail: :class:`huaweicloudsdkugo.v1.ProjectStatusDetail`
        """
        self._project_status_detail = project_status_detail

    @property
    def source_db_type(self):
        """Gets the source_db_type of this EvaluationProject.

        源数据库类型。

        :return: The source_db_type of this EvaluationProject.
        :rtype: str
        """
        return self._source_db_type

    @source_db_type.setter
    def source_db_type(self, source_db_type):
        """Sets the source_db_type of this EvaluationProject.

        源数据库类型。

        :param source_db_type: The source_db_type of this EvaluationProject.
        :type source_db_type: str
        """
        self._source_db_type = source_db_type

    @property
    def source_db_version(self):
        """Gets the source_db_version of this EvaluationProject.

        源数据库版本。

        :return: The source_db_version of this EvaluationProject.
        :rtype: str
        """
        return self._source_db_version

    @source_db_version.setter
    def source_db_version(self, source_db_version):
        """Sets the source_db_version of this EvaluationProject.

        源数据库版本。

        :param source_db_version: The source_db_version of this EvaluationProject.
        :type source_db_version: str
        """
        self._source_db_version = source_db_version

    @property
    def target_db_type(self):
        """Gets the target_db_type of this EvaluationProject.

        目标数据库类型。

        :return: The target_db_type of this EvaluationProject.
        :rtype: str
        """
        return self._target_db_type

    @target_db_type.setter
    def target_db_type(self, target_db_type):
        """Sets the target_db_type of this EvaluationProject.

        目标数据库类型。

        :param target_db_type: The target_db_type of this EvaluationProject.
        :type target_db_type: str
        """
        self._target_db_type = target_db_type

    @property
    def target_db_version(self):
        """Gets the target_db_version of this EvaluationProject.

        目标数据库版本。

        :return: The target_db_version of this EvaluationProject.
        :rtype: str
        """
        return self._target_db_version

    @target_db_version.setter
    def target_db_version(self, target_db_version):
        """Sets the target_db_version of this EvaluationProject.

        目标数据库版本。

        :param target_db_version: The target_db_version of this EvaluationProject.
        :type target_db_version: str
        """
        self._target_db_version = target_db_version

    @property
    def collect_size(self):
        """Gets the collect_size of this EvaluationProject.

        已收集的SQL大小，单位：B。

        :return: The collect_size of this EvaluationProject.
        :rtype: int
        """
        return self._collect_size

    @collect_size.setter
    def collect_size(self, collect_size):
        """Sets the collect_size of this EvaluationProject.

        已收集的SQL大小，单位：B。

        :param collect_size: The collect_size of this EvaluationProject.
        :type collect_size: int
        """
        self._collect_size = collect_size

    @property
    def resource_id(self):
        """Gets the resource_id of this EvaluationProject.

        资源ID。

        :return: The resource_id of this EvaluationProject.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this EvaluationProject.

        资源ID。

        :param resource_id: The resource_id of this EvaluationProject.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def created_time(self):
        """Gets the created_time of this EvaluationProject.

        创建时间。

        :return: The created_time of this EvaluationProject.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EvaluationProject.

        创建时间。

        :param created_time: The created_time of this EvaluationProject.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this EvaluationProject.

        更新时间。

        :return: The updated_time of this EvaluationProject.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this EvaluationProject.

        更新时间。

        :param updated_time: The updated_time of this EvaluationProject.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def error_reason(self):
        """Gets the error_reason of this EvaluationProject.

        失败原因。

        :return: The error_reason of this EvaluationProject.
        :rtype: str
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        """Sets the error_reason of this EvaluationProject.

        失败原因。

        :param error_reason: The error_reason of this EvaluationProject.
        :type error_reason: str
        """
        self._error_reason = error_reason

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
        if not isinstance(other, EvaluationProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
