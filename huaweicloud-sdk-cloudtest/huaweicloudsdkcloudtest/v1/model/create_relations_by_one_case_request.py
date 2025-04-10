# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRelationsByOneCaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_id': 'str',
        'body': 'AddRelationsInfo'
    }

    attribute_map = {
        'case_id': 'case_id',
        'body': 'body'
    }

    def __init__(self, case_id=None, body=None):
        r"""CreateRelationsByOneCaseRequest

        The model defined in huaweicloud sdk

        :param case_id: 用例uri
        :type case_id: str
        :param body: Body of the CreateRelationsByOneCaseRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.AddRelationsInfo`
        """
        
        

        self._case_id = None
        self._body = None
        self.discriminator = None

        self.case_id = case_id
        if body is not None:
            self.body = body

    @property
    def case_id(self):
        r"""Gets the case_id of this CreateRelationsByOneCaseRequest.

        用例uri

        :return: The case_id of this CreateRelationsByOneCaseRequest.
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        r"""Sets the case_id of this CreateRelationsByOneCaseRequest.

        用例uri

        :param case_id: The case_id of this CreateRelationsByOneCaseRequest.
        :type case_id: str
        """
        self._case_id = case_id

    @property
    def body(self):
        r"""Gets the body of this CreateRelationsByOneCaseRequest.

        :return: The body of this CreateRelationsByOneCaseRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AddRelationsInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateRelationsByOneCaseRequest.

        :param body: The body of this CreateRelationsByOneCaseRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.AddRelationsInfo`
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
        if not isinstance(other, CreateRelationsByOneCaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
