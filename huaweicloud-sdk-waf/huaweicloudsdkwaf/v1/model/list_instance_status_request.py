# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceStatusRequest:

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
        'instance_ids': 'list[str]',
        'run_status': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'page': 'page',
        'pagesize': 'pagesize',
        'instance_ids': 'instance_ids',
        'run_status': 'run_status'
    }

    def __init__(self, enterprise_project_id=None, page=None, pagesize=None, instance_ids=None, run_status=None):
        r"""ListInstanceStatusRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0
        :type enterprise_project_id: str
        :param page: **参数解释：** 分页查询时，返回第几页数据 **约束限制：** 不涉及 **取值范围：** page参数的实际有效范围取决于总数据量和pagesize的取值，不能大于总页数 **默认取值：** 1
        :type page: int
        :param pagesize: **参数解释：** 分页查询时，每页包含的结果条数 **约束限制：** 不涉及 **取值范围：** [0, 总数据量] **默认取值：** 10
        :type pagesize: int
        :param instance_ids: **参数解释：** 模糊查询，独享引擎名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type instance_ids: list[str]
        :param run_status: **参数解释：** 实例运行状态 **约束限制：** 不涉及 **取值范围：** - 0 创建中 - 1 运行中 - 2 删除中 - 3 已删除 - 4 创建失败 - 5 已冻结 - 6 异常 - 7 更新中 - 8 更新失败 **默认取值：** 不涉及
        :type run_status: int
        """
        
        

        self._enterprise_project_id = None
        self._page = None
        self._pagesize = None
        self._instance_ids = None
        self._run_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if run_status is not None:
            self.run_status = run_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListInstanceStatusRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0

        :return: The enterprise_project_id of this ListInstanceStatusRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListInstanceStatusRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0

        :param enterprise_project_id: The enterprise_project_id of this ListInstanceStatusRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def page(self):
        r"""Gets the page of this ListInstanceStatusRequest.

        **参数解释：** 分页查询时，返回第几页数据 **约束限制：** 不涉及 **取值范围：** page参数的实际有效范围取决于总数据量和pagesize的取值，不能大于总页数 **默认取值：** 1

        :return: The page of this ListInstanceStatusRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListInstanceStatusRequest.

        **参数解释：** 分页查询时，返回第几页数据 **约束限制：** 不涉及 **取值范围：** page参数的实际有效范围取决于总数据量和pagesize的取值，不能大于总页数 **默认取值：** 1

        :param page: The page of this ListInstanceStatusRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        r"""Gets the pagesize of this ListInstanceStatusRequest.

        **参数解释：** 分页查询时，每页包含的结果条数 **约束限制：** 不涉及 **取值范围：** [0, 总数据量] **默认取值：** 10

        :return: The pagesize of this ListInstanceStatusRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        r"""Sets the pagesize of this ListInstanceStatusRequest.

        **参数解释：** 分页查询时，每页包含的结果条数 **约束限制：** 不涉及 **取值范围：** [0, 总数据量] **默认取值：** 10

        :param pagesize: The pagesize of this ListInstanceStatusRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this ListInstanceStatusRequest.

        **参数解释：** 模糊查询，独享引擎名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The instance_ids of this ListInstanceStatusRequest.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this ListInstanceStatusRequest.

        **参数解释：** 模糊查询，独享引擎名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param instance_ids: The instance_ids of this ListInstanceStatusRequest.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def run_status(self):
        r"""Gets the run_status of this ListInstanceStatusRequest.

        **参数解释：** 实例运行状态 **约束限制：** 不涉及 **取值范围：** - 0 创建中 - 1 运行中 - 2 删除中 - 3 已删除 - 4 创建失败 - 5 已冻结 - 6 异常 - 7 更新中 - 8 更新失败 **默认取值：** 不涉及

        :return: The run_status of this ListInstanceStatusRequest.
        :rtype: int
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        r"""Sets the run_status of this ListInstanceStatusRequest.

        **参数解释：** 实例运行状态 **约束限制：** 不涉及 **取值范围：** - 0 创建中 - 1 运行中 - 2 删除中 - 3 已删除 - 4 创建失败 - 5 已冻结 - 6 异常 - 7 更新中 - 8 更新失败 **默认取值：** 不涉及

        :param run_status: The run_status of this ListInstanceStatusRequest.
        :type run_status: int
        """
        self._run_status = run_status

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
        if not isinstance(other, ListInstanceStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
