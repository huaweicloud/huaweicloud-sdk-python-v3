# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatabaseWaterMarkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'watermarks': 'list[str]'
    }

    attribute_map = {
        'watermarks': 'watermarks'
    }

    def __init__(self, watermarks=None):
        """ShowDatabaseWaterMarkResponse

        The model defined in huaweicloud sdk

        :param watermarks: 提取水印内容列表。上传数据中不同列可能包含不同水印，返回时将所有提取到的水印返回，列表中水印个数不超过100
        :type watermarks: list[str]
        """
        
        super(ShowDatabaseWaterMarkResponse, self).__init__()

        self._watermarks = None
        self.discriminator = None

        if watermarks is not None:
            self.watermarks = watermarks

    @property
    def watermarks(self):
        """Gets the watermarks of this ShowDatabaseWaterMarkResponse.

        提取水印内容列表。上传数据中不同列可能包含不同水印，返回时将所有提取到的水印返回，列表中水印个数不超过100

        :return: The watermarks of this ShowDatabaseWaterMarkResponse.
        :rtype: list[str]
        """
        return self._watermarks

    @watermarks.setter
    def watermarks(self, watermarks):
        """Sets the watermarks of this ShowDatabaseWaterMarkResponse.

        提取水印内容列表。上传数据中不同列可能包含不同水印，返回时将所有提取到的水印返回，列表中水印个数不超过100

        :param watermarks: The watermarks of this ShowDatabaseWaterMarkResponse.
        :type watermarks: list[str]
        """
        self._watermarks = watermarks

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
        if not isinstance(other, ShowDatabaseWaterMarkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
