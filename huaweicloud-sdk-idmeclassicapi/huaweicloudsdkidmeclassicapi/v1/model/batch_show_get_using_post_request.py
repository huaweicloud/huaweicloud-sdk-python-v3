# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowGetUsingPostRequest:

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
        'model_name': 'str',
        'body': 'RDMParamVOPersistObjectIdsDecryptDTO'
    }

    attribute_map = {
        'identifier': 'identifier',
        'model_name': 'modelName',
        'body': 'body'
    }

    def __init__(self, identifier=None, model_name=None, body=None):
        """BatchShowGetUsingPostRequest

        The model defined in huaweicloud sdk

        :param identifier: 应用ID。
        :type identifier: str
        :param model_name: 数据模型的英文名称。
        :type model_name: str
        :param body: Body of the BatchShowGetUsingPostRequest
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOPersistObjectIdsDecryptDTO`
        """
        
        

        self._identifier = None
        self._model_name = None
        self._body = None
        self.discriminator = None

        self.identifier = identifier
        self.model_name = model_name
        if body is not None:
            self.body = body

    @property
    def identifier(self):
        """Gets the identifier of this BatchShowGetUsingPostRequest.

        应用ID。

        :return: The identifier of this BatchShowGetUsingPostRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this BatchShowGetUsingPostRequest.

        应用ID。

        :param identifier: The identifier of this BatchShowGetUsingPostRequest.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def model_name(self):
        """Gets the model_name of this BatchShowGetUsingPostRequest.

        数据模型的英文名称。

        :return: The model_name of this BatchShowGetUsingPostRequest.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this BatchShowGetUsingPostRequest.

        数据模型的英文名称。

        :param model_name: The model_name of this BatchShowGetUsingPostRequest.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def body(self):
        """Gets the body of this BatchShowGetUsingPostRequest.

        :return: The body of this BatchShowGetUsingPostRequest.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOPersistObjectIdsDecryptDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchShowGetUsingPostRequest.

        :param body: The body of this BatchShowGetUsingPostRequest.
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOPersistObjectIdsDecryptDTO`
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
        if not isinstance(other, BatchShowGetUsingPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
