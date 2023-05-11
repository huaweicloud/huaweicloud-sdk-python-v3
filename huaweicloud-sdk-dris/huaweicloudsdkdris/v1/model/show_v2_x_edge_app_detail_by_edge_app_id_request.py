# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowV2XEdgeAppDetailByEdgeAppIdRequest:

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
        'instance_id': 'str',
        'v2x_edge_id': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'instance_id': 'Instance-Id',
        'v2x_edge_id': 'v2x_edge_id'
    }

    def __init__(self, edge_app_id=None, instance_id=None, v2x_edge_id=None):
        """ShowV2XEdgeAppDetailByEdgeAppIdRequest

        The model defined in huaweicloud sdk

        :param edge_app_id: **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。
        :type edge_app_id: str
        :param instance_id: **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。
        :type instance_id: str
        :param v2x_edge_id: **参数说明**：Edge ID，用于唯一标识一个Edge，创建Edge后获得。方法参见 [创建Edge](https://support.huaweicloud.com/api-v2x/v2x_04_0078.html)。
        :type v2x_edge_id: str
        """
        
        

        self._edge_app_id = None
        self._instance_id = None
        self._v2x_edge_id = None
        self.discriminator = None

        self.edge_app_id = edge_app_id
        if instance_id is not None:
            self.instance_id = instance_id
        self.v2x_edge_id = v2x_edge_id

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.

        **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。

        :return: The edge_app_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.

        **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。

        :param edge_app_id: The edge_app_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.

        **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。

        :return: The instance_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.

        **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。

        :param instance_id: The instance_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def v2x_edge_id(self):
        """Gets the v2x_edge_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.

        **参数说明**：Edge ID，用于唯一标识一个Edge，创建Edge后获得。方法参见 [创建Edge](https://support.huaweicloud.com/api-v2x/v2x_04_0078.html)。

        :return: The v2x_edge_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.
        :rtype: str
        """
        return self._v2x_edge_id

    @v2x_edge_id.setter
    def v2x_edge_id(self, v2x_edge_id):
        """Sets the v2x_edge_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.

        **参数说明**：Edge ID，用于唯一标识一个Edge，创建Edge后获得。方法参见 [创建Edge](https://support.huaweicloud.com/api-v2x/v2x_04_0078.html)。

        :param v2x_edge_id: The v2x_edge_id of this ShowV2XEdgeAppDetailByEdgeAppIdRequest.
        :type v2x_edge_id: str
        """
        self._v2x_edge_id = v2x_edge_id

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
        if not isinstance(other, ShowV2XEdgeAppDetailByEdgeAppIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
