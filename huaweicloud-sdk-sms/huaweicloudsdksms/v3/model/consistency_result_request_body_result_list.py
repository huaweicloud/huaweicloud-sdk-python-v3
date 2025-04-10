# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsistencyResultRequestBodyResultList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'finished_time': 'int',
        'check_result': 'str',
        'consistency_result': 'list[ConsistencyResult]'
    }

    attribute_map = {
        'finished_time': 'finished_time',
        'check_result': 'check_result',
        'consistency_result': 'consistency_result'
    }

    def __init__(self, finished_time=None, check_result=None, consistency_result=None):
        r"""ConsistencyResultRequestBodyResultList

        The model defined in huaweicloud sdk

        :param finished_time: 校验完成时间
        :type finished_time: int
        :param check_result: 校验结果
        :type check_result: str
        :param consistency_result: 校验结果
        :type consistency_result: list[:class:`huaweicloudsdksms.v3.ConsistencyResult`]
        """
        
        

        self._finished_time = None
        self._check_result = None
        self._consistency_result = None
        self.discriminator = None

        if finished_time is not None:
            self.finished_time = finished_time
        if check_result is not None:
            self.check_result = check_result
        if consistency_result is not None:
            self.consistency_result = consistency_result

    @property
    def finished_time(self):
        r"""Gets the finished_time of this ConsistencyResultRequestBodyResultList.

        校验完成时间

        :return: The finished_time of this ConsistencyResultRequestBodyResultList.
        :rtype: int
        """
        return self._finished_time

    @finished_time.setter
    def finished_time(self, finished_time):
        r"""Sets the finished_time of this ConsistencyResultRequestBodyResultList.

        校验完成时间

        :param finished_time: The finished_time of this ConsistencyResultRequestBodyResultList.
        :type finished_time: int
        """
        self._finished_time = finished_time

    @property
    def check_result(self):
        r"""Gets the check_result of this ConsistencyResultRequestBodyResultList.

        校验结果

        :return: The check_result of this ConsistencyResultRequestBodyResultList.
        :rtype: str
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        r"""Sets the check_result of this ConsistencyResultRequestBodyResultList.

        校验结果

        :param check_result: The check_result of this ConsistencyResultRequestBodyResultList.
        :type check_result: str
        """
        self._check_result = check_result

    @property
    def consistency_result(self):
        r"""Gets the consistency_result of this ConsistencyResultRequestBodyResultList.

        校验结果

        :return: The consistency_result of this ConsistencyResultRequestBodyResultList.
        :rtype: list[:class:`huaweicloudsdksms.v3.ConsistencyResult`]
        """
        return self._consistency_result

    @consistency_result.setter
    def consistency_result(self, consistency_result):
        r"""Sets the consistency_result of this ConsistencyResultRequestBodyResultList.

        校验结果

        :param consistency_result: The consistency_result of this ConsistencyResultRequestBodyResultList.
        :type consistency_result: list[:class:`huaweicloudsdksms.v3.ConsistencyResult`]
        """
        self._consistency_result = consistency_result

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
        if not isinstance(other, ConsistencyResultRequestBodyResultList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
