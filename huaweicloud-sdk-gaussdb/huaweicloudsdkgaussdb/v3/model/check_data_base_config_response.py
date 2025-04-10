# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckDataBaseConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_database_name': 'str',
        'source_db_config_check_results': 'list[DbConfigCheckResult]',
        'target_database_name': 'str',
        'target_db_config_check_results': 'list[DbConfigCheckResult]',
        'task_name': 'str'
    }

    attribute_map = {
        'source_database_name': 'source_database_name',
        'source_db_config_check_results': 'source_db_config_check_results',
        'target_database_name': 'target_database_name',
        'target_db_config_check_results': 'target_db_config_check_results',
        'task_name': 'task_name'
    }

    def __init__(self, source_database_name=None, source_db_config_check_results=None, target_database_name=None, target_db_config_check_results=None, task_name=None):
        r"""CheckDataBaseConfigResponse

        The model defined in huaweicloud sdk

        :param source_database_name: TaurusDB数据库名称。
        :type source_database_name: str
        :param source_db_config_check_results: TaurusDB数据库配置检查结果。
        :type source_db_config_check_results: list[:class:`huaweicloudsdkgaussdb.v3.DbConfigCheckResult`]
        :param target_database_name: 目标数据库名称。
        :type target_database_name: str
        :param target_db_config_check_results: 目标数据库配置检查结果。
        :type target_db_config_check_results: list[:class:`huaweicloudsdkgaussdb.v3.DbConfigCheckResult`]
        :param task_name: 同步任务名称。
        :type task_name: str
        """
        
        super(CheckDataBaseConfigResponse, self).__init__()

        self._source_database_name = None
        self._source_db_config_check_results = None
        self._target_database_name = None
        self._target_db_config_check_results = None
        self._task_name = None
        self.discriminator = None

        if source_database_name is not None:
            self.source_database_name = source_database_name
        if source_db_config_check_results is not None:
            self.source_db_config_check_results = source_db_config_check_results
        if target_database_name is not None:
            self.target_database_name = target_database_name
        if target_db_config_check_results is not None:
            self.target_db_config_check_results = target_db_config_check_results
        if task_name is not None:
            self.task_name = task_name

    @property
    def source_database_name(self):
        r"""Gets the source_database_name of this CheckDataBaseConfigResponse.

        TaurusDB数据库名称。

        :return: The source_database_name of this CheckDataBaseConfigResponse.
        :rtype: str
        """
        return self._source_database_name

    @source_database_name.setter
    def source_database_name(self, source_database_name):
        r"""Sets the source_database_name of this CheckDataBaseConfigResponse.

        TaurusDB数据库名称。

        :param source_database_name: The source_database_name of this CheckDataBaseConfigResponse.
        :type source_database_name: str
        """
        self._source_database_name = source_database_name

    @property
    def source_db_config_check_results(self):
        r"""Gets the source_db_config_check_results of this CheckDataBaseConfigResponse.

        TaurusDB数据库配置检查结果。

        :return: The source_db_config_check_results of this CheckDataBaseConfigResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DbConfigCheckResult`]
        """
        return self._source_db_config_check_results

    @source_db_config_check_results.setter
    def source_db_config_check_results(self, source_db_config_check_results):
        r"""Sets the source_db_config_check_results of this CheckDataBaseConfigResponse.

        TaurusDB数据库配置检查结果。

        :param source_db_config_check_results: The source_db_config_check_results of this CheckDataBaseConfigResponse.
        :type source_db_config_check_results: list[:class:`huaweicloudsdkgaussdb.v3.DbConfigCheckResult`]
        """
        self._source_db_config_check_results = source_db_config_check_results

    @property
    def target_database_name(self):
        r"""Gets the target_database_name of this CheckDataBaseConfigResponse.

        目标数据库名称。

        :return: The target_database_name of this CheckDataBaseConfigResponse.
        :rtype: str
        """
        return self._target_database_name

    @target_database_name.setter
    def target_database_name(self, target_database_name):
        r"""Sets the target_database_name of this CheckDataBaseConfigResponse.

        目标数据库名称。

        :param target_database_name: The target_database_name of this CheckDataBaseConfigResponse.
        :type target_database_name: str
        """
        self._target_database_name = target_database_name

    @property
    def target_db_config_check_results(self):
        r"""Gets the target_db_config_check_results of this CheckDataBaseConfigResponse.

        目标数据库配置检查结果。

        :return: The target_db_config_check_results of this CheckDataBaseConfigResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DbConfigCheckResult`]
        """
        return self._target_db_config_check_results

    @target_db_config_check_results.setter
    def target_db_config_check_results(self, target_db_config_check_results):
        r"""Sets the target_db_config_check_results of this CheckDataBaseConfigResponse.

        目标数据库配置检查结果。

        :param target_db_config_check_results: The target_db_config_check_results of this CheckDataBaseConfigResponse.
        :type target_db_config_check_results: list[:class:`huaweicloudsdkgaussdb.v3.DbConfigCheckResult`]
        """
        self._target_db_config_check_results = target_db_config_check_results

    @property
    def task_name(self):
        r"""Gets the task_name of this CheckDataBaseConfigResponse.

        同步任务名称。

        :return: The task_name of this CheckDataBaseConfigResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this CheckDataBaseConfigResponse.

        同步任务名称。

        :param task_name: The task_name of this CheckDataBaseConfigResponse.
        :type task_name: str
        """
        self._task_name = task_name

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
        if not isinstance(other, CheckDataBaseConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
