# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServerConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'onpremises': 'OnPremisesConfig',
        'federations': 'FederationConfig'
    }

    attribute_map = {
        'onpremises': 'onpremises',
        'federations': 'federations'
    }

    def __init__(self, onpremises=None, federations=None):
        r"""ListServerConfigsResponse

        The model defined in huaweicloud sdk

        :param onpremises: 
        :type onpremises: :class:`huaweicloudsdkucs.v1.OnPremisesConfig`
        :param federations: 
        :type federations: :class:`huaweicloudsdkucs.v1.FederationConfig`
        """
        
        super().__init__()

        self._onpremises = None
        self._federations = None
        self.discriminator = None

        if onpremises is not None:
            self.onpremises = onpremises
        if federations is not None:
            self.federations = federations

    @property
    def onpremises(self):
        r"""Gets the onpremises of this ListServerConfigsResponse.

        :return: The onpremises of this ListServerConfigsResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.OnPremisesConfig`
        """
        return self._onpremises

    @onpremises.setter
    def onpremises(self, onpremises):
        r"""Sets the onpremises of this ListServerConfigsResponse.

        :param onpremises: The onpremises of this ListServerConfigsResponse.
        :type onpremises: :class:`huaweicloudsdkucs.v1.OnPremisesConfig`
        """
        self._onpremises = onpremises

    @property
    def federations(self):
        r"""Gets the federations of this ListServerConfigsResponse.

        :return: The federations of this ListServerConfigsResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.FederationConfig`
        """
        return self._federations

    @federations.setter
    def federations(self, federations):
        r"""Sets the federations of this ListServerConfigsResponse.

        :param federations: The federations of this ListServerConfigsResponse.
        :type federations: :class:`huaweicloudsdkucs.v1.FederationConfig`
        """
        self._federations = federations

    def to_dict(self):
        import warnings
        warnings.warn("ListServerConfigsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListServerConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
