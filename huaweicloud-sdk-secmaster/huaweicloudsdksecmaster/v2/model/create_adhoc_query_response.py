# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAdhocQueryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_id': 'str'
    }

    attribute_map = {
        'operate_id': 'operate_id'
    }

    def __init__(self, operate_id=None):
        r"""CreateAdhocQueryResponse

        The model defined in huaweicloud sdk

        :param operate_id: 操作ID
        :type operate_id: str
        """
        
        super().__init__()

        self._operate_id = None
        self.discriminator = None

        if operate_id is not None:
            self.operate_id = operate_id

    @property
    def operate_id(self):
        r"""Gets the operate_id of this CreateAdhocQueryResponse.

        操作ID

        :return: The operate_id of this CreateAdhocQueryResponse.
        :rtype: str
        """
        return self._operate_id

    @operate_id.setter
    def operate_id(self, operate_id):
        r"""Sets the operate_id of this CreateAdhocQueryResponse.

        操作ID

        :param operate_id: The operate_id of this CreateAdhocQueryResponse.
        :type operate_id: str
        """
        self._operate_id = operate_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateAdhocQueryResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateAdhocQueryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
