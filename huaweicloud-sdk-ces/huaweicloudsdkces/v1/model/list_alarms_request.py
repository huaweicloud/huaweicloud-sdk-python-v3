# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start': 'str',
        'limit': 'int',
        'order': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'start': 'start',
        'limit': 'limit',
        'order': 'order',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, start=None, limit=None, order=None, enterprise_project_id=None):
        r"""ListAlarmsRequest

        The model defined in huaweicloud sdk

        :param start: **参数解释**： 分页起始值，内容为alarm_id **约束限制**： 不涉及。 **取值范围**： 以al开头，后跟22位字母或数字。字符长度为24 **默认取值**： 不涉及。
        :type start: str
        :param limit: **参数解释**： 用于限制结果数据条数。 **约束限制**： 不涉及。 **取值范围**： 取值范围(0,100] **默认取值**： 默认值为100
        :type limit: int
        :param order: **参数解释**： 用于标识结果排序方法，按创建时间排序。 **约束限制**： 不涉及 **取值范围**： 枚举值： - asc：升序 - desc：降序 **默认取值**： desc
        :type order: str
        :param enterprise_project_id: **参数解释**： 企业项目ID，当查询所有企业项目时，配置为：all_granted_eps。 当需要查询某个企业项目时，配置为对应的企业项目ID，请参考获“[获取企业项目ID](ces_03_0061.xml)”。 **约束限制**： 不涉及。 **取值范围**： 只能包含小写字母、数字、“-”、“_”，长度为36个字符。也可取值0或all_granted_eps。0：代表默认企业项目ID，all_granted_eps：代表所有企业项目ID。 **默认取值**： all_granted_eps 
        :type enterprise_project_id: str
        """
        
        

        self._start = None
        self._limit = None
        self._order = None
        self._enterprise_project_id = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def start(self):
        r"""Gets the start of this ListAlarmsRequest.

        **参数解释**： 分页起始值，内容为alarm_id **约束限制**： 不涉及。 **取值范围**： 以al开头，后跟22位字母或数字。字符长度为24 **默认取值**： 不涉及。

        :return: The start of this ListAlarmsRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListAlarmsRequest.

        **参数解释**： 分页起始值，内容为alarm_id **约束限制**： 不涉及。 **取值范围**： 以al开头，后跟22位字母或数字。字符长度为24 **默认取值**： 不涉及。

        :param start: The start of this ListAlarmsRequest.
        :type start: str
        """
        self._start = start

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmsRequest.

        **参数解释**： 用于限制结果数据条数。 **约束限制**： 不涉及。 **取值范围**： 取值范围(0,100] **默认取值**： 默认值为100

        :return: The limit of this ListAlarmsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmsRequest.

        **参数解释**： 用于限制结果数据条数。 **约束限制**： 不涉及。 **取值范围**： 取值范围(0,100] **默认取值**： 默认值为100

        :param limit: The limit of this ListAlarmsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order(self):
        r"""Gets the order of this ListAlarmsRequest.

        **参数解释**： 用于标识结果排序方法，按创建时间排序。 **约束限制**： 不涉及 **取值范围**： 枚举值： - asc：升序 - desc：降序 **默认取值**： desc

        :return: The order of this ListAlarmsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListAlarmsRequest.

        **参数解释**： 用于标识结果排序方法，按创建时间排序。 **约束限制**： 不涉及 **取值范围**： 枚举值： - asc：升序 - desc：降序 **默认取值**： desc

        :param order: The order of this ListAlarmsRequest.
        :type order: str
        """
        self._order = order

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAlarmsRequest.

        **参数解释**： 企业项目ID，当查询所有企业项目时，配置为：all_granted_eps。 当需要查询某个企业项目时，配置为对应的企业项目ID，请参考获“[获取企业项目ID](ces_03_0061.xml)”。 **约束限制**： 不涉及。 **取值范围**： 只能包含小写字母、数字、“-”、“_”，长度为36个字符。也可取值0或all_granted_eps。0：代表默认企业项目ID，all_granted_eps：代表所有企业项目ID。 **默认取值**： all_granted_eps 

        :return: The enterprise_project_id of this ListAlarmsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAlarmsRequest.

        **参数解释**： 企业项目ID，当查询所有企业项目时，配置为：all_granted_eps。 当需要查询某个企业项目时，配置为对应的企业项目ID，请参考获“[获取企业项目ID](ces_03_0061.xml)”。 **约束限制**： 不涉及。 **取值范围**： 只能包含小写字母、数字、“-”、“_”，长度为36个字符。也可取值0或all_granted_eps。0：代表默认企业项目ID，all_granted_eps：代表所有企业项目ID。 **默认取值**： all_granted_eps 

        :param enterprise_project_id: The enterprise_project_id of this ListAlarmsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListAlarmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
