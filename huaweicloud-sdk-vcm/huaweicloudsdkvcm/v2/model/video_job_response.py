# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoJobResponse:

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
        'name': 'str',
        'description': 'str',
        'state': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'input': 'object',
        'service_config': 'object',
        'output': 'object',
        'hosting_result': 'VideoJobResponseHostingResult',
        'service_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'input': 'input',
        'service_config': 'service_config',
        'output': 'output',
        'hosting_result': 'hosting_result',
        'service_version': 'service_version'
    }

    def __init__(self, id=None, name=None, description=None, state=None, created_at=None, updated_at=None, input=None, service_config=None, output=None, hosting_result=None, service_version=None):
        """VideoJobResponse

        The model defined in huaweicloud sdk

        :param id: 作业ID。
        :type id: str
        :param name: 作业名称。
        :type name: str
        :param description: 作业描述信息，默认值为空。
        :type description: str
        :param state: 作业状态： - PENDING：等待中 - RECOVERING ：恢复中 - STARTING：启动中 - UPGRADING ：更新中 - CREATE_FAILED：创建失败 - START_FAILED：启动失败 - RUNNING：运行中 - STOPPING：停止中 - STOPPED：已停止 - ABNORMAL：运行异常 - SUCCEEDED：运行成功 - FAILED：运行失败 - DELETING：删除中 - FREEZING ：冻结中 - FROZEN ：已冻结
        :type state: str
        :param created_at: 作业创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ。
        :type created_at: str
        :param updated_at: 作业更新时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ。
        :type updated_at: str
        :param input: 数据输入列表，默认值为[]。
        :type input: object
        :param service_config: 服务算法配置，字段结构跟服务相关。
        :type service_config: object
        :param output: 数据输出列表，默认值为[]
        :type output: object
        :param hosting_result: 
        :type hosting_result: :class:`huaweicloudsdkvcm.v2.VideoJobResponseHostingResult`
        :param service_version: 作业对应的服务版本。
        :type service_version: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._input = None
        self._service_config = None
        self._output = None
        self._hosting_result = None
        self._service_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if input is not None:
            self.input = input
        if service_config is not None:
            self.service_config = service_config
        if output is not None:
            self.output = output
        if hosting_result is not None:
            self.hosting_result = hosting_result
        if service_version is not None:
            self.service_version = service_version

    @property
    def id(self):
        """Gets the id of this VideoJobResponse.

        作业ID。

        :return: The id of this VideoJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VideoJobResponse.

        作业ID。

        :param id: The id of this VideoJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VideoJobResponse.

        作业名称。

        :return: The name of this VideoJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VideoJobResponse.

        作业名称。

        :param name: The name of this VideoJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this VideoJobResponse.

        作业描述信息，默认值为空。

        :return: The description of this VideoJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VideoJobResponse.

        作业描述信息，默认值为空。

        :param description: The description of this VideoJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        """Gets the state of this VideoJobResponse.

        作业状态： - PENDING：等待中 - RECOVERING ：恢复中 - STARTING：启动中 - UPGRADING ：更新中 - CREATE_FAILED：创建失败 - START_FAILED：启动失败 - RUNNING：运行中 - STOPPING：停止中 - STOPPED：已停止 - ABNORMAL：运行异常 - SUCCEEDED：运行成功 - FAILED：运行失败 - DELETING：删除中 - FREEZING ：冻结中 - FROZEN ：已冻结

        :return: The state of this VideoJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VideoJobResponse.

        作业状态： - PENDING：等待中 - RECOVERING ：恢复中 - STARTING：启动中 - UPGRADING ：更新中 - CREATE_FAILED：创建失败 - START_FAILED：启动失败 - RUNNING：运行中 - STOPPING：停止中 - STOPPED：已停止 - ABNORMAL：运行异常 - SUCCEEDED：运行成功 - FAILED：运行失败 - DELETING：删除中 - FREEZING ：冻结中 - FROZEN ：已冻结

        :param state: The state of this VideoJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this VideoJobResponse.

        作业创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ。

        :return: The created_at of this VideoJobResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VideoJobResponse.

        作业创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ。

        :param created_at: The created_at of this VideoJobResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this VideoJobResponse.

        作业更新时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ。

        :return: The updated_at of this VideoJobResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VideoJobResponse.

        作业更新时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ。

        :param updated_at: The updated_at of this VideoJobResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def input(self):
        """Gets the input of this VideoJobResponse.

        数据输入列表，默认值为[]。

        :return: The input of this VideoJobResponse.
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this VideoJobResponse.

        数据输入列表，默认值为[]。

        :param input: The input of this VideoJobResponse.
        :type input: object
        """
        self._input = input

    @property
    def service_config(self):
        """Gets the service_config of this VideoJobResponse.

        服务算法配置，字段结构跟服务相关。

        :return: The service_config of this VideoJobResponse.
        :rtype: object
        """
        return self._service_config

    @service_config.setter
    def service_config(self, service_config):
        """Sets the service_config of this VideoJobResponse.

        服务算法配置，字段结构跟服务相关。

        :param service_config: The service_config of this VideoJobResponse.
        :type service_config: object
        """
        self._service_config = service_config

    @property
    def output(self):
        """Gets the output of this VideoJobResponse.

        数据输出列表，默认值为[]

        :return: The output of this VideoJobResponse.
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this VideoJobResponse.

        数据输出列表，默认值为[]

        :param output: The output of this VideoJobResponse.
        :type output: object
        """
        self._output = output

    @property
    def hosting_result(self):
        """Gets the hosting_result of this VideoJobResponse.


        :return: The hosting_result of this VideoJobResponse.
        :rtype: :class:`huaweicloudsdkvcm.v2.VideoJobResponseHostingResult`
        """
        return self._hosting_result

    @hosting_result.setter
    def hosting_result(self, hosting_result):
        """Sets the hosting_result of this VideoJobResponse.


        :param hosting_result: The hosting_result of this VideoJobResponse.
        :type hosting_result: :class:`huaweicloudsdkvcm.v2.VideoJobResponseHostingResult`
        """
        self._hosting_result = hosting_result

    @property
    def service_version(self):
        """Gets the service_version of this VideoJobResponse.

        作业对应的服务版本。

        :return: The service_version of this VideoJobResponse.
        :rtype: str
        """
        return self._service_version

    @service_version.setter
    def service_version(self, service_version):
        """Sets the service_version of this VideoJobResponse.

        作业对应的服务版本。

        :param service_version: The service_version of this VideoJobResponse.
        :type service_version: str
        """
        self._service_version = service_version

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
        if not isinstance(other, VideoJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
