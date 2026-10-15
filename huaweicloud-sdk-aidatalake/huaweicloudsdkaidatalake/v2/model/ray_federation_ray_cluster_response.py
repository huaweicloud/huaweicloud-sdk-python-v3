# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayFederationRayClusterResponse:

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
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, status=None):
        r"""RayFederationRayClusterResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：RayCluster端点ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。
        :type id: str
        :param name: **参数解释**：RayCluster端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。
        :type name: str
        :param status: **参数解释**：RayCluster端点状态。 **取值范围**：   - CREATING：创建中。   - RUNNING：运行中。   - CREATE_FAILED：创建失败。   - DELETING：删除中。   - DELETED：已删除。   - UPDATING：更新中。   - UPDATE_FAILED：更新失败。   - DELETE_FAILED：删除失败。   - FROZEN：冻结。   - INACTIVE：未激活。   - ON_DEMAND_FROZEN：按需冻结。   - ABNORMAL：异常。
        :type status: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this RayFederationRayClusterResponse.

        **参数解释**：RayCluster端点ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。

        :return: The id of this RayFederationRayClusterResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RayFederationRayClusterResponse.

        **参数解释**：RayCluster端点ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。

        :param id: The id of this RayFederationRayClusterResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RayFederationRayClusterResponse.

        **参数解释**：RayCluster端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。

        :return: The name of this RayFederationRayClusterResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RayFederationRayClusterResponse.

        **参数解释**：RayCluster端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。

        :param name: The name of this RayFederationRayClusterResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this RayFederationRayClusterResponse.

        **参数解释**：RayCluster端点状态。 **取值范围**：   - CREATING：创建中。   - RUNNING：运行中。   - CREATE_FAILED：创建失败。   - DELETING：删除中。   - DELETED：已删除。   - UPDATING：更新中。   - UPDATE_FAILED：更新失败。   - DELETE_FAILED：删除失败。   - FROZEN：冻结。   - INACTIVE：未激活。   - ON_DEMAND_FROZEN：按需冻结。   - ABNORMAL：异常。

        :return: The status of this RayFederationRayClusterResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RayFederationRayClusterResponse.

        **参数解释**：RayCluster端点状态。 **取值范围**：   - CREATING：创建中。   - RUNNING：运行中。   - CREATE_FAILED：创建失败。   - DELETING：删除中。   - DELETED：已删除。   - UPDATING：更新中。   - UPDATE_FAILED：更新失败。   - DELETE_FAILED：删除失败。   - FROZEN：冻结。   - INACTIVE：未激活。   - ON_DEMAND_FROZEN：按需冻结。   - ABNORMAL：异常。

        :param status: The status of this RayFederationRayClusterResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, RayFederationRayClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
