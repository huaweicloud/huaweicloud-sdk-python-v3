# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAssetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'summary': 'str',
        'description': 'str',
        'picture': 'str',
        'labels': 'list[str]'
    }

    attribute_map = {
        'summary': 'summary',
        'description': 'description',
        'picture': 'picture',
        'labels': 'labels'
    }

    def __init__(self, summary=None, description=None, picture=None, labels=None):
        """UpdateAssetReq

        The model defined in huaweicloud sdk

        :param summary: 短描述
        :type summary: str
        :param description: 长描述
        :type description: str
        :param picture: 封面图片base64编码
        :type picture: str
        :param labels: 标签列表
        :type labels: list[str]
        """
        
        

        self._summary = None
        self._description = None
        self._picture = None
        self._labels = None
        self.discriminator = None

        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if picture is not None:
            self.picture = picture
        if labels is not None:
            self.labels = labels

    @property
    def summary(self):
        """Gets the summary of this UpdateAssetReq.

        短描述

        :return: The summary of this UpdateAssetReq.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this UpdateAssetReq.

        短描述

        :param summary: The summary of this UpdateAssetReq.
        :type summary: str
        """
        self._summary = summary

    @property
    def description(self):
        """Gets the description of this UpdateAssetReq.

        长描述

        :return: The description of this UpdateAssetReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAssetReq.

        长描述

        :param description: The description of this UpdateAssetReq.
        :type description: str
        """
        self._description = description

    @property
    def picture(self):
        """Gets the picture of this UpdateAssetReq.

        封面图片base64编码

        :return: The picture of this UpdateAssetReq.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this UpdateAssetReq.

        封面图片base64编码

        :param picture: The picture of this UpdateAssetReq.
        :type picture: str
        """
        self._picture = picture

    @property
    def labels(self):
        """Gets the labels of this UpdateAssetReq.

        标签列表

        :return: The labels of this UpdateAssetReq.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this UpdateAssetReq.

        标签列表

        :param labels: The labels of this UpdateAssetReq.
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
        if not isinstance(other, UpdateAssetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
