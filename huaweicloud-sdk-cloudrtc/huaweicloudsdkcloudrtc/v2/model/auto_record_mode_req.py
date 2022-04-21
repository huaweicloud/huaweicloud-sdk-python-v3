# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoRecordModeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'record_rule_id': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'record_rule_id': 'record_rule_id'
    }

    def __init__(self, mode=None, record_rule_id=None):
        """AutoRecordModeReq

        The model defined in huaweicloud sdk

        :param mode: 录制模式。 - AUTO_RECORD_OFF：关闭自动录制。 - AUTO_INDIVIDUAL_RECORD：开启单流自动录制，此时record_rule_id必须非空。 
        :type mode: str
        :param record_rule_id: 录制规则id。
        :type record_rule_id: str
        """
        
        

        self._mode = None
        self._record_rule_id = None
        self.discriminator = None

        self.mode = mode
        if record_rule_id is not None:
            self.record_rule_id = record_rule_id

    @property
    def mode(self):
        """Gets the mode of this AutoRecordModeReq.

        录制模式。 - AUTO_RECORD_OFF：关闭自动录制。 - AUTO_INDIVIDUAL_RECORD：开启单流自动录制，此时record_rule_id必须非空。 

        :return: The mode of this AutoRecordModeReq.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this AutoRecordModeReq.

        录制模式。 - AUTO_RECORD_OFF：关闭自动录制。 - AUTO_INDIVIDUAL_RECORD：开启单流自动录制，此时record_rule_id必须非空。 

        :param mode: The mode of this AutoRecordModeReq.
        :type mode: str
        """
        self._mode = mode

    @property
    def record_rule_id(self):
        """Gets the record_rule_id of this AutoRecordModeReq.

        录制规则id。

        :return: The record_rule_id of this AutoRecordModeReq.
        :rtype: str
        """
        return self._record_rule_id

    @record_rule_id.setter
    def record_rule_id(self, record_rule_id):
        """Sets the record_rule_id of this AutoRecordModeReq.

        录制规则id。

        :param record_rule_id: The record_rule_id of this AutoRecordModeReq.
        :type record_rule_id: str
        """
        self._record_rule_id = record_rule_id

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
        if not isinstance(other, AutoRecordModeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
