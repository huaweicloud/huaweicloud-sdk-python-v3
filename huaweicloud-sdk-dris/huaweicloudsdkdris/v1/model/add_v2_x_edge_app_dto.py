# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddV2XEdgeAppDTO:

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
        'app_version': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'app_version': 'app_version'
    }

    def __init__(self, edge_app_id=None, app_version=None):
        """AddV2XEdgeAppDTO

        The model defined in huaweicloud sdk

        :param edge_app_id: **参数说明**：用户自定义应用唯一ID，部署边缘应用前应先创建应用，方法参见：[创建应用](https://support.huaweicloud.com/api-v2x/v2x_04_0026.html)。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。
        :type edge_app_id: str
        :param app_version: **参数说明**：应用版本，部署边缘应用版本前应先创建应用版本并发布，创建应用版本方法参见：[创建应用](https://support.huaweicloud.com/api-v2x/v2x_04_0038.html)，发布应用版本方法参见：[更新应用版本状态](https://support.huaweicloud.com/api-v2x/v2x_04_0105.html)。  **取值范围**：只允许小写字母、数字、连接符（-）、点（.）的组合且要以小写字母或数字开头和结尾。
        :type app_version: str
        """
        
        

        self._edge_app_id = None
        self._app_version = None
        self.discriminator = None

        self.edge_app_id = edge_app_id
        self.app_version = app_version

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this AddV2XEdgeAppDTO.

        **参数说明**：用户自定义应用唯一ID，部署边缘应用前应先创建应用，方法参见：[创建应用](https://support.huaweicloud.com/api-v2x/v2x_04_0026.html)。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。

        :return: The edge_app_id of this AddV2XEdgeAppDTO.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this AddV2XEdgeAppDTO.

        **参数说明**：用户自定义应用唯一ID，部署边缘应用前应先创建应用，方法参见：[创建应用](https://support.huaweicloud.com/api-v2x/v2x_04_0026.html)。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。

        :param edge_app_id: The edge_app_id of this AddV2XEdgeAppDTO.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def app_version(self):
        """Gets the app_version of this AddV2XEdgeAppDTO.

        **参数说明**：应用版本，部署边缘应用版本前应先创建应用版本并发布，创建应用版本方法参见：[创建应用](https://support.huaweicloud.com/api-v2x/v2x_04_0038.html)，发布应用版本方法参见：[更新应用版本状态](https://support.huaweicloud.com/api-v2x/v2x_04_0105.html)。  **取值范围**：只允许小写字母、数字、连接符（-）、点（.）的组合且要以小写字母或数字开头和结尾。

        :return: The app_version of this AddV2XEdgeAppDTO.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this AddV2XEdgeAppDTO.

        **参数说明**：应用版本，部署边缘应用版本前应先创建应用版本并发布，创建应用版本方法参见：[创建应用](https://support.huaweicloud.com/api-v2x/v2x_04_0038.html)，发布应用版本方法参见：[更新应用版本状态](https://support.huaweicloud.com/api-v2x/v2x_04_0105.html)。  **取值范围**：只允许小写字母、数字、连接符（-）、点（.）的组合且要以小写字母或数字开头和结尾。

        :param app_version: The app_version of this AddV2XEdgeAppDTO.
        :type app_version: str
        """
        self._app_version = app_version

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
        if not isinstance(other, AddV2XEdgeAppDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
