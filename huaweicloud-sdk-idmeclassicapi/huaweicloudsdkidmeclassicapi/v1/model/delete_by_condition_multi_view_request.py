# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteByConditionMultiViewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identifier': 'str',
        'body': 'RDMParamVODeleteByConditionVo'
    }

    attribute_map = {
        'identifier': 'identifier',
        'body': 'body'
    }

    def __init__(self, identifier=None, body=None):
        """DeleteByConditionMultiViewRequest

        The model defined in huaweicloud sdk

        :param identifier: 应用ID。
        :type identifier: str
        :param body: Body of the DeleteByConditionMultiViewRequest
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVODeleteByConditionVo`
        """
        
        

        self._identifier = None
        self._body = None
        self.discriminator = None

        self.identifier = identifier
        if body is not None:
            self.body = body

    @property
    def identifier(self):
        """Gets the identifier of this DeleteByConditionMultiViewRequest.

        应用ID。

        :return: The identifier of this DeleteByConditionMultiViewRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this DeleteByConditionMultiViewRequest.

        应用ID。

        :param identifier: The identifier of this DeleteByConditionMultiViewRequest.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def body(self):
        """Gets the body of this DeleteByConditionMultiViewRequest.

        :return: The body of this DeleteByConditionMultiViewRequest.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVODeleteByConditionVo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteByConditionMultiViewRequest.

        :param body: The body of this DeleteByConditionMultiViewRequest.
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVODeleteByConditionVo`
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
        if not isinstance(other, DeleteByConditionMultiViewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
