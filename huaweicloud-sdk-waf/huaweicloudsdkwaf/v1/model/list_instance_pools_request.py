# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancePoolsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'page': 'int',
        'pagesize': 'int',
        'name': 'str',
        'type': 'list[str]',
        'vpc_id': 'str',
        'detail': 'bool'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'page': 'page',
        'pagesize': 'pagesize',
        'name': 'name',
        'type': 'type',
        'vpc_id': 'vpc_id',
        'detail': 'detail'
    }

    def __init__(self, enterprise_project_id=None, page=None, pagesize=None, name=None, type=None, vpc_id=None, detail=None):
        r"""ListInstancePoolsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0
        :type enterprise_project_id: str
        :param page: **参数解释：** 分页查询时，返回第几页数据 **约束限制：** 不涉及 **取值范围：** page参数的实际有效范围取决于总数据量和pagesize的取值，不能大于总页数 **默认取值：** 1
        :type page: int
        :param pagesize: **参数解释：** 分页查询时，每页包含的结果条数 **约束限制：** 不涉及 **取值范围：** [0,100] **默认取值：** 10
        :type pagesize: int
        :param name: **参数解释：** 模糊查询，实例组名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param type: **参数解释：** 实例组类型 **约束限制：** 不涉及 **取值范围：** - elb 基础elb类型 - elb-v2 elb-v2类型 - elb-container -容器化elb类型 - elb-shadow saas化elb类型 - standard-container 反向代理独享引擎组（云内，承载租户专用） - standard-cloud 反向代理独享引擎组（云内） - standard 反向代理独享引擎组（云外） - detector-cloud 旁路检测独享引擎组（云内） - detector 旁路检测独享引擎组（云外） - standard-maf-cloud 大模型防火墙实例组类型 **默认取值：** 不涉及
        :type type: list[str]
        :param vpc_id: **参数解释：** 实例组关联的vpc_id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type vpc_id: str
        :param detail: **参数解释：** 是否查询实例组详细信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type detail: bool
        """
        
        

        self._enterprise_project_id = None
        self._page = None
        self._pagesize = None
        self._name = None
        self._type = None
        self._vpc_id = None
        self._detail = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if detail is not None:
            self.detail = detail

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListInstancePoolsRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0

        :return: The enterprise_project_id of this ListInstancePoolsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListInstancePoolsRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0

        :param enterprise_project_id: The enterprise_project_id of this ListInstancePoolsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def page(self):
        r"""Gets the page of this ListInstancePoolsRequest.

        **参数解释：** 分页查询时，返回第几页数据 **约束限制：** 不涉及 **取值范围：** page参数的实际有效范围取决于总数据量和pagesize的取值，不能大于总页数 **默认取值：** 1

        :return: The page of this ListInstancePoolsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListInstancePoolsRequest.

        **参数解释：** 分页查询时，返回第几页数据 **约束限制：** 不涉及 **取值范围：** page参数的实际有效范围取决于总数据量和pagesize的取值，不能大于总页数 **默认取值：** 1

        :param page: The page of this ListInstancePoolsRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        r"""Gets the pagesize of this ListInstancePoolsRequest.

        **参数解释：** 分页查询时，每页包含的结果条数 **约束限制：** 不涉及 **取值范围：** [0,100] **默认取值：** 10

        :return: The pagesize of this ListInstancePoolsRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        r"""Sets the pagesize of this ListInstancePoolsRequest.

        **参数解释：** 分页查询时，每页包含的结果条数 **约束限制：** 不涉及 **取值范围：** [0,100] **默认取值：** 10

        :param pagesize: The pagesize of this ListInstancePoolsRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

    @property
    def name(self):
        r"""Gets the name of this ListInstancePoolsRequest.

        **参数解释：** 模糊查询，实例组名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this ListInstancePoolsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstancePoolsRequest.

        **参数解释：** 模糊查询，实例组名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this ListInstancePoolsRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ListInstancePoolsRequest.

        **参数解释：** 实例组类型 **约束限制：** 不涉及 **取值范围：** - elb 基础elb类型 - elb-v2 elb-v2类型 - elb-container -容器化elb类型 - elb-shadow saas化elb类型 - standard-container 反向代理独享引擎组（云内，承载租户专用） - standard-cloud 反向代理独享引擎组（云内） - standard 反向代理独享引擎组（云外） - detector-cloud 旁路检测独享引擎组（云内） - detector 旁路检测独享引擎组（云外） - standard-maf-cloud 大模型防火墙实例组类型 **默认取值：** 不涉及

        :return: The type of this ListInstancePoolsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListInstancePoolsRequest.

        **参数解释：** 实例组类型 **约束限制：** 不涉及 **取值范围：** - elb 基础elb类型 - elb-v2 elb-v2类型 - elb-container -容器化elb类型 - elb-shadow saas化elb类型 - standard-container 反向代理独享引擎组（云内，承载租户专用） - standard-cloud 反向代理独享引擎组（云内） - standard 反向代理独享引擎组（云外） - detector-cloud 旁路检测独享引擎组（云内） - detector 旁路检测独享引擎组（云外） - standard-maf-cloud 大模型防火墙实例组类型 **默认取值：** 不涉及

        :param type: The type of this ListInstancePoolsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListInstancePoolsRequest.

        **参数解释：** 实例组关联的vpc_id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The vpc_id of this ListInstancePoolsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListInstancePoolsRequest.

        **参数解释：** 实例组关联的vpc_id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param vpc_id: The vpc_id of this ListInstancePoolsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def detail(self):
        r"""Gets the detail of this ListInstancePoolsRequest.

        **参数解释：** 是否查询实例组详细信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The detail of this ListInstancePoolsRequest.
        :rtype: bool
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this ListInstancePoolsRequest.

        **参数解释：** 是否查询实例组详细信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param detail: The detail of this ListInstancePoolsRequest.
        :type detail: bool
        """
        self._detail = detail

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
        if not isinstance(other, ListInstancePoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
