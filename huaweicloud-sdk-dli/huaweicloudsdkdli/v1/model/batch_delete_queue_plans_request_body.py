# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteQueuePlansRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plan_ids': 'list[int]'
    }

    attribute_map = {
        'plan_ids': 'plan_ids'
    }

    def __init__(self, plan_ids=None):
        r"""BatchDeleteQueuePlansRequestBody

        The model defined in huaweicloud sdk

        :param plan_ids: 表示SQL语句的类型
        :type plan_ids: list[int]
        """
        
        

        self._plan_ids = None
        self.discriminator = None

        self.plan_ids = plan_ids

    @property
    def plan_ids(self):
        r"""Gets the plan_ids of this BatchDeleteQueuePlansRequestBody.

        表示SQL语句的类型

        :return: The plan_ids of this BatchDeleteQueuePlansRequestBody.
        :rtype: list[int]
        """
        return self._plan_ids

    @plan_ids.setter
    def plan_ids(self, plan_ids):
        r"""Sets the plan_ids of this BatchDeleteQueuePlansRequestBody.

        表示SQL语句的类型

        :param plan_ids: The plan_ids of this BatchDeleteQueuePlansRequestBody.
        :type plan_ids: list[int]
        """
        self._plan_ids = plan_ids

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
        if not isinstance(other, BatchDeleteQueuePlansRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
