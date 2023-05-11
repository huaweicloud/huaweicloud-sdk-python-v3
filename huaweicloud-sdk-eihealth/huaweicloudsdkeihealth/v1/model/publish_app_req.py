# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishAppReq:

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
        'version': 'str',
        'title': 'str',
        'picture': 'str',
        'summary': 'str',
        'description': 'str',
        'labels': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'title': 'title',
        'picture': 'picture',
        'summary': 'summary',
        'description': 'description',
        'labels': 'labels'
    }

    def __init__(self, name=None, version=None, title=None, picture=None, summary=None, description=None, labels=None):
        """PublishAppReq

        The model defined in huaweicloud sdk

        :param name: 资产名称
        :type name: str
        :param version: 资产版本
        :type version: str
        :param title: 展示名
        :type title: str
        :param picture: 封面图片base64编码
        :type picture: str
        :param summary: 短描述
        :type summary: str
        :param description: 长描述
        :type description: str
        :param labels: 标签列表
        :type labels: list[str]
        """
        
        

        self._name = None
        self._version = None
        self._title = None
        self._picture = None
        self._summary = None
        self._description = None
        self._labels = None
        self.discriminator = None

        self.name = name
        self.version = version
        if title is not None:
            self.title = title
        if picture is not None:
            self.picture = picture
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels

    @property
    def name(self):
        """Gets the name of this PublishAppReq.

        资产名称

        :return: The name of this PublishAppReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublishAppReq.

        资产名称

        :param name: The name of this PublishAppReq.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this PublishAppReq.

        资产版本

        :return: The version of this PublishAppReq.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PublishAppReq.

        资产版本

        :param version: The version of this PublishAppReq.
        :type version: str
        """
        self._version = version

    @property
    def title(self):
        """Gets the title of this PublishAppReq.

        展示名

        :return: The title of this PublishAppReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PublishAppReq.

        展示名

        :param title: The title of this PublishAppReq.
        :type title: str
        """
        self._title = title

    @property
    def picture(self):
        """Gets the picture of this PublishAppReq.

        封面图片base64编码

        :return: The picture of this PublishAppReq.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this PublishAppReq.

        封面图片base64编码

        :param picture: The picture of this PublishAppReq.
        :type picture: str
        """
        self._picture = picture

    @property
    def summary(self):
        """Gets the summary of this PublishAppReq.

        短描述

        :return: The summary of this PublishAppReq.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this PublishAppReq.

        短描述

        :param summary: The summary of this PublishAppReq.
        :type summary: str
        """
        self._summary = summary

    @property
    def description(self):
        """Gets the description of this PublishAppReq.

        长描述

        :return: The description of this PublishAppReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PublishAppReq.

        长描述

        :param description: The description of this PublishAppReq.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this PublishAppReq.

        标签列表

        :return: The labels of this PublishAppReq.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this PublishAppReq.

        标签列表

        :param labels: The labels of this PublishAppReq.
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
        if not isinstance(other, PublishAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
