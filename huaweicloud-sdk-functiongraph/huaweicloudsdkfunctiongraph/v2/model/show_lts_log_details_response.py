# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLtsLogDetailsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'stream_id': 'str',
        'stream_name': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'stream_id': 'stream_id',
        'stream_name': 'stream_name'
    }

    def __init__(self, group_id=None, stream_id=None, stream_name=None):
        """ShowLtsLogDetailsResponse - a model defined in huaweicloud sdk"""
        
        super(ShowLtsLogDetailsResponse, self).__init__()

        self._group_id = None
        self._stream_id = None
        self._stream_name = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if stream_id is not None:
            self.stream_id = stream_id
        if stream_name is not None:
            self.stream_name = stream_name

    @property
    def group_id(self):
        """Gets the group_id of this ShowLtsLogDetailsResponse.

        日志组id

        :return: The group_id of this ShowLtsLogDetailsResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowLtsLogDetailsResponse.

        日志组id

        :param group_id: The group_id of this ShowLtsLogDetailsResponse.
        :type: str
        """
        self._group_id = group_id

    @property
    def stream_id(self):
        """Gets the stream_id of this ShowLtsLogDetailsResponse.

        日志流id

        :return: The stream_id of this ShowLtsLogDetailsResponse.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this ShowLtsLogDetailsResponse.

        日志流id

        :param stream_id: The stream_id of this ShowLtsLogDetailsResponse.
        :type: str
        """
        self._stream_id = stream_id

    @property
    def stream_name(self):
        """Gets the stream_name of this ShowLtsLogDetailsResponse.

        日志流名称

        :return: The stream_name of this ShowLtsLogDetailsResponse.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this ShowLtsLogDetailsResponse.

        日志流名称

        :param stream_name: The stream_name of this ShowLtsLogDetailsResponse.
        :type: str
        """
        self._stream_name = stream_name

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
        if not isinstance(other, ShowLtsLogDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
