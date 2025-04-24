# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'name': 'str',
        'instance_id': 'str',
        'status': 'str',
        'include_failure': 'str',
        'exact_match_name': 'str',
        'enterprise_project_id': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'name': 'name',
        'instance_id': 'instance_id',
        'status': 'status',
        'include_failure': 'include_failure',
        'exact_match_name': 'exact_match_name',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, engine=None, name=None, instance_id=None, status=None, include_failure=None, exact_match_name=None, enterprise_project_id=None, offset=None, limit=None):
        r"""ListInstancesDetailsRequest

        The model defined in huaweicloud sdk

        :param engine: **参数解释**： 引擎类型：rabbitmq。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type engine: str
        :param name: **参数解释**： 实例名称。获取方式：登录RabbitMQ控制台，在RabbitMQ实例详情页面查找实例名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param instance_id: **参数解释**： 实例ID。获取方法如下：登录RabbitMQ控制台，在RabbitMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: str
        :param status: **参数解释**： 实例状态，[详细状态说明请参考[实例状态说明](rabbitmq-api-180514012.xml)](tag:hws,hws_eu,hws_hk,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm)[详细状态说明请参考[实例状态说明](kafka-api-180514012.xml)](tag:hcs)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type status: str
        :param include_failure: **参数解释**： 是否返回创建失败的实例数。 **约束限制**： 不涉及。 **取值范围**： - true：返回创建失败的实例数。 - false：不返回创建失败的实例数。  **默认取值**： 不涉及。
        :type include_failure: str
        :param exact_match_name: **参数解释**： 是否按照实例名称进行精确匹配查询。 **约束限制**： 不涉及。 **取值范围**： - true：按照实例名称进行精确匹配查询。 - false：按照模糊匹配实例名称查询。  **默认取值**： false
        :type exact_match_name: str
        :param enterprise_project_id: **参数解释**： 企业项目ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type enterprise_project_id: str
        :param offset: **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 不涉及。
        :type offset: str
        :param limit: **参数解释**： 当次查询返回的最大实例个数。 **约束限制**： 不涉及。 **取值范围**： 1~50 **默认取值**： 10
        :type limit: str
        """
        
        

        self._engine = None
        self._name = None
        self._instance_id = None
        self._status = None
        self._include_failure = None
        self._exact_match_name = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.engine = engine
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if include_failure is not None:
            self.include_failure = include_failure
        if exact_match_name is not None:
            self.exact_match_name = exact_match_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def engine(self):
        r"""Gets the engine of this ListInstancesDetailsRequest.

        **参数解释**： 引擎类型：rabbitmq。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The engine of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListInstancesDetailsRequest.

        **参数解释**： 引擎类型：rabbitmq。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param engine: The engine of this ListInstancesDetailsRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def name(self):
        r"""Gets the name of this ListInstancesDetailsRequest.

        **参数解释**： 实例名称。获取方式：登录RabbitMQ控制台，在RabbitMQ实例详情页面查找实例名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstancesDetailsRequest.

        **参数解释**： 实例名称。获取方式：登录RabbitMQ控制台，在RabbitMQ实例详情页面查找实例名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this ListInstancesDetailsRequest.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstancesDetailsRequest.

        **参数解释**： 实例ID。获取方法如下：登录RabbitMQ控制台，在RabbitMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstancesDetailsRequest.

        **参数解释**： 实例ID。获取方法如下：登录RabbitMQ控制台，在RabbitMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this ListInstancesDetailsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this ListInstancesDetailsRequest.

        **参数解释**： 实例状态，[详细状态说明请参考[实例状态说明](rabbitmq-api-180514012.xml)](tag:hws,hws_eu,hws_hk,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm)[详细状态说明请参考[实例状态说明](kafka-api-180514012.xml)](tag:hcs)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The status of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListInstancesDetailsRequest.

        **参数解释**： 实例状态，[详细状态说明请参考[实例状态说明](rabbitmq-api-180514012.xml)](tag:hws,hws_eu,hws_hk,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm)[详细状态说明请参考[实例状态说明](kafka-api-180514012.xml)](tag:hcs)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param status: The status of this ListInstancesDetailsRequest.
        :type status: str
        """
        self._status = status

    @property
    def include_failure(self):
        r"""Gets the include_failure of this ListInstancesDetailsRequest.

        **参数解释**： 是否返回创建失败的实例数。 **约束限制**： 不涉及。 **取值范围**： - true：返回创建失败的实例数。 - false：不返回创建失败的实例数。  **默认取值**： 不涉及。

        :return: The include_failure of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._include_failure

    @include_failure.setter
    def include_failure(self, include_failure):
        r"""Sets the include_failure of this ListInstancesDetailsRequest.

        **参数解释**： 是否返回创建失败的实例数。 **约束限制**： 不涉及。 **取值范围**： - true：返回创建失败的实例数。 - false：不返回创建失败的实例数。  **默认取值**： 不涉及。

        :param include_failure: The include_failure of this ListInstancesDetailsRequest.
        :type include_failure: str
        """
        self._include_failure = include_failure

    @property
    def exact_match_name(self):
        r"""Gets the exact_match_name of this ListInstancesDetailsRequest.

        **参数解释**： 是否按照实例名称进行精确匹配查询。 **约束限制**： 不涉及。 **取值范围**： - true：按照实例名称进行精确匹配查询。 - false：按照模糊匹配实例名称查询。  **默认取值**： false

        :return: The exact_match_name of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._exact_match_name

    @exact_match_name.setter
    def exact_match_name(self, exact_match_name):
        r"""Sets the exact_match_name of this ListInstancesDetailsRequest.

        **参数解释**： 是否按照实例名称进行精确匹配查询。 **约束限制**： 不涉及。 **取值范围**： - true：按照实例名称进行精确匹配查询。 - false：按照模糊匹配实例名称查询。  **默认取值**： false

        :param exact_match_name: The exact_match_name of this ListInstancesDetailsRequest.
        :type exact_match_name: str
        """
        self._exact_match_name = exact_match_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListInstancesDetailsRequest.

        **参数解释**： 企业项目ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The enterprise_project_id of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListInstancesDetailsRequest.

        **参数解释**： 企业项目ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this ListInstancesDetailsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstancesDetailsRequest.

        **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 不涉及。

        :return: The offset of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstancesDetailsRequest.

        **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 不涉及。

        :param offset: The offset of this ListInstancesDetailsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstancesDetailsRequest.

        **参数解释**： 当次查询返回的最大实例个数。 **约束限制**： 不涉及。 **取值范围**： 1~50 **默认取值**： 10

        :return: The limit of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstancesDetailsRequest.

        **参数解释**： 当次查询返回的最大实例个数。 **约束限制**： 不涉及。 **取值范围**： 1~50 **默认取值**： 10

        :param limit: The limit of this ListInstancesDetailsRequest.
        :type limit: str
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
        if not isinstance(other, ListInstancesDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
