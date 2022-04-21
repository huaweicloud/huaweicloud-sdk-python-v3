# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateYmlsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'edit': 'UpdateYmlsReqEdit'
    }

    attribute_map = {
        'edit': 'edit'
    }

    def __init__(self, edit=None):
        """UpdateYmlsReq

        The model defined in huaweicloud sdk

        :param edit: 
        :type edit: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEdit`
        """
        
        

        self._edit = None
        self.discriminator = None

        self.edit = edit

    @property
    def edit(self):
        """Gets the edit of this UpdateYmlsReq.


        :return: The edit of this UpdateYmlsReq.
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEdit`
        """
        return self._edit

    @edit.setter
    def edit(self, edit):
        """Sets the edit of this UpdateYmlsReq.


        :param edit: The edit of this UpdateYmlsReq.
        :type edit: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEdit`
        """
        self._edit = edit

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
        if not isinstance(other, UpdateYmlsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
