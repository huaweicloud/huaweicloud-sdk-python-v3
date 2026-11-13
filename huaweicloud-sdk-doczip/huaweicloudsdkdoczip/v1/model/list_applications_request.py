# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'status': 'int',
        'application_name': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status',
        'application_name': 'application_name',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, offset=None, limit=None, status=None, application_name=None, tenant_id=None):
        r"""ListApplicationsRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释**： 页码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 1。
        :type offset: int
        :param limit: **参数解释**： 单页数量。 **约束限制**： 不涉及。 **取值范围**： [1-100]。 **默认取值**： 20。
        :type limit: int
        :param status: **参数解释**： 应用状态，不传入则返回全部未失效应用。 **约束限制**： 不涉及。 **取值范围**： - 0：待发布。 - 1：已发布，生效状态。 - 2：已发布，失效状态。 **默认取值**： 不涉及。
        :type status: int
        :param application_name: **参数解释**： 应用名称，不传入则返回全部未失效应用。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。
        :type application_name: str
        :param tenant_id: **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。
        :type tenant_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._status = None
        self._application_name = None
        self._tenant_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if application_name is not None:
            self.application_name = application_name
        self.tenant_id = tenant_id

    @property
    def offset(self):
        r"""Gets the offset of this ListApplicationsRequest.

        **参数解释**： 页码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 1。

        :return: The offset of this ListApplicationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListApplicationsRequest.

        **参数解释**： 页码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 1。

        :param offset: The offset of this ListApplicationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListApplicationsRequest.

        **参数解释**： 单页数量。 **约束限制**： 不涉及。 **取值范围**： [1-100]。 **默认取值**： 20。

        :return: The limit of this ListApplicationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListApplicationsRequest.

        **参数解释**： 单页数量。 **约束限制**： 不涉及。 **取值范围**： [1-100]。 **默认取值**： 20。

        :param limit: The limit of this ListApplicationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        r"""Gets the status of this ListApplicationsRequest.

        **参数解释**： 应用状态，不传入则返回全部未失效应用。 **约束限制**： 不涉及。 **取值范围**： - 0：待发布。 - 1：已发布，生效状态。 - 2：已发布，失效状态。 **默认取值**： 不涉及。

        :return: The status of this ListApplicationsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListApplicationsRequest.

        **参数解释**： 应用状态，不传入则返回全部未失效应用。 **约束限制**： 不涉及。 **取值范围**： - 0：待发布。 - 1：已发布，生效状态。 - 2：已发布，失效状态。 **默认取值**： 不涉及。

        :param status: The status of this ListApplicationsRequest.
        :type status: int
        """
        self._status = status

    @property
    def application_name(self):
        r"""Gets the application_name of this ListApplicationsRequest.

        **参数解释**： 应用名称，不传入则返回全部未失效应用。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :return: The application_name of this ListApplicationsRequest.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this ListApplicationsRequest.

        **参数解释**： 应用名称，不传入则返回全部未失效应用。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :param application_name: The application_name of this ListApplicationsRequest.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ListApplicationsRequest.

        **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。

        :return: The tenant_id of this ListApplicationsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ListApplicationsRequest.

        **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。

        :param tenant_id: The tenant_id of this ListApplicationsRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, ListApplicationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
