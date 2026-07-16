# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferDeploymentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'sort_key': 'str',
        'status': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int',
        'delete_after': 'int'
    }

    attribute_map = {
        'service_id': 'service_id',
        'sort_key': 'sort_key',
        'status': 'status',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset',
        'delete_after': 'delete_after'
    }

    def __init__(self, service_id=None, sort_key=None, status=None, sort_dir=None, limit=None, offset=None, delete_after=None):
        r"""ListInferDeploymentsRequest

        The model defined in huaweicloud sdk

        :param service_id: **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。
        :type service_id: str
        :param sort_key: **参数解释：** 排序字段，多个字段以\&quot;,\&quot;分隔，支持create_at, update_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。
        :type sort_key: str
        :param status: **参数解释：** 当取值为all时查询包含指定天数内已删除的部署，与delete_after同时使用；当取值为空或非all时进查询未删除的部署。 **约束限制：** 不涉及。 **取值范围：** - all：查询包含已删除。 **默认取值：** 空。
        :type status: str
        :param sort_dir: **参数解释：** 排序方式 **约束限制：** 不涉及。 **取值范围：** - ASC: 递增排序。 - DESC: 递减排序。 **默认取值：** DESC。
        :type sort_dir: str
        :param limit: **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。
        :type limit: int
        :param offset: **参数解释：** 分页列表查询的偏移量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。
        :type offset: int
        :param delete_after: **参数解释：** 表示查询包含指定天数内已删除的部署，与status同时使用，仅当status取值为all时生效。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 7
        :type delete_after: int
        """
        
        

        self._service_id = None
        self._sort_key = None
        self._status = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self._delete_after = None
        self.discriminator = None

        self.service_id = service_id
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if delete_after is not None:
            self.delete_after = delete_after

    @property
    def service_id(self):
        r"""Gets the service_id of this ListInferDeploymentsRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :return: The service_id of this ListInferDeploymentsRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ListInferDeploymentsRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :param service_id: The service_id of this ListInferDeploymentsRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListInferDeploymentsRequest.

        **参数解释：** 排序字段，多个字段以\",\"分隔，支持create_at, update_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。

        :return: The sort_key of this ListInferDeploymentsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListInferDeploymentsRequest.

        **参数解释：** 排序字段，多个字段以\",\"分隔，支持create_at, update_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。

        :param sort_key: The sort_key of this ListInferDeploymentsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        r"""Gets the status of this ListInferDeploymentsRequest.

        **参数解释：** 当取值为all时查询包含指定天数内已删除的部署，与delete_after同时使用；当取值为空或非all时进查询未删除的部署。 **约束限制：** 不涉及。 **取值范围：** - all：查询包含已删除。 **默认取值：** 空。

        :return: The status of this ListInferDeploymentsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListInferDeploymentsRequest.

        **参数解释：** 当取值为all时查询包含指定天数内已删除的部署，与delete_after同时使用；当取值为空或非all时进查询未删除的部署。 **约束限制：** 不涉及。 **取值范围：** - all：查询包含已删除。 **默认取值：** 空。

        :param status: The status of this ListInferDeploymentsRequest.
        :type status: str
        """
        self._status = status

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListInferDeploymentsRequest.

        **参数解释：** 排序方式 **约束限制：** 不涉及。 **取值范围：** - ASC: 递增排序。 - DESC: 递减排序。 **默认取值：** DESC。

        :return: The sort_dir of this ListInferDeploymentsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListInferDeploymentsRequest.

        **参数解释：** 排序方式 **约束限制：** 不涉及。 **取值范围：** - ASC: 递增排序。 - DESC: 递减排序。 **默认取值：** DESC。

        :param sort_dir: The sort_dir of this ListInferDeploymentsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListInferDeploymentsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :return: The limit of this ListInferDeploymentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInferDeploymentsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :param limit: The limit of this ListInferDeploymentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInferDeploymentsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。

        :return: The offset of this ListInferDeploymentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInferDeploymentsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。

        :param offset: The offset of this ListInferDeploymentsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def delete_after(self):
        r"""Gets the delete_after of this ListInferDeploymentsRequest.

        **参数解释：** 表示查询包含指定天数内已删除的部署，与status同时使用，仅当status取值为all时生效。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 7

        :return: The delete_after of this ListInferDeploymentsRequest.
        :rtype: int
        """
        return self._delete_after

    @delete_after.setter
    def delete_after(self, delete_after):
        r"""Sets the delete_after of this ListInferDeploymentsRequest.

        **参数解释：** 表示查询包含指定天数内已删除的部署，与status同时使用，仅当status取值为all时生效。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 7

        :param delete_after: The delete_after of this ListInferDeploymentsRequest.
        :type delete_after: int
        """
        self._delete_after = delete_after

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
        if not isinstance(other, ListInferDeploymentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
