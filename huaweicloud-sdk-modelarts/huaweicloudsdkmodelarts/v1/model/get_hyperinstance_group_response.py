# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetHyperinstanceGroupResponse(SdkResponse):

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
        'npu_count_limit': 'str',
        'npu_count': 'str',
        'hyperinstance_cluster_id': 'str',
        'created_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'npu_count_limit': 'npu_count_limit',
        'npu_count': 'npu_count',
        'hyperinstance_cluster_id': 'hyperinstance_cluster_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, npu_count_limit=None, npu_count=None, hyperinstance_cluster_id=None, created_at=None, updated_at=None):
        r"""GetHyperinstanceGroupResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：hyperinstance-group ID。 **默认取值**：不涉及。
        :type id: str
        :param name: **参数解释**：hyperinstance-group名称。 **默认取值**：不涉及。
        :type name: str
        :param npu_count_limit: **参数解释**：npu数量限制。 **默认取值**：不涉及。
        :type npu_count_limit: str
        :param npu_count: **参数解释**：npu数量。 **默认取值**：不涉及。
        :type npu_count: str
        :param hyperinstance_cluster_id: **参数解释**：超节点集群ID。 **默认取值**：不涉及。
        :type hyperinstance_cluster_id: str
        :param created_at: **参数解释**：创建时间。 **默认取值**：不涉及。
        :type created_at: int
        :param updated_at: **参数解释**：更新时间。 **默认取值**：不涉及。
        :type updated_at: int
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._npu_count_limit = None
        self._npu_count = None
        self._hyperinstance_cluster_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if npu_count_limit is not None:
            self.npu_count_limit = npu_count_limit
        if npu_count is not None:
            self.npu_count = npu_count
        if hyperinstance_cluster_id is not None:
            self.hyperinstance_cluster_id = hyperinstance_cluster_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this GetHyperinstanceGroupResponse.

        **参数解释**：hyperinstance-group ID。 **默认取值**：不涉及。

        :return: The id of this GetHyperinstanceGroupResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetHyperinstanceGroupResponse.

        **参数解释**：hyperinstance-group ID。 **默认取值**：不涉及。

        :param id: The id of this GetHyperinstanceGroupResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GetHyperinstanceGroupResponse.

        **参数解释**：hyperinstance-group名称。 **默认取值**：不涉及。

        :return: The name of this GetHyperinstanceGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetHyperinstanceGroupResponse.

        **参数解释**：hyperinstance-group名称。 **默认取值**：不涉及。

        :param name: The name of this GetHyperinstanceGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def npu_count_limit(self):
        r"""Gets the npu_count_limit of this GetHyperinstanceGroupResponse.

        **参数解释**：npu数量限制。 **默认取值**：不涉及。

        :return: The npu_count_limit of this GetHyperinstanceGroupResponse.
        :rtype: str
        """
        return self._npu_count_limit

    @npu_count_limit.setter
    def npu_count_limit(self, npu_count_limit):
        r"""Sets the npu_count_limit of this GetHyperinstanceGroupResponse.

        **参数解释**：npu数量限制。 **默认取值**：不涉及。

        :param npu_count_limit: The npu_count_limit of this GetHyperinstanceGroupResponse.
        :type npu_count_limit: str
        """
        self._npu_count_limit = npu_count_limit

    @property
    def npu_count(self):
        r"""Gets the npu_count of this GetHyperinstanceGroupResponse.

        **参数解释**：npu数量。 **默认取值**：不涉及。

        :return: The npu_count of this GetHyperinstanceGroupResponse.
        :rtype: str
        """
        return self._npu_count

    @npu_count.setter
    def npu_count(self, npu_count):
        r"""Sets the npu_count of this GetHyperinstanceGroupResponse.

        **参数解释**：npu数量。 **默认取值**：不涉及。

        :param npu_count: The npu_count of this GetHyperinstanceGroupResponse.
        :type npu_count: str
        """
        self._npu_count = npu_count

    @property
    def hyperinstance_cluster_id(self):
        r"""Gets the hyperinstance_cluster_id of this GetHyperinstanceGroupResponse.

        **参数解释**：超节点集群ID。 **默认取值**：不涉及。

        :return: The hyperinstance_cluster_id of this GetHyperinstanceGroupResponse.
        :rtype: str
        """
        return self._hyperinstance_cluster_id

    @hyperinstance_cluster_id.setter
    def hyperinstance_cluster_id(self, hyperinstance_cluster_id):
        r"""Sets the hyperinstance_cluster_id of this GetHyperinstanceGroupResponse.

        **参数解释**：超节点集群ID。 **默认取值**：不涉及。

        :param hyperinstance_cluster_id: The hyperinstance_cluster_id of this GetHyperinstanceGroupResponse.
        :type hyperinstance_cluster_id: str
        """
        self._hyperinstance_cluster_id = hyperinstance_cluster_id

    @property
    def created_at(self):
        r"""Gets the created_at of this GetHyperinstanceGroupResponse.

        **参数解释**：创建时间。 **默认取值**：不涉及。

        :return: The created_at of this GetHyperinstanceGroupResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GetHyperinstanceGroupResponse.

        **参数解释**：创建时间。 **默认取值**：不涉及。

        :param created_at: The created_at of this GetHyperinstanceGroupResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GetHyperinstanceGroupResponse.

        **参数解释**：更新时间。 **默认取值**：不涉及。

        :return: The updated_at of this GetHyperinstanceGroupResponse.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GetHyperinstanceGroupResponse.

        **参数解释**：更新时间。 **默认取值**：不涉及。

        :param updated_at: The updated_at of this GetHyperinstanceGroupResponse.
        :type updated_at: int
        """
        self._updated_at = updated_at

    def to_dict(self):
        import warnings
        warnings.warn("GetHyperinstanceGroupResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetHyperinstanceGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
