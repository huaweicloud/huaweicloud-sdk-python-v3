# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetConsistencyResultRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'consistency_result': 'list[ConsistencyResult]'
    }

    attribute_map = {
        'consistency_result': 'consistency_result'
    }

    def __init__(self, consistency_result=None):
        r"""SetConsistencyResultRequestBody

        The model defined in huaweicloud sdk

        :param consistency_result: 一致性校验结果
        :type consistency_result: list[:class:`huaweicloudsdksms.v3.ConsistencyResult`]
        """
        
        

        self._consistency_result = None
        self.discriminator = None

        if consistency_result is not None:
            self.consistency_result = consistency_result

    @property
    def consistency_result(self):
        r"""Gets the consistency_result of this SetConsistencyResultRequestBody.

        一致性校验结果

        :return: The consistency_result of this SetConsistencyResultRequestBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.ConsistencyResult`]
        """
        return self._consistency_result

    @consistency_result.setter
    def consistency_result(self, consistency_result):
        r"""Sets the consistency_result of this SetConsistencyResultRequestBody.

        一致性校验结果

        :param consistency_result: The consistency_result of this SetConsistencyResultRequestBody.
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
        if not isinstance(other, SetConsistencyResultRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
