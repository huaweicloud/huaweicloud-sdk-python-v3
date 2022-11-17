# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLogDumpObsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_dump_obs_id': 'str'
    }

    attribute_map = {
        'log_dump_obs_id': 'log_dump_obs_id'
    }

    def __init__(self, log_dump_obs_id=None):
        """CreateLogDumpObsResponse

        The model defined in huaweicloud sdk

        :param log_dump_obs_id: 转储id。
        :type log_dump_obs_id: str
        """
        
        super(CreateLogDumpObsResponse, self).__init__()

        self._log_dump_obs_id = None
        self.discriminator = None

        if log_dump_obs_id is not None:
            self.log_dump_obs_id = log_dump_obs_id

    @property
    def log_dump_obs_id(self):
        """Gets the log_dump_obs_id of this CreateLogDumpObsResponse.

        转储id。

        :return: The log_dump_obs_id of this CreateLogDumpObsResponse.
        :rtype: str
        """
        return self._log_dump_obs_id

    @log_dump_obs_id.setter
    def log_dump_obs_id(self, log_dump_obs_id):
        """Sets the log_dump_obs_id of this CreateLogDumpObsResponse.

        转储id。

        :param log_dump_obs_id: The log_dump_obs_id of this CreateLogDumpObsResponse.
        :type log_dump_obs_id: str
        """
        self._log_dump_obs_id = log_dump_obs_id

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
        if not isinstance(other, CreateLogDumpObsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
