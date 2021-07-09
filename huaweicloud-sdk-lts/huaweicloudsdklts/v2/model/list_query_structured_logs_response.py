# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListQueryStructuredLogsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'struct_logs': 'list[StructLogContents]'
    }

    attribute_map = {
        'struct_logs': 'struct_logs'
    }

    def __init__(self, struct_logs=None):
        """ListQueryStructuredLogsResponse - a model defined in huaweicloud sdk"""
        
        super(ListQueryStructuredLogsResponse, self).__init__()

        self._struct_logs = None
        self.discriminator = None

        if struct_logs is not None:
            self.struct_logs = struct_logs

    @property
    def struct_logs(self):
        """Gets the struct_logs of this ListQueryStructuredLogsResponse.

        日志信息。

        :return: The struct_logs of this ListQueryStructuredLogsResponse.
        :rtype: list[StructLogContents]
        """
        return self._struct_logs

    @struct_logs.setter
    def struct_logs(self, struct_logs):
        """Sets the struct_logs of this ListQueryStructuredLogsResponse.

        日志信息。

        :param struct_logs: The struct_logs of this ListQueryStructuredLogsResponse.
        :type: list[StructLogContents]
        """
        self._struct_logs = struct_logs

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListQueryStructuredLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
