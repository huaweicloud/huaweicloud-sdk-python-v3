# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfirmTargetDbTypeResponse(SdkResponse):

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
        'target_db_version': 'str'
    }

    attribute_map = {
        'evaluation_project_id': 'evaluation_project_id',
        'evaluation_project_name': 'evaluation_project_name',
        'evaluation_project_status': 'evaluation_project_status',
        'project_status_detail': 'project_status_detail',
        'source_db_type': 'source_db_type',
        'source_db_version': 'source_db_version',
        'target_db_type': 'target_db_type',
        'target_db_version': 'target_db_version'
    }

    def __init__(self, evaluation_project_id=None, evaluation_project_name=None, evaluation_project_status=None, project_status_detail=None, source_db_type=None, source_db_version=None, target_db_type=None, target_db_version=None):
        r"""ConfirmTargetDbTypeResponse

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
        """
        
        super(ConfirmTargetDbTypeResponse, self).__init__()

        self._evaluation_project_id = None
        self._evaluation_project_name = None
        self._evaluation_project_status = None
        self._project_status_detail = None
        self._source_db_type = None
        self._source_db_version = None
        self._target_db_type = None
        self._target_db_version = None
        self.discriminator = None

        if evaluation_project_id is not None:
            self.evaluation_project_id = evaluation_project_id
        if evaluation_project_name is not None:
            self.evaluation_project_name = evaluation_project_name
        if evaluation_project_status is not None:
            self.evaluation_project_status = evaluation_project_status
        if project_status_detail is not None:
            self.project_status_detail = project_status_detail
        if source_db_type is not None:
            self.source_db_type = source_db_type
        if source_db_version is not None:
            self.source_db_version = source_db_version
        if target_db_type is not None:
            self.target_db_type = target_db_type
        if target_db_version is not None:
            self.target_db_version = target_db_version

    @property
    def evaluation_project_id(self):
        r"""Gets the evaluation_project_id of this ConfirmTargetDbTypeResponse.

        评估项目ID。

        :return: The evaluation_project_id of this ConfirmTargetDbTypeResponse.
        :rtype: int
        """
        return self._evaluation_project_id

    @evaluation_project_id.setter
    def evaluation_project_id(self, evaluation_project_id):
        r"""Sets the evaluation_project_id of this ConfirmTargetDbTypeResponse.

        评估项目ID。

        :param evaluation_project_id: The evaluation_project_id of this ConfirmTargetDbTypeResponse.
        :type evaluation_project_id: int
        """
        self._evaluation_project_id = evaluation_project_id

    @property
    def evaluation_project_name(self):
        r"""Gets the evaluation_project_name of this ConfirmTargetDbTypeResponse.

        评估项目名称。

        :return: The evaluation_project_name of this ConfirmTargetDbTypeResponse.
        :rtype: str
        """
        return self._evaluation_project_name

    @evaluation_project_name.setter
    def evaluation_project_name(self, evaluation_project_name):
        r"""Sets the evaluation_project_name of this ConfirmTargetDbTypeResponse.

        评估项目名称。

        :param evaluation_project_name: The evaluation_project_name of this ConfirmTargetDbTypeResponse.
        :type evaluation_project_name: str
        """
        self._evaluation_project_name = evaluation_project_name

    @property
    def evaluation_project_status(self):
        r"""Gets the evaluation_project_status of this ConfirmTargetDbTypeResponse.

        评估项目状态。

        :return: The evaluation_project_status of this ConfirmTargetDbTypeResponse.
        :rtype: str
        """
        return self._evaluation_project_status

    @evaluation_project_status.setter
    def evaluation_project_status(self, evaluation_project_status):
        r"""Sets the evaluation_project_status of this ConfirmTargetDbTypeResponse.

        评估项目状态。

        :param evaluation_project_status: The evaluation_project_status of this ConfirmTargetDbTypeResponse.
        :type evaluation_project_status: str
        """
        self._evaluation_project_status = evaluation_project_status

    @property
    def project_status_detail(self):
        r"""Gets the project_status_detail of this ConfirmTargetDbTypeResponse.

        :return: The project_status_detail of this ConfirmTargetDbTypeResponse.
        :rtype: :class:`huaweicloudsdkugo.v1.ProjectStatusDetail`
        """
        return self._project_status_detail

    @project_status_detail.setter
    def project_status_detail(self, project_status_detail):
        r"""Sets the project_status_detail of this ConfirmTargetDbTypeResponse.

        :param project_status_detail: The project_status_detail of this ConfirmTargetDbTypeResponse.
        :type project_status_detail: :class:`huaweicloudsdkugo.v1.ProjectStatusDetail`
        """
        self._project_status_detail = project_status_detail

    @property
    def source_db_type(self):
        r"""Gets the source_db_type of this ConfirmTargetDbTypeResponse.

        源数据库类型。

        :return: The source_db_type of this ConfirmTargetDbTypeResponse.
        :rtype: str
        """
        return self._source_db_type

    @source_db_type.setter
    def source_db_type(self, source_db_type):
        r"""Sets the source_db_type of this ConfirmTargetDbTypeResponse.

        源数据库类型。

        :param source_db_type: The source_db_type of this ConfirmTargetDbTypeResponse.
        :type source_db_type: str
        """
        self._source_db_type = source_db_type

    @property
    def source_db_version(self):
        r"""Gets the source_db_version of this ConfirmTargetDbTypeResponse.

        源数据库版本。

        :return: The source_db_version of this ConfirmTargetDbTypeResponse.
        :rtype: str
        """
        return self._source_db_version

    @source_db_version.setter
    def source_db_version(self, source_db_version):
        r"""Sets the source_db_version of this ConfirmTargetDbTypeResponse.

        源数据库版本。

        :param source_db_version: The source_db_version of this ConfirmTargetDbTypeResponse.
        :type source_db_version: str
        """
        self._source_db_version = source_db_version

    @property
    def target_db_type(self):
        r"""Gets the target_db_type of this ConfirmTargetDbTypeResponse.

        目标数据库类型。

        :return: The target_db_type of this ConfirmTargetDbTypeResponse.
        :rtype: str
        """
        return self._target_db_type

    @target_db_type.setter
    def target_db_type(self, target_db_type):
        r"""Sets the target_db_type of this ConfirmTargetDbTypeResponse.

        目标数据库类型。

        :param target_db_type: The target_db_type of this ConfirmTargetDbTypeResponse.
        :type target_db_type: str
        """
        self._target_db_type = target_db_type

    @property
    def target_db_version(self):
        r"""Gets the target_db_version of this ConfirmTargetDbTypeResponse.

        目标数据库版本。

        :return: The target_db_version of this ConfirmTargetDbTypeResponse.
        :rtype: str
        """
        return self._target_db_version

    @target_db_version.setter
    def target_db_version(self, target_db_version):
        r"""Sets the target_db_version of this ConfirmTargetDbTypeResponse.

        目标数据库版本。

        :param target_db_version: The target_db_version of this ConfirmTargetDbTypeResponse.
        :type target_db_version: str
        """
        self._target_db_version = target_db_version

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
        if not isinstance(other, ConfirmTargetDbTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
