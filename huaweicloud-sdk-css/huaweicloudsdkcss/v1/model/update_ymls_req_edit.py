# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateYmlsReqEdit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'modify': 'UpdateYmlsReqEditModify'
    }

    attribute_map = {
        'modify': 'modify'
    }

    def __init__(self, modify=None):
        """UpdateYmlsReqEdit

        The model defined in huaweicloud sdk

        :param modify: 
        :type modify: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        """
        
        

        self._modify = None
        self.discriminator = None

        self.modify = modify

    @property
    def modify(self):
        """Gets the modify of this UpdateYmlsReqEdit.

        :return: The modify of this UpdateYmlsReqEdit.
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        """
        return self._modify

    @modify.setter
    def modify(self, modify):
        """Sets the modify of this UpdateYmlsReqEdit.

        :param modify: The modify of this UpdateYmlsReqEdit.
        :type modify: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        """
        self._modify = modify

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
        if not isinstance(other, UpdateYmlsReqEdit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
