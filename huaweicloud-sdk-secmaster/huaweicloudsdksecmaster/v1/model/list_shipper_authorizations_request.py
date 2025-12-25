# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShipperAuthorizationsRequest:

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
        'workspace_id': 'str',
        'source_region': 'str',
        'destination_shipper_type': 'str',
        'shipper_status': 'str',
        'auth_status': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'source_region': 'source_region',
        'destination_shipper_type': 'destination_shipper_type',
        'shipper_status': 'shipper_status',
        'auth_status': 'auth_status',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, project_id=None, workspace_id=None, source_region=None, destination_shipper_type=None, shipper_status=None, auth_status=None, limit=None, offset=None):
        r"""ListShipperAuthorizationsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param source_region: 数据源
        :type source_region: str
        :param destination_shipper_type: 目的投递类型
        :type destination_shipper_type: str
        :param shipper_status: 数据投递状态
        :type shipper_status: str
        :param auth_status: 授权状态
        :type auth_status: str
        :param limit: 每页数量
        :type limit: int
        :param offset: 第几页
        :type offset: int
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._source_region = None
        self._destination_shipper_type = None
        self._shipper_status = None
        self._auth_status = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if source_region is not None:
            self.source_region = source_region
        if destination_shipper_type is not None:
            self.destination_shipper_type = destination_shipper_type
        if shipper_status is not None:
            self.shipper_status = shipper_status
        if auth_status is not None:
            self.auth_status = auth_status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def project_id(self):
        r"""Gets the project_id of this ListShipperAuthorizationsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListShipperAuthorizationsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListShipperAuthorizationsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListShipperAuthorizationsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListShipperAuthorizationsRequest.

        工作空间ID

        :return: The workspace_id of this ListShipperAuthorizationsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListShipperAuthorizationsRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListShipperAuthorizationsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def source_region(self):
        r"""Gets the source_region of this ListShipperAuthorizationsRequest.

        数据源

        :return: The source_region of this ListShipperAuthorizationsRequest.
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        r"""Sets the source_region of this ListShipperAuthorizationsRequest.

        数据源

        :param source_region: The source_region of this ListShipperAuthorizationsRequest.
        :type source_region: str
        """
        self._source_region = source_region

    @property
    def destination_shipper_type(self):
        r"""Gets the destination_shipper_type of this ListShipperAuthorizationsRequest.

        目的投递类型

        :return: The destination_shipper_type of this ListShipperAuthorizationsRequest.
        :rtype: str
        """
        return self._destination_shipper_type

    @destination_shipper_type.setter
    def destination_shipper_type(self, destination_shipper_type):
        r"""Sets the destination_shipper_type of this ListShipperAuthorizationsRequest.

        目的投递类型

        :param destination_shipper_type: The destination_shipper_type of this ListShipperAuthorizationsRequest.
        :type destination_shipper_type: str
        """
        self._destination_shipper_type = destination_shipper_type

    @property
    def shipper_status(self):
        r"""Gets the shipper_status of this ListShipperAuthorizationsRequest.

        数据投递状态

        :return: The shipper_status of this ListShipperAuthorizationsRequest.
        :rtype: str
        """
        return self._shipper_status

    @shipper_status.setter
    def shipper_status(self, shipper_status):
        r"""Sets the shipper_status of this ListShipperAuthorizationsRequest.

        数据投递状态

        :param shipper_status: The shipper_status of this ListShipperAuthorizationsRequest.
        :type shipper_status: str
        """
        self._shipper_status = shipper_status

    @property
    def auth_status(self):
        r"""Gets the auth_status of this ListShipperAuthorizationsRequest.

        授权状态

        :return: The auth_status of this ListShipperAuthorizationsRequest.
        :rtype: str
        """
        return self._auth_status

    @auth_status.setter
    def auth_status(self, auth_status):
        r"""Sets the auth_status of this ListShipperAuthorizationsRequest.

        授权状态

        :param auth_status: The auth_status of this ListShipperAuthorizationsRequest.
        :type auth_status: str
        """
        self._auth_status = auth_status

    @property
    def limit(self):
        r"""Gets the limit of this ListShipperAuthorizationsRequest.

        每页数量

        :return: The limit of this ListShipperAuthorizationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListShipperAuthorizationsRequest.

        每页数量

        :param limit: The limit of this ListShipperAuthorizationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListShipperAuthorizationsRequest.

        第几页

        :return: The offset of this ListShipperAuthorizationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListShipperAuthorizationsRequest.

        第几页

        :param offset: The offset of this ListShipperAuthorizationsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListShipperAuthorizationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
