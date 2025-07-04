# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatabaseAuthorityResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'view_sql': 'list[str]'
    }

    attribute_map = {
        'view_sql': 'view_sql'
    }

    def __init__(self, view_sql=None):
        r"""UpdateDatabaseAuthorityResponse

        The model defined in huaweicloud sdk

        :param view_sql: **参数解释**： sql列表。 **取值范围**： 不涉及。
        :type view_sql: list[str]
        """
        
        super(UpdateDatabaseAuthorityResponse, self).__init__()

        self._view_sql = None
        self.discriminator = None

        if view_sql is not None:
            self.view_sql = view_sql

    @property
    def view_sql(self):
        r"""Gets the view_sql of this UpdateDatabaseAuthorityResponse.

        **参数解释**： sql列表。 **取值范围**： 不涉及。

        :return: The view_sql of this UpdateDatabaseAuthorityResponse.
        :rtype: list[str]
        """
        return self._view_sql

    @view_sql.setter
    def view_sql(self, view_sql):
        r"""Sets the view_sql of this UpdateDatabaseAuthorityResponse.

        **参数解释**： sql列表。 **取值范围**： 不涉及。

        :param view_sql: The view_sql of this UpdateDatabaseAuthorityResponse.
        :type view_sql: list[str]
        """
        self._view_sql = view_sql

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
        if not isinstance(other, UpdateDatabaseAuthorityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
