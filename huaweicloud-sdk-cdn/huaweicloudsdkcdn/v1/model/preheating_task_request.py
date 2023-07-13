# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreheatingTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'preheating_task': 'PreheatingTaskRequestBody'
    }

    attribute_map = {
        'preheating_task': 'preheating_task'
    }

    def __init__(self, preheating_task=None):
        """PreheatingTaskRequest

        The model defined in huaweicloud sdk

        :param preheating_task: 
        :type preheating_task: :class:`huaweicloudsdkcdn.v1.PreheatingTaskRequestBody`
        """
        
        

        self._preheating_task = None
        self.discriminator = None

        self.preheating_task = preheating_task

    @property
    def preheating_task(self):
        """Gets the preheating_task of this PreheatingTaskRequest.

        :return: The preheating_task of this PreheatingTaskRequest.
        :rtype: :class:`huaweicloudsdkcdn.v1.PreheatingTaskRequestBody`
        """
        return self._preheating_task

    @preheating_task.setter
    def preheating_task(self, preheating_task):
        """Sets the preheating_task of this PreheatingTaskRequest.

        :param preheating_task: The preheating_task of this PreheatingTaskRequest.
        :type preheating_task: :class:`huaweicloudsdkcdn.v1.PreheatingTaskRequestBody`
        """
        self._preheating_task = preheating_task

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
        if not isinstance(other, PreheatingTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
