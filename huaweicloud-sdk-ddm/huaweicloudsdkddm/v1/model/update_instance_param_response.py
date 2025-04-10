# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceParamResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_list': 'str',
        'need_restart': 'bool',
        'job_id': 'str',
        'config_id': 'str',
        'config_name': 'str'
    }

    attribute_map = {
        'node_list': 'nodeList',
        'need_restart': 'needRestart',
        'job_id': 'jobId',
        'config_id': 'configId',
        'config_name': 'configName'
    }

    def __init__(self, node_list=None, need_restart=None, job_id=None, config_id=None, config_name=None):
        r"""UpdateInstanceParamResponse

        The model defined in huaweicloud sdk

        :param node_list: 节点列表。
        :type node_list: str
        :param need_restart: 是否需要重启实例。
        :type need_restart: bool
        :param job_id: 任务id。
        :type job_id: str
        :param config_id: 参数组id。
        :type config_id: str
        :param config_name: 参数组名称。
        :type config_name: str
        """
        
        super(UpdateInstanceParamResponse, self).__init__()

        self._node_list = None
        self._need_restart = None
        self._job_id = None
        self._config_id = None
        self._config_name = None
        self.discriminator = None

        if node_list is not None:
            self.node_list = node_list
        if need_restart is not None:
            self.need_restart = need_restart
        if job_id is not None:
            self.job_id = job_id
        if config_id is not None:
            self.config_id = config_id
        if config_name is not None:
            self.config_name = config_name

    @property
    def node_list(self):
        r"""Gets the node_list of this UpdateInstanceParamResponse.

        节点列表。

        :return: The node_list of this UpdateInstanceParamResponse.
        :rtype: str
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this UpdateInstanceParamResponse.

        节点列表。

        :param node_list: The node_list of this UpdateInstanceParamResponse.
        :type node_list: str
        """
        self._node_list = node_list

    @property
    def need_restart(self):
        r"""Gets the need_restart of this UpdateInstanceParamResponse.

        是否需要重启实例。

        :return: The need_restart of this UpdateInstanceParamResponse.
        :rtype: bool
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        r"""Sets the need_restart of this UpdateInstanceParamResponse.

        是否需要重启实例。

        :param need_restart: The need_restart of this UpdateInstanceParamResponse.
        :type need_restart: bool
        """
        self._need_restart = need_restart

    @property
    def job_id(self):
        r"""Gets the job_id of this UpdateInstanceParamResponse.

        任务id。

        :return: The job_id of this UpdateInstanceParamResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this UpdateInstanceParamResponse.

        任务id。

        :param job_id: The job_id of this UpdateInstanceParamResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def config_id(self):
        r"""Gets the config_id of this UpdateInstanceParamResponse.

        参数组id。

        :return: The config_id of this UpdateInstanceParamResponse.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        r"""Sets the config_id of this UpdateInstanceParamResponse.

        参数组id。

        :param config_id: The config_id of this UpdateInstanceParamResponse.
        :type config_id: str
        """
        self._config_id = config_id

    @property
    def config_name(self):
        r"""Gets the config_name of this UpdateInstanceParamResponse.

        参数组名称。

        :return: The config_name of this UpdateInstanceParamResponse.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        r"""Sets the config_name of this UpdateInstanceParamResponse.

        参数组名称。

        :param config_name: The config_name of this UpdateInstanceParamResponse.
        :type config_name: str
        """
        self._config_name = config_name

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
        if not isinstance(other, UpdateInstanceParamResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
