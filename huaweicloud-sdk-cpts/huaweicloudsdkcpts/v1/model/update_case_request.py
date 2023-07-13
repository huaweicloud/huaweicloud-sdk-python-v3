# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_id': 'int',
        'target': 'str',
        'body': 'CaseInfoDetail'
    }

    attribute_map = {
        'case_id': 'case_id',
        'target': 'target',
        'body': 'body'
    }

    def __init__(self, case_id=None, target=None, body=None):
        """UpdateCaseRequest

        The model defined in huaweicloud sdk

        :param case_id: 用例id
        :type case_id: int
        :param target: 类型
        :type target: str
        :param body: Body of the UpdateCaseRequest
        :type body: :class:`huaweicloudsdkcpts.v1.CaseInfoDetail`
        """
        
        

        self._case_id = None
        self._target = None
        self._body = None
        self.discriminator = None

        self.case_id = case_id
        self.target = target
        if body is not None:
            self.body = body

    @property
    def case_id(self):
        """Gets the case_id of this UpdateCaseRequest.

        用例id

        :return: The case_id of this UpdateCaseRequest.
        :rtype: int
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        """Sets the case_id of this UpdateCaseRequest.

        用例id

        :param case_id: The case_id of this UpdateCaseRequest.
        :type case_id: int
        """
        self._case_id = case_id

    @property
    def target(self):
        """Gets the target of this UpdateCaseRequest.

        类型

        :return: The target of this UpdateCaseRequest.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this UpdateCaseRequest.

        类型

        :param target: The target of this UpdateCaseRequest.
        :type target: str
        """
        self._target = target

    @property
    def body(self):
        """Gets the body of this UpdateCaseRequest.

        :return: The body of this UpdateCaseRequest.
        :rtype: :class:`huaweicloudsdkcpts.v1.CaseInfoDetail`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateCaseRequest.

        :param body: The body of this UpdateCaseRequest.
        :type body: :class:`huaweicloudsdkcpts.v1.CaseInfoDetail`
        """
        self._body = body

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
        if not isinstance(other, UpdateCaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
