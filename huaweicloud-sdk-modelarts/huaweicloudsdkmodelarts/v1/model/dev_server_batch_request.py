# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevServerBatchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'servers': 'list[BatchActionDevServerIds]',
        'extend_param': 'ServerOsRequest'
    }

    attribute_map = {
        'type': 'type',
        'servers': 'servers',
        'extend_param': 'extend_param'
    }

    def __init__(self, type=None, servers=None, extend_param=None):
        r"""DevServerBatchRequest

        The model defined in huaweicloud sdk

        :param type: **参数解释**：批量操作类型。 **约束限制**：不涉及。 **取值范围**： - START：批量启动Lite Server实例 - STOP：批量停止Lite Server实例 - REBOOT：批量重启Lite Server实例 - CHANGEOS：批量切换Lite Server服务器操作系统镜像 - REINSTALLOS：批量重装Lite Server服务器操作系统镜像 - DELETE：批量删除Lite Server实例 **默认取值**：不涉及。
        :type type: str
        :param servers: **参数解释**：批量操作Lite Server ID列表。
        :type servers: list[:class:`huaweicloudsdkmodelarts.v1.BatchActionDevServerIds`]
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkmodelarts.v1.ServerOsRequest`
        """
        
        

        self._type = None
        self._servers = None
        self._extend_param = None
        self.discriminator = None

        self.type = type
        self.servers = servers
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def type(self):
        r"""Gets the type of this DevServerBatchRequest.

        **参数解释**：批量操作类型。 **约束限制**：不涉及。 **取值范围**： - START：批量启动Lite Server实例 - STOP：批量停止Lite Server实例 - REBOOT：批量重启Lite Server实例 - CHANGEOS：批量切换Lite Server服务器操作系统镜像 - REINSTALLOS：批量重装Lite Server服务器操作系统镜像 - DELETE：批量删除Lite Server实例 **默认取值**：不涉及。

        :return: The type of this DevServerBatchRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DevServerBatchRequest.

        **参数解释**：批量操作类型。 **约束限制**：不涉及。 **取值范围**： - START：批量启动Lite Server实例 - STOP：批量停止Lite Server实例 - REBOOT：批量重启Lite Server实例 - CHANGEOS：批量切换Lite Server服务器操作系统镜像 - REINSTALLOS：批量重装Lite Server服务器操作系统镜像 - DELETE：批量删除Lite Server实例 **默认取值**：不涉及。

        :param type: The type of this DevServerBatchRequest.
        :type type: str
        """
        self._type = type

    @property
    def servers(self):
        r"""Gets the servers of this DevServerBatchRequest.

        **参数解释**：批量操作Lite Server ID列表。

        :return: The servers of this DevServerBatchRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.BatchActionDevServerIds`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this DevServerBatchRequest.

        **参数解释**：批量操作Lite Server ID列表。

        :param servers: The servers of this DevServerBatchRequest.
        :type servers: list[:class:`huaweicloudsdkmodelarts.v1.BatchActionDevServerIds`]
        """
        self._servers = servers

    @property
    def extend_param(self):
        r"""Gets the extend_param of this DevServerBatchRequest.

        :return: The extend_param of this DevServerBatchRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServerOsRequest`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this DevServerBatchRequest.

        :param extend_param: The extend_param of this DevServerBatchRequest.
        :type extend_param: :class:`huaweicloudsdkmodelarts.v1.ServerOsRequest`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, DevServerBatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
