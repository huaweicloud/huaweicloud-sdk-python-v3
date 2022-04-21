# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLabelValuesAomPromGetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'label_name': 'str'
    }

    attribute_map = {
        'label_name': 'label_name'
    }

    def __init__(self, label_name=None):
        """ListLabelValuesAomPromGetRequest

        The model defined in huaweicloud sdk

        :param label_name: 查询所用标签。
        :type label_name: str
        """
        
        

        self._label_name = None
        self.discriminator = None

        self.label_name = label_name

    @property
    def label_name(self):
        """Gets the label_name of this ListLabelValuesAomPromGetRequest.

        查询所用标签。

        :return: The label_name of this ListLabelValuesAomPromGetRequest.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        """Sets the label_name of this ListLabelValuesAomPromGetRequest.

        查询所用标签。

        :param label_name: The label_name of this ListLabelValuesAomPromGetRequest.
        :type label_name: str
        """
        self._label_name = label_name

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
        if not isinstance(other, ListLabelValuesAomPromGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
