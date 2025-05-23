# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFsDirUsageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dir_usage': 'FsDirUasge',
        'x_request_id': 'str'
    }

    attribute_map = {
        'dir_usage': 'dir_usage',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, dir_usage=None, x_request_id=None):
        r"""ShowFsDirUsageResponse

        The model defined in huaweicloud sdk

        :param dir_usage: 
        :type dir_usage: :class:`huaweicloudsdksfsturbo.v1.FsDirUasge`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowFsDirUsageResponse, self).__init__()

        self._dir_usage = None
        self._x_request_id = None
        self.discriminator = None

        if dir_usage is not None:
            self.dir_usage = dir_usage
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def dir_usage(self):
        r"""Gets the dir_usage of this ShowFsDirUsageResponse.

        :return: The dir_usage of this ShowFsDirUsageResponse.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.FsDirUasge`
        """
        return self._dir_usage

    @dir_usage.setter
    def dir_usage(self, dir_usage):
        r"""Sets the dir_usage of this ShowFsDirUsageResponse.

        :param dir_usage: The dir_usage of this ShowFsDirUsageResponse.
        :type dir_usage: :class:`huaweicloudsdksfsturbo.v1.FsDirUasge`
        """
        self._dir_usage = dir_usage

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowFsDirUsageResponse.

        :return: The x_request_id of this ShowFsDirUsageResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowFsDirUsageResponse.

        :param x_request_id: The x_request_id of this ShowFsDirUsageResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowFsDirUsageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
