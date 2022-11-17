# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step': 'int',
        'status': 'int'
    }

    attribute_map = {
        'step': 'step',
        'status': 'status'
    }

    def __init__(self, step=None, status=None):
        """AccessProgress

        The model defined in huaweicloud sdk

        :param step: 步骤   - 1: 指回源IP加白   - 2: 指本地验证   - 指修改DNS解析
        :type step: int
        :param status: 状态，0：未完成这个步骤；1：已完成这个状态”
        :type status: int
        """
        
        

        self._step = None
        self._status = None
        self.discriminator = None

        if step is not None:
            self.step = step
        if status is not None:
            self.status = status

    @property
    def step(self):
        """Gets the step of this AccessProgress.

        步骤   - 1: 指回源IP加白   - 2: 指本地验证   - 指修改DNS解析

        :return: The step of this AccessProgress.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this AccessProgress.

        步骤   - 1: 指回源IP加白   - 2: 指本地验证   - 指修改DNS解析

        :param step: The step of this AccessProgress.
        :type step: int
        """
        self._step = step

    @property
    def status(self):
        """Gets the status of this AccessProgress.

        状态，0：未完成这个步骤；1：已完成这个状态”

        :return: The status of this AccessProgress.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccessProgress.

        状态，0：未完成这个步骤；1：已完成这个状态”

        :param status: The status of this AccessProgress.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, AccessProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
