# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDocumentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'document_id': 'str'
    }

    attribute_map = {
        'document_id': 'document_id'
    }

    def __init__(self, document_id=None):
        r"""DeleteDocumentRequest

        The model defined in huaweicloud sdk

        :param document_id: 作业uuid
        :type document_id: str
        """
        
        

        self._document_id = None
        self.discriminator = None

        self.document_id = document_id

    @property
    def document_id(self):
        r"""Gets the document_id of this DeleteDocumentRequest.

        作业uuid

        :return: The document_id of this DeleteDocumentRequest.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this DeleteDocumentRequest.

        作业uuid

        :param document_id: The document_id of this DeleteDocumentRequest.
        :type document_id: str
        """
        self._document_id = document_id

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
        if not isinstance(other, DeleteDocumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
