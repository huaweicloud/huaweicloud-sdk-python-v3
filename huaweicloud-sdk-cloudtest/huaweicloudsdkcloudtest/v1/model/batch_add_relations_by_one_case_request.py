# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddRelationsByOneCaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workitem_id': 'str',
        'body': 'AddRelationsInfo'
    }

    attribute_map = {
        'workitem_id': 'workitem_id',
        'body': 'body'
    }

    def __init__(self, workitem_id=None, body=None):
        """BatchAddRelationsByOneCaseRequest

        The model defined in huaweicloud sdk

        :param workitem_id: 需求/缺陷id
        :type workitem_id: str
        :param body: Body of the BatchAddRelationsByOneCaseRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.AddRelationsInfo`
        """
        
        

        self._workitem_id = None
        self._body = None
        self.discriminator = None

        self.workitem_id = workitem_id
        if body is not None:
            self.body = body

    @property
    def workitem_id(self):
        """Gets the workitem_id of this BatchAddRelationsByOneCaseRequest.

        需求/缺陷id

        :return: The workitem_id of this BatchAddRelationsByOneCaseRequest.
        :rtype: str
        """
        return self._workitem_id

    @workitem_id.setter
    def workitem_id(self, workitem_id):
        """Sets the workitem_id of this BatchAddRelationsByOneCaseRequest.

        需求/缺陷id

        :param workitem_id: The workitem_id of this BatchAddRelationsByOneCaseRequest.
        :type workitem_id: str
        """
        self._workitem_id = workitem_id

    @property
    def body(self):
        """Gets the body of this BatchAddRelationsByOneCaseRequest.

        :return: The body of this BatchAddRelationsByOneCaseRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AddRelationsInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchAddRelationsByOneCaseRequest.

        :param body: The body of this BatchAddRelationsByOneCaseRequest.
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
        if not isinstance(other, BatchAddRelationsByOneCaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
