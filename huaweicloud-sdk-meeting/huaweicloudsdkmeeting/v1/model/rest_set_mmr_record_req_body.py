# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestSetMmrRecordReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_type': 'int'
    }

    attribute_map = {
        'record_type': 'recordType'
    }

    def __init__(self, record_type=None):
        r"""RestSetMmrRecordReqBody

        The model defined in huaweicloud sdk

        :param record_type: 0：暂停MMR会议录制 1：启动MMR会议录制 2：停止MMR会议录制
        :type record_type: int
        """
        
        

        self._record_type = None
        self.discriminator = None

        self.record_type = record_type

    @property
    def record_type(self):
        r"""Gets the record_type of this RestSetMmrRecordReqBody.

        0：暂停MMR会议录制 1：启动MMR会议录制 2：停止MMR会议录制

        :return: The record_type of this RestSetMmrRecordReqBody.
        :rtype: int
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        r"""Sets the record_type of this RestSetMmrRecordReqBody.

        0：暂停MMR会议录制 1：启动MMR会议录制 2：停止MMR会议录制

        :param record_type: The record_type of this RestSetMmrRecordReqBody.
        :type record_type: int
        """
        self._record_type = record_type

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
        if not isinstance(other, RestSetMmrRecordReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
