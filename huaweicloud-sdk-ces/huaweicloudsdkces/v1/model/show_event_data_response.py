# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datapoints': 'list[EventDataInfo]'
    }

    attribute_map = {
        'datapoints': 'datapoints'
    }

    def __init__(self, datapoints=None):
        """ShowEventDataResponse

        The model defined in huaweicloud sdk

        :param datapoints: 配置信息列表。如果不存在对应的配置信息，则datapoints为空数组[]。
        :type datapoints: list[:class:`huaweicloudsdkces.v1.EventDataInfo`]
        """
        
        super(ShowEventDataResponse, self).__init__()

        self._datapoints = None
        self.discriminator = None

        if datapoints is not None:
            self.datapoints = datapoints

    @property
    def datapoints(self):
        """Gets the datapoints of this ShowEventDataResponse.

        配置信息列表。如果不存在对应的配置信息，则datapoints为空数组[]。

        :return: The datapoints of this ShowEventDataResponse.
        :rtype: list[:class:`huaweicloudsdkces.v1.EventDataInfo`]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        """Sets the datapoints of this ShowEventDataResponse.

        配置信息列表。如果不存在对应的配置信息，则datapoints为空数组[]。

        :param datapoints: The datapoints of this ShowEventDataResponse.
        :type datapoints: list[:class:`huaweicloudsdkces.v1.EventDataInfo`]
        """
        self._datapoints = datapoints

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
        if not isinstance(other, ShowEventDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
