# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectionsAllInstancesRequest:

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
        'instance_id': 'str',
        'vpc_id': 'str',
        'virsubnet_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance_id': 'instance_id',
        'vpc_id': 'vpc_id',
        'virsubnet_id': 'virsubnet_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, id=None, name=None, instance_id=None, vpc_id=None, virsubnet_id=None, limit=None, marker=None):
        r"""ListConnectionsAllInstancesRequest

        The model defined in huaweicloud sdk

        :param id: - 参数解释：二层连接资源ID。二层连接创建成功后，会生成一个ID，是二层连接对应的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type id: str
        :param name: - 参数解释：二层连接的名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type name: str
        :param instance_id: - 参数解释：ESW资源ID。ESW创建成功后，会生成一个ESW ID，是ESW对应的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type instance_id: str
        :param vpc_id: - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type vpc_id: str
        :param virsubnet_id: - 参数解释：二层连接关联的二层子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type virsubnet_id: str
        :param limit: - 参数解释：分页查询每页返回的记录个数。 - 约束限制：limit需要和marker配合使用，详细规则请见marker的参数说明。 - 取值范围：0~2^31-1。 - 默认取值：2000。
        :type limit: int
        :param marker: - 参数解释：分页查询的起始资源ID，表示从指定资源的下一条记录开始查询。 - 约束限制：marker需要和limit配合使用。   - 若不传入marker和limit参数，查询结果返回第一页全部资源记录。   - 若不传入marker参数，limit为10，查询结果返回第1~10条资源记录。   - 若marker为第10条记录的资源ID，limit为10，查询结果返回第11~20条资源记录。   - 若marker为第10条记录的资源ID，不传入limit参数，查询结果返回第11~2000条（limit默认值2000）资源记录。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type marker: str
        """
        
        

        self._id = None
        self._name = None
        self._instance_id = None
        self._vpc_id = None
        self._virsubnet_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListConnectionsAllInstancesRequest.

        - 参数解释：二层连接资源ID。二层连接创建成功后，会生成一个ID，是二层连接对应的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The id of this ListConnectionsAllInstancesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListConnectionsAllInstancesRequest.

        - 参数解释：二层连接资源ID。二层连接创建成功后，会生成一个ID，是二层连接对应的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param id: The id of this ListConnectionsAllInstancesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListConnectionsAllInstancesRequest.

        - 参数解释：二层连接的名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The name of this ListConnectionsAllInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListConnectionsAllInstancesRequest.

        - 参数解释：二层连接的名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param name: The name of this ListConnectionsAllInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListConnectionsAllInstancesRequest.

        - 参数解释：ESW资源ID。ESW创建成功后，会生成一个ESW ID，是ESW对应的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The instance_id of this ListConnectionsAllInstancesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListConnectionsAllInstancesRequest.

        - 参数解释：ESW资源ID。ESW创建成功后，会生成一个ESW ID，是ESW对应的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param instance_id: The instance_id of this ListConnectionsAllInstancesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListConnectionsAllInstancesRequest.

        - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The vpc_id of this ListConnectionsAllInstancesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListConnectionsAllInstancesRequest.

        - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param vpc_id: The vpc_id of this ListConnectionsAllInstancesRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this ListConnectionsAllInstancesRequest.

        - 参数解释：二层连接关联的二层子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The virsubnet_id of this ListConnectionsAllInstancesRequest.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this ListConnectionsAllInstancesRequest.

        - 参数解释：二层连接关联的二层子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param virsubnet_id: The virsubnet_id of this ListConnectionsAllInstancesRequest.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def limit(self):
        r"""Gets the limit of this ListConnectionsAllInstancesRequest.

        - 参数解释：分页查询每页返回的记录个数。 - 约束限制：limit需要和marker配合使用，详细规则请见marker的参数说明。 - 取值范围：0~2^31-1。 - 默认取值：2000。

        :return: The limit of this ListConnectionsAllInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListConnectionsAllInstancesRequest.

        - 参数解释：分页查询每页返回的记录个数。 - 约束限制：limit需要和marker配合使用，详细规则请见marker的参数说明。 - 取值范围：0~2^31-1。 - 默认取值：2000。

        :param limit: The limit of this ListConnectionsAllInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListConnectionsAllInstancesRequest.

        - 参数解释：分页查询的起始资源ID，表示从指定资源的下一条记录开始查询。 - 约束限制：marker需要和limit配合使用。   - 若不传入marker和limit参数，查询结果返回第一页全部资源记录。   - 若不传入marker参数，limit为10，查询结果返回第1~10条资源记录。   - 若marker为第10条记录的资源ID，limit为10，查询结果返回第11~20条资源记录。   - 若marker为第10条记录的资源ID，不传入limit参数，查询结果返回第11~2000条（limit默认值2000）资源记录。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The marker of this ListConnectionsAllInstancesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListConnectionsAllInstancesRequest.

        - 参数解释：分页查询的起始资源ID，表示从指定资源的下一条记录开始查询。 - 约束限制：marker需要和limit配合使用。   - 若不传入marker和limit参数，查询结果返回第一页全部资源记录。   - 若不传入marker参数，limit为10，查询结果返回第1~10条资源记录。   - 若marker为第10条记录的资源ID，limit为10，查询结果返回第11~20条资源记录。   - 若marker为第10条记录的资源ID，不传入limit参数，查询结果返回第11~2000条（limit默认值2000）资源记录。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param marker: The marker of this ListConnectionsAllInstancesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListConnectionsAllInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
