# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckAudioJobResponse(SdkResponse):

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
        'description': 'str',
        'state': 'str',
        'name': 'str',
        'service_config': 'AudioServiceConfig',
        'input': 'CheckAudioJobResponseBodyInput',
        'output': 'AudioResponseOutput',
        'service_version': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'state': 'state',
        'name': 'name',
        'service_config': 'service_config',
        'input': 'input',
        'output': 'output',
        'service_version': 'service_version',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, description=None, state=None, name=None, service_config=None, input=None, output=None, service_version=None, created_at=None, updated_at=None):
        r"""CheckAudioJobResponse

        The model defined in huaweicloud sdk

        :param id: 作业ID.
        :type id: str
        :param description: 作业描述
        :type description: str
        :param state: 作业状态：   - PENDING_CREATE：等待中   - SCHEDULING：调度中   - CREATE_FAIL：创建失败   - STARTING：启动中   - RUNNING：运行中   - SUCCEEDED：运行成功   - FAILED：运行失败   - PENDING_DELETE：删除中   - DELETE_FAIL：删除失败   - ABNORMAL：运行异常
        :type state: str
        :param name: 作业名称.
        :type name: str
        :param service_config: 
        :type service_config: :class:`huaweicloudsdkvcm.v2.AudioServiceConfig`
        :param input: 
        :type input: :class:`huaweicloudsdkvcm.v2.CheckAudioJobResponseBodyInput`
        :param output: 
        :type output: :class:`huaweicloudsdkvcm.v2.AudioResponseOutput`
        :param service_version: 服务版本
        :type service_version: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 修改时间
        :type updated_at: str
        """
        
        super(CheckAudioJobResponse, self).__init__()

        self._id = None
        self._description = None
        self._state = None
        self._name = None
        self._service_config = None
        self._input = None
        self._output = None
        self._service_version = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if state is not None:
            self.state = state
        if name is not None:
            self.name = name
        if service_config is not None:
            self.service_config = service_config
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if service_version is not None:
            self.service_version = service_version
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this CheckAudioJobResponse.

        作业ID.

        :return: The id of this CheckAudioJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CheckAudioJobResponse.

        作业ID.

        :param id: The id of this CheckAudioJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this CheckAudioJobResponse.

        作业描述

        :return: The description of this CheckAudioJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CheckAudioJobResponse.

        作业描述

        :param description: The description of this CheckAudioJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        r"""Gets the state of this CheckAudioJobResponse.

        作业状态：   - PENDING_CREATE：等待中   - SCHEDULING：调度中   - CREATE_FAIL：创建失败   - STARTING：启动中   - RUNNING：运行中   - SUCCEEDED：运行成功   - FAILED：运行失败   - PENDING_DELETE：删除中   - DELETE_FAIL：删除失败   - ABNORMAL：运行异常

        :return: The state of this CheckAudioJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CheckAudioJobResponse.

        作业状态：   - PENDING_CREATE：等待中   - SCHEDULING：调度中   - CREATE_FAIL：创建失败   - STARTING：启动中   - RUNNING：运行中   - SUCCEEDED：运行成功   - FAILED：运行失败   - PENDING_DELETE：删除中   - DELETE_FAIL：删除失败   - ABNORMAL：运行异常

        :param state: The state of this CheckAudioJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def name(self):
        r"""Gets the name of this CheckAudioJobResponse.

        作业名称.

        :return: The name of this CheckAudioJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CheckAudioJobResponse.

        作业名称.

        :param name: The name of this CheckAudioJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def service_config(self):
        r"""Gets the service_config of this CheckAudioJobResponse.

        :return: The service_config of this CheckAudioJobResponse.
        :rtype: :class:`huaweicloudsdkvcm.v2.AudioServiceConfig`
        """
        return self._service_config

    @service_config.setter
    def service_config(self, service_config):
        r"""Sets the service_config of this CheckAudioJobResponse.

        :param service_config: The service_config of this CheckAudioJobResponse.
        :type service_config: :class:`huaweicloudsdkvcm.v2.AudioServiceConfig`
        """
        self._service_config = service_config

    @property
    def input(self):
        r"""Gets the input of this CheckAudioJobResponse.

        :return: The input of this CheckAudioJobResponse.
        :rtype: :class:`huaweicloudsdkvcm.v2.CheckAudioJobResponseBodyInput`
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this CheckAudioJobResponse.

        :param input: The input of this CheckAudioJobResponse.
        :type input: :class:`huaweicloudsdkvcm.v2.CheckAudioJobResponseBodyInput`
        """
        self._input = input

    @property
    def output(self):
        r"""Gets the output of this CheckAudioJobResponse.

        :return: The output of this CheckAudioJobResponse.
        :rtype: :class:`huaweicloudsdkvcm.v2.AudioResponseOutput`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this CheckAudioJobResponse.

        :param output: The output of this CheckAudioJobResponse.
        :type output: :class:`huaweicloudsdkvcm.v2.AudioResponseOutput`
        """
        self._output = output

    @property
    def service_version(self):
        r"""Gets the service_version of this CheckAudioJobResponse.

        服务版本

        :return: The service_version of this CheckAudioJobResponse.
        :rtype: str
        """
        return self._service_version

    @service_version.setter
    def service_version(self, service_version):
        r"""Sets the service_version of this CheckAudioJobResponse.

        服务版本

        :param service_version: The service_version of this CheckAudioJobResponse.
        :type service_version: str
        """
        self._service_version = service_version

    @property
    def created_at(self):
        r"""Gets the created_at of this CheckAudioJobResponse.

        创建时间

        :return: The created_at of this CheckAudioJobResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CheckAudioJobResponse.

        创建时间

        :param created_at: The created_at of this CheckAudioJobResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CheckAudioJobResponse.

        修改时间

        :return: The updated_at of this CheckAudioJobResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CheckAudioJobResponse.

        修改时间

        :param updated_at: The updated_at of this CheckAudioJobResponse.
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
        if not isinstance(other, CheckAudioJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
