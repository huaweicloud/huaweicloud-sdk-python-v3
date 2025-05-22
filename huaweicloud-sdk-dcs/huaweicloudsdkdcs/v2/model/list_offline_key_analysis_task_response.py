# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOfflineKeyAnalysisTaskResponse(SdkResponse):

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
        'total': 'int',
        'records': 'list[OfflineKeyAnalysisRecord]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'total': 'total',
        'records': 'records'
    }

    def __init__(self, instance_id=None, total=None, records=None):
        r"""ListOfflineKeyAnalysisTaskResponse

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。 **取值范围**： 不涉及。 
        :type instance_id: str
        :param total: **参数解释**： 离线全量key分析的总数。 **取值范围**： 不涉及。 
        :type total: int
        :param records: **参数解释**： 离线全量key分析记录列表。 
        :type records: list[:class:`huaweicloudsdkdcs.v2.OfflineKeyAnalysisRecord`]
        """
        
        super(ListOfflineKeyAnalysisTaskResponse, self).__init__()

        self._instance_id = None
        self._total = None
        self._records = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if total is not None:
            self.total = total
        if records is not None:
            self.records = records

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListOfflineKeyAnalysisTaskResponse.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。 

        :return: The instance_id of this ListOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListOfflineKeyAnalysisTaskResponse.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。 

        :param instance_id: The instance_id of this ListOfflineKeyAnalysisTaskResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def total(self):
        r"""Gets the total of this ListOfflineKeyAnalysisTaskResponse.

        **参数解释**： 离线全量key分析的总数。 **取值范围**： 不涉及。 

        :return: The total of this ListOfflineKeyAnalysisTaskResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOfflineKeyAnalysisTaskResponse.

        **参数解释**： 离线全量key分析的总数。 **取值范围**： 不涉及。 

        :param total: The total of this ListOfflineKeyAnalysisTaskResponse.
        :type total: int
        """
        self._total = total

    @property
    def records(self):
        r"""Gets the records of this ListOfflineKeyAnalysisTaskResponse.

        **参数解释**： 离线全量key分析记录列表。 

        :return: The records of this ListOfflineKeyAnalysisTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.OfflineKeyAnalysisRecord`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListOfflineKeyAnalysisTaskResponse.

        **参数解释**： 离线全量key分析记录列表。 

        :param records: The records of this ListOfflineKeyAnalysisTaskResponse.
        :type records: list[:class:`huaweicloudsdkdcs.v2.OfflineKeyAnalysisRecord`]
        """
        self._records = records

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
        if not isinstance(other, ListOfflineKeyAnalysisTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
