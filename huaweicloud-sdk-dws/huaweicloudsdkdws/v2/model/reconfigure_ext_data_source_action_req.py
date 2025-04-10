# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReconfigureExtDataSourceActionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reconfigure': 'ReconfigureExtDataSourceAction'
    }

    attribute_map = {
        'reconfigure': 'reconfigure'
    }

    def __init__(self, reconfigure=None):
        r"""ReconfigureExtDataSourceActionReq

        The model defined in huaweicloud sdk

        :param reconfigure: 
        :type reconfigure: :class:`huaweicloudsdkdws.v2.ReconfigureExtDataSourceAction`
        """
        
        

        self._reconfigure = None
        self.discriminator = None

        self.reconfigure = reconfigure

    @property
    def reconfigure(self):
        r"""Gets the reconfigure of this ReconfigureExtDataSourceActionReq.

        :return: The reconfigure of this ReconfigureExtDataSourceActionReq.
        :rtype: :class:`huaweicloudsdkdws.v2.ReconfigureExtDataSourceAction`
        """
        return self._reconfigure

    @reconfigure.setter
    def reconfigure(self, reconfigure):
        r"""Sets the reconfigure of this ReconfigureExtDataSourceActionReq.

        :param reconfigure: The reconfigure of this ReconfigureExtDataSourceActionReq.
        :type reconfigure: :class:`huaweicloudsdkdws.v2.ReconfigureExtDataSourceAction`
        """
        self._reconfigure = reconfigure

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
        if not isinstance(other, ReconfigureExtDataSourceActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
