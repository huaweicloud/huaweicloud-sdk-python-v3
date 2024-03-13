# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGetByUniqueKeyRequest:

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
        'get_unique_field_method': 'str',
        'body': 'RDMParamVOPersistableModelUniqueKeyDTO'
    }

    attribute_map = {
        'identifier': 'identifier',
        'model_name': 'modelName',
        'get_unique_field_method': 'getUniqueFieldMethod',
        'body': 'body'
    }

    def __init__(self, identifier=None, model_name=None, get_unique_field_method=None, body=None):
        """ShowGetByUniqueKeyRequest

        The model defined in huaweicloud sdk

        :param identifier: 应用ID。
        :type identifier: str
        :param model_name: 数据模型的英文名称。
        :type model_name: str
        :param get_unique_field_method: 方法名称，格式为：getBy{uniqueName}。  uniqueName：表示“唯一键”为“是”的属性英文名称。
        :type get_unique_field_method: str
        :param body: Body of the ShowGetByUniqueKeyRequest
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOPersistableModelUniqueKeyDTO`
        """
        
        

        self._identifier = None
        self._model_name = None
        self._get_unique_field_method = None
        self._body = None
        self.discriminator = None

        self.identifier = identifier
        self.model_name = model_name
        self.get_unique_field_method = get_unique_field_method
        if body is not None:
            self.body = body

    @property
    def identifier(self):
        """Gets the identifier of this ShowGetByUniqueKeyRequest.

        应用ID。

        :return: The identifier of this ShowGetByUniqueKeyRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ShowGetByUniqueKeyRequest.

        应用ID。

        :param identifier: The identifier of this ShowGetByUniqueKeyRequest.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def model_name(self):
        """Gets the model_name of this ShowGetByUniqueKeyRequest.

        数据模型的英文名称。

        :return: The model_name of this ShowGetByUniqueKeyRequest.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this ShowGetByUniqueKeyRequest.

        数据模型的英文名称。

        :param model_name: The model_name of this ShowGetByUniqueKeyRequest.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def get_unique_field_method(self):
        """Gets the get_unique_field_method of this ShowGetByUniqueKeyRequest.

        方法名称，格式为：getBy{uniqueName}。  uniqueName：表示“唯一键”为“是”的属性英文名称。

        :return: The get_unique_field_method of this ShowGetByUniqueKeyRequest.
        :rtype: str
        """
        return self._get_unique_field_method

    @get_unique_field_method.setter
    def get_unique_field_method(self, get_unique_field_method):
        """Sets the get_unique_field_method of this ShowGetByUniqueKeyRequest.

        方法名称，格式为：getBy{uniqueName}。  uniqueName：表示“唯一键”为“是”的属性英文名称。

        :param get_unique_field_method: The get_unique_field_method of this ShowGetByUniqueKeyRequest.
        :type get_unique_field_method: str
        """
        self._get_unique_field_method = get_unique_field_method

    @property
    def body(self):
        """Gets the body of this ShowGetByUniqueKeyRequest.

        :return: The body of this ShowGetByUniqueKeyRequest.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOPersistableModelUniqueKeyDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ShowGetByUniqueKeyRequest.

        :param body: The body of this ShowGetByUniqueKeyRequest.
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOPersistableModelUniqueKeyDTO`
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
        if not isinstance(other, ShowGetByUniqueKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
