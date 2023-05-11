# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeApplicationVersionStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'version': 'str',
        'description': 'str',
        'created_time': 'str',
        'last_modified_time': 'str',
        'state': 'str',
        'publish_time': 'str',
        'off_shelf_time': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'version': 'version',
        'description': 'description',
        'created_time': 'created_time',
        'last_modified_time': 'last_modified_time',
        'state': 'state',
        'publish_time': 'publish_time',
        'off_shelf_time': 'off_shelf_time'
    }

    def __init__(self, edge_app_id=None, version=None, description=None, created_time=None, last_modified_time=None, state=None, publish_time=None, off_shelf_time=None):
        """UpdateEdgeApplicationVersionStateResponse

        The model defined in huaweicloud sdk

        :param edge_app_id: **参数说明**：用户自定义应用唯一ID。
        :type edge_app_id: str
        :param version: **参数说明**：应用版本。
        :type version: str
        :param description: **参数说明**：应用描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文引号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。
        :type description: str
        :param created_time: **参数说明**：创建时间。
        :type created_time: str
        :param last_modified_time: **参数说明**：最后一次修改时间。
        :type last_modified_time: str
        :param state: **参数说明**：应用版本状态。  **取值范围**：  - DRAFT：草稿  - PUBLISHED：发布  - OFF_SHELF：下线
        :type state: str
        :param publish_time: **参数说明**：发布时间。
        :type publish_time: str
        :param off_shelf_time: **参数说明**：下线时间。
        :type off_shelf_time: str
        """
        
        super(UpdateEdgeApplicationVersionStateResponse, self).__init__()

        self._edge_app_id = None
        self._version = None
        self._description = None
        self._created_time = None
        self._last_modified_time = None
        self._state = None
        self._publish_time = None
        self._off_shelf_time = None
        self.discriminator = None

        if edge_app_id is not None:
            self.edge_app_id = edge_app_id
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if created_time is not None:
            self.created_time = created_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if state is not None:
            self.state = state
        if publish_time is not None:
            self.publish_time = publish_time
        if off_shelf_time is not None:
            self.off_shelf_time = off_shelf_time

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：用户自定义应用唯一ID。

        :return: The edge_app_id of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：用户自定义应用唯一ID。

        :param edge_app_id: The edge_app_id of this UpdateEdgeApplicationVersionStateResponse.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def version(self):
        """Gets the version of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：应用版本。

        :return: The version of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：应用版本。

        :param version: The version of this UpdateEdgeApplicationVersionStateResponse.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        """Gets the description of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：应用描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文引号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :return: The description of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：应用描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文引号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :param description: The description of this UpdateEdgeApplicationVersionStateResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_time(self):
        """Gets the created_time of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：创建时间。

        :return: The created_time of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：创建时间。

        :param created_time: The created_time of this UpdateEdgeApplicationVersionStateResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：最后一次修改时间。

        :return: The last_modified_time of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：最后一次修改时间。

        :param last_modified_time: The last_modified_time of this UpdateEdgeApplicationVersionStateResponse.
        :type last_modified_time: str
        """
        self._last_modified_time = last_modified_time

    @property
    def state(self):
        """Gets the state of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：应用版本状态。  **取值范围**：  - DRAFT：草稿  - PUBLISHED：发布  - OFF_SHELF：下线

        :return: The state of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：应用版本状态。  **取值范围**：  - DRAFT：草稿  - PUBLISHED：发布  - OFF_SHELF：下线

        :param state: The state of this UpdateEdgeApplicationVersionStateResponse.
        :type state: str
        """
        self._state = state

    @property
    def publish_time(self):
        """Gets the publish_time of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：发布时间。

        :return: The publish_time of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：发布时间。

        :param publish_time: The publish_time of this UpdateEdgeApplicationVersionStateResponse.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def off_shelf_time(self):
        """Gets the off_shelf_time of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：下线时间。

        :return: The off_shelf_time of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._off_shelf_time

    @off_shelf_time.setter
    def off_shelf_time(self, off_shelf_time):
        """Sets the off_shelf_time of this UpdateEdgeApplicationVersionStateResponse.

        **参数说明**：下线时间。

        :param off_shelf_time: The off_shelf_time of this UpdateEdgeApplicationVersionStateResponse.
        :type off_shelf_time: str
        """
        self._off_shelf_time = off_shelf_time

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
        if not isinstance(other, UpdateEdgeApplicationVersionStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
