# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBindingGeipRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gcb_id': 'str',
        'global_eips': 'list[BindingGeipBody]'
    }

    attribute_map = {
        'gcb_id': 'gcb_id',
        'global_eips': 'global_eips'
    }

    def __init__(self, gcb_id=None, global_eips=None):
        r"""CreateBindingGeipRequestBody

        The model defined in huaweicloud sdk

        :param gcb_id: 带宽包id
        :type gcb_id: str
        :param global_eips: 
        :type global_eips: list[:class:`huaweicloudsdkdc.v3.BindingGeipBody`]
        """
        
        

        self._gcb_id = None
        self._global_eips = None
        self.discriminator = None

        if gcb_id is not None:
            self.gcb_id = gcb_id
        if global_eips is not None:
            self.global_eips = global_eips

    @property
    def gcb_id(self):
        r"""Gets the gcb_id of this CreateBindingGeipRequestBody.

        带宽包id

        :return: The gcb_id of this CreateBindingGeipRequestBody.
        :rtype: str
        """
        return self._gcb_id

    @gcb_id.setter
    def gcb_id(self, gcb_id):
        r"""Sets the gcb_id of this CreateBindingGeipRequestBody.

        带宽包id

        :param gcb_id: The gcb_id of this CreateBindingGeipRequestBody.
        :type gcb_id: str
        """
        self._gcb_id = gcb_id

    @property
    def global_eips(self):
        r"""Gets the global_eips of this CreateBindingGeipRequestBody.

        :return: The global_eips of this CreateBindingGeipRequestBody.
        :rtype: list[:class:`huaweicloudsdkdc.v3.BindingGeipBody`]
        """
        return self._global_eips

    @global_eips.setter
    def global_eips(self, global_eips):
        r"""Sets the global_eips of this CreateBindingGeipRequestBody.

        :param global_eips: The global_eips of this CreateBindingGeipRequestBody.
        :type global_eips: list[:class:`huaweicloudsdkdc.v3.BindingGeipBody`]
        """
        self._global_eips = global_eips

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
        if not isinstance(other, CreateBindingGeipRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
