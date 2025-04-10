# coding: utf-8

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
        'has_more_app': 'bool',
        'apps': 'list[DescribeAppResult]',
        'total_number': 'int'
    }

    attribute_map = {
        'has_more_app': 'has_more_app',
        'apps': 'apps',
        'total_number': 'total_number'
    }

    def __init__(self, has_more_app=None, apps=None, total_number=None):
        r"""ListAppResponse

        The model defined in huaweicloud sdk

        :param has_more_app: 是否还有更多满足条件的App。  - true：是。 - false：否。
        :type has_more_app: bool
        :param apps: AppEntry list that meets the current request.
        :type apps: list[:class:`huaweicloudsdkdis.v2.DescribeAppResult`]
        :param total_number: 满足条件的App总数。
        :type total_number: int
        """
        
        super(ListAppResponse, self).__init__()

        self._has_more_app = None
        self._apps = None
        self._total_number = None
        self.discriminator = None

        if has_more_app is not None:
            self.has_more_app = has_more_app
        if apps is not None:
            self.apps = apps
        if total_number is not None:
            self.total_number = total_number

    @property
    def has_more_app(self):
        r"""Gets the has_more_app of this ListAppResponse.

        是否还有更多满足条件的App。  - true：是。 - false：否。

        :return: The has_more_app of this ListAppResponse.
        :rtype: bool
        """
        return self._has_more_app

    @has_more_app.setter
    def has_more_app(self, has_more_app):
        r"""Sets the has_more_app of this ListAppResponse.

        是否还有更多满足条件的App。  - true：是。 - false：否。

        :param has_more_app: The has_more_app of this ListAppResponse.
        :type has_more_app: bool
        """
        self._has_more_app = has_more_app

    @property
    def apps(self):
        r"""Gets the apps of this ListAppResponse.

        AppEntry list that meets the current request.

        :return: The apps of this ListAppResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.DescribeAppResult`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        r"""Sets the apps of this ListAppResponse.

        AppEntry list that meets the current request.

        :param apps: The apps of this ListAppResponse.
        :type apps: list[:class:`huaweicloudsdkdis.v2.DescribeAppResult`]
        """
        self._apps = apps

    @property
    def total_number(self):
        r"""Gets the total_number of this ListAppResponse.

        满足条件的App总数。

        :return: The total_number of this ListAppResponse.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        r"""Sets the total_number of this ListAppResponse.

        满足条件的App总数。

        :param total_number: The total_number of this ListAppResponse.
        :type total_number: int
        """
        self._total_number = total_number

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
