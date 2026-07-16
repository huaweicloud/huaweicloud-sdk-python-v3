# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevServerTaskResponse:

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
        'server_id': 'str',
        'server_name': 'str',
        'status': 'str',
        'cloud_server': 'dict(str, str)',
        'message': 'str',
        'create_at': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'server_id': 'server_id',
        'server_name': 'server_name',
        'status': 'status',
        'cloud_server': 'cloud_server',
        'message': 'message',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, id=None, server_id=None, server_name=None, status=None, cloud_server=None, message=None, create_at=None, update_at=None):
        r"""DevServerTaskResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：task的ID。 **取值范围**：不涉及。
        :type id: str
        :param server_id: **参数解释**：devserver机器ID。 **取值范围**：不涉及。
        :type server_id: str
        :param server_name: **参数解释**：devserver机器名称。 **取值范围**：不涉及。
        :type server_name: str
        :param status: **参数解释**：task状态。 **取值范围**：- PROCESSING  -SUCCESS  - FAILED  - SKIPPED
        :type status: str
        :param cloud_server: **参数解释**：底层ECS/BMS/HPS ID。
        :type cloud_server: dict(str, str)
        :param message: **参数解释**：输出信息。 **取值范围**：不涉及。
        :type message: str
        :param create_at: **参数解释**：创建时间。 **取值范围**：不涉及。
        :type create_at: str
        :param update_at: **参数解释**：更新时间。 **取值范围**：不涉及。
        :type update_at: str
        """
        
        

        self._id = None
        self._server_id = None
        self._server_name = None
        self._status = None
        self._cloud_server = None
        self._message = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if server_id is not None:
            self.server_id = server_id
        if server_name is not None:
            self.server_name = server_name
        if status is not None:
            self.status = status
        if cloud_server is not None:
            self.cloud_server = cloud_server
        if message is not None:
            self.message = message
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this DevServerTaskResponse.

        **参数解释**：task的ID。 **取值范围**：不涉及。

        :return: The id of this DevServerTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DevServerTaskResponse.

        **参数解释**：task的ID。 **取值范围**：不涉及。

        :param id: The id of this DevServerTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def server_id(self):
        r"""Gets the server_id of this DevServerTaskResponse.

        **参数解释**：devserver机器ID。 **取值范围**：不涉及。

        :return: The server_id of this DevServerTaskResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this DevServerTaskResponse.

        **参数解释**：devserver机器ID。 **取值范围**：不涉及。

        :param server_id: The server_id of this DevServerTaskResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def server_name(self):
        r"""Gets the server_name of this DevServerTaskResponse.

        **参数解释**：devserver机器名称。 **取值范围**：不涉及。

        :return: The server_name of this DevServerTaskResponse.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this DevServerTaskResponse.

        **参数解释**：devserver机器名称。 **取值范围**：不涉及。

        :param server_name: The server_name of this DevServerTaskResponse.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def status(self):
        r"""Gets the status of this DevServerTaskResponse.

        **参数解释**：task状态。 **取值范围**：- PROCESSING  -SUCCESS  - FAILED  - SKIPPED

        :return: The status of this DevServerTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DevServerTaskResponse.

        **参数解释**：task状态。 **取值范围**：- PROCESSING  -SUCCESS  - FAILED  - SKIPPED

        :param status: The status of this DevServerTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def cloud_server(self):
        r"""Gets the cloud_server of this DevServerTaskResponse.

        **参数解释**：底层ECS/BMS/HPS ID。

        :return: The cloud_server of this DevServerTaskResponse.
        :rtype: dict(str, str)
        """
        return self._cloud_server

    @cloud_server.setter
    def cloud_server(self, cloud_server):
        r"""Sets the cloud_server of this DevServerTaskResponse.

        **参数解释**：底层ECS/BMS/HPS ID。

        :param cloud_server: The cloud_server of this DevServerTaskResponse.
        :type cloud_server: dict(str, str)
        """
        self._cloud_server = cloud_server

    @property
    def message(self):
        r"""Gets the message of this DevServerTaskResponse.

        **参数解释**：输出信息。 **取值范围**：不涉及。

        :return: The message of this DevServerTaskResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this DevServerTaskResponse.

        **参数解释**：输出信息。 **取值范围**：不涉及。

        :param message: The message of this DevServerTaskResponse.
        :type message: str
        """
        self._message = message

    @property
    def create_at(self):
        r"""Gets the create_at of this DevServerTaskResponse.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :return: The create_at of this DevServerTaskResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this DevServerTaskResponse.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :param create_at: The create_at of this DevServerTaskResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this DevServerTaskResponse.

        **参数解释**：更新时间。 **取值范围**：不涉及。

        :return: The update_at of this DevServerTaskResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this DevServerTaskResponse.

        **参数解释**：更新时间。 **取值范围**：不涉及。

        :param update_at: The update_at of this DevServerTaskResponse.
        :type update_at: str
        """
        self._update_at = update_at

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DevServerTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
