# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatabaseWaterMarkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marked_data': 'list[dict(str, object)]'
    }

    attribute_map = {
        'marked_data': 'marked_data'
    }

    def __init__(self, marked_data=None):
        r"""CreateDatabaseWaterMarkResponse

        The model defined in huaweicloud sdk

        :param marked_data: 嵌入水印后的数据
        :type marked_data: list[dict(str, object)]
        """
        
        super(CreateDatabaseWaterMarkResponse, self).__init__()

        self._marked_data = None
        self.discriminator = None

        if marked_data is not None:
            self.marked_data = marked_data

    @property
    def marked_data(self):
        r"""Gets the marked_data of this CreateDatabaseWaterMarkResponse.

        嵌入水印后的数据

        :return: The marked_data of this CreateDatabaseWaterMarkResponse.
        :rtype: list[dict(str, object)]
        """
        return self._marked_data

    @marked_data.setter
    def marked_data(self, marked_data):
        r"""Sets the marked_data of this CreateDatabaseWaterMarkResponse.

        嵌入水印后的数据

        :param marked_data: The marked_data of this CreateDatabaseWaterMarkResponse.
        :type marked_data: list[dict(str, object)]
        """
        self._marked_data = marked_data

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
        if not isinstance(other, CreateDatabaseWaterMarkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
