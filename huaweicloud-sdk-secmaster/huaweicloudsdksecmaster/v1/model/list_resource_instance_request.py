# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'resource_type': 'str',
        'limit': 'str',
        'offset': 'str',
        'body': 'QueryResourceInstanceRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'resource_type': 'resource_type',
        'limit': 'limit',
        'offset': 'offset',
        'body': 'body'
    }

    def __init__(self, project_id=None, resource_type=None, limit=None, offset=None, body=None):
        r"""ListResourceInstanceRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param limit: 查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1
        :type limit: str
        :param offset: 索引位置，偏移量（action为count时无此参数）从第一条数据偏移offset条数据后开始查询，如果action为filter默认为0（偏移0条数据，表示从第一条数据开始查询）,必须为数字，不能为负数
        :type offset: str
        :param body: Body of the ListResourceInstanceRequest
        :type body: :class:`huaweicloudsdksecmaster.v1.QueryResourceInstanceRequestBody`
        """
        
        

        self._project_id = None
        self._resource_type = None
        self._limit = None
        self._offset = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.resource_type = resource_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this ListResourceInstanceRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListResourceInstanceRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListResourceInstanceRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListResourceInstanceRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListResourceInstanceRequest.

        资源类型

        :return: The resource_type of this ListResourceInstanceRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListResourceInstanceRequest.

        资源类型

        :param resource_type: The resource_type of this ListResourceInstanceRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def limit(self):
        r"""Gets the limit of this ListResourceInstanceRequest.

        查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1

        :return: The limit of this ListResourceInstanceRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourceInstanceRequest.

        查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1

        :param limit: The limit of this ListResourceInstanceRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListResourceInstanceRequest.

        索引位置，偏移量（action为count时无此参数）从第一条数据偏移offset条数据后开始查询，如果action为filter默认为0（偏移0条数据，表示从第一条数据开始查询）,必须为数字，不能为负数

        :return: The offset of this ListResourceInstanceRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListResourceInstanceRequest.

        索引位置，偏移量（action为count时无此参数）从第一条数据偏移offset条数据后开始查询，如果action为filter默认为0（偏移0条数据，表示从第一条数据开始查询）,必须为数字，不能为负数

        :param offset: The offset of this ListResourceInstanceRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def body(self):
        r"""Gets the body of this ListResourceInstanceRequest.

        :return: The body of this ListResourceInstanceRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v1.QueryResourceInstanceRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListResourceInstanceRequest.

        :param body: The body of this ListResourceInstanceRequest.
        :type body: :class:`huaweicloudsdksecmaster.v1.QueryResourceInstanceRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ListResourceInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
