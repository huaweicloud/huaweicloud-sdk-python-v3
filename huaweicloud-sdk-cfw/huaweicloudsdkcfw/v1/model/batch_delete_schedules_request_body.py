# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteSchedulesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'schedule_ids': 'list[str]'
    }

    attribute_map = {
        'object_id': 'object_id',
        'schedule_ids': 'schedule_ids'
    }

    def __init__(self, object_id=None, schedule_ids=None):
        r"""BatchDeleteSchedulesRequestBody

        The model defined in huaweicloud sdk

        :param object_id: **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type object_id: str
        :param schedule_ids: **参数解释**： 时间表ID列表，可以通过调用[查询时间表列表接口]获得，通过返回值中的data.records.schedule_id获得 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type schedule_ids: list[str]
        """
        
        

        self._object_id = None
        self._schedule_ids = None
        self.discriminator = None

        self.object_id = object_id
        self.schedule_ids = schedule_ids

    @property
    def object_id(self):
        r"""Gets the object_id of this BatchDeleteSchedulesRequestBody.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The object_id of this BatchDeleteSchedulesRequestBody.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this BatchDeleteSchedulesRequestBody.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param object_id: The object_id of this BatchDeleteSchedulesRequestBody.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def schedule_ids(self):
        r"""Gets the schedule_ids of this BatchDeleteSchedulesRequestBody.

        **参数解释**： 时间表ID列表，可以通过调用[查询时间表列表接口]获得，通过返回值中的data.records.schedule_id获得 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The schedule_ids of this BatchDeleteSchedulesRequestBody.
        :rtype: list[str]
        """
        return self._schedule_ids

    @schedule_ids.setter
    def schedule_ids(self, schedule_ids):
        r"""Sets the schedule_ids of this BatchDeleteSchedulesRequestBody.

        **参数解释**： 时间表ID列表，可以通过调用[查询时间表列表接口]获得，通过返回值中的data.records.schedule_id获得 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param schedule_ids: The schedule_ids of this BatchDeleteSchedulesRequestBody.
        :type schedule_ids: list[str]
        """
        self._schedule_ids = schedule_ids

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
        if not isinstance(other, BatchDeleteSchedulesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
