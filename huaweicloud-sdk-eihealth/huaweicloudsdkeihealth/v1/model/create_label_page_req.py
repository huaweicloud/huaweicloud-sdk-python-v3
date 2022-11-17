# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLabelPageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'feature': 'FeatureEnum',
        'labels': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'feature': 'feature',
        'labels': 'labels'
    }

    def __init__(self, name=None, feature=None, labels=None):
        """CreateLabelPageReq

        The model defined in huaweicloud sdk

        :param name: 标签页面标题，正则匹配中文，英文字母和数字及下划线
        :type name: str
        :param feature: 
        :type feature: :class:`huaweicloudsdkeihealth.v1.FeatureEnum`
        :param labels: 标签页面包含的标签值，正则匹配中文，英文字母和数字及下划线
        :type labels: list[str]
        """
        
        

        self._name = None
        self._feature = None
        self._labels = None
        self.discriminator = None

        self.name = name
        self.feature = feature
        self.labels = labels

    @property
    def name(self):
        """Gets the name of this CreateLabelPageReq.

        标签页面标题，正则匹配中文，英文字母和数字及下划线

        :return: The name of this CreateLabelPageReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLabelPageReq.

        标签页面标题，正则匹配中文，英文字母和数字及下划线

        :param name: The name of this CreateLabelPageReq.
        :type name: str
        """
        self._name = name

    @property
    def feature(self):
        """Gets the feature of this CreateLabelPageReq.

        :return: The feature of this CreateLabelPageReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.FeatureEnum`
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this CreateLabelPageReq.

        :param feature: The feature of this CreateLabelPageReq.
        :type feature: :class:`huaweicloudsdkeihealth.v1.FeatureEnum`
        """
        self._feature = feature

    @property
    def labels(self):
        """Gets the labels of this CreateLabelPageReq.

        标签页面包含的标签值，正则匹配中文，英文字母和数字及下划线

        :return: The labels of this CreateLabelPageReq.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreateLabelPageReq.

        标签页面包含的标签值，正则匹配中文，英文字母和数字及下划线

        :param labels: The labels of this CreateLabelPageReq.
        :type labels: list[str]
        """
        self._labels = labels

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
        if not isinstance(other, CreateLabelPageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
