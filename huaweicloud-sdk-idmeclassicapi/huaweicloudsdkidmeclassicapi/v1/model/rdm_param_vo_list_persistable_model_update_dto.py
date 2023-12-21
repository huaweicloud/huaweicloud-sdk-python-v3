# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RDMParamVOListPersistableModelUpdateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'params': 'list[PersistableModelUpdateDTO]'
    }

    attribute_map = {
        'application_id': 'applicationId',
        'params': 'params'
    }

    def __init__(self, application_id=None, params=None):
        """RDMParamVOListPersistableModelUpdateDTO

        The model defined in huaweicloud sdk

        :param application_id: 应用ID。
        :type application_id: str
        :param params: 参数对象。
        :type params: list[:class:`huaweicloudsdkidmeclassicapi.v1.PersistableModelUpdateDTO`]
        """
        
        

        self._application_id = None
        self._params = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if params is not None:
            self.params = params

    @property
    def application_id(self):
        """Gets the application_id of this RDMParamVOListPersistableModelUpdateDTO.

        应用ID。

        :return: The application_id of this RDMParamVOListPersistableModelUpdateDTO.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this RDMParamVOListPersistableModelUpdateDTO.

        应用ID。

        :param application_id: The application_id of this RDMParamVOListPersistableModelUpdateDTO.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def params(self):
        """Gets the params of this RDMParamVOListPersistableModelUpdateDTO.

        参数对象。

        :return: The params of this RDMParamVOListPersistableModelUpdateDTO.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.PersistableModelUpdateDTO`]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this RDMParamVOListPersistableModelUpdateDTO.

        参数对象。

        :param params: The params of this RDMParamVOListPersistableModelUpdateDTO.
        :type params: list[:class:`huaweicloudsdkidmeclassicapi.v1.PersistableModelUpdateDTO`]
        """
        self._params = params

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
        if not isinstance(other, RDMParamVOListPersistableModelUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
