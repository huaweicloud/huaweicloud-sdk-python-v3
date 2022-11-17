# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apps': 'list[AppListDto]',
        'count': 'int'
    }

    attribute_map = {
        'apps': 'apps',
        'count': 'count'
    }

    def __init__(self, apps=None, count=None):
        """ListAppResponse

        The model defined in huaweicloud sdk

        :param apps: 应用列表
        :type apps: list[:class:`huaweicloudsdkeihealth.v1.AppListDto`]
        :param count: 应用总条数
        :type count: int
        """
        
        super(ListAppResponse, self).__init__()

        self._apps = None
        self._count = None
        self.discriminator = None

        if apps is not None:
            self.apps = apps
        if count is not None:
            self.count = count

    @property
    def apps(self):
        """Gets the apps of this ListAppResponse.

        应用列表

        :return: The apps of this ListAppResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AppListDto`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this ListAppResponse.

        应用列表

        :param apps: The apps of this ListAppResponse.
        :type apps: list[:class:`huaweicloudsdkeihealth.v1.AppListDto`]
        """
        self._apps = apps

    @property
    def count(self):
        """Gets the count of this ListAppResponse.

        应用总条数

        :return: The count of this ListAppResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAppResponse.

        应用总条数

        :param count: The count of this ListAppResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
