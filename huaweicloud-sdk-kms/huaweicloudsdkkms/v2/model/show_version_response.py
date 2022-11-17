# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'object'
    }

    attribute_map = {
        'version': 'version'
    }

    def __init__(self, version=None):
        """ShowVersionResponse

        The model defined in huaweicloud sdk

        :param version: 描述version 对象的列表，详情请参见 ApiVersionDetail字段数据结构说明。
        :type version: object
        """
        
        super(ShowVersionResponse, self).__init__()

        self._version = None
        self.discriminator = None

        if version is not None:
            self.version = version

    @property
    def version(self):
        """Gets the version of this ShowVersionResponse.

        描述version 对象的列表，详情请参见 ApiVersionDetail字段数据结构说明。

        :return: The version of this ShowVersionResponse.
        :rtype: object
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowVersionResponse.

        描述version 对象的列表，详情请参见 ApiVersionDetail字段数据结构说明。

        :param version: The version of this ShowVersionResponse.
        :type version: object
        """
        self._version = version

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
        if not isinstance(other, ShowVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
