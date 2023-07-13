# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTasklogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'param_info': 'ParamInfo',
        'log_info': 'list[LogInfo]'
    }

    attribute_map = {
        'param_info': 'param_info',
        'log_info': 'log_info'
    }

    def __init__(self, param_info=None, log_info=None):
        """ShowTasklogResponse

        The model defined in huaweicloud sdk

        :param param_info: 
        :type param_info: :class:`huaweicloudsdkcodeartscheck.v2.ParamInfo`
        :param log_info: 日志信息
        :type log_info: list[:class:`huaweicloudsdkcodeartscheck.v2.LogInfo`]
        """
        
        super(ShowTasklogResponse, self).__init__()

        self._param_info = None
        self._log_info = None
        self.discriminator = None

        if param_info is not None:
            self.param_info = param_info
        if log_info is not None:
            self.log_info = log_info

    @property
    def param_info(self):
        """Gets the param_info of this ShowTasklogResponse.

        :return: The param_info of this ShowTasklogResponse.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ParamInfo`
        """
        return self._param_info

    @param_info.setter
    def param_info(self, param_info):
        """Sets the param_info of this ShowTasklogResponse.

        :param param_info: The param_info of this ShowTasklogResponse.
        :type param_info: :class:`huaweicloudsdkcodeartscheck.v2.ParamInfo`
        """
        self._param_info = param_info

    @property
    def log_info(self):
        """Gets the log_info of this ShowTasklogResponse.

        日志信息

        :return: The log_info of this ShowTasklogResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.LogInfo`]
        """
        return self._log_info

    @log_info.setter
    def log_info(self, log_info):
        """Sets the log_info of this ShowTasklogResponse.

        日志信息

        :param log_info: The log_info of this ShowTasklogResponse.
        :type log_info: list[:class:`huaweicloudsdkcodeartscheck.v2.LogInfo`]
        """
        self._log_info = log_info

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
        if not isinstance(other, ShowTasklogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
