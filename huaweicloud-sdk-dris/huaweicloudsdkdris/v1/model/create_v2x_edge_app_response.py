# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateV2xEdgeAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'v2x_edge_id': 'str',
        'edge_app_id': 'str',
        'app_version': 'str',
        'status': 'str'
    }

    attribute_map = {
        'v2x_edge_id': 'v2x_edge_id',
        'edge_app_id': 'edge_app_id',
        'app_version': 'app_version',
        'status': 'status'
    }

    def __init__(self, v2x_edge_id=None, edge_app_id=None, app_version=None, status=None):
        r"""CreateV2xEdgeAppResponse

        The model defined in huaweicloud sdk

        :param v2x_edge_id: **参数说明**：Edge ID，用于唯一标识一个Edge。
        :type v2x_edge_id: str
        :param edge_app_id: **参数说明**：用户自定义应用唯一ID。
        :type edge_app_id: str
        :param app_version: **参数说明**：应用版本，比如1.0.0。
        :type app_version: str
        :param status: **参数说明**：应用部署状态。  **取值范围**：  - UNINSTALLED：待部署  - INSTALLED：部署中  - OFFLINE：离线  - ONLINE：在线  - UPGRADING：升级中  - DELETING：删除中  - RUNNING：运行中
        :type status: str
        """
        
        super(CreateV2xEdgeAppResponse, self).__init__()

        self._v2x_edge_id = None
        self._edge_app_id = None
        self._app_version = None
        self._status = None
        self.discriminator = None

        if v2x_edge_id is not None:
            self.v2x_edge_id = v2x_edge_id
        if edge_app_id is not None:
            self.edge_app_id = edge_app_id
        if app_version is not None:
            self.app_version = app_version
        if status is not None:
            self.status = status

    @property
    def v2x_edge_id(self):
        r"""Gets the v2x_edge_id of this CreateV2xEdgeAppResponse.

        **参数说明**：Edge ID，用于唯一标识一个Edge。

        :return: The v2x_edge_id of this CreateV2xEdgeAppResponse.
        :rtype: str
        """
        return self._v2x_edge_id

    @v2x_edge_id.setter
    def v2x_edge_id(self, v2x_edge_id):
        r"""Sets the v2x_edge_id of this CreateV2xEdgeAppResponse.

        **参数说明**：Edge ID，用于唯一标识一个Edge。

        :param v2x_edge_id: The v2x_edge_id of this CreateV2xEdgeAppResponse.
        :type v2x_edge_id: str
        """
        self._v2x_edge_id = v2x_edge_id

    @property
    def edge_app_id(self):
        r"""Gets the edge_app_id of this CreateV2xEdgeAppResponse.

        **参数说明**：用户自定义应用唯一ID。

        :return: The edge_app_id of this CreateV2xEdgeAppResponse.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        r"""Sets the edge_app_id of this CreateV2xEdgeAppResponse.

        **参数说明**：用户自定义应用唯一ID。

        :param edge_app_id: The edge_app_id of this CreateV2xEdgeAppResponse.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def app_version(self):
        r"""Gets the app_version of this CreateV2xEdgeAppResponse.

        **参数说明**：应用版本，比如1.0.0。

        :return: The app_version of this CreateV2xEdgeAppResponse.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this CreateV2xEdgeAppResponse.

        **参数说明**：应用版本，比如1.0.0。

        :param app_version: The app_version of this CreateV2xEdgeAppResponse.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def status(self):
        r"""Gets the status of this CreateV2xEdgeAppResponse.

        **参数说明**：应用部署状态。  **取值范围**：  - UNINSTALLED：待部署  - INSTALLED：部署中  - OFFLINE：离线  - ONLINE：在线  - UPGRADING：升级中  - DELETING：删除中  - RUNNING：运行中

        :return: The status of this CreateV2xEdgeAppResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateV2xEdgeAppResponse.

        **参数说明**：应用部署状态。  **取值范围**：  - UNINSTALLED：待部署  - INSTALLED：部署中  - OFFLINE：离线  - ONLINE：在线  - UPGRADING：升级中  - DELETING：删除中  - RUNNING：运行中

        :param status: The status of this CreateV2xEdgeAppResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, CreateV2xEdgeAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
