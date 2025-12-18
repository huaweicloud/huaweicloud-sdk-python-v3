# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListItemCommitsRequest:

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
        'item_id': 'str',
        'type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'item_id': 'item_id',
        'type': 'type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, item_id=None, type=None, offset=None, limit=None):
        r"""ListItemCommitsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[[查询项目列表](https://support.huaweicloud.com/eu/api-projectman/ListProjectsV4.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。
        :type project_id: str
        :param item_id: **参数解释：** 工作项Id。 **约束限制：** 不涉及  **取值范围：** 字符串长度不少于1，不超过128。
        :type item_id: str
        :param type: **参数解释：** 工作项关联的提交类型。 **约束限制：** 不涉及  **取值范围：** - commit，提交。 - branch，分支。 - mergerequest，合并请求。
        :type type: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._project_id = None
        self._item_id = None
        self._type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        self.item_id = item_id
        if type is not None:
            self.type = type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ListItemCommitsRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[[查询项目列表](https://support.huaweicloud.com/eu/api-projectman/ListProjectsV4.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :return: The project_id of this ListItemCommitsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListItemCommitsRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[[查询项目列表](https://support.huaweicloud.com/eu/api-projectman/ListProjectsV4.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :param project_id: The project_id of this ListItemCommitsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def item_id(self):
        r"""Gets the item_id of this ListItemCommitsRequest.

        **参数解释：** 工作项Id。 **约束限制：** 不涉及  **取值范围：** 字符串长度不少于1，不超过128。

        :return: The item_id of this ListItemCommitsRequest.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this ListItemCommitsRequest.

        **参数解释：** 工作项Id。 **约束限制：** 不涉及  **取值范围：** 字符串长度不少于1，不超过128。

        :param item_id: The item_id of this ListItemCommitsRequest.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def type(self):
        r"""Gets the type of this ListItemCommitsRequest.

        **参数解释：** 工作项关联的提交类型。 **约束限制：** 不涉及  **取值范围：** - commit，提交。 - branch，分支。 - mergerequest，合并请求。

        :return: The type of this ListItemCommitsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListItemCommitsRequest.

        **参数解释：** 工作项关联的提交类型。 **约束限制：** 不涉及  **取值范围：** - commit，提交。 - branch，分支。 - mergerequest，合并请求。

        :param type: The type of this ListItemCommitsRequest.
        :type type: str
        """
        self._type = type

    @property
    def offset(self):
        r"""Gets the offset of this ListItemCommitsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListItemCommitsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListItemCommitsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListItemCommitsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListItemCommitsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListItemCommitsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListItemCommitsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListItemCommitsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListItemCommitsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
