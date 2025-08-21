# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryForksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'order_by': 'str',
        'sort': 'str',
        'view': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'order_by': 'order_by',
        'sort': 'sort',
        'view': 'view'
    }

    def __init__(self, repository_id=None, order_by=None, sort=None, view=None):
        r"""ListRepositoryForksRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param order_by: **参数解释：**  排序字段。 **约束限制：**  必须为枚举值中的选项。 **取值范围：**  - created_at，创建时间。 - updated_at，更新时间。 **默认取值：**  created_at。
        :type order_by: str
        :param sort: **参数解释：** 排列顺序。 **约束限制：** 必须为枚举值中的选项。 **取值范围：**  - asc - desc **默认取值：** desc。
        :type sort: str
        :param view: **参数解释：**  视图。 **约束限制：**  必须为枚举值中的选项。 **取值范围：**  - basic，基本信息。  - least，最简信息。 **默认取值：**  least。
        :type view: str
        """
        
        

        self._repository_id = None
        self._order_by = None
        self._sort = None
        self._view = None
        self.discriminator = None

        self.repository_id = repository_id
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort
        if view is not None:
            self.view = view

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListRepositoryForksRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListRepositoryForksRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListRepositoryForksRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListRepositoryForksRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def order_by(self):
        r"""Gets the order_by of this ListRepositoryForksRequest.

        **参数解释：**  排序字段。 **约束限制：**  必须为枚举值中的选项。 **取值范围：**  - created_at，创建时间。 - updated_at，更新时间。 **默认取值：**  created_at。

        :return: The order_by of this ListRepositoryForksRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListRepositoryForksRequest.

        **参数解释：**  排序字段。 **约束限制：**  必须为枚举值中的选项。 **取值范围：**  - created_at，创建时间。 - updated_at，更新时间。 **默认取值：**  created_at。

        :param order_by: The order_by of this ListRepositoryForksRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListRepositoryForksRequest.

        **参数解释：** 排列顺序。 **约束限制：** 必须为枚举值中的选项。 **取值范围：**  - asc - desc **默认取值：** desc。

        :return: The sort of this ListRepositoryForksRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListRepositoryForksRequest.

        **参数解释：** 排列顺序。 **约束限制：** 必须为枚举值中的选项。 **取值范围：**  - asc - desc **默认取值：** desc。

        :param sort: The sort of this ListRepositoryForksRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def view(self):
        r"""Gets the view of this ListRepositoryForksRequest.

        **参数解释：**  视图。 **约束限制：**  必须为枚举值中的选项。 **取值范围：**  - basic，基本信息。  - least，最简信息。 **默认取值：**  least。

        :return: The view of this ListRepositoryForksRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ListRepositoryForksRequest.

        **参数解释：**  视图。 **约束限制：**  必须为枚举值中的选项。 **取值范围：**  - basic，基本信息。  - least，最简信息。 **默认取值：**  least。

        :param view: The view of this ListRepositoryForksRequest.
        :type view: str
        """
        self._view = view

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListRepositoryForksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
