# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetRecordSetsStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'recordset_ids': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'recordset_ids': 'recordset_ids'
    }

    def __init__(self, status=None, recordset_ids=None):
        r"""BatchSetRecordSetsStatusRequestBody

        The model defined in huaweicloud sdk

        :param status: **参数解释：** 待设置记录集状态。 **约束限制：** 不涉及。 **取值范围：** - DISABLE：暂停解析 - ENABLE：启用解析  **默认取值：** 不涉及。
        :type status: str
        :param recordset_ids: **参数解释：** 待设置记录集ID列表。 **约束限制：** 最多支持50个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type recordset_ids: list[str]
        """
        
        

        self._status = None
        self._recordset_ids = None
        self.discriminator = None

        self.status = status
        self.recordset_ids = recordset_ids

    @property
    def status(self):
        r"""Gets the status of this BatchSetRecordSetsStatusRequestBody.

        **参数解释：** 待设置记录集状态。 **约束限制：** 不涉及。 **取值范围：** - DISABLE：暂停解析 - ENABLE：启用解析  **默认取值：** 不涉及。

        :return: The status of this BatchSetRecordSetsStatusRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchSetRecordSetsStatusRequestBody.

        **参数解释：** 待设置记录集状态。 **约束限制：** 不涉及。 **取值范围：** - DISABLE：暂停解析 - ENABLE：启用解析  **默认取值：** 不涉及。

        :param status: The status of this BatchSetRecordSetsStatusRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def recordset_ids(self):
        r"""Gets the recordset_ids of this BatchSetRecordSetsStatusRequestBody.

        **参数解释：** 待设置记录集ID列表。 **约束限制：** 最多支持50个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The recordset_ids of this BatchSetRecordSetsStatusRequestBody.
        :rtype: list[str]
        """
        return self._recordset_ids

    @recordset_ids.setter
    def recordset_ids(self, recordset_ids):
        r"""Sets the recordset_ids of this BatchSetRecordSetsStatusRequestBody.

        **参数解释：** 待设置记录集ID列表。 **约束限制：** 最多支持50个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param recordset_ids: The recordset_ids of this BatchSetRecordSetsStatusRequestBody.
        :type recordset_ids: list[str]
        """
        self._recordset_ids = recordset_ids

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
        if not isinstance(other, BatchSetRecordSetsStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
