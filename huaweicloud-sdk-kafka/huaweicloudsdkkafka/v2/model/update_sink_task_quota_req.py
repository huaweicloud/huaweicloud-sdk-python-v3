# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSinkTaskQuotaReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sink_max_tasks': 'int'
    }

    attribute_map = {
        'sink_max_tasks': 'sink_max_tasks'
    }

    def __init__(self, sink_max_tasks=None):
        """UpdateSinkTaskQuotaReq

        The model defined in huaweicloud sdk

        :param sink_max_tasks: 转储任务的总个数。 
        :type sink_max_tasks: int
        """
        
        

        self._sink_max_tasks = None
        self.discriminator = None

        self.sink_max_tasks = sink_max_tasks

    @property
    def sink_max_tasks(self):
        """Gets the sink_max_tasks of this UpdateSinkTaskQuotaReq.

        转储任务的总个数。 

        :return: The sink_max_tasks of this UpdateSinkTaskQuotaReq.
        :rtype: int
        """
        return self._sink_max_tasks

    @sink_max_tasks.setter
    def sink_max_tasks(self, sink_max_tasks):
        """Sets the sink_max_tasks of this UpdateSinkTaskQuotaReq.

        转储任务的总个数。 

        :param sink_max_tasks: The sink_max_tasks of this UpdateSinkTaskQuotaReq.
        :type sink_max_tasks: int
        """
        self._sink_max_tasks = sink_max_tasks

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
        if not isinstance(other, UpdateSinkTaskQuotaReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
