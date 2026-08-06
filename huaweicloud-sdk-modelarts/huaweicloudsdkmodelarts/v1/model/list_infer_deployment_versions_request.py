# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferDeploymentVersionsRequest:

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
        'deployment_id': 'str',
        'sort_key': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'service_id': 'service_id',
        'deployment_id': 'deployment_id',
        'sort_key': 'sort_key',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, service_id=None, deployment_id=None, sort_key=None, limit=None, offset=None):
        r"""ListInferDeploymentVersionsRequest

        The model defined in huaweicloud sdk

        :param service_id: **参数解释：** 服务ID，在创建服务时即可在返回体中获取，也可通过查询服务列表接口获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type service_id: str
        :param deployment_id: **参数解释：** 部署ID，在[添加部署](CreateInferDeployment.xml)时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其中deployment_id字段即为部署ID。 **约束限制：** 不涉及。 **取值范围：** 部署ID。 **默认取值：** 不涉及。
        :type deployment_id: str
        :param sort_key: **参数解释：** 排序字段。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。
        :type sort_key: str
        :param limit: **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。
        :type limit: int
        :param offset: **参数解释：** 分页列表查询的偏移量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。
        :type offset: int
        """
        
        

        self._service_id = None
        self._deployment_id = None
        self._sort_key = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.service_id = service_id
        self.deployment_id = deployment_id
        if sort_key is not None:
            self.sort_key = sort_key
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def service_id(self):
        r"""Gets the service_id of this ListInferDeploymentVersionsRequest.

        **参数解释：** 服务ID，在创建服务时即可在返回体中获取，也可通过查询服务列表接口获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The service_id of this ListInferDeploymentVersionsRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ListInferDeploymentVersionsRequest.

        **参数解释：** 服务ID，在创建服务时即可在返回体中获取，也可通过查询服务列表接口获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param service_id: The service_id of this ListInferDeploymentVersionsRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this ListInferDeploymentVersionsRequest.

        **参数解释：** 部署ID，在[添加部署](CreateInferDeployment.xml)时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其中deployment_id字段即为部署ID。 **约束限制：** 不涉及。 **取值范围：** 部署ID。 **默认取值：** 不涉及。

        :return: The deployment_id of this ListInferDeploymentVersionsRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this ListInferDeploymentVersionsRequest.

        **参数解释：** 部署ID，在[添加部署](CreateInferDeployment.xml)时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其中deployment_id字段即为部署ID。 **约束限制：** 不涉及。 **取值范围：** 部署ID。 **默认取值：** 不涉及。

        :param deployment_id: The deployment_id of this ListInferDeploymentVersionsRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListInferDeploymentVersionsRequest.

        **参数解释：** 排序字段。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。

        :return: The sort_key of this ListInferDeploymentVersionsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListInferDeploymentVersionsRequest.

        **参数解释：** 排序字段。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。

        :param sort_key: The sort_key of this ListInferDeploymentVersionsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def limit(self):
        r"""Gets the limit of this ListInferDeploymentVersionsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :return: The limit of this ListInferDeploymentVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInferDeploymentVersionsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :param limit: The limit of this ListInferDeploymentVersionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInferDeploymentVersionsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。

        :return: The offset of this ListInferDeploymentVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInferDeploymentVersionsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。

        :param offset: The offset of this ListInferDeploymentVersionsRequest.
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
        if not isinstance(other, ListInferDeploymentVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
