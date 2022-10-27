# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestPicLayoutBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'rest_pic_layout': 'RestPicLayout'
    }

    attribute_map = {
        'rest_pic_layout': 'restPicLayout'
    }

    def __init__(self, rest_pic_layout=None):
        """RestPicLayoutBody

        The model defined in huaweicloud sdk

        :param rest_pic_layout: 
        :type rest_pic_layout: :class:`huaweicloudsdkmeeting.v1.RestPicLayout`
        """
        
        

        self._rest_pic_layout = None
        self.discriminator = None

        if rest_pic_layout is not None:
            self.rest_pic_layout = rest_pic_layout

    @property
    def rest_pic_layout(self):
        """Gets the rest_pic_layout of this RestPicLayoutBody.


        :return: The rest_pic_layout of this RestPicLayoutBody.
        :rtype: :class:`huaweicloudsdkmeeting.v1.RestPicLayout`
        """
        return self._rest_pic_layout

    @rest_pic_layout.setter
    def rest_pic_layout(self, rest_pic_layout):
        """Sets the rest_pic_layout of this RestPicLayoutBody.


        :param rest_pic_layout: The rest_pic_layout of this RestPicLayoutBody.
        :type rest_pic_layout: :class:`huaweicloudsdkmeeting.v1.RestPicLayout`
        """
        self._rest_pic_layout = rest_pic_layout

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
        if not isinstance(other, RestPicLayoutBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
