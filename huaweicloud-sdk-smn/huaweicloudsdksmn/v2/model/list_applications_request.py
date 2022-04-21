# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'platform': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'platform': 'platform'
    }

    def __init__(self, offset=None, limit=None, name=None, platform=None):
        """ListApplicationsRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。
        :type offset: int
        :param limit: 查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。
        :type limit: int
        :param name: 检索应用名称。  支持后向模糊匹配，长度不得超过64个字符，只能包含英文字母、下划线和数字。
        :type name: str
        :param platform: 应用平台。  目前仅支持HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。
        :type platform: str
        """
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self._platform = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if platform is not None:
            self.platform = platform

    @property
    def offset(self):
        """Gets the offset of this ListApplicationsRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :return: The offset of this ListApplicationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListApplicationsRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :param offset: The offset of this ListApplicationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListApplicationsRequest.

        查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :return: The limit of this ListApplicationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApplicationsRequest.

        查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :param limit: The limit of this ListApplicationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListApplicationsRequest.

        检索应用名称。  支持后向模糊匹配，长度不得超过64个字符，只能包含英文字母、下划线和数字。

        :return: The name of this ListApplicationsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListApplicationsRequest.

        检索应用名称。  支持后向模糊匹配，长度不得超过64个字符，只能包含英文字母、下划线和数字。

        :param name: The name of this ListApplicationsRequest.
        :type name: str
        """
        self._name = name

    @property
    def platform(self):
        """Gets the platform of this ListApplicationsRequest.

        应用平台。  目前仅支持HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。

        :return: The platform of this ListApplicationsRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ListApplicationsRequest.

        应用平台。  目前仅支持HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。

        :param platform: The platform of this ListApplicationsRequest.
        :type platform: str
        """
        self._platform = platform

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
        if not isinstance(other, ListApplicationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
