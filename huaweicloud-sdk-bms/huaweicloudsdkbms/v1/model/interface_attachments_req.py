# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterfaceAttachmentsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'delete_on_termination': 'str'
    }

    attribute_map = {
        'delete_on_termination': 'delete_on_termination'
    }

    def __init__(self, delete_on_termination=None):
        """InterfaceAttachmentsReq

        The model defined in huaweicloud sdk

        :param delete_on_termination: 
        :type delete_on_termination: str
        """
        
        

        self._delete_on_termination = None
        self.discriminator = None

        if delete_on_termination is not None:
            self.delete_on_termination = delete_on_termination

    @property
    def delete_on_termination(self):
        """Gets the delete_on_termination of this InterfaceAttachmentsReq.


        :return: The delete_on_termination of this InterfaceAttachmentsReq.
        :rtype: str
        """
        return self._delete_on_termination

    @delete_on_termination.setter
    def delete_on_termination(self, delete_on_termination):
        """Sets the delete_on_termination of this InterfaceAttachmentsReq.


        :param delete_on_termination: The delete_on_termination of this InterfaceAttachmentsReq.
        :type delete_on_termination: str
        """
        self._delete_on_termination = delete_on_termination

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
        if not isinstance(other, InterfaceAttachmentsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
