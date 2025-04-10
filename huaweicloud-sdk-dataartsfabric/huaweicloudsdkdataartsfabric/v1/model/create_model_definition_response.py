# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModelDefinitionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'version_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version_id': 'version_id',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, id=None, version_id=None, x_request_id=None):
        r"""CreateModelDefinitionResponse

        The model defined in huaweicloud sdk

        :param id: 模型ID，32~36位的英文、数字、短横组合
        :type id: str
        :param version_id: 模型版本ID，32~36位的英文、数字、短横组合，系统自动生成无法修改，输入不生效。
        :type version_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateModelDefinitionResponse, self).__init__()

        self._id = None
        self._version_id = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version_id is not None:
            self.version_id = version_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this CreateModelDefinitionResponse.

        模型ID，32~36位的英文、数字、短横组合

        :return: The id of this CreateModelDefinitionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateModelDefinitionResponse.

        模型ID，32~36位的英文、数字、短横组合

        :param id: The id of this CreateModelDefinitionResponse.
        :type id: str
        """
        self._id = id

    @property
    def version_id(self):
        r"""Gets the version_id of this CreateModelDefinitionResponse.

        模型版本ID，32~36位的英文、数字、短横组合，系统自动生成无法修改，输入不生效。

        :return: The version_id of this CreateModelDefinitionResponse.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this CreateModelDefinitionResponse.

        模型版本ID，32~36位的英文、数字、短横组合，系统自动生成无法修改，输入不生效。

        :param version_id: The version_id of this CreateModelDefinitionResponse.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateModelDefinitionResponse.

        :return: The x_request_id of this CreateModelDefinitionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateModelDefinitionResponse.

        :param x_request_id: The x_request_id of this CreateModelDefinitionResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CreateModelDefinitionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
