# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'script_records': 'list[ScriptRecordSimpleInfo]'
    }

    attribute_map = {
        'count': 'count',
        'script_records': 'script_records'
    }

    def __init__(self, count=None, script_records=None):
        r"""ListScriptRecordsResponse

        The model defined in huaweicloud sdk

        :param count: 总数。
        :type count: int
        :param script_records: 脚本执行记录列表。
        :type script_records: list[:class:`huaweicloudsdkworkspace.v2.ScriptRecordSimpleInfo`]
        """
        
        super(ListScriptRecordsResponse, self).__init__()

        self._count = None
        self._script_records = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if script_records is not None:
            self.script_records = script_records

    @property
    def count(self):
        r"""Gets the count of this ListScriptRecordsResponse.

        总数。

        :return: The count of this ListScriptRecordsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListScriptRecordsResponse.

        总数。

        :param count: The count of this ListScriptRecordsResponse.
        :type count: int
        """
        self._count = count

    @property
    def script_records(self):
        r"""Gets the script_records of this ListScriptRecordsResponse.

        脚本执行记录列表。

        :return: The script_records of this ListScriptRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ScriptRecordSimpleInfo`]
        """
        return self._script_records

    @script_records.setter
    def script_records(self, script_records):
        r"""Sets the script_records of this ListScriptRecordsResponse.

        脚本执行记录列表。

        :param script_records: The script_records of this ListScriptRecordsResponse.
        :type script_records: list[:class:`huaweicloudsdkworkspace.v2.ScriptRecordSimpleInfo`]
        """
        self._script_records = script_records

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
        if not isinstance(other, ListScriptRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
