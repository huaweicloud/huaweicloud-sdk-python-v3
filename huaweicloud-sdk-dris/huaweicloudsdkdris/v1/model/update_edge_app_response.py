# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeAppResponse(SdkResponse):

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
        'description': 'str',
        'created_time': 'str',
        'last_modified_time': 'str',
        'last_published_version': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'description': 'description',
        'created_time': 'created_time',
        'last_modified_time': 'last_modified_time',
        'last_published_version': 'last_published_version'
    }

    def __init__(self, edge_app_id=None, description=None, created_time=None, last_modified_time=None, last_published_version=None):
        """UpdateEdgeAppResponse

        The model defined in huaweicloud sdk

        :param edge_app_id: **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。
        :type edge_app_id: str
        :param description: **参数说明**：应用描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文引号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。
        :type description: str
        :param created_time: **参数说明**：创建时间。
        :type created_time: str
        :param last_modified_time: **参数说明**：更新时间。
        :type last_modified_time: str
        :param last_published_version: **参数说明**：最新发布版本。
        :type last_published_version: str
        """
        
        super(UpdateEdgeAppResponse, self).__init__()

        self._edge_app_id = None
        self._description = None
        self._created_time = None
        self._last_modified_time = None
        self._last_published_version = None
        self.discriminator = None

        if edge_app_id is not None:
            self.edge_app_id = edge_app_id
        if description is not None:
            self.description = description
        if created_time is not None:
            self.created_time = created_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if last_published_version is not None:
            self.last_published_version = last_published_version

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this UpdateEdgeAppResponse.

        **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。

        :return: The edge_app_id of this UpdateEdgeAppResponse.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this UpdateEdgeAppResponse.

        **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。

        :param edge_app_id: The edge_app_id of this UpdateEdgeAppResponse.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def description(self):
        """Gets the description of this UpdateEdgeAppResponse.

        **参数说明**：应用描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文引号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :return: The description of this UpdateEdgeAppResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateEdgeAppResponse.

        **参数说明**：应用描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文引号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :param description: The description of this UpdateEdgeAppResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_time(self):
        """Gets the created_time of this UpdateEdgeAppResponse.

        **参数说明**：创建时间。

        :return: The created_time of this UpdateEdgeAppResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UpdateEdgeAppResponse.

        **参数说明**：创建时间。

        :param created_time: The created_time of this UpdateEdgeAppResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this UpdateEdgeAppResponse.

        **参数说明**：更新时间。

        :return: The last_modified_time of this UpdateEdgeAppResponse.
        :rtype: str
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this UpdateEdgeAppResponse.

        **参数说明**：更新时间。

        :param last_modified_time: The last_modified_time of this UpdateEdgeAppResponse.
        :type last_modified_time: str
        """
        self._last_modified_time = last_modified_time

    @property
    def last_published_version(self):
        """Gets the last_published_version of this UpdateEdgeAppResponse.

        **参数说明**：最新发布版本。

        :return: The last_published_version of this UpdateEdgeAppResponse.
        :rtype: str
        """
        return self._last_published_version

    @last_published_version.setter
    def last_published_version(self, last_published_version):
        """Sets the last_published_version of this UpdateEdgeAppResponse.

        **参数说明**：最新发布版本。

        :param last_published_version: The last_published_version of this UpdateEdgeAppResponse.
        :type last_published_version: str
        """
        self._last_published_version = last_published_version

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
        if not isinstance(other, UpdateEdgeAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
