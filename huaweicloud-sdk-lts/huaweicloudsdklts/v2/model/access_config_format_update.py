# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigFormatUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'single': 'AccessConfigFormatSingle',
        'multi': 'AccessConfigFormatMutil'
    }

    attribute_map = {
        'single': 'single',
        'multi': 'multi'
    }

    def __init__(self, single=None, multi=None):
        """AccessConfigFormatUpdate

        The model defined in huaweicloud sdk

        :param single: 
        :type single: :class:`huaweicloudsdklts.v2.AccessConfigFormatSingle`
        :param multi: 
        :type multi: :class:`huaweicloudsdklts.v2.AccessConfigFormatMutil`
        """
        
        

        self._single = None
        self._multi = None
        self.discriminator = None

        if single is not None:
            self.single = single
        if multi is not None:
            self.multi = multi

    @property
    def single(self):
        """Gets the single of this AccessConfigFormatUpdate.

        :return: The single of this AccessConfigFormatUpdate.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigFormatSingle`
        """
        return self._single

    @single.setter
    def single(self, single):
        """Sets the single of this AccessConfigFormatUpdate.

        :param single: The single of this AccessConfigFormatUpdate.
        :type single: :class:`huaweicloudsdklts.v2.AccessConfigFormatSingle`
        """
        self._single = single

    @property
    def multi(self):
        """Gets the multi of this AccessConfigFormatUpdate.

        :return: The multi of this AccessConfigFormatUpdate.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigFormatMutil`
        """
        return self._multi

    @multi.setter
    def multi(self, multi):
        """Sets the multi of this AccessConfigFormatUpdate.

        :param multi: The multi of this AccessConfigFormatUpdate.
        :type multi: :class:`huaweicloudsdklts.v2.AccessConfigFormatMutil`
        """
        self._multi = multi

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
        if not isinstance(other, AccessConfigFormatUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
