# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManagementEventSelector:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exclude_service': 'list[str]'
    }

    attribute_map = {
        'exclude_service': 'exclude_service'
    }

    def __init__(self, exclude_service=None):
        """ManagementEventSelector

        The model defined in huaweicloud sdk

        :param exclude_service: 标识不转储的云服务名称。 目前只支持设置为KMS，表示屏蔽KMS服务的createDatakey事件。
        :type exclude_service: list[str]
        """
        
        

        self._exclude_service = None
        self.discriminator = None

        if exclude_service is not None:
            self.exclude_service = exclude_service

    @property
    def exclude_service(self):
        """Gets the exclude_service of this ManagementEventSelector.

        标识不转储的云服务名称。 目前只支持设置为KMS，表示屏蔽KMS服务的createDatakey事件。

        :return: The exclude_service of this ManagementEventSelector.
        :rtype: list[str]
        """
        return self._exclude_service

    @exclude_service.setter
    def exclude_service(self, exclude_service):
        """Sets the exclude_service of this ManagementEventSelector.

        标识不转储的云服务名称。 目前只支持设置为KMS，表示屏蔽KMS服务的createDatakey事件。

        :param exclude_service: The exclude_service of this ManagementEventSelector.
        :type exclude_service: list[str]
        """
        self._exclude_service = exclude_service

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
        if not isinstance(other, ManagementEventSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
