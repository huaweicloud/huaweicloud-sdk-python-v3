# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyPrefineTag:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'new_tag': 'PredefineTagRequest',
        'old_tag': 'PredefineTagRequest'
    }

    attribute_map = {
        'new_tag': 'new_tag',
        'old_tag': 'old_tag'
    }

    def __init__(self, new_tag=None, old_tag=None):
        """ModifyPrefineTag

        The model defined in huaweicloud sdk

        :param new_tag: 
        :type new_tag: :class:`huaweicloudsdktms.v1.PredefineTagRequest`
        :param old_tag: 
        :type old_tag: :class:`huaweicloudsdktms.v1.PredefineTagRequest`
        """
        
        

        self._new_tag = None
        self._old_tag = None
        self.discriminator = None

        self.new_tag = new_tag
        self.old_tag = old_tag

    @property
    def new_tag(self):
        """Gets the new_tag of this ModifyPrefineTag.


        :return: The new_tag of this ModifyPrefineTag.
        :rtype: :class:`huaweicloudsdktms.v1.PredefineTagRequest`
        """
        return self._new_tag

    @new_tag.setter
    def new_tag(self, new_tag):
        """Sets the new_tag of this ModifyPrefineTag.


        :param new_tag: The new_tag of this ModifyPrefineTag.
        :type new_tag: :class:`huaweicloudsdktms.v1.PredefineTagRequest`
        """
        self._new_tag = new_tag

    @property
    def old_tag(self):
        """Gets the old_tag of this ModifyPrefineTag.


        :return: The old_tag of this ModifyPrefineTag.
        :rtype: :class:`huaweicloudsdktms.v1.PredefineTagRequest`
        """
        return self._old_tag

    @old_tag.setter
    def old_tag(self, old_tag):
        """Sets the old_tag of this ModifyPrefineTag.


        :param old_tag: The old_tag of this ModifyPrefineTag.
        :type old_tag: :class:`huaweicloudsdktms.v1.PredefineTagRequest`
        """
        self._old_tag = old_tag

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
        if not isinstance(other, ModifyPrefineTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
