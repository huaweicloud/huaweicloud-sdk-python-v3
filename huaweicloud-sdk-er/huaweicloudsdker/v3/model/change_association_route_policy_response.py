# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeAssociationRoutePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'association': 'Association',
        'request_id': 'str'
    }

    attribute_map = {
        'association': 'association',
        'request_id': 'request_id'
    }

    def __init__(self, association=None, request_id=None):
        r"""ChangeAssociationRoutePolicyResponse

        The model defined in huaweicloud sdk

        :param association: 
        :type association: :class:`huaweicloudsdker.v3.Association`
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super().__init__()

        self._association = None
        self._request_id = None
        self.discriminator = None

        if association is not None:
            self.association = association
        if request_id is not None:
            self.request_id = request_id

    @property
    def association(self):
        r"""Gets the association of this ChangeAssociationRoutePolicyResponse.

        :return: The association of this ChangeAssociationRoutePolicyResponse.
        :rtype: :class:`huaweicloudsdker.v3.Association`
        """
        return self._association

    @association.setter
    def association(self, association):
        r"""Sets the association of this ChangeAssociationRoutePolicyResponse.

        :param association: The association of this ChangeAssociationRoutePolicyResponse.
        :type association: :class:`huaweicloudsdker.v3.Association`
        """
        self._association = association

    @property
    def request_id(self):
        r"""Gets the request_id of this ChangeAssociationRoutePolicyResponse.

        请求ID

        :return: The request_id of this ChangeAssociationRoutePolicyResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ChangeAssociationRoutePolicyResponse.

        请求ID

        :param request_id: The request_id of this ChangeAssociationRoutePolicyResponse.
        :type request_id: str
        """
        self._request_id = request_id

    def to_dict(self):
        import warnings
        warnings.warn("ChangeAssociationRoutePolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ChangeAssociationRoutePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
