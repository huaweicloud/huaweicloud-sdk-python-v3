# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectConfigRequest:

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
        'region_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'csvc': 'str',
        'domain_id': 'str',
        'query_statistics': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'region_id': 'region_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'csvc': 'csvc',
        'domain_id': 'domain_id',
        'query_statistics': 'query_statistics'
    }

    def __init__(self, project_id=None, region_id=None, offset=None, limit=None, sort_key=None, sort_dir=None, csvc=None, domain_id=None, query_statistics=None):
        r"""ListCollectConfigRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param offset: 第几页
        :type offset: int
        :param limit: 每页数量
        :type limit: int
        :param sort_key: 排序字段
        :type sort_key: str
        :param sort_dir: 排序顺序
        :type sort_dir: str
        :param csvc: 云服务
        :type csvc: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param query_statistics: 是否查询云服务接入指标， 默认为 True
        :type query_statistics: bool
        """
        
        

        self._project_id = None
        self._region_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._csvc = None
        self._domain_id = None
        self._query_statistics = None
        self.discriminator = None

        self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if csvc is not None:
            self.csvc = csvc
        self.domain_id = domain_id
        if query_statistics is not None:
            self.query_statistics = query_statistics

    @property
    def project_id(self):
        r"""Gets the project_id of this ListCollectConfigRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListCollectConfigRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListCollectConfigRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListCollectConfigRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListCollectConfigRequest.

        区域ID

        :return: The region_id of this ListCollectConfigRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListCollectConfigRequest.

        区域ID

        :param region_id: The region_id of this ListCollectConfigRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCollectConfigRequest.

        第几页

        :return: The offset of this ListCollectConfigRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCollectConfigRequest.

        第几页

        :param offset: The offset of this ListCollectConfigRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCollectConfigRequest.

        每页数量

        :return: The limit of this ListCollectConfigRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCollectConfigRequest.

        每页数量

        :param limit: The limit of this ListCollectConfigRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListCollectConfigRequest.

        排序字段

        :return: The sort_key of this ListCollectConfigRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListCollectConfigRequest.

        排序字段

        :param sort_key: The sort_key of this ListCollectConfigRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListCollectConfigRequest.

        排序顺序

        :return: The sort_dir of this ListCollectConfigRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListCollectConfigRequest.

        排序顺序

        :param sort_dir: The sort_dir of this ListCollectConfigRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def csvc(self):
        r"""Gets the csvc of this ListCollectConfigRequest.

        云服务

        :return: The csvc of this ListCollectConfigRequest.
        :rtype: str
        """
        return self._csvc

    @csvc.setter
    def csvc(self, csvc):
        r"""Sets the csvc of this ListCollectConfigRequest.

        云服务

        :param csvc: The csvc of this ListCollectConfigRequest.
        :type csvc: str
        """
        self._csvc = csvc

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListCollectConfigRequest.

        账号ID

        :return: The domain_id of this ListCollectConfigRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListCollectConfigRequest.

        账号ID

        :param domain_id: The domain_id of this ListCollectConfigRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def query_statistics(self):
        r"""Gets the query_statistics of this ListCollectConfigRequest.

        是否查询云服务接入指标， 默认为 True

        :return: The query_statistics of this ListCollectConfigRequest.
        :rtype: bool
        """
        return self._query_statistics

    @query_statistics.setter
    def query_statistics(self, query_statistics):
        r"""Sets the query_statistics of this ListCollectConfigRequest.

        是否查询云服务接入指标， 默认为 True

        :param query_statistics: The query_statistics of this ListCollectConfigRequest.
        :type query_statistics: bool
        """
        self._query_statistics = query_statistics

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
        if not isinstance(other, ListCollectConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
