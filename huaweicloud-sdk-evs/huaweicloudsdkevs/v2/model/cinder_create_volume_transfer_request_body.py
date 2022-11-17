# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CinderCreateVolumeTransferRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transfer': 'CreateVolumeTransferOption'
    }

    attribute_map = {
        'transfer': 'transfer'
    }

    def __init__(self, transfer=None):
        """CinderCreateVolumeTransferRequestBody

        The model defined in huaweicloud sdk

        :param transfer: 
        :type transfer: :class:`huaweicloudsdkevs.v2.CreateVolumeTransferOption`
        """
        
        

        self._transfer = None
        self.discriminator = None

        self.transfer = transfer

    @property
    def transfer(self):
        """Gets the transfer of this CinderCreateVolumeTransferRequestBody.

        :return: The transfer of this CinderCreateVolumeTransferRequestBody.
        :rtype: :class:`huaweicloudsdkevs.v2.CreateVolumeTransferOption`
        """
        return self._transfer

    @transfer.setter
    def transfer(self, transfer):
        """Sets the transfer of this CinderCreateVolumeTransferRequestBody.

        :param transfer: The transfer of this CinderCreateVolumeTransferRequestBody.
        :type transfer: :class:`huaweicloudsdkevs.v2.CreateVolumeTransferOption`
        """
        self._transfer = transfer

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
        if not isinstance(other, CinderCreateVolumeTransferRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
