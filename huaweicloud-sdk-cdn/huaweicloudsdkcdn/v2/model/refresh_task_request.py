# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RefreshTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'refresh_task': 'RefreshTaskRequestBody'
    }

    attribute_map = {
        'refresh_task': 'refresh_task'
    }

    def __init__(self, refresh_task=None):
        """RefreshTaskRequest

        The model defined in huaweicloud sdk

        :param refresh_task: 
        :type refresh_task: :class:`huaweicloudsdkcdn.v2.RefreshTaskRequestBody`
        """
        
        

        self._refresh_task = None
        self.discriminator = None

        self.refresh_task = refresh_task

    @property
    def refresh_task(self):
        """Gets the refresh_task of this RefreshTaskRequest.

        :return: The refresh_task of this RefreshTaskRequest.
        :rtype: :class:`huaweicloudsdkcdn.v2.RefreshTaskRequestBody`
        """
        return self._refresh_task

    @refresh_task.setter
    def refresh_task(self, refresh_task):
        """Sets the refresh_task of this RefreshTaskRequest.

        :param refresh_task: The refresh_task of this RefreshTaskRequest.
        :type refresh_task: :class:`huaweicloudsdkcdn.v2.RefreshTaskRequestBody`
        """
        self._refresh_task = refresh_task

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
        if not isinstance(other, RefreshTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
