# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceConfigurationModifyHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'entity_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'entity_id': 'entity_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, entity_id=None, offset=None, limit=None):
        r"""ShowInstanceConfigurationModifyHistoryRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param entity_id: 实例ID或组ID或节点ID。可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。
        :type entity_id: str
        :param offset: 索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询个数上限值。 - 取值范围: 1~100。 - 不传该参数时，默认查询前100条信息。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._entity_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.entity_id = entity_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceConfigurationModifyHistoryRequest.

        实例ID。

        :return: The instance_id of this ShowInstanceConfigurationModifyHistoryRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceConfigurationModifyHistoryRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowInstanceConfigurationModifyHistoryRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def entity_id(self):
        r"""Gets the entity_id of this ShowInstanceConfigurationModifyHistoryRequest.

        实例ID或组ID或节点ID。可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The entity_id of this ShowInstanceConfigurationModifyHistoryRequest.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this ShowInstanceConfigurationModifyHistoryRequest.

        实例ID或组ID或节点ID。可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param entity_id: The entity_id of this ShowInstanceConfigurationModifyHistoryRequest.
        :type entity_id: str
        """
        self._entity_id = entity_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowInstanceConfigurationModifyHistoryRequest.

        索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。

        :return: The offset of this ShowInstanceConfigurationModifyHistoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowInstanceConfigurationModifyHistoryRequest.

        索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。

        :param offset: The offset of this ShowInstanceConfigurationModifyHistoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowInstanceConfigurationModifyHistoryRequest.

        查询个数上限值。 - 取值范围: 1~100。 - 不传该参数时，默认查询前100条信息。

        :return: The limit of this ShowInstanceConfigurationModifyHistoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowInstanceConfigurationModifyHistoryRequest.

        查询个数上限值。 - 取值范围: 1~100。 - 不传该参数时，默认查询前100条信息。

        :param limit: The limit of this ShowInstanceConfigurationModifyHistoryRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowInstanceConfigurationModifyHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
