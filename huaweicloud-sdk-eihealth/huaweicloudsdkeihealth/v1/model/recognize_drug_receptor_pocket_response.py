# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecognizeDrugReceptorPocketResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'RecognizeReceptorPocketMode',
        'pockets': 'list[DrugBoundingBoxDto]'
    }

    attribute_map = {
        'mode': 'mode',
        'pockets': 'pockets'
    }

    def __init__(self, mode=None, pockets=None):
        """RecognizeDrugReceptorPocketResponse

        The model defined in huaweicloud sdk

        :param mode: 
        :type mode: :class:`huaweicloudsdkeihealth.v1.RecognizeReceptorPocketMode`
        :param pockets: 口袋列表
        :type pockets: list[:class:`huaweicloudsdkeihealth.v1.DrugBoundingBoxDto`]
        """
        
        super(RecognizeDrugReceptorPocketResponse, self).__init__()

        self._mode = None
        self._pockets = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if pockets is not None:
            self.pockets = pockets

    @property
    def mode(self):
        """Gets the mode of this RecognizeDrugReceptorPocketResponse.

        :return: The mode of this RecognizeDrugReceptorPocketResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.RecognizeReceptorPocketMode`
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this RecognizeDrugReceptorPocketResponse.

        :param mode: The mode of this RecognizeDrugReceptorPocketResponse.
        :type mode: :class:`huaweicloudsdkeihealth.v1.RecognizeReceptorPocketMode`
        """
        self._mode = mode

    @property
    def pockets(self):
        """Gets the pockets of this RecognizeDrugReceptorPocketResponse.

        口袋列表

        :return: The pockets of this RecognizeDrugReceptorPocketResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DrugBoundingBoxDto`]
        """
        return self._pockets

    @pockets.setter
    def pockets(self, pockets):
        """Sets the pockets of this RecognizeDrugReceptorPocketResponse.

        口袋列表

        :param pockets: The pockets of this RecognizeDrugReceptorPocketResponse.
        :type pockets: list[:class:`huaweicloudsdkeihealth.v1.DrugBoundingBoxDto`]
        """
        self._pockets = pockets

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
        if not isinstance(other, RecognizeDrugReceptorPocketResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
