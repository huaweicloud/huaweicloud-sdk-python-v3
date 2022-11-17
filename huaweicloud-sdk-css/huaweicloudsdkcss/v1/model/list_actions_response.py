# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListActionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'actions': 'list[Actions]'
    }

    attribute_map = {
        'actions': 'actions'
    }

    def __init__(self, actions=None):
        """ListActionsResponse

        The model defined in huaweicloud sdk

        :param actions: 操作记录列表。
        :type actions: list[:class:`huaweicloudsdkcss.v1.Actions`]
        """
        
        super(ListActionsResponse, self).__init__()

        self._actions = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions

    @property
    def actions(self):
        """Gets the actions of this ListActionsResponse.

        操作记录列表。

        :return: The actions of this ListActionsResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.Actions`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ListActionsResponse.

        操作记录列表。

        :param actions: The actions of this ListActionsResponse.
        :type actions: list[:class:`huaweicloudsdkcss.v1.Actions`]
        """
        self._actions = actions

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
        if not isinstance(other, ListActionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
