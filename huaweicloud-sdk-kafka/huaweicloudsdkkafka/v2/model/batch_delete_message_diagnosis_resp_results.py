# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteMessageDiagnosisRespResults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'bool',
        'id': 'str'
    }

    attribute_map = {
        'result': 'result',
        'id': 'id'
    }

    def __init__(self, result=None, id=None):
        """BatchDeleteMessageDiagnosisRespResults

        The model defined in huaweicloud sdk

        :param result: 报告删除结果
        :type result: bool
        :param id: 报告ID
        :type id: str
        """
        
        

        self._result = None
        self._id = None
        self.discriminator = None

        self.result = result
        self.id = id

    @property
    def result(self):
        """Gets the result of this BatchDeleteMessageDiagnosisRespResults.

        报告删除结果

        :return: The result of this BatchDeleteMessageDiagnosisRespResults.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this BatchDeleteMessageDiagnosisRespResults.

        报告删除结果

        :param result: The result of this BatchDeleteMessageDiagnosisRespResults.
        :type result: bool
        """
        self._result = result

    @property
    def id(self):
        """Gets the id of this BatchDeleteMessageDiagnosisRespResults.

        报告ID

        :return: The id of this BatchDeleteMessageDiagnosisRespResults.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchDeleteMessageDiagnosisRespResults.

        报告ID

        :param id: The id of this BatchDeleteMessageDiagnosisRespResults.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, BatchDeleteMessageDiagnosisRespResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
