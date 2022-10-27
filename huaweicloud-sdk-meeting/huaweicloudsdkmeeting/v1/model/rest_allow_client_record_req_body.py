# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestAllowClientRecordReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'allow_client_record': 'int'
    }

    attribute_map = {
        'allow_client_record': 'allowClientRecord'
    }

    def __init__(self, allow_client_record=None):
        """RestAllowClientRecordReqBody

        The model defined in huaweicloud sdk

        :param allow_client_record: * 0：取消与会者客户端录制权限 * 1：允许与会者客户端录制 
        :type allow_client_record: int
        """
        
        

        self._allow_client_record = None
        self.discriminator = None

        self.allow_client_record = allow_client_record

    @property
    def allow_client_record(self):
        """Gets the allow_client_record of this RestAllowClientRecordReqBody.

        * 0：取消与会者客户端录制权限 * 1：允许与会者客户端录制 

        :return: The allow_client_record of this RestAllowClientRecordReqBody.
        :rtype: int
        """
        return self._allow_client_record

    @allow_client_record.setter
    def allow_client_record(self, allow_client_record):
        """Sets the allow_client_record of this RestAllowClientRecordReqBody.

        * 0：取消与会者客户端录制权限 * 1：允许与会者客户端录制 

        :param allow_client_record: The allow_client_record of this RestAllowClientRecordReqBody.
        :type allow_client_record: int
        """
        self._allow_client_record = allow_client_record

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
        if not isinstance(other, RestAllowClientRecordReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
