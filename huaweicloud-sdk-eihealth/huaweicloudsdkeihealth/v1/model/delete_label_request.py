# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLabelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label_id': 'str'
    }

    attribute_map = {
        'label_id': 'label_id'
    }

    def __init__(self, label_id=None):
        """DeleteLabelRequest

        The model defined in huaweicloud sdk

        :param label_id: 标签id
        :type label_id: str
        """
        
        

        self._label_id = None
        self.discriminator = None

        self.label_id = label_id

    @property
    def label_id(self):
        """Gets the label_id of this DeleteLabelRequest.

        标签id

        :return: The label_id of this DeleteLabelRequest.
        :rtype: str
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this DeleteLabelRequest.

        标签id

        :param label_id: The label_id of this DeleteLabelRequest.
        :type label_id: str
        """
        self._label_id = label_id

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
        if not isinstance(other, DeleteLabelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
