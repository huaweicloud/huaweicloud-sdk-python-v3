# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeApplicationVersionStateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'edge_app_id': 'str',
        'version': 'str',
        'body': 'UpdateEdgeAppVersionStateDTO'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'edge_app_id': 'edge_app_id',
        'version': 'version',
        'body': 'body'
    }

    def __init__(self, instance_id=None, edge_app_id=None, version=None, body=None):
        r"""UpdateEdgeApplicationVersionStateRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。
        :type instance_id: str
        :param edge_app_id: **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。
        :type edge_app_id: str
        :param version: **参数说明**：应用版本，应用内版本唯一。
        :type version: str
        :param body: Body of the UpdateEdgeApplicationVersionStateRequest
        :type body: :class:`huaweicloudsdkdris.v1.UpdateEdgeAppVersionStateDTO`
        """
        
        

        self._instance_id = None
        self._edge_app_id = None
        self._version = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.edge_app_id = edge_app_id
        self.version = version
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateEdgeApplicationVersionStateRequest.

        **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。

        :return: The instance_id of this UpdateEdgeApplicationVersionStateRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateEdgeApplicationVersionStateRequest.

        **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。

        :param instance_id: The instance_id of this UpdateEdgeApplicationVersionStateRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def edge_app_id(self):
        r"""Gets the edge_app_id of this UpdateEdgeApplicationVersionStateRequest.

        **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。

        :return: The edge_app_id of this UpdateEdgeApplicationVersionStateRequest.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        r"""Sets the edge_app_id of this UpdateEdgeApplicationVersionStateRequest.

        **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。

        :param edge_app_id: The edge_app_id of this UpdateEdgeApplicationVersionStateRequest.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def version(self):
        r"""Gets the version of this UpdateEdgeApplicationVersionStateRequest.

        **参数说明**：应用版本，应用内版本唯一。

        :return: The version of this UpdateEdgeApplicationVersionStateRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateEdgeApplicationVersionStateRequest.

        **参数说明**：应用版本，应用内版本唯一。

        :param version: The version of this UpdateEdgeApplicationVersionStateRequest.
        :type version: str
        """
        self._version = version

    @property
    def body(self):
        r"""Gets the body of this UpdateEdgeApplicationVersionStateRequest.

        :return: The body of this UpdateEdgeApplicationVersionStateRequest.
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateEdgeAppVersionStateDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateEdgeApplicationVersionStateRequest.

        :param body: The body of this UpdateEdgeApplicationVersionStateRequest.
        :type body: :class:`huaweicloudsdkdris.v1.UpdateEdgeAppVersionStateDTO`
        """
        self._body = body

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
        if not isinstance(other, UpdateEdgeApplicationVersionStateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
