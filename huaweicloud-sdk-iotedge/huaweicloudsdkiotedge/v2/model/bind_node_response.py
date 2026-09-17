# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindNodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'type': 'str',
        'subsystem_count': 'int',
        'resource_type': 'str',
        'resource_spec_type': 'str',
        'associated_edge_node_id': 'str',
        'associated_edge_node_name': 'str',
        'extend_params': 'str',
        'resource_size': 'int'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'type': 'type',
        'subsystem_count': 'subsystem_count',
        'resource_type': 'resource_type',
        'resource_spec_type': 'resource_spec_type',
        'associated_edge_node_id': 'associated_edge_node_id',
        'associated_edge_node_name': 'associated_edge_node_name',
        'extend_params': 'extend_params',
        'resource_size': 'resource_size'
    }

    def __init__(self, resource_id=None, type=None, subsystem_count=None, resource_type=None, resource_spec_type=None, associated_edge_node_id=None, associated_edge_node_name=None, extend_params=None, resource_size=None):
        r"""BindNodeResponse

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID
        :type resource_id: str
        :param type: 资源类型：industry|campus
        :type type: str
        :param subsystem_count: 对接的子系统数量
        :type subsystem_count: int
        :param resource_type: CBC上注册的资源类型编码。
        :type resource_type: str
        :param resource_spec_type: CBC上注册的资源类型编码。
        :type resource_spec_type: str
        :param associated_edge_node_id: 关联的边缘节点ID
        :type associated_edge_node_id: str
        :param associated_edge_node_name: 关联的边缘节点名称
        :type associated_edge_node_name: str
        :param extend_params: 扩展开通参数。
        :type extend_params: str
        :param resource_size: 资源容量大小，线性产品使用
        :type resource_size: int
        """
        
        super().__init__()

        self._resource_id = None
        self._type = None
        self._subsystem_count = None
        self._resource_type = None
        self._resource_spec_type = None
        self._associated_edge_node_id = None
        self._associated_edge_node_name = None
        self._extend_params = None
        self._resource_size = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if type is not None:
            self.type = type
        if subsystem_count is not None:
            self.subsystem_count = subsystem_count
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_type is not None:
            self.resource_spec_type = resource_spec_type
        if associated_edge_node_id is not None:
            self.associated_edge_node_id = associated_edge_node_id
        if associated_edge_node_name is not None:
            self.associated_edge_node_name = associated_edge_node_name
        if extend_params is not None:
            self.extend_params = extend_params
        if resource_size is not None:
            self.resource_size = resource_size

    @property
    def resource_id(self):
        r"""Gets the resource_id of this BindNodeResponse.

        资源ID

        :return: The resource_id of this BindNodeResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this BindNodeResponse.

        资源ID

        :param resource_id: The resource_id of this BindNodeResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def type(self):
        r"""Gets the type of this BindNodeResponse.

        资源类型：industry|campus

        :return: The type of this BindNodeResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BindNodeResponse.

        资源类型：industry|campus

        :param type: The type of this BindNodeResponse.
        :type type: str
        """
        self._type = type

    @property
    def subsystem_count(self):
        r"""Gets the subsystem_count of this BindNodeResponse.

        对接的子系统数量

        :return: The subsystem_count of this BindNodeResponse.
        :rtype: int
        """
        return self._subsystem_count

    @subsystem_count.setter
    def subsystem_count(self, subsystem_count):
        r"""Sets the subsystem_count of this BindNodeResponse.

        对接的子系统数量

        :param subsystem_count: The subsystem_count of this BindNodeResponse.
        :type subsystem_count: int
        """
        self._subsystem_count = subsystem_count

    @property
    def resource_type(self):
        r"""Gets the resource_type of this BindNodeResponse.

        CBC上注册的资源类型编码。

        :return: The resource_type of this BindNodeResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this BindNodeResponse.

        CBC上注册的资源类型编码。

        :param resource_type: The resource_type of this BindNodeResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_type(self):
        r"""Gets the resource_spec_type of this BindNodeResponse.

        CBC上注册的资源类型编码。

        :return: The resource_spec_type of this BindNodeResponse.
        :rtype: str
        """
        return self._resource_spec_type

    @resource_spec_type.setter
    def resource_spec_type(self, resource_spec_type):
        r"""Sets the resource_spec_type of this BindNodeResponse.

        CBC上注册的资源类型编码。

        :param resource_spec_type: The resource_spec_type of this BindNodeResponse.
        :type resource_spec_type: str
        """
        self._resource_spec_type = resource_spec_type

    @property
    def associated_edge_node_id(self):
        r"""Gets the associated_edge_node_id of this BindNodeResponse.

        关联的边缘节点ID

        :return: The associated_edge_node_id of this BindNodeResponse.
        :rtype: str
        """
        return self._associated_edge_node_id

    @associated_edge_node_id.setter
    def associated_edge_node_id(self, associated_edge_node_id):
        r"""Sets the associated_edge_node_id of this BindNodeResponse.

        关联的边缘节点ID

        :param associated_edge_node_id: The associated_edge_node_id of this BindNodeResponse.
        :type associated_edge_node_id: str
        """
        self._associated_edge_node_id = associated_edge_node_id

    @property
    def associated_edge_node_name(self):
        r"""Gets the associated_edge_node_name of this BindNodeResponse.

        关联的边缘节点名称

        :return: The associated_edge_node_name of this BindNodeResponse.
        :rtype: str
        """
        return self._associated_edge_node_name

    @associated_edge_node_name.setter
    def associated_edge_node_name(self, associated_edge_node_name):
        r"""Sets the associated_edge_node_name of this BindNodeResponse.

        关联的边缘节点名称

        :param associated_edge_node_name: The associated_edge_node_name of this BindNodeResponse.
        :type associated_edge_node_name: str
        """
        self._associated_edge_node_name = associated_edge_node_name

    @property
    def extend_params(self):
        r"""Gets the extend_params of this BindNodeResponse.

        扩展开通参数。

        :return: The extend_params of this BindNodeResponse.
        :rtype: str
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this BindNodeResponse.

        扩展开通参数。

        :param extend_params: The extend_params of this BindNodeResponse.
        :type extend_params: str
        """
        self._extend_params = extend_params

    @property
    def resource_size(self):
        r"""Gets the resource_size of this BindNodeResponse.

        资源容量大小，线性产品使用

        :return: The resource_size of this BindNodeResponse.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this BindNodeResponse.

        资源容量大小，线性产品使用

        :param resource_size: The resource_size of this BindNodeResponse.
        :type resource_size: int
        """
        self._resource_size = resource_size

    def to_dict(self):
        import warnings
        warnings.warn("BindNodeResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, BindNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
