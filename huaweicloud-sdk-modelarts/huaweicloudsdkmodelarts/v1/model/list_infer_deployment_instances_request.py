# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferDeploymentInstancesRequest:

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
        'status': 'list[str]',
        'limit': 'int',
        'offset': 'str',
        'pod_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'limit': 'limit',
        'offset': 'offset',
        'pod_name': 'pod_name'
    }

    def __init__(self, id=None, name=None, status=None, limit=None, offset=None, pod_name=None):
        r"""ListInferDeploymentInstancesRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 服务唯一id
        :type id: str
        :param name: **参数解释：** 服务部署名字，可以为all
        :type name: str
        :param status: **参数解释：** 服务实例状态，一次支持多种状态筛选，多种状态以\&quot;,\&quot;连接，不能存在空格。默认不过滤。取值范围有4种RUNNING（运行中）、ERROR（错误）、INIT（初始化）、DELETED（已删除)。 **约束限制：** 不涉及。
        :type status: list[str]
        :param limit: **参数解释：** 指定每一页返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。
        :type limit: int
        :param offset: **参数解释：** 分页列表的起始页。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。
        :type offset: str
        :param pod_name: **参数解释：** pod名字。 **取值范围：** 不涉及。
        :type pod_name: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._limit = None
        self._offset = None
        self._pod_name = None
        self.discriminator = None

        self.id = id
        self.name = name
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if pod_name is not None:
            self.pod_name = pod_name

    @property
    def id(self):
        r"""Gets the id of this ListInferDeploymentInstancesRequest.

        **参数解释：** 服务唯一id

        :return: The id of this ListInferDeploymentInstancesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListInferDeploymentInstancesRequest.

        **参数解释：** 服务唯一id

        :param id: The id of this ListInferDeploymentInstancesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListInferDeploymentInstancesRequest.

        **参数解释：** 服务部署名字，可以为all

        :return: The name of this ListInferDeploymentInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInferDeploymentInstancesRequest.

        **参数解释：** 服务部署名字，可以为all

        :param name: The name of this ListInferDeploymentInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListInferDeploymentInstancesRequest.

        **参数解释：** 服务实例状态，一次支持多种状态筛选，多种状态以\",\"连接，不能存在空格。默认不过滤。取值范围有4种RUNNING（运行中）、ERROR（错误）、INIT（初始化）、DELETED（已删除)。 **约束限制：** 不涉及。

        :return: The status of this ListInferDeploymentInstancesRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListInferDeploymentInstancesRequest.

        **参数解释：** 服务实例状态，一次支持多种状态筛选，多种状态以\",\"连接，不能存在空格。默认不过滤。取值范围有4种RUNNING（运行中）、ERROR（错误）、INIT（初始化）、DELETED（已删除)。 **约束限制：** 不涉及。

        :param status: The status of this ListInferDeploymentInstancesRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def limit(self):
        r"""Gets the limit of this ListInferDeploymentInstancesRequest.

        **参数解释：** 指定每一页返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :return: The limit of this ListInferDeploymentInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInferDeploymentInstancesRequest.

        **参数解释：** 指定每一页返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :param limit: The limit of this ListInferDeploymentInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInferDeploymentInstancesRequest.

        **参数解释：** 分页列表的起始页。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。

        :return: The offset of this ListInferDeploymentInstancesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInferDeploymentInstancesRequest.

        **参数解释：** 分页列表的起始页。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。

        :param offset: The offset of this ListInferDeploymentInstancesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ListInferDeploymentInstancesRequest.

        **参数解释：** pod名字。 **取值范围：** 不涉及。

        :return: The pod_name of this ListInferDeploymentInstancesRequest.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ListInferDeploymentInstancesRequest.

        **参数解释：** pod名字。 **取值范围：** 不涉及。

        :param pod_name: The pod_name of this ListInferDeploymentInstancesRequest.
        :type pod_name: str
        """
        self._pod_name = pod_name

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
        if not isinstance(other, ListInferDeploymentInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
