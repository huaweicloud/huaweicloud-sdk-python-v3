# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckTableRestoreResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_table_name_result': 'CheckTableNameResult'
    }

    attribute_map = {
        'check_table_name_result': 'check_table_name_result'
    }

    def __init__(self, check_table_name_result=None):
        """CheckTableRestoreResponse

        The model defined in huaweicloud sdk

        :param check_table_name_result: 
        :type check_table_name_result: :class:`huaweicloudsdkdws.v2.CheckTableNameResult`
        """
        
        super(CheckTableRestoreResponse, self).__init__()

        self._check_table_name_result = None
        self.discriminator = None

        if check_table_name_result is not None:
            self.check_table_name_result = check_table_name_result

    @property
    def check_table_name_result(self):
        """Gets the check_table_name_result of this CheckTableRestoreResponse.

        :return: The check_table_name_result of this CheckTableRestoreResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.CheckTableNameResult`
        """
        return self._check_table_name_result

    @check_table_name_result.setter
    def check_table_name_result(self, check_table_name_result):
        """Sets the check_table_name_result of this CheckTableRestoreResponse.

        :param check_table_name_result: The check_table_name_result of this CheckTableRestoreResponse.
        :type check_table_name_result: :class:`huaweicloudsdkdws.v2.CheckTableNameResult`
        """
        self._check_table_name_result = check_table_name_result

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
        if not isinstance(other, CheckTableRestoreResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
